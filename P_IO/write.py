
a = 5

with open('utf-8.txt','w') as f:
    while( a > 0):
        f.write('测试用')
        a-=1


b = 5

with open('gdk.txt','w',encoding='gbk') as f:
    while( b > 0):
        f.write('测试用')
        b-=1


with open('utf-8.txt','r') as f:
    print(f.read())

with open('gdk.txt','r') as f:
    print(f.read())

with open('utf-8.txt','rb') as f:
    print(f.read())

with open('gdk.txt','rb') as f:
    print(f.read())
