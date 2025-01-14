i=1
for i in range(1,1001):
      j=i
      digitsum=0
      while j > 0:
          digitsum += j%10
          j //= 10

      if digitsum==20:
          print(i)
          i+=1
