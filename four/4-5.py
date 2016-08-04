# -*- coding:utf-8 -*-

'''
    str()和repr()。
    内建函数str()与repr()之间的不同是什么?
    哪一个等价于反引号(``)运算符?
'''

'''
    功能:将任意值转化为字符串
    str():转化为适合人阅读的形式
    repr():转化为供解释器读取的形式
    反引号等价于repr()
'''
List = [1,2,3]
print repr(List)
