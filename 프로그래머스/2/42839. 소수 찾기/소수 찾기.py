import itertools

def solution(numbers):
  total = []
  for i in range(1, len(numbers)+1):
      step = itertools.permutations(numbers, i)
      for s in step:
          total.append(s)
              
  total1 = list(set([int(''.join(x)) for x in total]))   

  max1 = max(total1)

  eratosthenes = [False,False] + [True]*(max1-1)

  primes=[]

  for i in range(2,max1+1):
    if eratosthenes[i]:
      primes.append(i)
      for j in range(2*i, max1+1, i):
          eratosthenes[j] = False
          
  answer = [x for x in total1 if x in primes]

  return len(answer)

print(solution('17'))
