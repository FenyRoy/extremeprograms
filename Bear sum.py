import sys
n=input()
r=[]
for i in range(n):
    f=-1
    v=raw_input().split()
    d=raw_input().split()
    for k in range(1,int(v[1])-1):
        for j in range(int(v[1])-k):
            s=int(d[j])+int(d[j+k])
            if(s==int(v[0])):
                f=1
                r.append([int(d[j]),int(d[j+k])])
                break
        if(f==1):
            break
    if(f==-1):
        r.append(-1)
for i in range(len(r)):
    if(r[i]==-1):
        print('!Ok')
    else:
        r[i].sort()
        print r[i][0],r[i][1]
        
