# Excel2Flatbuffers
此工具为了方便在游戏开发中，将 Excel 配表数据，以 flatbuffers 的形式存储，并将表结构转为 flatbuffers 代码，然后自动生成客户端 (**Unity3D**) 数据加载解析代码，其他语言加载逻辑需要手写（因为我不会Go语言），例如服务器的Go语言端。

> **客户端的数据加载解析逻辑可以不使用本工具的实现逻辑，自己按习惯的方式实现**



## 工具内部做的事情如下

- [x] 将 Excel 表结构解析成 flatbuffers 的 fbs 文件

- [x] 通过 flatc 生成目标语言 flatbuffers 代码 (**C#或其他**)

- [x] 将 excel 表数据按 flatbuffers 的结构，将每一个表打包成二进制文件。

- [ ] 生成 Unity3D 客户端加载解析二进制文件代码 (**这一步可以不用本工具生成的代码，可自己手写**)

## 如何使用

`cd Excel2Flatbuffers` 进入工具目录

然后执行

```python run.py```

> 工具用到了`xlrd`和`flatbuffers`，如果运行报错，提示没有安装这两个模块，需要先使用pip3安装
>
> 这个工具用到的Python是 python3.7.2，应该 python3.x 都可以运行吧



### 详细的说明文档，以及一些预先目录清理工作，晚点补充