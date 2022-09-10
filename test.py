import os

print('Whats your name \t')
name = input()
print('hello', name)
for c in name:
    print(c.upper(),'\t')
    #print(\t)
age=input('Enter your age\t')
#print(name, 'Is ', age, 'year old')
f"My name is {name} and my age is {age}"
#print({f})
print('Current working directory is ',os.getcwd())