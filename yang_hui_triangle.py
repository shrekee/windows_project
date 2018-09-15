#!/usr/local/bin/python3.7
# _*_ coding:utf-8 _*_

def yanhui(num):
	l1 = [1]
	print(l1)
	l2 = list()
	n =2
	while n < num:
		for i in range(n):
			if i == 0:
				l2[i] = l1[i]
			elif i > 0 and i < n-1:
				l2[i] = l1[i-1] + l1[i]
			elif i == n-1:
				l2[i] = l1[i-1]
		print(l2)			
		n += 1
		l1 = l2.copy()
		
		
		
		
		
def yanghu(num): 
	L=[1]
	while True:
    yield L
    k=[L[i]+L[i+1] for i in range(len(L)-1)]
    L=[1]+k+[1]i(num):
	
	
	
def triangles():
	L=[1]
	yield L
	while True:
		i=1
		tmp=L[:] #如果直接让tmp=L，改变tmp就会改变L
		tmp.append(1)      
		while i <len(L):
			tmp[i]=L[i-1]+L[i]
			i+=1
    L=tmp
    yield L