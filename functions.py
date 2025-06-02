from os import system
from time import sleep
import platform

# Função para limpar o terminal 
def x():
    a = platform.system()

    if a == 'Windows':
        system('cls')

    elif a == 'Linux':
        system('clear')
        
def y(timer) :
    sleep(timer)


def menu() : 
    print("\nGS - PYTHON\n")
    print("Escolha uma das opcao: \n")
    print("[1] - Adicionar uma task")
    print("[2] - Remover uma task")
    print("[3] - Buscar uma task por palavra-chave")
    print("[4] - Buscar todas as tasks")
    print("[5] - Alterar uma task")
    print("[6] - Sair do programa")
    
    # opcao = int(input("\nInforme uma opcao valida: "))
    opcao = leitorCoringa(int, "\nInforme uma opcao valida: ", "Opcao inválida, tente novamente!")
    x()
    return opcao

# Função que inputar um valor com o tipo primitivo específico   
def leitorCoringa(tipoPrimitivo, msg, msgError) :
        
    while True : 
        try :
            x  = tipoPrimitivo(input(f'{msg}').replace(',','.'))
        except :
            print(f'\n{msgError}\n')
            y(1)
        else : 
            return x; 