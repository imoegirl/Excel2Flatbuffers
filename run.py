import fbs_generator
import bytes_generator


if __name__ == '__main__':
	fbs_generator.run()		# 必须先生成代码
	bytes_generator.run()	# 然后将excel数据打包成 flatbuffers 的二进制

