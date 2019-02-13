import functools

def now():
	print('2015-3-25')
	
def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper
	
now1 = log(now)

now()

now1()

print('now().__name %s' % now.__name__)
print('now1().__name %s' % now1.__name__)

	
@log
def now2():
	print('now2:2015-3-35')

print('now2().__name %s' % now2.__name__)
now2()
#把@log放到now()函数的定义处，相当于执行了语句：now2=log(now2)
	
#foo = timeit(foo)换成foo1 = timeit(foo)然后你调用foo就是原函数，调用foo1就是装饰过的函数。
#装饰器的作用是可以抽离出大量与函数功能本身无关的雷同代码并继续重用，简单点说就是重用

def log2(text):
        def decorator(func):
                def wrapper(*args,**kw):
                        print('%s %s():' % (text,func.__name__))
                        return func(*args,**kw)
                return wrapper
        return decorator


@log2('execute')
def now3():
        print('2015-3-25')

now3()
print('now3().__name %s' % now3.__name__)

def log3(text):
        def decorator(func):
                @functools.wraps(func)
                def wrapper(*args,**kw):
                        print('%s %s():' % (text,func.__name__))
                        return func(*args,**kw)
                return wrapper
        return decorator


@log3('execute')
def now4():
        print('2015-3-25')

now3()
print('now4().__name %s' % now4.__name__)


