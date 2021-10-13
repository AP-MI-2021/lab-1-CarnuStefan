'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if (n<=2): return False
  for i in range(2,n//2):
      if(n%i==0):return False
  return True
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  produs=1
  for i in range (len(lst)):produs=produs*lst[i]
  return produs

  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while(x!=y):
    if (x>y):x=x-y
    if (x<y):y=y-x
  return x
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while(y!=0):
    r=x%y
    x=y
    y=r
  return x

  
  
def main():
    n=int(input('Introduceti n:'))
    nr=int(input('Introduceti nr de numere din lista:'))
    lst=[]
    for i in range (nr):
      lst.append(int(input()))
    
    x=int(input('Introduceti x:'))
    y=int(input('Introduceti y:'))
    print (is_prime(n))

    print (get_product(lst))

    print (get_cmmdc_v1(x, y))

    print (get_cmmdc_v2(x, y))


if __name__ == '__main__':
  main()
