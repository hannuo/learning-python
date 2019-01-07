import asyncio
import threading
#1.asyncio的编程模型就是一个消息循环，从asyncio模块直接获取一个EventLoop循环，然后
#把需要执行的协程扔到EventLoop中执行，就实现了异步IO


@asyncio.coroutine
def hello():
    print("hello world") 
    r = yield from asyncio.sleep(2)
    print("hello again!")


#loop = asyncio.get_event_loop()
#loop.run_until_complete(hello())
#print("midle message")
#loop.close()

#@asyncio.coroutine把一个generator标记为coroutine类型

#01sample，直接yield一个变量，即调用生成器者发过来的数据
#yield from语法可以让我们方便地调用另一个generator。
#由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()
#而是直接中断并执行下一个消息循环

#把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去
#执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。

#执行顺序为
#打印 hello,world，等待两秒，假设其为2秒的io操作，继而执行下面的代码。

#用Task封装两个coroutine
#打印的当前线程名称可以看出
#两个coroutine是由同一个线程并发执行的。
#loop2 = asyncio.get_event_loop()
#tasks = [hello(), hello()]
#loop2.run_until_complete(asyncio.wait(tasks))
#loop2.close()

#用asyncio的异步网络连接来获取sina、sohu和163的网站首页：

@asyncio.coroutine
def wget(host):
    print('wget %s...'%host)
    connect = asyncio.open_connection(host,80)
    reader,writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost:%s\r\n\r\n'%host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s'%(host,line.decode('utf-8').rstrip()))
    #ignore the body,close the socket
    writer.close()

loop3 = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
loop3.run_until_complete(asyncio.wait(tasks))
loop3.close()

#asyncio提供了完善的异步IO支持
#异步操作需要在coroutine中通过yield from完成
#多个coroutine可以封装成一组Task然后并发执行

#理解了异步IO的意义，这里才能更好的理解
#当前进程执行不受影响，io过程交给其他系统过程读取，好了，系统工程或我们指定的程序直接处理读取好的内容
#即多个协程时，三个weget%在一个线程中依次执行，不管io的过程





























