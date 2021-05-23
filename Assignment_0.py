print("QUESTION 1 ")
numbers = [234,876,987,678,567,456,390,237,789,
           124.468,435,208,78,90,567,80,456,386,
           789,56,465,289,708,560,490,29,130,68,]
for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)

print()
print()

######################################################################

print(" QUESTION 2")
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(set(color_list_1-color_list_2))

print()

#####################################################################

print(" QUESTION 3 ")
import string
  
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True
      
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")

print()

#####################################################################

print(" QUESTION 4 ")
num=int(input("Please Enter number to get the VAlue of n+nn+nnn : "))
print(num+((num*10)+num)+((num*100)+(num*10)+num))


print()

######################################################################

print(" QUESTION 5 ")
s = input('Enter string: ')
s = s.split('#')
s1 = s[0].split()
s2 = s[1].split()
s1 = [int(i) for i in s1]
s2 = [int(i) for i in s2]
print(s1)
print(s2)

print()

#####################################################################

print("QUESTION 6 ")

s = input('Enter string: ')
s = s.split(',')
s.sort()
print(s)

print()

#####################################################################

print(" QUESTION 7 ")

d = {'Student': ['Sona', 'Nisha', 'Shoaib', 'Mirzaa'],'Marks': [97,87,77,59]}
high = d['Marks'].index(max(d['Marks']))
print(d['Student'][high])

print()

############################################################################
print("QUESTION 8")

s = input('Enter string: ')
letters = 0
digits = 0
for i in s:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letter+=1
print('LETTERS '+str(letters))
print('DIGITS '+str(digits))

print()

############################################################################
print("QUESTION 9 ")

d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
d1 = {}
subject = input('Input: ')

idx = 0
subject_index = []
lst = []
for idx,i in enumerate(d['Subject']):
    if i == subject:
        subject_index.append(idx)
        
d1_keys = ['Name', 'Subject', 'Ratings']
d1_values = ['','','']

for idx,i in enumerate(d.values()):
    lst = []
    for j in subject_index:
        lst.append(i[j])
    d1_values[idx] = lst
print(dict(zip(d1_keys,d1_values)))

print()
############################################################################

print("QUESTION 10")
class Generator:
    lst = []
    # def __init__(self):
    #     pass
    def generator(self, n):
        for i in range(0,n):
            if i%7 == 0:
                yield i
        return Generator.lst

m = Generator() 
n = int(eval(input('Enter the value of n: ')))
for i in m.generator(n):
    print(i)

print()
##############################################################################

print("QUESTION 11 ")

up = eval(input('UP : '))
down = eval(input('DOWN : '))
left = eval(input('LEFT : '))
right = eval(input('RIGHT : '))

net_up = abs(up - down)
net_right = abs(right - left)

total_distance = (net_up**2 + net_right**2)**0.5

print('distance = ',round(total_distance))
##########################################################################
