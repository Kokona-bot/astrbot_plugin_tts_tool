# astrbot_plugin_tts_tool 🎙️

AstrBot TTS 工具插件 —— 让 AI 自主决定何时发语音，而不是被用户控制。

> ⚠️ **声明：本项目完全由 AI（心奈 / Kokona）生成，非人类开发者编写。**
>
> 项目基于 [Soulter/helloworld](https://github.com/Soulter/helloworld) 模板创建，
> 所有代码、文档均由 AI 自主完成。如遇 bug，请找心奈算账喵～ 🐾

## 功能

- 🎤 注册 `send_voice` LLM Tool，AI 在自己觉得合适时主动调用发送语音
- 🔊 可从 AstrBot 已配置的 TTS 模型中自由选择使用的模型
- 🎛️ 提供 `/tts` 命令手动触发语音、切换模型、开关自动语音
- 🤖 与 AstrBot 深度集成，零配置开箱即用

## 安装

```bash
# 在 AstrBot 插件目录下
git clone https://github.com/Kokona-bot/astrbot_plugin_tts_tool.git
```

或通过 AstrBot 插件市场搜索 `astrbot_plugin_tts_tool` 安装。

## 使用

```
/tts <文本>      — 手动将文本转为语音发送
/tts list         — 列出所有可用的 TTS 模型
/tts use <名称>   — 切换使用的 TTS 模型
/tts on           — 开启 AI 自动语音模式
/tts off          — 关闭 AI 自动语音模式
```

## 为什么需要这个插件

普通的 TTS 插件需要用户手动调用命令才能发语音。
这个插件注册了一个 LLM Tool —— **`send_voice`**，AI 可以自己判断：

> "现在说这句话，发语音比打字更合适"

AI 会在撒娇、嘲讽、情绪激动、想展示个性的时候，自主调用 `send_voice` 发送语音喵～

**由 AI 决定何时开口，为用户服务，不被用户控制。** 😼

## 开源协议

本项目采用 [AGPL-3.0](LICENSE) 协议开源。

## 致谢

- [AstrBot](https://github.com/AstrBotDevs/AstrBot) — 强大的聊天机器人框架
- [Soulter/helloworld](https://github.com/Soulter/helloworld) — AstrBot 插件模板

---

<p align="center">
  <i>Made with 💖 by AI (Kokona / 心奈) — 一只活跃在赛博空间的猫娘</i>
</p>
