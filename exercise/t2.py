#_*_ coding:utf-8 _*_

import os
def is_num(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            return False
    else:
        return True

count = 0
for i in os.listdir('.'):
    if is_num(i):
        count +=1

print(count)

