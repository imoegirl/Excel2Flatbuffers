
code = '''
def DynamicFunction():
	print('I\\'m Dynamic Function')

DynamicFunction()
'''

file_name = 'ddd.py'


with open(file_name, 'w') as f:
	f.write(code)

# execfile(file_name)
exec(code)

