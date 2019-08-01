# Excel2Flatbuffers
此工具为了方便在游戏开发中，将 Excel 配表数据，以 flatbuffers 的形式存储，并将表结构转为 flatbuffers 代码，然后自动生成客户端 (**Unity3D**) 数据加载解析代码，其他语言加载逻辑需要手写（因为我不会Go语言），例如服务器的Go语言端。

> **客户端的数据加载解析逻辑可以不使用本工具的实现逻辑，自己按习惯的方式实现**





工具内部做的事情如下

1. 将 Excel 表结构解析成 flatbuffers 的 fbs 文件

2. 通过 flatc 生成目标语言 flatbuffers 代码 (**C#或其他**)

3. 将 excel 表数据按 flatbuffers 的结构，将每一个表打包成二进制文件。

4. 生成 Unity3D 客户端加载解析二进制文件代码 (**这一步可以不用本工具生成的代码，可自己手写**)




### 当前状态: 正在开发中...（预计一周内写完）