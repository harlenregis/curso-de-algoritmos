vetor = []
tem_maior_50 = False

for n in range(0, 5):
    num = int(input("Informe o {0}º valor para o vetor: ".format(n+1)))
    vetor.append(num)
    
for n in vetor:
    if n > 50:
        print("O número {0} está na posição {1} do vetor.".format(n, vetor.index(n)+1))
        tem_maior_50 = True
        
if tem_maior_50 == False:
    print("Não existe número maior que 50")