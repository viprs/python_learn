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

	占位符

- 如何知道一个python对象的类型？

	type 比如type('1')，返回字符串

	isinstance('1', basestring) 判断'1'是否basestring，返回True或False

- 如何进行数据类型的转换？

如何查看对象的标识符？

Python如何定义一个函数?

介绍一下except的用法和作用？

什么是lambda函数？它有什么好处?
匿名函数。没啥好处。

Python是如何进行内存管理的？
gc, 引用计数。

如何打开一个文件？
hfile = open('file.txt', 'r')
hfile.close()

介绍一下Python下range()函数的用法？

Python里面如何生成随机数？

如何用Python来发送邮件？

如何用Python来进行查询和替换一个文本字符串？

Python里面search()和match()的区别？

有没有一个工具可以帮助查找python的bug和进行静态的代码分析？
pycheck pylint

如何在一个function里面设置一个全局的变量？
global