1. 文件备份脚本------>李文强
	要求:
		1. 写明备份思路
		2. 备份脚本
		3. 脚本执行方法
		4. 体现函数应用
		
		思路:
		1.先打开一个文件(读的方式)-->f1,
		2.再打开一个文件(写的方式'w')--->f2
		3.然后把f1的内容读出来,写入f2中,
		4.分别关闭这两个文件.
		
	函数的思路:
		def my_copy(src,des):
			with open('src',r) as f1:
				f2 = open('des','w')
				f2.write(f1.read())
				f2.close()
				f1.close()
		my_copy('/root/123.txt','/tmp/123.txt')
		
2、文件或目录创建脚本  （ 创建文件或者目录？）
	要求：
		1、写明思路
		2、解释所应用模块
		3、备份脚本
		4、脚本执行方法


思路:
	1. 创建目录可以 import os 模块的中的 os.mkdir/makedirs(函数来是实现)
		其中,os.mkdir 只能创建单级目录, 而makedirs可以创建多级目录(类似 linux中的mkdir -p)
	
	2. 创建文件,则还是使用 python内建函数 open('','w')的方式来创建.
	3. 为了更严谨一些,在创建目录或者文件之前应该先判断下目录/文件是否已经存在了?
	
	脚本:
	import os
	def get_dir():
		d = input("please input the dir that you want to create...")
		if os.path.exists(d):
			print('%s 已经存在..请重新输入...')
			return get_dir()	#如果已存在则要求重新输入..
		#if  not os.path.exists(os.path.dirname(d)):
		#	return get_dir()	#如果输入不合法,(即路径输入错误,则递归输入..)
		
		os.makedirs('d')
		return d
		
3、使用常见模块
	要求：
		1、常见模块功能介绍
		2、常见模块使用方法
		
	常见的模块:
		1.getpass   常用方法:getpass.getpass() 用于获取密码时,不会明文显示在屏幕上.
		2.keyword	keyword.kwlist--->返回对象,而打印此对象,则会获取python的关键字列表
		3.sys	
			系统模块, 比如,sys.exit() 退出程序;sys.path保存python系统变量
			sys.agrv 可以传参给脚本
		5.random
			伪随机数生成模块.
			比较常用的有 random.choice('string')  #从字符串中随机选取一个字符
			random.choices('string',k = n)   #可以从字符串中随机选取n个字符
			random.randint(1,15) --->从[1,15]中随机返回一个值..
			等等吧
		6.shutil
			常用的功能时.shutil.copy()   用于复制旧文件-->新文件
		7.psutil
			可以查看系统的信息.
		8.functools
			from functools import reduce
			reduce(func,[1,2,3,4,5....]) 缩减函数.
		
4、多包情况下使用模块
	要求：
		1、设计项目中包含多个包
		2、不同包之间模块导入及使用方法		
		
	思路:
		1. 可以创建多级目录,但是在每级目录下都必须有一个__init__.py的文件.
		2. 然后可以.通过导入sys模块,修改sys.path列表,添加本模块路径,即可导入本包
		3. 次级包,可以通过'.'点操作符来导入
		
		
5、密码生成器
	要求：
		使用相关模块生成不少于8位密码的脚本

	思路:
		使用模块random.choices函数, 和string模块即可

		
		import random,string
		
		password = ''.join(random.choices(string.ascii_letters+string.digits,k = 8))
		
		忘记录制视频了...
		解释一下操作步骤:
		首先,生成字符串(大小写字母+数字),然后从中随机选8个,
		然后,再用''.join()拼接起来,就是一个密码了
		
		演示如下:
		ok!
		
6、设计并实现一款菜单
	要求：
		操作方便，可由用户选择是否退出。
		
		
		由于这个类似任务我记在9月13日写成博客了,,所以,我的博客地址是:
		https://blog.csdn.net/weixin_40545512/article/details/82694036
		
		
		[root@centos7-5 python3]# cat stone_jianzi_bu.py 
#!/usr/bin/python36
# coding=utf-8
 
#石头、剪子、布的游戏
import random
import os
#sum = ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2))
win = (('0','2'),('1','0'),('2','1'))   #定义了赢的组合（元组）
welcome = '''欢迎体验石头、剪子、布游戏
再游戏中，您会和电脑较量..have a fun^_^
1、剪子用数字“0”代替
2、石头用数字“1”代替
3、布 用数字“2”代替
4、输入‘quit’或者‘q’退出本游戏
'''
#建立数字和手法的对应字典
dic = {'0':'剪子','1':'石头','2':'布'}
def getnum():
    client = input("请输入一个数字[0-2]...")
    if client in ['quit','q']:
        os._exit(0)
#判断输入是否为字符[0-2]，否则重新输入
    if client not in ['1','2','0']:
        return getnum()
    return client
while True:
    print(welcome)
    rand_ = str(random.randint(0,2))
#   print(rand_)
    client = getnum()
#    print(dic[rand_],dic[client])
#    print(client)
    if rand_ == client:
        print("\033[44;37m您输入的是：%s--电脑输入的是：%s...平局\033[0m"%(dic[client],dic[rand_]))
        continue
    if (rand_,client) in win:
        print("\033[42;30m您输入的是：%s---电脑输入的是：%s...您输掉了比赛\033[0m"%(dic[client],dic[rand_]))
    else:
        print("\033[41;37m您输入的是：%s---电脑输入的是：%s...恭喜您赢得比赛\033[0m"%(dic[client],dic[rand_]))

		
		
		
		

		