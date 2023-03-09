import random
a=[1,23,7,6,88,4,78]
print("using choice:")
print(random.choice(a))
print("using random int:")
print(random.randint(100,5000))
len=4
num='abcdhgk'
print("sample:")
print(random.sample(num,len))
random.seed(1)
print("seed")
print(random.random())
x = random.getstate()
print("getstate:")
print(x)
