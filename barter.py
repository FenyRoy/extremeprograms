import sys
n=input()
com={}
def exrate(m,n):
    r=1
    global f
    global com
    if m in com.keys():
        if(com[m][0]==n):
            r=r*com[m][1]
            f=1
            return(r)
        else:
            r=com[m][1]
            r=r*exrate(com[m][0],n)
            return(r)
    return(r)
for i in range(n):
    c=raw_input()
    temp=c.split()
    com[temp[0]]=[temp[1],int(temp[2])]
q=input()
query=[]
for i in range(q):
    c=raw_input()
    temp=c.split()
    query.append(temp)
rates=[]

for i in range(q):
    f=-1
    if(query[i][0]==query[i][1]):
        val=1
    else:
        val=(exrate(query[i][0],query[i][1]))%998244353
        if(f==-1):
            val=-1
    print(val)
        


    
