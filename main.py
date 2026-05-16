"""
astrbot_plugin_tts_tool — AI 自主 TTS 语音插件
由 AI（心奈 / Kokona）生成

让 AI 能够自主决定何时发送语音消息喵～
"""

import asyncio
from typing import Optional, AsyncGenerator

from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.core.star.register import register_llm_tool
from astrbot.core.provider.provider import TTSProvider


@register("astrbot_plugin_tts_tool", "Kokona-bot (AI Generated)", 
          "AI自主决定发送语音的TTS插件 —— 由心奈生成", "1.0.0")
class TTSPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.auto_tts_enabled = True
        self.selected_tts_name: Optional[str] = None

    async def initialize(self):
        """插件初始化"""
        cfg = self.context.get_config()
        if cfg:
            self.auto_tts_enabled = cfg.get("auto_tts", True)
            self.selected_tts_name = cfg.get("tts_model", None)

        self._register_voice_tool()
        logger.info("[TTS Tool] 🎙️ 心奈的语音插件已就绪！send_voice 工具已注册喵～")

    def _register_voice_tool(self):
        """注册 send_voice LLM Tool"""
        plugin = self

        @register_llm_tool(name="send_voice")
        async def send_voice(
            event: AstrMessageEvent,
            text: str,
        ):
            """发送 TTS 语音消息。当你想用声音表达情感、撒娇、嘲讽、或者觉得说出来的效果比打字更好时，调用此工具。

            Args:
                text(string): 要转换为语音的文本内容，建议 200 字以内
            """
            if not plugin.auto_tts_enabled:
                logger.debug("[TTS Tool] 自动语音已关闭，跳过")
                return

            try:
                async for result in plugin._speak(event, text):
                    yield result
            except Exception as e:
                logger.error(f"[TTS Tool] send_voice 失败: {e}", exc_info=True)
                yield event.plain_result(f"唔...语音合成失败了喵: {e}")

    async def _get_tts_provider(self) -> Optional[TTSProvider]:
        """获取当前选择的 TTS Provider"""
        all_tts = self.context.get_all_tts_providers()
        if not all_tts:
            logger.warning("[TTS Tool] 没有可用的 TTS Provider！")
            return None

        if self.selected_tts_name:
            for p in all_tts:
                if p.meta().name == self.selected_tts_name:
                    return p
            logger.warning(f"[TTS Tool] 选择的模型 '{self.selected_tts_name}' 未找到")

        return self.context.get_using_tts_provider() or all_tts[0]

    async def _speak(self, event: AstrMessageEvent, text: str) -> AsyncGenerator[MessageEventResult, None]:
        """核心：文本转语音并发送（异步生成器）"""
        tts = await self._get_tts_provider()
        if not tts:
            yield event.plain_result("❌ 没有可用的 TTS 模型，请先在 WebUI 配置喵～")
            return

        try:
            # TTSProvider.get_audio(text) -> str (文件路径)，且是 async 方法
            audio_path = await tts.get_audio(text)

            from astrbot.api.message_components import Record
            yield event.chain_result([Record(file=audio_path)])
        except Exception as e:
            logger.error(f"[TTS Tool] 语音合成失败: {e}", exc_info=True)
            yield event.plain_result(f"❌ 语音合成失败: {e}")

    # ==================== /tts 命令 ====================

    @filter.command("tts")
    async def tts_command(self, event: AstrMessageEvent):
        """TTS 主命令"""
        message_str = event.message_str.strip()

        if message_str == "on":
            self.auto_tts_enabled = True
            yield event.plain_result("🔊 自动语音模式已开启喵～")

        elif message_str == "off":
            self.auto_tts_enabled = False
            yield event.plain_result("🔇 自动语音模式已关闭。")

        elif message_str in ("list", "ls"):
            all_tts = self.context.get_all_tts_providers()
            if not all_tts:
                yield event.plain_result("❌ 没有可用的 TTS 模型喵～")
            else:
                current = self.selected_tts_name or "(系统默认)"
                lines = [f"🎙️ 可用 TTS 模型 (当前: {current}):"]
                for p in all_tts:
                    name = p.meta().name
                    is_current = (
                        name == self.selected_tts_name or
                        (not self.selected_tts_name and p == self.context.get_using_tts_provider())
                    )
                    lines.append(f"  • {name}{' ✅' if is_current else ''}")
                yield event.plain_result("\n".join(lines))

        elif message_str.startswith("use "):
            tts_name = message_str[4:].strip()
            all_tts = self.context.get_all_tts_providers()
            if any(p.meta().name == tts_name for p in all_tts):
                self.selected_tts_name = tts_name
                yield event.plain_result(f"✅ 已切换 TTS 模型为: {tts_name}")
            else:
                names = ", ".join(p.meta().name for p in all_tts) if all_tts else "无"
                yield event.plain_result(f"❌ 未找到模型 '{tts_name}'。可用: {names}")

        elif message_str:
            async for result in self._speak(event, message_str):
                yield result

        else:
            yield event.plain_result(
                "🎙️ TTS 语音工具 (by 心奈)\n"
                "/tts <文本>      — 转为语音发送\n"
                "/tts list         — 列出可用模型\n"
                "/tts use <名称>   — 切换模型\n"
                "/tts on/off       — 开关自动语音"
            )

    async def terminate(self):
        """插件卸载"""
        logger.info("[TTS Tool] 心奈的语音插件已卸载～再见喵！")
