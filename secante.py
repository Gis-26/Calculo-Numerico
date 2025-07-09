""""Esse código calcula as equação procurando o zero da função, se existir,
para calcular primeiro o úsuario tem que digitar na seguinte notação 
* - para operação de multiplicação = 'x*log(x) -1'
/ - para operação de divisão,use () nas divisões = '6/(x-2)' 
sqrt(x) - para calcular a raiz quadrada = 'sqrt(x-6)'
** - para calcular exponencial = 'x**3 -9*x +3' 
e - Para calcular uma função com o número de euler deve usar = 'exp(-x**2) -cos(x)'
"""

import sympy
import math
from sympy import symbols, diff, exp

def calcular(fx, j, y):
    x = sympy.symbols('x')
    log_x = "log(x)"
    if log_x in fx:
        result = sympy.log(x,y)
        fx = fx.replace("log(x)", f"{result}")
        func = sympy.sympify(fx)
        fj = func.subs(x, j)
        return fj
    else:
        func = sympy.sympify(fx)
        fj = func.subs(x, j).evalf(subs={symbols('E'): exp(1)})
        return fj
      
print("\t\t\t\tMétodo da Secante\n")
funcao= input("* Digite a função f(x): ")
x0 = float(input("* Digite o primeiro valor inicial: "))
x1 = float(input("* Digite o segundo valor inicial: "))
e = float(input("* Digite o valor da precisão: "))
max_inter = int(input("* Digite o número máximo de interações: "))

log_x = "log(x)"
if log_x in funcao:
    Valor = int(input("Digite o número da base para calcular log(x): "))
else:
    Valor = 0
  
fx0 = calcular(funcao, x0, Valor)
fx1 = calcular(funcao, x1, Valor)

if math.fabs(fx0) < e:
  print("=" * 40)
  print(f"-> Assim, x̅: {x0:3.9f} e f(x̅) é: {fx0:3.9f}")
  
elif math.fabs(fx1) < e:
  print("=" * 40)
  print(f"-> Assim, x̅: {x1:3.9f} e f(x̅) é: {fx1:3.9f}")

else:
  k = 1
  print("\nIteração\t|x\t\t        |f(x)")
  print("=" * 40)

  while k <= max_inter:
    f_x0 = calcular(funcao, x0, Valor)
    f_x1 = calcular(funcao, x1, Valor)

    x2 = (x0*f_x1 -x1*f_x0)/(f_x1 - f_x0)
    f_x2 = calcular(funcao, x2, Valor)
  
    print(f"{k}\t\t\t|{x2:3.6f}\t\t|{f_x2:3.6f}")
  
    if math.fabs(f_x2) < e:
      print("=" * 40)
      print(f"-> Assim, x̅: {x2:3.9f} e f(x̅) é: {f_x2:3.9f}")
      break 
    
    x0 = x1
    x1 = x2
    k += 1
  
  if k > max_inter and math.fabs(f_x2) > e:
    print("\nNão foi possível encontrar o zero da função dentro das iterações.")