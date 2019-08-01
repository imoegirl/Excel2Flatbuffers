import generated_python.FBMonster as SFbMonster
import flatbuffers

output_bytes_file = './generated_bytes/fbmonster.bytes'

def do_serialize():
	builder = flatbuffers.Builder(0)
	name = builder.CreateString('JJCat')
	SFbMonster.FBMonsterStart(builder)
	SFbMonster.FBMonsterAddName(builder, name)
	SFbMonster.FBMonsterAddHp(builder, 100)
	SFbMonster.FBMonsterAddAttack(builder, 54)
	end_obj = SFbMonster.FBMonsterEnd(builder)
	builder.Finish(end_obj)

	buf = builder.Output()

	with open(output_bytes_file, 'wb') as f:
		f.write(buf);

def de_serialize():
	with open(output_bytes_file, 'rb') as f:
		buf = f.read()
		login_obj = cslogin.CSLogin.GetRootAsCSLogin(buf, 0)
		assert login_obj.Nickname() == 'FredShao'
		print(login_obj.Nickname())
		print(login_obj.Age())
		print(login_obj.Gender())


def read_all_excel_file_data():
	pass


def generate_fbs():
	pass


# 根据fbs生成Python代码，这一步是必须的，用来打包表数据为二进制
def flatc_fbs_to_python_code():
	pass

# 根据fbs生成C#代码
def flatc_fbs_to_csharp_code():
	pass

# 根据fbs生成Go代码
def flatc_fbs_to_go_code():
	pass

# 根据fbs生成Rust代码
def flatc_fbs_to_rust_code():
	pass

# 将所有的Excel表数据打包成flatbuffers结构的二进制文件
def pack_excel_data_to_binary():
	pass

# 拷贝生成的C#代码到某个地方
def copy_csharp_code_to():
	pass

# 拷贝生成的GO代码到某个地方
def copy_go_code_to():
	pass

# 拷贝打包后的表数据flatbuffers二进制文件到某个地方
def copy_excel_binary_file_to():
	pass


# 删除生成fbs文件
def delete_fbs_file():
	pass

# 删除生成的python代码
def delete_python_code():
	pass


if __name__ == '__main__':
	# do_serialize()
	# de_serialize()
	# 读取所有的Excel文件数据（必须）
	read_all_excel_file_data()

	# 根据Excel表结构，生成fbs文件（必须）
	generate_fbs()
	
	# 根据fbs文件生成Python代码（必须）
	flatc_fbs_to_python_code()
	
	# 将所有的表数据打包成二进制（必须）
	pack_excel_data_to_binary()

	# --------------------------------
	# 下面为非必须代码，根据需要自己修改
	# --------------------------------

	# 生成Unity3D客户端使用的C#代码（非必须，根据语言需要决定）
	flatc_fbs_to_csharp_code()

	# 生成服务器端使用的Go代码（非必须，根据语言需要决定）
	flatc_fbs_to_go_code()

	# 拷贝C#代码到Unity工程
	copy_csharp_code_to()

