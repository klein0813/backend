try:
    x = 4 / 0
except ZeroDivisionError as e:
     print('ZeroDivisionError:', e)


try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

def func(num):
    if not isinstance(num, int):
        raise Exception('bad operand type')
        
class FooError(ValueError):
    pass
'''
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
'''

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

import logging
logging.basicConfig(level=logging.INFO)

s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

import logging
logging.basicConfig(filename='app.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',datefmt='%Y-%m-%d')
logging.info('test info')
logging.debug('test debug')
logging.warning('test warning')
logging.error('test error')
logging.critical('test critical')
