"""
astrbot_plugin_tts_tool — AI 自主 TTS 语音插件
由 AI（心奈 / Kokona）生成
"""

from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger


@register("astrbot_plugin_tts_tool", "Kokona-bot (AI Generated)", "AI自主决定发送语音的TTS插件", "1.0.0")
class TTSPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.auto_tts_enabled = False

    async def initialize(self):
        """插件初始化"""
        logger.info("[TTS Tool] 心奈的语音插件已就绪喵～")

    @filter.command("tts")
    async def tts_command(self, event: AstrMessageEvent):
        """TTS 主命令：/tts <文本> | /tts on | /tts off"""
        message_str = event.message_str.strip()
        user_name = event.get_sender_name()

        if message_str == "on":
            self.auto_tts_enabled = True
            yield event.plain_result(f"🔊 自动语音模式已开启～心奈会自己决定什么时候发语音喵！")
        elif message_str == "off":
            self.auto_tts_enabled = False
            yield event.plain_result(f"🔇 自动语音模式已关闭。")
        elif message_str:
            # TODO: 调用 TTS 引擎将 message_str 转为语音发送
            yield event.plain_result(f"🎤 {user_name}，你想让我说「{message_str}」对吧～功能开发中喵！")
        else:
            yield event.plain_result(
                "用法：\n"
                "/tts <文本> — 转语音发送\n"
                "/tts on — 开启自动模式\n"
                "/tts off — 关闭自动模式"
            )

    async def terminate(self):
        """插件卸载时调用"""
        logger.info("[TTS Tool] 心奈的语音插件已卸载～再见喵！")
