import os

excel_row1_data = [
	{
		'field_name': 'ID',
		'field_value': 1,
		'field_type': 'int32'
	},
	{
		'field_name': 'NoteName',
		'field_value': 'Note1',
		'field_type': 'string'
	},
	{
		'field_name': 'BGMName',
		'field_value': 'BGM1',
		'field_type': 'string'
	},
	{
		'field_name': 'TotalTime',
		'field_value': 128,
		'field_type': 'int32'
	},
]

excel_row2_data = [
	{
		'field_name': 'ID',
		'field_value': 2,
		'field_type': 'int32'
	},
	{
		'field_name': 'NoteName',
		'field_value': 'Note2',
		'field_type': 'string'
	},
	{
		'field_name': 'BGMName',
		'field_value': 'BGM2',
		'field_type': 'string'
	},
	{
		'field_name': 'TotalTime',
		'field_value': 129,
		'field_type': 'int32'
	},
]

excel_row3_data = [
	{
		'field_name': 'ID',
		'field_value': 3,
		'field_type': 'int32'
	},
	{
		'field_name': 'NoteName',
		'field_value': 'Note3',
		'field_type': 'string'
	},
	{
		'field_name': 'BGMName',
		'field_value': 'BGM3',
		'field_type': 'string'
	},
	{
		'field_name': 'TotalTime',
		'field_value': 130,
		'field_type': 'int32'
	},
]

excel_row_list = [
	excel_row1_data,
	excel_row2_data,
	excel_row3_data
]


# singleModName = 'TShowMusicsConfigRowData'
# listModName = 'TShowMusicsConfig'

def get_assign_code(mod_name, field_name, field_value, field_type, index):
	if field_type == 'string':
		value_code = "{}{}".format(field_name, index)
	else:
		value_code = field_value
	code = "{ModName}.{ModName}Add{FieldName}(builder, {ValueCode})".format(
				ModName = mod_name, FieldName = field_name, ValueCode = value_code)
	return code


def get_single_data_code(mod_name, row_data, index):
	code = \
"""
{VariableCreate}
{ModName}.{ModName}Start(builder)
{AssignCode}
single_data{Index} = {ModName}.{ModName}End(builder)
"""
	
	variable_create_code = ''
	for field in row_data:
		if field['field_type'] == 'string':
			variable_create_code += "{}{} = builder.CreateString('{}')".format(field['field_name'], index, field['field_value'])
			variable_create_code += '\n'
	

	assign_code = ''
	for field in row_data:
		assign_code += get_assign_code(
											mod_name, 
											field['field_name'],
											field['field_value'],
											field['field_type'],
											index
										)
		assign_code += '\n'

	assign_code = assign_code[:-1]
	code = code.format(VariableCreate = variable_create_code, ModName = mod_name, AssignCode = assign_code, Index = index)
	return code


def get_list_data_code(mod_name, single_mod_name, list_data):
	row_count = len(list_data)
	all_assign_code = ''
	index = 0
	for row_data in list_data:
		all_assign_code += get_single_data_code(single_mod_name, row_data, index)
		index += 1
		all_assign_code += '\n'

	offset_code = ''
	for index in range(0, row_count):
		data_name = "single_data{}".format(index)
		offset_code += "builder.PrependUOffsetTRelative({})".format(data_name)
		offset_code += '\n'

	code = \
"""
import generated_python.{SingleModName} as {SingleModName}
import generated_python.{ModName} as {ModName}
import flatbuffers

builder = flatbuffers.Builder(1)

{AllAssignCode}
{ModName}.{ModName}StartDatalistVector(builder, {DataCount})
{OffsetCode}
data_array = builder.EndVector({DataCount})

{ModName}.{ModName}Start(builder)
{ModName}.{ModName}AddDatalist(builder, data_array)
final_data = {ModName}.{ModName}End(builder)
builder.Finish(final_data)
buf = builder.Output()
""".format(
		SingleModName = single_mod_name,
		ModName = mod_name,
		AllAssignCode = all_assign_code,
		DataCount = row_count,
		OffsetCode = offset_code
	)
	
	return code


def generate_bytes(mod_name, single_mod_name, bytes_root_path, excel_row_list):
	list_code = get_list_data_code(mod_name, single_mod_name, excel_row_list)
	byte_file_path = os.path.join(bytes_root_path, "{}.bytes".format(mod_name))
	byte_file_path = byte_file_path.replace('\\', '/')
	code = """
{ListCode}

with open('{ByteFilePath}', 'wb') as f:
	f.write(buf)
""".format(ListCode = list_code, ByteFilePath = byte_file_path)
	exec(code)
	print('Generated: ', byte_file_path)



bytes_root_path = os.path.join(os.getcwd(), 'generated_bytes')
mod_name = 'TShowMusicsConfig'
single_mod_name = 'TShowMusicsConfigRowData'

generate_bytes(mod_name, single_mod_name, bytes_root_path, excel_row_list)
