# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class TShowConditionConfigRowData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTShowConditionConfigRowData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TShowConditionConfigRowData()
        x.Init(buf, n + offset)
        return x

    # TShowConditionConfigRowData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TShowConditionConfigRowData
    def ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TShowConditionConfigRowData
    def OpenTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TShowConditionConfigRowData
    def EndTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TShowConditionConfigRowData
    def StyleCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TShowConditionConfigRowData
    def StyleNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TShowConditionConfigRowData
    def ClothesCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def TShowConditionConfigRowDataStart(builder): builder.StartObject(6)
def TShowConditionConfigRowDataAddID(builder, ID): builder.PrependInt32Slot(0, ID, 0)
def TShowConditionConfigRowDataAddOpenTime(builder, OpenTime): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(OpenTime), 0)
def TShowConditionConfigRowDataAddEndTime(builder, EndTime): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(EndTime), 0)
def TShowConditionConfigRowDataAddStyleCondition(builder, StyleCondition): builder.PrependInt32Slot(3, StyleCondition, 0)
def TShowConditionConfigRowDataAddStyleNum(builder, StyleNum): builder.PrependInt32Slot(4, StyleNum, 0)
def TShowConditionConfigRowDataAddClothesCondition(builder, ClothesCondition): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ClothesCondition), 0)
def TShowConditionConfigRowDataEnd(builder): return builder.EndObject()