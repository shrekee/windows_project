# _*_ coding:utf-8 _*_

__author__ = 'lwqiang'

import sys
import string
import random
def passgen(num):
    pwd = ''
    all_choice = string.ascii_letters + string.digits
    password = ''.join(random.choices(all_choice, k=num))
    print(password)

if __name__ == "__main__":
    passgen(int(sys.argv[1]))

