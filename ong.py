
def factorial(n):
   
   if n == 0 or n == 1:
      return 1
   else:
      return n * factorial(n - 1)
   
def productoria(lista):
   resultado = 1
   for numero in lista:
      resultado *= numero

   return resultado

def calcular(**kwargs):
   for k, v in kwargs.items():
      if "fact" in k:
         resultado = factorial(v)
         print(f"El factorial de valor {v} es: {resultado}")

      elif "prod" in k:
         resultado = productoria(v)
         print(f"La productoria de {v} es: {resultado}")

calcular (fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)
