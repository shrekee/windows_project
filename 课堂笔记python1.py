
PYTHON
通过github安装pyenv(python版本控制器)

	git clone https://github.com/pyenv/pyenv.git ~/.pyenv
李文强 15:18:18
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile


常用工具包:
	yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel 
	sqlite-devel readline-devel tk-devel gdbm-devel db4-devel 
	libpcap-devel xz-devel


解压序列赋值给多个变量：			解压赋值可以用在任何可迭代对象上面
解压可迭代对象赋值给多个变量；		解压可迭代对象？
保留最后N个元素					
查找最大或最小的N个元素；
实现一个优先级队列；
字典中的键映射多个值
字典排序
字典的运算；
查找字典的相同点
删除序列相同元素并保持顺序
命名切片
序列中出现次数最多的元素
通过某个关键字排序一个字典列表
通过某个字段将记录分组
过滤序列元素
从字典中提取子集
映射名称到序列元素
转换并同时计算数据
合并多个字典或映射

尝试捕获assert异常
尝试捕获assert异常；
尝试捕获assert异常 尝试捕获assert异常：尝试捕获assert异常；

python内置的函数和类型：
abs()	dict()	min() setattr() all() dir()	hex()
next()	
声明定义一个变量? 一般而言?模块的属性?内部定义的类?调用属性?
无论是类,还是属性和方法?getattr()hasattr() 文件的功能?b和c都是模块?
b载入c模块?基本功能?自带模块?自objectc 所有的模块?
所有的模块?所有的模块?自带模块?标准库模块?

一个python程序通常包含一个顶层程序文件和其他是模块文件(0个或多个)
顶层文件:包含了程序的主要控制流程
模块文件:为顶层文件或其他的模块的提供各种功能性组件
	模块首次导入(或重载时),python会立即执行模块文件顶层程序代码,
而位于函数内的代码则知道函数被调用后才会执行.

模块首次导入时

在导入模块时,只能使用模块名,而不能使用带.py后缀的模块文件名
import语句:
	导入指定的整个模块,包括生成一个以模块名命名给的名称空间

import random as rd;  别名方式的导入模块;

from  module import name1[,name2,name3...]

比如:from random import randint  ;会只导入randint函数;


import 和 from - import时赋值语句:
	import 和 from时可执行语句,类似于def,因此他们可以
	嵌套于if测试中,出现def中等.

	python执行到这些语句时,才会对其进行解析: 这意味着,所有来自模块的属性权
	尽在import语句执行后才能使用.

	import 和 from 都是隐形赋值语句:
		import将整个模块对象赋值给一个变量名.

		from 将一个或多个变量名  赋值给导入此模块中的同名对象.

	模块就是名称空间.
		模块的名称空间可以通过属性  __dict__


	IMPORT的工作机制:
		找到模块文件:
			在指定路径下搜索模块文件
		编译成字节码
			在文件导入时就会编译,因此,顶层文件.pyc字节码文件在使用后
		会被丢弃.只有被导入的文件才会留下.pyc文件.

		执行模块的代码来创建其所定义的对象.


	PYTHON解释器在import模块时,必须先找到对应的模块文件.
		当前工作目录
		程序的主目录:
		PYTHONPATH 目录(环境变量)
		标准连接库目录
		任何.pth文件的内容.

	以上四个组合起来后,目录综合,记载sys.path中.
	
	python在在第一个符合的路径中找到对应的模块.

	顶层代码?30? 模块?代码写错了?怎么办?
	if __name__ == "__main__":
		pass
		测试语句:用于自测试模块的


PYTHON包

	包:用于将一组模块归并到一个目录中,此目录即为包,目录名为包名.

		包是一个由层次的文件目录结构,它定义了一个模块和子包组成的
		python应用程序执行环境.

		基于包,python在执行模块导入时,可以指定模块的导入路劲.

		比如:	import dir1.dir2.mod1

	要使用如图所示的package1,则py......

	包导入语句中路径内的每个目录内都必须由__init__.py文件,
		__init__.py 可包含python代码,单通常为空.仅用于扮演包的
		初始化的挂钩、替目录产生模块命名空间，以及使用目录导入时实现
		from * 行为的角色。


		py——pkg——mod  

	python 网络编程：
	PYthon提供了两个级别的访问网络服务：
		低级别的网络服务几倍呢？
		高级别的网络服务几倍呢？

	python 网络对象？两个级别的服务？l4？字符串大哥？字符串？
	元组？列表？字典？字典？字符串？字符串
	python网络对象？两个级别的服务？14？字符串个数？函数？range()

	列表生成：range() 
列表生成式:
	x = {1,23,44,5}
	l1 = [i for i in x]
列表生成式
列表生成式?列表生成式?列表生成式?
列表生成式?列表

导入一个包模块?

PYthon模块.扩展和应用程序可以按一下几种形式进行打包和发布:

	压缩文件:
	python eggs
	distutils 模块能够帮助完成模块或程序发布:

	发布:指一个文件集合,这些文件在一起可使用disutils构建.打包.发布模块?
	创建好的发布可以用于安装,也可以上传到pypi与他人共享.

具体方法:
	将各代码文件组织到模块容器中.
	准备一个readme或readme.txt文件
	而后在容器中创建setup.py文件.

	导入 创建模块的模块::
		from disutils.core import setup

		setup(
			name 		= "testmod",
			version		=	'0.0.1',
			author		=	'lwq',
			author_mail	=	'***@qq.com',


			)
python基本语法:

python运行时错误称之为异常:
	1.输入错误:
	2.逻辑错误:

pyton异常时一个对象,表示错误或意外情况.
	在python检测到一个错误时,将出发一个异常:
		1.python可以通过异常传导机制传递一个异常对象,发出一个异常
		情况出现的信号
		2.程序员也可以在代码中手动触发异常:

python异常也可以理解为:程序出了错误而在正常控制流以外采取的行为:
	第一阶段:解释器触发异常,此时当前程序流被打断;
	第二阶段:异常处理,如忽略非致命性错误,减轻错误带来的影响.

	交互式程序?
	如何避免因为用户发非法输入而导致程序崩溃?


错误处理:
	1.python的默认处理:停止程序,打印错误信息;
	2.使用try语句处理异常并从异常中恢复
事件通知:
	用于发出有效状态信号.
特殊情况处理:
	无法调整代码区处理的场景.
终止行为
	try/finally 语句可以确保执行必须的结束处理机制.
非常规控制流程.
	异常是一种高级跳转(goto)机制

异常通过try语句来检测:
	任何在try语句块里的代码都会被检测,以检查有无异常发生
try语句主要由两种形式:
	try-except:检测和处理异常
		可以有多个except
		支持使用else子句处理么有

	try-finally:仅检查异常并做一些必要的清理工作.
		!!!仅能有一个finally

try语句的复合形式:
	try-except-finally

	产品过期了?工商产品?三个语句结合起来?
try:
	try_suite
except  Exception[,reasn]:
	except_suite

例子:
	try用于捕获异常,异常会向上传递.解释器:捕获?
	只有一个操作?终止程序?嵌套?向外抛出?
	else语句?

try-finally语句
	无论异常是否发生,finally子句都会执行.

	finally中的所有代码执行完毕后,继续像上一层引发异常!!!希望来被处理.
	try语句中?比较常见的方式?


	分句形式:
		except:				捕捉所有异常
		except name 		之捕捉特定异常
		except name,value	捕捉所列的异常和其额外的数据(或实例)
		except (name1,name2) 捕捉列出的异常
	except (name1,name2),value:捕捉任何列出的异常,并取得额外数据
	else:						如果没有异常,则运行.
	finally:					总是会运行此代码块.


raise 语句可显示触发异常:
	raise [SomeException [,args[,traceback]]]
		SomeException:可选,异常的名字,仅能使用字符串,类或实例.
		args:可选,以元组形式传递给异常的参数.		