n = int(input("Enter number of elements : "))
lst = []
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
sum = 0
for i in range(len(lst)):
    sum = sum + lst[i]
print( "sum is: ", sum)
