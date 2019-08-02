import xlrd
from datetime import date, datetime
import sys
import os

test_file = './excel/走秀配置表.xlsx'
fbs_root_path = './generated_fbs/'

__excel_extension = 'xlsx'

__support_datatypes = [
	'string',
	'int32',
	'int64',
	'byte',
]


__row_code = """
table %s {
    %s
}
"""

__group_code = """
table %s {
    datalist:[%s];
}
"""

def export_all_excel_to_fbs(excel_root_path, target_fbs_path):
	for root, dirs, files in os.walk(excel_root_path, topdown=True):
		for name in files:
			file_path = os.path.join(root, name)
			if file_path.endswith(__excel_extension):
				__export_excel_to_fbs(file_path)

def __export_excel_to_fbs(excel_path):
	# 打开excel，分别将每一个sheet导出fbs
	wb = xlrd.open_workbook(excel_path)
	sheet_count = len(wb.sheet_names())
	sheet1 = wb.sheet_by_index(0)
	for x in range(0, sheet_count):
		sheet = wb.sheet_by_index(x)
		__export_sheet_to_fbs(sheet)


def __export_sheet_to_fbs(sheet):
	variable_dict = {}
	sheet_name = sheet.name
	row_table_name = sheet_name + 'RowData'
	group_table_name = sheet_name;
	header = sheet.row(0)
	for item in header:
		raw_data = item.value.split('#')[0].split(':')
		variable_name = raw_data[0]
		data_type = raw_data[1]
		if variable_name in variable_dict:
			print('存在相同的字段名: ', variable_name)
			print('异常退出')
			sys.exit()

		if not data_type in __support_datatypes:
			print('字段', variable_name, '的数据类型', data_type,'不在支持的列表中')
			print('异常退出')
			sys.exit()

		variable_dict[variable_name] = data_type
		# print(variable_name, data_type, data_type in support_datatype)

	# 组合变量定义代码字符串
	variables_str = ''
	for variable in variable_dict:
		data_type = variable_dict[variable]
		variables_str += '    %s:%s;\n' % (variable, data_type)

	variables_str = variables_str.strip(' \t\n\t')

	row_data_table_code_str = __row_code % (row_table_name, variables_str)

	# 组合列表代码字符串
	group_data_table_code_str = __group_code % (group_table_name, row_table_name)

	# 写入文件
	fbs_file_path = os.path.join(fbs_root_path, group_table_name + '.fbs')
	print('已生成: ', fbs_file_path)
	write_str = row_data_table_code_str + '\n' + group_data_table_code_str
	with open(fbs_file_path, 'w') as f:
		f.write(write_str)

# export_excel_to_fbs(test_file)
export_all_excel_to_fbs('./excel', './generated_fbs')

	# raw_data = item.split('text:')
	# data = raw_data[1].trim()
	# if data == '':
	# 	continue
	# print(data)

# for row in sheet1.get_rows():
# 	print(row)


