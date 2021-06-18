import math
#===================================================
#BASKARA
def baskara(a,b,c):
    delta = ((b*b) - (4*a*c))
    if delta > 0:
        x1 = (b + math.sqrt(delta))/2*a
        x2 = (b - math.sqrt(delta))/2*a
        print("X1: ", x1,"\nX2: ",x2)
    else:
        print("RAIZ INDISPONIVEL")


a = int(input("Defina o valor de A : \n"))
b = int(input("Defina o valor de B : \n"))
c = int(input("Defina o valor de c : \n"))

print("Esta eh sua Expressão: ",a,"x² + ",b,"x + ",c)
baskara(a,b,c)

#===================================================
#QUADRADO DA DIFERENÇA - PRODUTO NOTAVEL

def QuaDif (a,b):
    print((a+b)*(a-b))

a = int(input("Insira o valor de A: \n"))
b = int(input("Insira o valor de B: \n"))

print("Sua expressao: ",a,"² - ",b,"²")
QuaDif(a,b)

#===================================================
#SOMA ENTRE DOIS CUBOS
def SomCubos (a,b):
    print((a+b)*((a*a)-(a*b)+(b*b)))

a = int(input("Insira o valor de A: \n"))
b = int(input("Insira o valor de B: \n"))

print("Sua expressao: ",a,"³ - ",b,"³")
SomCubos(a,b)
#===================================================
#DIFERENÇA ENTRE DOIS CUBOS
def DifCubos (a,b):
    print((a+b)*((a*a)+(a*b)+(b*b)))

a = int(input("Insira o valor de A: \n"))
b = int(input("Insira o valor de B: \n"))

print("Sua expressao: ",a,"³ - ",b,"³")
DifCubos(a,b)



