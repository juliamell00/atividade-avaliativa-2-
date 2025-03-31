import os 
os.system ("cls || clear")

soma = 0
contador = 0 
preco = 0


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
            case 2:
                print("Prato: Parmediana, Valor: 50,00")
                prato ="Parmediana"
                preco = 50
            case 3:
                print("Prato: Macarrão á Carbonara, Valor: 75,00")
                prato ="Macarrão á Carbonara"
                preco = 75
            case 4:
                print("Prato: Risoto de Camarão, Valor: 80,00")
                prato ="Risoto de Camarão"
                preco = 80
            case 5:
                print("Prato: Lasanha, Valor: 20,00")
                prato ="Lasanha"
                preco = 20
            case 6: 
                print("Prato: Filé de Frango, Valor: 25,00")
                prato = "Filé de frango"
                preco = 25
            case 7:
                print("Prato: Escondidinho, Valor: 65,00")
                prato = "Escondidinho"
                preco = 65
            
            case _:
                print("Opção inválida")
    soma += preco
    continuar = input("Deseja escolher outra coisa? \nDigite 'S' ou '0':").lower()
    if continuar == "0":
        break

    
forma_de_pagamento = int(input("""
    Código \t Forma de pagamento:
    1         Á vista
    2         Cartão de Crédito
    forma de pagamento: """))
if forma_de_pagamento == 1:
        desconto = soma * 0.10
        print(f"Valor do desconto: {desconto}")
        print(f"Valor total: {soma - desconto}")
        
elif forma_de_pagamento == 2:
    acrescimo = soma * 1.10
    print(f"Valor do acrescimo: {acrescimo}")
    print(f"Valor total: {soma - acrescimo}")
       
    
        
junta_pratos = ""

junta_pratos += prato + " "
   

print(f"Subtotal: {soma}")

print(f"Forma de pagamento {forma_de_pagamento}")
print (f"Pratos: {junta_pratos}")

   

        


