n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    d,e,f=map(int,input().split())
    fsum=0
    ssum=0
    fsum=a+b+c 
    ssum=d+e+f 
    if fsum>ssum:
        print("DRAGON") 
    elif fsum<ssum:
        print("SLOTH") 
    else:
            if a>d:
                print("DRAGON")
            elif a<d:
                print("SLOTH")
            else:
                if b>e:
                    print("DRAGON")
                elif e>b:
                    print("SLOTH")
                else:
                    print("TIE")
       
    
        
        
