def flib(max):
    a,b = 0,1
    while b < max:
        print(b)
        temp = b
        b = a + b
        a = temp
    return 'done'

def flib2(max):
    a,b = 0,1
    while b < max:
        yield b
        temp = b
        b = a + b
        a = temp
    return 'done'
    
#flib(30)

for n in flib2(15):
    print(n)


g = flib2(25)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
