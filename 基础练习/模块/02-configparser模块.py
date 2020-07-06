import configparser

config = configparser.ConfigParser()
config.read('text.ini')

# 获取sections
# print(config.sections())

# 获取sections下的所有options
# print(config.options('section1'))

# 获取items
# print(config.items('section1'))

# 获取单一的items
ret = config.get('section1',"k1")
print(ret,type(ret))
