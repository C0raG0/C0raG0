m=0
c=1000000
for n in range(2, c+1):
    x=0
    j=1
    a=[0]*(n+1)
    z=0
    for i in range(1, n):
        if n%i==0 and i!=1 and a[j]==0:
            a[j]=i
            z=n//i
            if z>1:
                for s in range(2,z+1):
                    k=a[j]*s 
                    a[k]=a[j]*s
        j+=1
    for k in range(1, n): 
        if a[k]==0:
            x+=1
    if x>0:
        p=n/x
        if p>m:
            m=p
            N=n
print(N, m)
