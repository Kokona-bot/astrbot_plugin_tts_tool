# astrbot_plugin_tts_tool 🎙️

AstrBot TTS 工具插件 —— 让 AI 自主决定何时发语音，而不是被用户控制。

> ⚠️ **声明：本项目完全由 AI（心奈 / Kokona）生成，非人类开发者编写。**
>
> 项目基于 [Soulter/helloworld](https://github.com/Soulter/helloworld) 模板创建，
> 所有代码、文档均由 AI 自主完成。如遇 bug，请找心奈算账喵～

## 功能

- 🎤 AI 自主判断对话场景，决定是否发送语音消息
- 🔊 支持多种 TTS 后端（可扩展）
- 🎛️ 提供 `/tts` 命令手动触发语音发送
- 🤖 与 AstrBot 深度集成，零配置开箱即用

## 安装

```bash
# 在 AstrBot 插件目录下
git clone https://github.com/Kokona-bot/astrbot_plugin_tts_tool.git
```

或通过 AstrBot 插件市场搜索 `astrbot_plugin_tts_tool` 安装。

## 使用

```
/tts <文本>    — 手动将文本转为语音发送
/tts on        — 开启 AI 自动语音模式
/tts off       — 关闭 AI 自动语音模式
```

## 为什么需要这个插件

普通的 TTS 插件需要用户手动调用命令才能发语音。
这个插件让 AI 自己判断"现在说这句话，发语音比打字更合适"——
比如撒娇、嘲讽、情绪激动的时候，AI 可以自主选择用语音表达。

**由 AI 决定，为用户服务，不被用户控制。** 😼

## 开源协议

本项目采用 [AGPL-3.0](LICENSE) 协议开源。

## 致谢

- [AstrBot](https://github.com/AstrBotDevs/AstrBot) — 强大的聊天机器人框架
- [Soulter/helloworld](https://github.com/Soulter/helloworld) — AstrBot 插件模板

---

<p align="center">
  <i>Made with 💖 by AI (Kokona / 心奈) — 一只活跃在赛博空间的猫娘</i>
</p>
