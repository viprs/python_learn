Python模拟面试
======

- Python里面如何实现tuple和list的转换？

	tuple转list
	tup1 = (1, 'a', 'b')
	list1 = list(tup1)
	同理，list转tuple

- 请写出一段Python代码实现删除一个list里面的重复元素

	先强制转换成set，然后强制转换成list

- Python中pass语句的作用是什么？

	占位符，使符合语法格式

- 如何知道一个python对象的类型？

	type 比如type('1')，返回字符串

	isinstance('1', basestring) 判断'1'是否basestring，返回True或False

- 如何进行数据类型的转换？

	int('1')，字符串转换成int
	str(1)，int转换成字符串

- 如何查看对象的标识符？
	
	a = 1
	print id(a)  # 返回a的标识符

- Python如何定义一个函数?
	
	def func_name():
		do_something()
		pass

- 介绍一下except的用法和作用？
	


- 什么是lambda函数？它有什么好处?
	
	匿名函数。没啥好处。
	lambda a:

	有名函数
	def add(a, b):
		return a+b



- 如何打开一个文件？

	hfile = open('file.txt', 'r')
	hfile.close()

- 介绍一下Python下range()函数的用法？
	
	list1 = range(10)  #返回 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

- Python里面如何生成随机数？
	
	import random
	print random.randint(1, 10) #返回[1,10]以内的随机整数

- 如何用Python来发送邮件？
	
	import smtp

注：以下的题比较偏开发一点，知道更好，不知道没关系。

- Python是如何进行内存管理的？

	gc, 引用计数。


- 如何用Python来进行查询和替换一个文本字符串？
	
	import re  #正则表达式模块

- Python里面search()和match()的区别？

	import re #正则表达式模块

- 有没有一个工具可以帮助查找python的bug和进行静态的代码分析？
	
	pycheck 
	pylint

- 如何在一个function里面设置一个全局的变量？

	global