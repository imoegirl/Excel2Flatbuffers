import xlrd
from datetime import date, datetime
import sys
import os

__excel_extension = 'xlsx'

__support_datatypes = [
	'string',
	'int32',
	'int64',
	'float',
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

def __export_all_excel_to_fbs(excel_root_path, target_fbs_path):
	for root, dirs, files in os.walk(excel_root_path, topdown=True):
		for name in files:
			file_path = os.path.join(root, name)
			if file_path.endswith(__excel_extension) and not name.startswith('~'):
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


def __get_all_fbs_file(root_path):
	file_list = []
	for root, dirs, files in os.walk(root_path):
		for file in files:
			file_path = os.path.join(root, file)
			file_list.append(file_path)
	return file_list


def __generate_target_file(fbs_file, target_folder_name, language_sign):
	root_path = os.getcwd()
	flatc_path = os.path.join(root_path, 'flatc/flatc.exe')
	target_path = os.path.join(root_path, target_folder_name)
	command = '{} --{} -o {} {} --gen-onefile'.format(flatc_path, language_sign, target_path, fbs_file)
	os.system(command)


def __generate_target(target_folder_name, language_sign):
	print('生成 {} 代码'.format(language_sign))
	fbs_path_list = __get_all_fbs_file(fbs_root_path)
	for file_path in fbs_path_list:
		__generate_target_file(file_path, target_folder_name, language_sign)



bytes_root_path = os.path.join(os.getcwd(), 'generated_bytes')
excel_root_path = os.path.join(os.getcwd(), 'excel')
fbs_root_path = os.path.join(os.getcwd(), 'generated_fbs')


def run():
	print('---------------- 生成fbs文件, 生成不同语言代码 ----------------')
	__export_all_excel_to_fbs(excel_root_path, bytes_root_path)
	__generate_target('generated_python', 'python')	# 生成Python代码是必须的，因为要用来打包数据
	__generate_target('generated_csharp', 'csharp')
	__generate_target('generated_go', 'go')

	# 还可以自己扩展，生成指定语言的代码