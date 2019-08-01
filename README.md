# Excel2Flatbuffers
此工具的初衷是为了方便游戏开发中的配表数据组织。

此工具的目标如下:

1. 将 Excel 表结构翻译成目标语言的 flatbuffer 类 (这一步首先Python会将 excel 生成flatbuffer的fbs文件，然后通过flatc生成对应语言的代码)
2. 将 Excel 表数据导出成 flatbuffers 结构的二进制文件
3. 自动生成 C# 读取解析 flatbuffers 文件的代码 (这里主要是为了客户端, Unity3D, 其他语言读取和解析 flatbuffers 二进制文件代码可以手动写，或者加一下python脚本去生成)

### 当前状态: 正在开发中...