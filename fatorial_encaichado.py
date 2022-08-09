
def fatorial(x, f):    
    while x > 1:
        f = f * x
        x = x - 1
        if x == 1:
            print(f)

        
    
    
x = 1
while x != -1:
    x = int(input("Digite o número terminando com 1 negativo: "))
    f = 1
    if x >= 0:
        x = fatorial(x, f)

    
    
    
    
  
    
    
  

