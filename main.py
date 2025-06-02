from functions import * 
from crud import *


while True: 
    
    opcao = menu()
    
    if opcao < 1 or opcao > 6 :
        print("Opcao invalida digite uma opcao entre 1 e 6.\n")
        y(0.8)
        continue
    else :
        match opcao : 
            case 1 : 
                addTask()
            case 2 : 
                removeTask()
            case 3 : 
                findByWord()
            case 4 : 
                listTasks()
            case 5 :
                updateTask()
            case 6 : 
                print("\nSaindo do programa...\n")
                break






