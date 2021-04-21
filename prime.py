def sieve():
        n=int(input())
        prime=[]

        for i in range(0,n):
            prime.append(1)
        prime[0]=0
        prime[1]=0
        for i in range(2,n):
            if prime[i]==1:
                for j in range(2,n):
                    if i*j>=n:
                        break 
                    else:
                        prime[i*j]=0
        print(prime)
        for i in range(len(prime)):
            if prime[n-1]==0:
                print(" not Prime")
                break 
        else:
            print("Not prime")

def simpleprimerange():
    l=int(input())
    r=int(input())
    for i in range(l,r+1):
        if i>1:
            flag=0
            for j in range(2,i):
                if i%j==0:
                    flag=1
                    break
            if flag==0:
                print(i)


def primefind():
    n=int(input())
    for i in range(2,n):
        if n%i==0:
            return False 
    return True



def isPrime(n, i = 2):

	
	if (n <= 2):
		return True if(n == 2) else False
	if (n % i == 0):
		return False
	if (i * i > n):
		return true

	return isPrime(n, i + 1)



n = 15
if (isPrime(n)):
	print("Yes")
else:
	print("No")
	


primefind()



sieve()