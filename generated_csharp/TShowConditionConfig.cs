// <auto-generated>
//  automatically generated by the FlatBuffers compiler, do not modify
// </auto-generated>

using global::System;
using global::FlatBuffers;

public struct TShowConditionConfigRowData : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static TShowConditionConfigRowData GetRootAsTShowConditionConfigRowData(ByteBuffer _bb) { return GetRootAsTShowConditionConfigRowData(_bb, new TShowConditionConfigRowData()); }
  public static TShowConditionConfigRowData GetRootAsTShowConditionConfigRowData(ByteBuffer _bb, TShowConditionConfigRowData obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p.bb_pos = _i; __p.bb = _bb; }
  public TShowConditionConfigRowData __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public int ID { get { int o = __p.__offset(4); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }
  public string OpenTime { get { int o = __p.__offset(6); return o != 0 ? __p.__string(o + __p.bb_pos) : null; } }
#if ENABLE_SPAN_T
  public Span<byte> GetOpenTimeBytes() { return __p.__vector_as_span(6); }
#else
  public ArraySegment<byte>? GetOpenTimeBytes() { return __p.__vector_as_arraysegment(6); }
#endif
  public byte[] GetOpenTimeArray() { return __p.__vector_as_array<byte>(6); }
  public string EndTime { get { int o = __p.__offset(8); return o != 0 ? __p.__string(o + __p.bb_pos) : null; } }
#if ENABLE_SPAN_T
  public Span<byte> GetEndTimeBytes() { return __p.__vector_as_span(8); }
#else
  public ArraySegment<byte>? GetEndTimeBytes() { return __p.__vector_as_arraysegment(8); }
#endif
  public byte[] GetEndTimeArray() { return __p.__vector_as_array<byte>(8); }
  public int StyleCondition { get { int o = __p.__offset(10); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }
  public int StyleNum { get { int o = __p.__offset(12); return o != 0 ? __p.bb.GetInt(o + __p.bb_pos) : (int)0; } }
  public string ClothesCondition { get { int o = __p.__offset(14); return o != 0 ? __p.__string(o + __p.bb_pos) : null; } }
#if ENABLE_SPAN_T
  public Span<byte> GetClothesConditionBytes() { return __p.__vector_as_span(14); }
#else
  public ArraySegment<byte>? GetClothesConditionBytes() { return __p.__vector_as_arraysegment(14); }
#endif
  public byte[] GetClothesConditionArray() { return __p.__vector_as_array<byte>(14); }

  public static Offset<TShowConditionConfigRowData> CreateTShowConditionConfigRowData(FlatBufferBuilder builder,
      int ID = 0,
      StringOffset OpenTimeOffset = default(StringOffset),
      StringOffset EndTimeOffset = default(StringOffset),
      int StyleCondition = 0,
      int StyleNum = 0,
      StringOffset ClothesConditionOffset = default(StringOffset)) {
    builder.StartObject(6);
    TShowConditionConfigRowData.AddClothesCondition(builder, ClothesConditionOffset);
    TShowConditionConfigRowData.AddStyleNum(builder, StyleNum);
    TShowConditionConfigRowData.AddStyleCondition(builder, StyleCondition);
    TShowConditionConfigRowData.AddEndTime(builder, EndTimeOffset);
    TShowConditionConfigRowData.AddOpenTime(builder, OpenTimeOffset);
    TShowConditionConfigRowData.AddID(builder, ID);
    return TShowConditionConfigRowData.EndTShowConditionConfigRowData(builder);
  }

  public static void StartTShowConditionConfigRowData(FlatBufferBuilder builder) { builder.StartObject(6); }
  public static void AddID(FlatBufferBuilder builder, int ID) { builder.AddInt(0, ID, 0); }
  public static void AddOpenTime(FlatBufferBuilder builder, StringOffset OpenTimeOffset) { builder.AddOffset(1, OpenTimeOffset.Value, 0); }
  public static void AddEndTime(FlatBufferBuilder builder, StringOffset EndTimeOffset) { builder.AddOffset(2, EndTimeOffset.Value, 0); }
  public static void AddStyleCondition(FlatBufferBuilder builder, int StyleCondition) { builder.AddInt(3, StyleCondition, 0); }
  public static void AddStyleNum(FlatBufferBuilder builder, int StyleNum) { builder.AddInt(4, StyleNum, 0); }
  public static void AddClothesCondition(FlatBufferBuilder builder, StringOffset ClothesConditionOffset) { builder.AddOffset(5, ClothesConditionOffset.Value, 0); }
  public static Offset<TShowConditionConfigRowData> EndTShowConditionConfigRowData(FlatBufferBuilder builder) {
    int o = builder.EndObject();
    return new Offset<TShowConditionConfigRowData>(o);
  }
};

public struct TShowConditionConfig : IFlatbufferObject
{
  private Table __p;
  public ByteBuffer ByteBuffer { get { return __p.bb; } }
  public static TShowConditionConfig GetRootAsTShowConditionConfig(ByteBuffer _bb) { return GetRootAsTShowConditionConfig(_bb, new TShowConditionConfig()); }
  public static TShowConditionConfig GetRootAsTShowConditionConfig(ByteBuffer _bb, TShowConditionConfig obj) { return (obj.__assign(_bb.GetInt(_bb.Position) + _bb.Position, _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __p.bb_pos = _i; __p.bb = _bb; }
  public TShowConditionConfig __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public TShowConditionConfigRowData? Datalist(int j) { int o = __p.__offset(4); return o != 0 ? (TShowConditionConfigRowData?)(new TShowConditionConfigRowData()).__assign(__p.__indirect(__p.__vector(o) + j * 4), __p.bb) : null; }
  public int DatalistLength { get { int o = __p.__offset(4); return o != 0 ? __p.__vector_len(o) : 0; } }

  public static Offset<TShowConditionConfig> CreateTShowConditionConfig(FlatBufferBuilder builder,
      VectorOffset datalistOffset = default(VectorOffset)) {
    builder.StartObject(1);
    TShowConditionConfig.AddDatalist(builder, datalistOffset);
    return TShowConditionConfig.EndTShowConditionConfig(builder);
  }

  public static void StartTShowConditionConfig(FlatBufferBuilder builder) { builder.StartObject(1); }
  public static void AddDatalist(FlatBufferBuilder builder, VectorOffset datalistOffset) { builder.AddOffset(0, datalistOffset.Value, 0); }
  public static VectorOffset CreateDatalistVector(FlatBufferBuilder builder, Offset<TShowConditionConfigRowData>[] data) { builder.StartVector(4, data.Length, 4); for (int i = data.Length - 1; i >= 0; i--) builder.AddOffset(data[i].Value); return builder.EndVector(); }
  public static VectorOffset CreateDatalistVectorBlock(FlatBufferBuilder builder, Offset<TShowConditionConfigRowData>[] data) { builder.StartVector(4, data.Length, 4); builder.Add(data); return builder.EndVector(); }
  public static void StartDatalistVector(FlatBufferBuilder builder, int numElems) { builder.StartVector(4, numElems, 4); }
  public static Offset<TShowConditionConfig> EndTShowConditionConfig(FlatBufferBuilder builder) {
    int o = builder.EndObject();
    return new Offset<TShowConditionConfig>(o);
  }
};

