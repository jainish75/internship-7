#day 2 data type:numpy ,pandas
#sololearn website 

a=['a','b','c','d','e','f','g','h','i']
b=a[1:3]
print(b)


a={1,2,3,4,5}
b={4,5,6}
print(a|b)#duplicate value delete
print(a-b)#b-a

a={'a':3,'b':4,'c':5,'d':6}
b=a['a']
print(a)
a['a']=6#ipdate
print(a)
for i in a:
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
a=[1,2,3,4,5]
for i in a:
    print(i)
a=['how','hello','are','you']
for i in a:
    print(i[0])
a=['hello','how','are','you','']
for i in a:
	if(i != ''):
		print(1[0])#use continue 