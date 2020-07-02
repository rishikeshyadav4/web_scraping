# finding primes from 1 to 100
for i in range(1,100):
    m=2
    while (m<i):
        if (i % m==0):
            break
        m+=1
    if (m ==i):
      print(i)