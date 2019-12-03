# Excel2Flatbuffers
此工具为了方便在游戏开发中，将 Excel 配表数据，以 flatbuffers 的形式存储，并将表结构转为 flatbuffers 代码，然后自动生成客户端 (**Unity3D**) 数据加载解析代码，其他语言加载逻辑需要手写（因为我不会Go语言），例如服务器的Go语言端。

> **客户端的数据加载解析逻辑可以不使用本工具的实现逻辑，自己按习惯的方式实现**



## 工具内部做的事情如下

- [x] 将 Excel 表结构解析成 flatbuffers 的 fbs 文件

- [x] 通过 flatc 生成目标语言 flatbuffers 代码 (**C#或其他**)

- [x] 将 excel 表数据按 flatbuffers 的结构，将每一个表打包成二进制文件。

## 如何使用

`cd Excel2Flatbuffers` 进入工具目录

然后执行

```python run.py```

> 工具用到了`xlrd`和`flatbuffers`，如果运行报错，提示没有安装这两个模块，需要先使用pip3安装
>
> 这个工具用到的Python是 python3.7.2，应该 python3.x 都可以运行吧

## 在 Unity 中如何加载和使用生成后的代码和 bytes 文件，代码如下 (需根据自己的工程自己定制)

```csharp
private void LoadConfigData()
{
    string path = Path.Combine(Application.dataPath, "DanceMusicConfig.bytes");
    byte[] bytes = File.ReadAllBytes(path);

    ByteBuffer bb = new ByteBuffer(bytes);
    DanceMusicConfig config = DanceMusicConfig.GetRootAsDanceMusicConfig(bb);
    for(int i = 0; i < config.DatalistLength; ++i)
    {
        // 表中每一行的数据
        DanceMusicConfigRowData rowData = config.Datalist(i).Value;
        string noteName = rowData.NoteName;
        string bgmName = rowData.BGMName;
        int totalTime = rowData.TotalTime;
        float totalTime2 = rowData.TotalTime2;

        // -- 可以自己建立一个数据类，然后将上面的数值存到自己的数据类中，去使用
    }
}
```

> 对于任何一个表，最后生成的代码中， XXXConfig，就是整个表的类，XXXConfigRowData，这是对应这个表中的一行数据

