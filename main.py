# YOUR CODE HERE
def summation(lis1,lis2):
    updated_list=[]
    for i in range(len(lis1)):
        sum=lis1[i]+lis2[i]
        updated_list.append(sum)
    return updated_list  
def find_min_max(x):
    b=max(x)
    s=min(x)
    return (s,b)
lis1=[]
lis2=[]
n=int(input())
for i1 in range(n):
    lis1.append(int(input()))
for i2 in range(n):
    lis2.append(int(input()))      
print(summation(lis1,lis2))
print(find_min_max(summation(lis1,lis2)))
