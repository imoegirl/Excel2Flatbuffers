# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class TShowMusicsConfigRowData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTShowMusicsConfigRowData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TShowMusicsConfigRowData()
        x.Init(buf, n + offset)
        return x

    # TShowMusicsConfigRowData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TShowMusicsConfigRowData
    def ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TShowMusicsConfigRowData
    def NoteName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TShowMusicsConfigRowData
    def BGMName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TShowMusicsConfigRowData
    def TotalTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def TShowMusicsConfigRowDataStart(builder): builder.StartObject(4)
def TShowMusicsConfigRowDataAddID(builder, ID): builder.PrependInt32Slot(0, ID, 0)
def TShowMusicsConfigRowDataAddNoteName(builder, NoteName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(NoteName), 0)
def TShowMusicsConfigRowDataAddBGMName(builder, BGMName): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(BGMName), 0)
def TShowMusicsConfigRowDataAddTotalTime(builder, TotalTime): builder.PrependInt32Slot(3, TotalTime, 0)
def TShowMusicsConfigRowDataEnd(builder): return builder.EndObject()
