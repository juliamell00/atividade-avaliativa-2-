import os 
os.system ("cls || clear")

soma = 0
contador = 0 
preco = 0
junta_pratos = ""
junta_codigos =""

#Exibir um menu com 7 pratos, apresentando o código do prato, nome e o preço.
while True:
    menu = int(input(""""
    Código    Prato           |    Valor
    1 \t Costelinha           |  R$ 30,00
    2 \t Parmegiana           |  R$ 50,00
    3 \t Macarrão á Carbonara |  R$ 75,00
    4 \t Risoto de Camarão    |  R$ 80,00
    5 \t Lasanha              |  R$ 20,00
    6 \t Filé de Frango       |  R$ 25,00
    7 \t Escondidinho         |  R$ 65,00
    

    Digite a opção desejada: """))

    match menu:
        
            case 1:

                print("Prato: Costelinha, Valor: 30,00")
                prato ="Costelinha"
                preco = 30
                codigo = "1"
            case 2:
                print("Prato: Parmediana, Valor: 50,00")
                prato ="Parmediana"
                preco = 50
                codigo = "2"
            case 3:
                print("Prato: Macarrão á Carbonara, Valor: 75,00")
                prato ="Macarrão á Carbonara"
                preco = 75
                codigo = "3"
            case 4:
                print("Prato: Risoto de Camarão, Valor: 80,00")
                prato ="Risoto de Camarão"
                preco = 80
                codigo = "4"
            case 5:
                print("Prato: Lasanha, Valor: 20,00")
                prato ="Lasanha"
                preco = 20
                codigo = "5"
            case 6: 
                print("Prato: Filé de Frango, Valor: 25,00")
                prato = "Filé de frango"
                preco = 25
                codigo = "6"
            case 7:
                print("Prato: Escondidinho, Valor: 65,00")
                prato = "Escondidinho"
                preco = 65
                codigo = "7"
            #Caso o código seja inválido, o sistema deve alertar o usuário e pedir novamente um código válido.
            case _:
                print("Opção inválida")
    #Acumular os valores de cada prato escolhido.
    soma += preco
    junta_pratos += prato + " "
    junta_codigos += codigo + " "
    #O sistema deverá perguntar ao usuário se ele deseja fazer outro pedido e, se sim, permitir a adição de mais pratos ao pedido.
    continuar = input("Deseja escolher outra coisa? \nDigite 's' ou '0':").lower()
    #Se o usuário digitar o código "0", o programa encerrará o pedido e calculará o valor total.
    if continuar == "0":
        break

#O sistema deve solicitar a forma de pagamento:
#À vista (desconto de 10% sobre o valor total).
#Cartão de crédito (acréscimo de 10% sobre o valor total).

forma_de_pagamento = int(input("""
    Código \t Forma de pagamento:
    1         Á vista
    2         Cartão de Crédito
    forma de pagamento: """))

#Exibir os resultados ao final:
#A lista com os códigos e nomes dos pratos escolhidos.
# subtotal (valor total sem acréscimo ou desconto).
#A forma de pagamento escolhida.
#O valor do desconto ou acréscimo aplicado.
#O valor final a ser pago.

if forma_de_pagamento == 1:
        desconto = soma * 0.10
        print(f"Subtotal: {soma}")
        print(f"Valor do desconto: {desconto}")
        print(f"Valor total: {soma - desconto}")
        
elif forma_de_pagamento == 2:
    total_pagar = soma * 1.10
    acrescimo = total_pagar - soma
    print(f"Subtotal: {soma}")
    print(f"Valor do acrescimo: {acrescimo}")
    print(f"Valor total: {total_pagar:.2f}")
if forma_de_pagamento == 1:
         pagamento = "Á Vista"
elif forma_de_pagamento == 2:
         pagamento = "Cartão de Crédito"     
       
    
        



   

print(f"Forma de pagamento: {pagamento}")
print (f"Código dos Pratos: {junta_codigos}, Pratos escolhidos: {junta_pratos}.")
print(f"")
   
