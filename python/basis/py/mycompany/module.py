'''
在Python中，一个.py文件就称之为一个模块（Module）
我们在编写程序的时候，也经常引用其他模块，包括Python内置的模块和来自第三方的模块。
'''
import sys
'''此时就有了变量sys指向该模块'''

sys.path

'''如果一个只想导入一个模块的某个函数'''
from collections.abc import Iterator

'''
按目录来组织模块的方法，称为包（Package）

mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py
'''
import mycompany.abc

'''
注意的是：
1. 一个包必须有__init__.py，如果没有，python会认为它是一个普通的文件夹,
__init__.py可以是一个空文件夹，也可以存载pyhon代码，__init__于普通模块还有个区别
是它的模块名就是上级包名（mycompany）
2. 模块名要遵循Python变量命名规范，不要使用中文、特殊字符
3. 模块名不要和系统模块名冲突

'''

'''
操作第三方模块
在命令提示符窗口下运行pip
'''
pip install pillow
pip show pillow
pip uninstall pillow
