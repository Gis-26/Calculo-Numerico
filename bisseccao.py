""""Esse código calcula as equação procurando o zero da função, se existir,
para calcular primeiro o úsuario tem que digitar na seguinte notação 
* - para operação de multiplicação = 'x*log(x) -1'
/ - para operação de divisão,use () nas divisões = '6/(x-2)' 
sqrt(x) - para calcular a raiz quadrada = 'sqrt(x-6)'
** - para calcular exponencial = 'x**3 -9*x +3' """

import sympy 
import math
from sympy import symbols, exp

def calcular(fx, j, y):
  x = sympy.symbols('x')
  log_x = "log(x)"
  if log_x in fx:
    result = math.log(j, y)
    fx = fx.replace("log(x)", f"{result}")
    func = sympy.sympify(fx)
    fj = func.subs(x, j).evalf(subs={symbols('e'):exp(1)})
    return fj
  else:
    func = sympy.sympify(fx)
    fj = func.subs(x, j).evalf(subs={symbols('e'):exp(1)})
    return fj

print("\t\t\t\tMétodo da bisseção\n")

funcao = input("* Digite a função: ")
a = float(input("* Digite o intervalo (a): "))
b = float(input("* Digite o intervalo (b): "))
e = float(input("* Digite O valor da precisão: "))
log_x = "log(x)"
if log_x in funcao:
  Valor = int(input("Digite o número da base para calcular log(x): "))
else:
  Valor = 0
fa = calcular(funcao, a, Valor)
fb = calcular(funcao, b, Valor)
inter =1

if fa * fb < 0:
  print("\nIteração\t|x\t\t        |f(x)\t\t    |b-a")
  print("=" * 55)

  while b - a > e:
    x_zero = (b+a)/2
    f_x_zero = calcular(funcao, x_zero, Valor)

    if fa * f_x_zero < 0:
      b = x_zero
      
    else:
      a = x_zero

    comp = b - a
    
    print(f"{inter}\t\t\t|{x_zero:3.6f}\t\t|{f_x_zero:3.6f}\t\t|{comp:3.6f}")

    if math.fabs(f_x_zero) < e:
      break
    inter += 1
    
  print("=" * 55)
  print(f"\n-> Assim, x̅: {x_zero} e f(x̅) é: {f_x_zero}")

else:
  print("Não há zero de função nesse intervalo!")
