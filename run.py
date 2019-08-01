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


if __name__ == '__main__':
	do_serialize()
	# de_serialize()