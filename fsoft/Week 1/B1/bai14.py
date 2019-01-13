def Fibo(n):
   if n <= 1:
       return n
   else:
       return(Fibo(n-1) + Fibo(n-2))

for i in range(1,100):
	temp = Fibo(i) 
	if (temp) < 100 :
		print(temp)