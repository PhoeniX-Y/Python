# n = int(input("Enter the marks: "))
# if not 0 <= n <= 100:
#     print("Invalid marks")
# elif n >= 90:
#     print("Grade A")
# elif n >= 80:
#     print("Grade B")
# elif n >= 70:
#     print("Grade C")
# elif n >= 60:
#     print("Grade D")
# elif n >= 0:
#     print("Fail")


#Day2

#Q1 check single valued values
'''mylist=[1,2,3,'4' ]
c=[int,float,bool,complex]
for i in range(len(mylist)):
    if type(mylist[i]) in c:
        print(mylist[i],end=' ')'''


'''mylist=[1,2,3,4,'8']
i=0
while i<len(mylist):
    if type(mylist[i]) in (int, float, bool, complex):
        print("Single Valued DT", mylist[i])
    else:
        print("Multi Valued DT", mylist[i])
    i+=1'''


#Q2 printing even/odd numbers
'''for i in range(10):
    if i%2==0:       # for odd use !=0
        print(i)
        i+=1'''
#Q3 sum of even/odd numbers
'''sum=0
for i in range(10):
    if i%2==0:       # for odd use !=0
        sum+=i
        print(sum)'''
#Q4 print even indexed characters from a string
'''b='swapnodaya'
i=0
while i<len(b):
    print(b[i])
    i+=2'''
#Q5 print the numbers,alphabets and special characters in a give string
'''s='2EW2CS040#'
i=0
num=''
chr=''
spc=''
while i<len(s):
    if s[i] in '1234567890':
        num=num+s[i]
    elif s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='Z':
        chr=chr+s[i]
    else:
        spc=spc+s[i]
    i+=1        
print("Numbers",num)
print("Characters",chr)
print("Special characters: ",spc)     '''
#Q6 count of the number,alphabets and special characters
'''s='2EW2CS040#'
i=0
num=0
chr=0
spc=0
while i<len(s):
    if s[i] in '1234567890':
        num+=1
    elif s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='Z':
        chr+=1
    else:
        spc+=1
    i+=1        
print("Numbers: ",num)
print("Characters: ",chr)
print("Special characters: ",spc) '''
#Q7 extract only special characters
'''s = '2EW2CS040#'
i = 0
spc = ''
while i < len(s):
    if not(('0' <= s[i] <= '9') or ('a' <= s[i] <= 'z') or ('A' <= s[i] <= 'Z')):
        spc += s[i]
    i += 1
print("Special characters: ", spc)'''
#Q8 c=['hi','90','hello',90] output: d=['hi','90','hello']
'''c=['hi','90','hello',90]
d=[]
i=0
while i<len(c):
    if type(c[i])==str:
        d=d+[c[i]]
    i+=1
print(d)'''
#Q9 e='OK!Bye' output : f=2
'''e='!OKByewwwwwwww'
f=0
i=0
while i<len(e):
    if  e[i] in ('aeiouAEIOU'):
        f+=1
    i+=1
print(f)'''  
#Q10
'''a=['Hi','Python','jello']    
i=0
o=[]
while i<len(a):
    if 'A'<=a[i][0]<='Z':
        o=o+[a[i]]
    i+=1    
print(o)'''
#Q11
'''
a='Python'
i=0
o=''
while i<len(a):
    o=a[i]+o
    i+=1
print(o)
'''

#DAY 3
#Q1
'''
a=['Python','Sql']
lst=[]
for i in a:
    count=0
    for j in i:
        count+=1
    lst+=[count]
print(lst)
'''
#Q2
'''
d=['Hello','hi']
lst=[]
for i in d:
    count=0
    for j in i:
       if j in 'aeiouAEIOU':
           count+=1
    lst+=[count]
print(lst)
'''
#Q3
'''
d=['Pythopn','Workshop']
lst=[]
for i in d:
    count=0
    for j in range(len(i)):
        if j%2==0:
            count+=1
    lst+=[count]
print(lst)
'''
#Q4
'''
z='aabbccbbc'
o=''
for i in z:
    if i not in o:
        c=0
        for j in z:
            if i==j:
                c+=1
        o=o+i+str(c)
print(o)
'''
''''
z='aabbccbbc'
o=''
e=''
for i in z:
    if i not in o:
        c=0
        for j in z:
            if i==j:
                c+=1
        o+=i
        e+=str(c)
print(o+e)
'''
#Q5
'''
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)

print(fact(6))
'''
#Q6
'''
def even(a):
    if a%2==0:
        print("EVEN")
    else:
        print("ODD")
even(4)
even(5)
'''
#Q7
'''
def sum(a,b):
    return a+b
print(sum(4,6))
'''
#Q8
'''
def sum(*a):
    print(a.items)
sum(1,45,6,0,7,7,8,8)
'''
#Q9
'''
def dit(**ag):
    print(ag)
dit(name="Rahul",age=20)
'''
#Q10
def display2(*a,**b):
    print(a)
    print(b)
display2(1,2,3,k=1,l=2,m=3)

