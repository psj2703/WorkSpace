import re

# 1. Group 그룹

'''
02-512-3232
010-2343-3333
1-32-321
aaa-bbb-ccc
010-23435-5555
010-2343-55555
'''

# 1) 매칭되는 문자열 한개
str1 = '010-2343-3333'
result = re.match('\d{2,3}-\d{3,4}-\d{4}$', str1)
print(result)

# 2) 매칭되는 문자열 여러개
str2 = '02-512-3232,010-2343-3333,1-32-321,aaa-bbb-ccc,010-23435-5555,010-2343-55555'
results = re.finditer('\d{2,3}-\d{3,4}-(\d{4})(?=|$)', str2)

for result in results:
    print(result.group(1))

# 2. substitution (교체)
str3 = '010-2343-3333'
result = re.sub('(?<=\d{3}-\d{4}-)\d{4}', '****', str3)
print(result)
