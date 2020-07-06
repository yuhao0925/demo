import re

# \w/W匹配数字字母下划线
# print(re.findall("\w",'aBbcd_()=.'))
# print(re.findall("\W",'aBbcd_()=.*/'))

# print(re.findall("\d",'aBbc1d_()=2.*4/'))
# print(re.findall("\D",'aBbc1d_()=2.*4/'))

# print(re.findall('\Ayuhao','yuhao is yuhao1 man'))

# print(re.findall('\Ayuhao','yuhao is yuhao1 man'))

# 1  .:除了\n之外的任意一个字符,指定re.DOTALL之后才能匹配换行符
# print(re.findall("a.b", 'a1b' 'a2b' 'a b' 'a*b' 'a\nb'))
# ['a1b', 'a2b', 'a b', 'a*b']

# 2  #:左侧字符重复0次或者无穷次,性格贪婪   ab*意思就是b可以是0个或者无穷个,但是a是必须要有的
# print(re.findall('ab*', 'a' 'abb' 'ab' 'abbbbbbbb' 'bbbbbb'))

# 3  +:左侧字符重复一次或者无穷次,性格贪婪
# print(re.findall('ab+', 'a abb abbbbb bbbbbb'))

# 4 ?:左侧字符重复0从或者1次,性格贪婪
# print(re.findall('ab?', 'a abbb ab bbbbbbbb'))
# ['a', 'ab', 'ab']


# 5 {n,m} 左侧字符重复n次到m次 性格贪婪 {n} 代表出现n次,多出现一次都不行
# print(re.findall('ab{2,5}', 'a ab abbb abbbbbbbbbbbb'))
# ['abbb', 'abbbbb']

# 6 []匹配指定字符  ^加到中括号内是指取反意思
# print(re.findall('a[0-9]b', 'a1b a*b a-b a=b'))
# print(re.findall('a[^1*-]b', 'a1b a*b a-b a=b'))
# print(re.findall('a[a-z]b', 'a1b a*b a-b a=b aeb'))
# print(re.findall('a[a-zA-Z]b','a1b a*b a-b a=b aeb aEb'))

# 7 \ 发生转义
# print(re.findall(r'a\\c','a\c a\\c a\\\\\c'))


# search
# result = re.search('yuhao', 'ale aayuhaoee feeaa')
# ret = result.group()
# print(ret)
# print(result)



# match
# result = re.match('yuhao', 'yuhao haha yuhao aa')
# ret = result.group()
# print(ret)
# print(result)

