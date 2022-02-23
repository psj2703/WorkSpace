
import re

dates = [
    ''
]

regex =  '^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$'

for data in dates :
    matchObj = re.match(regex, dates)
    result = (lambda x : True if x != None else False)(matchObj)
    print(f'{data} {result}')



regex = re.compile('^[\w-]+@[a-zA-Z0-9-]+\.[a-zA-Z0_9.]+$')

datas = [
    ''
]

for data in datas:
    matchObj = regex.match(data)
    result = (lambda x : True if x != None else False)







