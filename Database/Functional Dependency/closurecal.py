print('Please input the amount of FD')
a = input()
a=int(a)
x=[]
y=[]
print('Please input the FD(left decides right use space to split)')
for i in range(a):
  l,f=input().split()
  x.append(l)
  y.append(f)
def combination_k(s, k):
    if k == 0: return ['']
    subletters=[]
    for i in range(len(s)):
        for letter in combination_k(s[i+1:], k-1):
            subletters += [s[i] + letter]
    return subletters
def combination_all(s):
    comb_list = []
    for i in range(1, len(s)+1):
        comb_list += combination_k(s, i)
    return comb_list
def closure(q):
    cc=[]
    qq=''
    while len(q)>len(qq):
        qq=q
        for i in (range(a)):
            t=set(x[i])
            tt=set(q)
            if t&tt==t:
               q=q+x[i]+y[i]
               q=sorted(set(q))
               q=''.join(q)
    cc=list(q)
    return combination_all(cc)

print ('F(',end='')
for i in range(a):
 print (x[i], "->", y[i],' ',end='')
print (')')
b=''.join(x)+''.join(y)
print (b)
w=list(b)
b=sorted(set(w))
print(b)
zuhe=combination_all(b)
l= int(len(zuhe))
print(zuhe)
num=0
for i in range(l):
    out=closure(zuhe[i])
    for ii in range(len(closure(zuhe[i]))):
        print (zuhe[i],"->",out[ii],' ',end='')
        num=num+1
print(' ')
print("""Total number of closure:""",num)        

