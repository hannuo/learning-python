def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[consumer] consuming %s..'%n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[producer] producing %s...'%n)
        r = c.send(n)
        print('[producer] consumer return:%s'%r)
    c.close()

c = consumer()
produce(c)

#Python对协程的支持是通过generator实现的
#整个流程无锁，由一个线程执行，produce和consumer协作完成任务，
#所以称为“协程”，而非线程的抢占式多任务。

#1.consuer函数是一个generator
#2.调用c.send(None)启动生成器
#3.一旦生产了东西，通过c.send(n)切换到consumer执行
#4.consumer通过yield拿到信息处理，又通过yield把结果传回
#5.produce拿到consumer处理的结果，继续生产下一条消息；
#6.produce决定不生产了，通过c.close()关闭consumer

#即把一个生成器函数，作为参数传给函数
#调用生成器函数，send接口激活生成器函数，发送数据，并于生成器中生成结果（也可不生成接口）
#调用生成器函数，close接口，关闭协程合作关系
#一个线程，类似于goto






























