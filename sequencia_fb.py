ter1 = int(0)
ter2 = int(1)
ter3 = int(0)

val = int(input('Digite um número: '))

while val > ter3:
    ter3 = ter1 + ter2
    ter1 = ter2
    ter2 = ter3

if val == 0 or val == 1:
    print ('O número faz parte da sequência de Fibonacci.')
elif val == ter3:
    print ('O número faz parte da sequência de Fibonacci.')
else:
    print ('O número digitado não faz parte da sequência de Fibonacci.')