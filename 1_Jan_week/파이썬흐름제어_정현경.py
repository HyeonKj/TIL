'''
# Q1 A: shirt
'''
a="life is too short, you need python"
if"wife" in a : print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a : print("need")
else: print("none")

'''
# Q2 A: 166833
'''
n=0
s=0
while n<1000:
    n+=1
    if(n%3)!=0:continue
    s=s+n
print(s)

'''
# Q3
'''

num = 0
while num <4:
    num+=1
    print("*"*num)

'''
# Q4 A: 5050
'''
sum = 0
for x in range(1,101):
    sum += x
print(sum)

'''
# Q5 A: 79.0
'''
A=[70,60,55,75,95,90,80,80,85,100]
sum=0
for x in A:
    sum+=x
print(sum/10)

'''
# Q6 A: [2, 6, 10]
'''
numbers=[1,2,3,4,5]
result=[n*2 for n in numbers if n%2==1]
print(result)
