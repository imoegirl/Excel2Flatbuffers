// automatically generated by the FlatBuffers compiler, do not modify



use std::mem;
use std::cmp::Ordering;

extern crate flatbuffers;
use self::flatbuffers::EndianScalar;

pub enum PlayConditionConfigRowDataOffset {}
#[derive(Copy, Clone, Debug, PartialEq)]

pub struct PlayConditionConfigRowData<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for PlayConditionConfigRowData<'a> {
    type Inner = PlayConditionConfigRowData<'a>;
    #[inline]
    fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
        Self {
            _tab: flatbuffers::Table { buf: buf, loc: loc },
        }
    }
}

impl<'a> PlayConditionConfigRowData<'a> {
    #[inline]
    pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
        PlayConditionConfigRowData {
            _tab: table,
        }
    }
    #[allow(unused_mut)]
    pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
        _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
        args: &'args PlayConditionConfigRowDataArgs<'args>) -> flatbuffers::WIPOffset<PlayConditionConfigRowData<'bldr>> {
      let mut builder = PlayConditionConfigRowDataBuilder::new(_fbb);
      if let Some(x) = args.ClothesCondition { builder.add_ClothesCondition(x); }
      builder.add_StyleNum(args.StyleNum);
      builder.add_StyleCondition(args.StyleCondition);
      if let Some(x) = args.EndTime { builder.add_EndTime(x); }
      if let Some(x) = args.OpenTime { builder.add_OpenTime(x); }
      builder.add_ID(args.ID);
      builder.finish()
    }

    pub const VT_ID: flatbuffers::VOffsetT = 4;
    pub const VT_OPENTIME: flatbuffers::VOffsetT = 6;
    pub const VT_ENDTIME: flatbuffers::VOffsetT = 8;
    pub const VT_STYLECONDITION: flatbuffers::VOffsetT = 10;
    pub const VT_STYLENUM: flatbuffers::VOffsetT = 12;
    pub const VT_CLOTHESCONDITION: flatbuffers::VOffsetT = 14;

  #[inline]
  pub fn ID(&self) -> i32 {
    self._tab.get::<i32>(PlayConditionConfigRowData::VT_ID, Some(0)).unwrap()
  }
  #[inline]
  pub fn OpenTime(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(PlayConditionConfigRowData::VT_OPENTIME, None)
  }
  #[inline]
  pub fn EndTime(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(PlayConditionConfigRowData::VT_ENDTIME, None)
  }
  #[inline]
  pub fn StyleCondition(&self) -> i32 {
    self._tab.get::<i32>(PlayConditionConfigRowData::VT_STYLECONDITION, Some(0)).unwrap()
  }
  #[inline]
  pub fn StyleNum(&self) -> i32 {
    self._tab.get::<i32>(PlayConditionConfigRowData::VT_STYLENUM, Some(0)).unwrap()
  }
  #[inline]
  pub fn ClothesCondition(&self) -> Option<&'a str> {
    self._tab.get::<flatbuffers::ForwardsUOffset<&str>>(PlayConditionConfigRowData::VT_CLOTHESCONDITION, None)
  }
}

pub struct PlayConditionConfigRowDataArgs<'a> {
    pub ID: i32,
    pub OpenTime: Option<flatbuffers::WIPOffset<&'a  str>>,
    pub EndTime: Option<flatbuffers::WIPOffset<&'a  str>>,
    pub StyleCondition: i32,
    pub StyleNum: i32,
    pub ClothesCondition: Option<flatbuffers::WIPOffset<&'a  str>>,
}
impl<'a> Default for PlayConditionConfigRowDataArgs<'a> {
    #[inline]
    fn default() -> Self {
        PlayConditionConfigRowDataArgs {
            ID: 0,
            OpenTime: None,
            EndTime: None,
            StyleCondition: 0,
            StyleNum: 0,
            ClothesCondition: None,
        }
    }
}
pub struct PlayConditionConfigRowDataBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> PlayConditionConfigRowDataBuilder<'a, 'b> {
  #[inline]
  pub fn add_ID(&mut self, ID: i32) {
    self.fbb_.push_slot::<i32>(PlayConditionConfigRowData::VT_ID, ID, 0);
  }
  #[inline]
  pub fn add_OpenTime(&mut self, OpenTime: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(PlayConditionConfigRowData::VT_OPENTIME, OpenTime);
  }
  #[inline]
  pub fn add_EndTime(&mut self, EndTime: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(PlayConditionConfigRowData::VT_ENDTIME, EndTime);
  }
  #[inline]
  pub fn add_StyleCondition(&mut self, StyleCondition: i32) {
    self.fbb_.push_slot::<i32>(PlayConditionConfigRowData::VT_STYLECONDITION, StyleCondition, 0);
  }
  #[inline]
  pub fn add_StyleNum(&mut self, StyleNum: i32) {
    self.fbb_.push_slot::<i32>(PlayConditionConfigRowData::VT_STYLENUM, StyleNum, 0);
  }
  #[inline]
  pub fn add_ClothesCondition(&mut self, ClothesCondition: flatbuffers::WIPOffset<&'b  str>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(PlayConditionConfigRowData::VT_CLOTHESCONDITION, ClothesCondition);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> PlayConditionConfigRowDataBuilder<'a, 'b> {
    let start = _fbb.start_table();
    PlayConditionConfigRowDataBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<PlayConditionConfigRowData<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

pub enum PlayConditionConfigOffset {}
#[derive(Copy, Clone, Debug, PartialEq)]

pub struct PlayConditionConfig<'a> {
  pub _tab: flatbuffers::Table<'a>,
}

impl<'a> flatbuffers::Follow<'a> for PlayConditionConfig<'a> {
    type Inner = PlayConditionConfig<'a>;
    #[inline]
    fn follow(buf: &'a [u8], loc: usize) -> Self::Inner {
        Self {
            _tab: flatbuffers::Table { buf: buf, loc: loc },
        }
    }
}

impl<'a> PlayConditionConfig<'a> {
    #[inline]
    pub fn init_from_table(table: flatbuffers::Table<'a>) -> Self {
        PlayConditionConfig {
            _tab: table,
        }
    }
    #[allow(unused_mut)]
    pub fn create<'bldr: 'args, 'args: 'mut_bldr, 'mut_bldr>(
        _fbb: &'mut_bldr mut flatbuffers::FlatBufferBuilder<'bldr>,
        args: &'args PlayConditionConfigArgs<'args>) -> flatbuffers::WIPOffset<PlayConditionConfig<'bldr>> {
      let mut builder = PlayConditionConfigBuilder::new(_fbb);
      if let Some(x) = args.datalist { builder.add_datalist(x); }
      builder.finish()
    }

    pub const VT_DATALIST: flatbuffers::VOffsetT = 4;

  #[inline]
  pub fn datalist(&self) -> Option<flatbuffers::Vector<'a, flatbuffers::ForwardsUOffset<PlayConditionConfigRowData<'a>>>> {
    self._tab.get::<flatbuffers::ForwardsUOffset<flatbuffers::Vector<flatbuffers::ForwardsUOffset<PlayConditionConfigRowData<'a>>>>>(PlayConditionConfig::VT_DATALIST, None)
  }
}

pub struct PlayConditionConfigArgs<'a> {
    pub datalist: Option<flatbuffers::WIPOffset<flatbuffers::Vector<'a , flatbuffers::ForwardsUOffset<PlayConditionConfigRowData<'a >>>>>,
}
impl<'a> Default for PlayConditionConfigArgs<'a> {
    #[inline]
    fn default() -> Self {
        PlayConditionConfigArgs {
            datalist: None,
        }
    }
}
pub struct PlayConditionConfigBuilder<'a: 'b, 'b> {
  fbb_: &'b mut flatbuffers::FlatBufferBuilder<'a>,
  start_: flatbuffers::WIPOffset<flatbuffers::TableUnfinishedWIPOffset>,
}
impl<'a: 'b, 'b> PlayConditionConfigBuilder<'a, 'b> {
  #[inline]
  pub fn add_datalist(&mut self, datalist: flatbuffers::WIPOffset<flatbuffers::Vector<'b , flatbuffers::ForwardsUOffset<PlayConditionConfigRowData<'b >>>>) {
    self.fbb_.push_slot_always::<flatbuffers::WIPOffset<_>>(PlayConditionConfig::VT_DATALIST, datalist);
  }
  #[inline]
  pub fn new(_fbb: &'b mut flatbuffers::FlatBufferBuilder<'a>) -> PlayConditionConfigBuilder<'a, 'b> {
    let start = _fbb.start_table();
    PlayConditionConfigBuilder {
      fbb_: _fbb,
      start_: start,
    }
  }
  #[inline]
  pub fn finish(self) -> flatbuffers::WIPOffset<PlayConditionConfig<'a>> {
    let o = self.fbb_.end_table(self.start_);
    flatbuffers::WIPOffset::new(o.value())
  }
}

