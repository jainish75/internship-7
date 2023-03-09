import random
len=int(input("enter num:"))
num='123456789qwertyuiopasdfghjklzxcvbnm!@#$%^&*()'
print(" ".join(random.sample(num,len)))