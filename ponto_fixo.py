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


print("\t\t\t\tMétodo do ponto fixo\n")

funcao = input("* Digite o f(x): ")
funcao_var = input("* Digite o φ(x): ")
x0 = float(input("* Digite o valor inicial: "))
e1 = float(input("* Digite o valor da precisão e1: "))
inter_max = int(input("* Digite o número máximo de interações: "))
log_x = "log(x)"
if log_x in funcao:
   Valor = int(input("Digite o número da base para calcular log(x): "))
else:
  Valor=0
 
fx0 = calcular(funcao, x0,Valor)
if math.fabs(fx0) < e1:
  print(f" Assim, x̅: {x0} e f(x̅) é: {fx0}")
else:
  k=1
  print("\nIteração\t|x\t\t        |f(x)")
  print("=" * 40)
  while k<=inter_max:
    x1 = calcular(funcao_var,x0,Valor)
    fx1 = calcular(funcao,x1,Valor)
    print(f"{k}\t\t\t|{x1:3.6f}\t\t|  {fx1:3.6f}")
    if math.fabs(fx1)<e1:
        print("="*40)
        print(f"\n -> Assim, x̅: {x0} e f(x̅) é: {fx0}")
        break
    x0 = x1
    k+=1
  if k>inter_max and math.fabs(fx1)>e1:
    print("Não foi possível encontrar uma raiz dentro das iterações especificadas.")
 