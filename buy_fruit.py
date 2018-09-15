#!/usr/local/bin/python3
#_*_ coding:utf-8 _*_
#购买水果的简单python脚本，可以简单判断：输入是否合法，若不合法则会要求重新输入。
#定义一个菜单函数，自动打印（形参）传入的键值对。
def menu(dic):
	print('*'*40)
	for i in dic.keys():
		print("%s的价格是：%.2f 元/500克"%(i,dic[i]))
	print('*'*40)
def getname(dic):
	name = input("请输入您想购买的水果的名称（grape/apple/banana）")
	if name not in dic.keys():
		return getname(dic)
	return name
def getnum():
	num = input("请输入想购买的克数，比如500 克，则输入“500”即可")
	if num.isdigit() and int(num) > 0:
		pass
	else:
		return getnum()
	return num	

if __name__ == '__main__':
	dic = dict(apple=5.0,banana=3.5,grape=3)
	menu(dic)
	name = getname(dic)
	num = getnum()
	print("您购买的%s克的%s 的价格为：%.2f 元"%(num,name,(int(num)/500*dic[name])))