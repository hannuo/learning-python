import pickle,json

d = dict(name='Bob',age=20,score=88)

with open('dump.txt','wb') as f:
    pickle.dump(d,f)

with open('dump.txt','rb') as f:
    dd = pickle.load(f)

print(dd)


d = dict(name='hanhan',age=20,socre=99)

print(json.dumps(d))

json_str = '{"age":20,"score":88,"name":"ruoruo"}'
print(json.loads(json_str))


class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {'name':std.name,'age':std.age,'score':std.score}

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

s = Student('qingyueen',20,33)

print(json.dumps(s,default = student2dict))

print(json.dumps(s,default = lambda obj:obj.__dict__))

json_str2 = '{"age":20,"score":88,"name":"Qingqing"}'
      
print(json.loads(json_str2,object_hook=dict2student))







