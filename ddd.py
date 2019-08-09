import generated_python.TShowMusicsConfigRowData as TShowMusicsConfigRowData
import generated_python.TShowMusicsConfig as TShowMusicsConfig
import flatbuffers

builder = flatbuffers.Builder(1)

dataId = 0
noteName = builder.CreateString('Note1')
bgmName = builder.CreateString('bgm1')
totalTime = 128

TShowMusicsConfigRowData.TShowMusicsConfigRowDataStart(builder)
TShowMusicsConfigRowData.TShowMusicsConfigRowDataAddID(builder, dataId)
TShowMusicsConfigRowData.TShowMusicsConfigRowDataAddNoteName(builder, noteName)
TShowMusicsConfigRowData.TShowMusicsConfigRowDataAddBGMName(builder, bgmName)
TShowMusicsConfigRowData.TShowMusicsConfigRowDataAddTotalTime(builder, totalTime)
rowData1 = TShowMusicsConfigRowData.TShowMusicsConfigRowDataEnd(builder)

dataId = 1
noteName = builder.CreateString('Note2')
bgmName = builder.CreateString('bgm2')
totalTime = 130

TShowMusicsConfigRowData.TShowMusicsConfigRowDataStart(builder)
TShowMusicsConfigRowData.TShowMusicsConfigRowDataAddID(builder, dataId)
TShowMusicsConfigRowData.TShowMusicsConfigRowDataAddNoteName(builder, noteName)
TShowMusicsConfigRowData.TShowMusicsConfigRowDataAddBGMName(builder, bgmName)
TShowMusicsConfigRowData.TShowMusicsConfigRowDataAddTotalTime(builder, totalTime)
rowData2 = TShowMusicsConfigRowData.TShowMusicsConfigRowDataEnd(builder)

TShowMusicsConfig.TShowMusicsConfigStartDatalistVector(builder, 2)
builder.PrependUOffsetTRelative(rowData1)
builder.PrependUOffsetTRelative(rowData2)
data_array = builder.EndVector(2)

TShowMusicsConfig.TShowMusicsConfigStart(builder)
TShowMusicsConfig.TShowMusicsConfigAddDatalist(builder, data_array)
final_data = TShowMusicsConfig.TShowMusicsConfigEnd(builder)

builder.Finish(final_data)

buf = builder.Output()

with open('./generated_bytes/music.bytes', 'wb') as f:
	f.write(buf)