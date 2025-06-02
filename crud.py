from functions import *

status = ["","Em andamento", "Cancelado", "Concluida"]
tasks = [["a", status[1]], ["b", status[3]], ["a", status[3]]]

index = 0

def addTask():
    while True:
        titulo = leitorCoringa(str, "Informe o titulo da task: ", "Informe um nome válido")
        if titulo == "":
            print("\nTitulo nao pode ser vazio. Tente novamente.\n")
            continue
        else:
            tasks.append([titulo, status[1]])
            print("\nTask adicionada com sucesso.\n")
            
            y(1)
            x()
            
            break

def removeTask():
    
    while True:
        y(0.5)
        
        if len(tasks) != 0 :
            listTasks()
            remove = leitorCoringa(int, "\nInforme o numero da task que voce deseja remover: ", "Informe um numero valido! Tente novamente: ")
            x()
            if remove >= 0 and remove <= (len(tasks) - 1): 
                tasks.pop(remove)
                print(f"\nTask {remove} removida com sucesso.\n")
                y(1)
                x()
                break
            else: 
                print("\nDigite o número de uma task válida\n")
                continue
        else : 
            print("\nNão há tasks disponíveis. Por favor, adicione uma task para prosseguir com a remoção.\n")        
            break
    
def listTasks():
    print("\n----- Lista de Tasks -----\n")
    print("{:<10}{:<50}{}".format("ID", "task", "Status"))
    print("-" * 70)
    for index, task in enumerate(tasks):
        print("{:<10}{:<50}{}".format(index, task[0], task[1]))

def findByWord():
    taskFinded = False

    word = leitorCoringa(str, "Informe a palavra-chave para buscar: ", "Erro! Tente novamente...")
    print(f"\n----- Lista de Tasks com a palavra-chave {word} -----\n")
    print("{:<10}{:<50}{}".format("ID", "task", "Status"))
    print("-" * 70)
    for x, task in enumerate(tasks):
        splitedText = tasks[x][0].lower().split()

        for y, wordTask in enumerate(splitedText):
            if wordTask == word.lower():
                taskFinded = True
                print("{:<10}{:<50}{}".format(x, task[0], task[1]))
                break
    if taskFinded == False:
        print(f"\nNenhuma task encontrada com a palavra-chave '{word}'.")
    
def updateStatus():
    x()
    while True:
        listTasks()
        
        numTask = leitorCoringa(int, "\nInforme o ID da task que voce deseja alterar o status: ", "Numero invalido! Tente novamente...")
        
        if numTask >= 0 and numTask <= len(tasks) -1 : 
            
            while True: 
                
                print(f"\nInforme o status para a task com ID {numTask}:\n")
                print("[1] - Em Andamento")
                print("[2] - Cancelado")
                print("[3] - Concluido")
                
                statTask = leitorCoringa(int, "\nStatus desejado: ", "Numero invalido, tente novamente!")
                
                x()
                listTasks()
                
                if statTask < 0 or statTask > 3: 
                    print("\nOpcao invalida digite uma opcao entre 1 e 3.")
                    y(0.7)
                    continue
                else:
                    tasks[numTask][1] = status[statTask]
                    break
                
        else :
            print("\nOpcao invalida digite o ID de uma task valida\n")
            continue
        x()
        listTasks()
        break

        

def updateName():
    
    while True:
        
        listTasks() 
        
        numTask = leitorCoringa(int, "\nInforme o ID da task que voce deseja alterar: ", "Numero invalido, tente novamente...")
        
        if numTask >= 0 and numTask <= len(tasks) -1 : 
            
            newTask = leitorCoringa(str, "\nInforme o novo titulo da task: ", "Task invalida, tente novamente...")
            
            if newTask == "":
                print("\nTitulo nao pode ser vazio. Tente novamente.")
                break
            else : 
                tasks[numTask][0] = newTask
                print(f"\nTask com ID {numTask} titulo alterado para '{newTask}' com sucesso.")
        
        else: 
            print("\nOpcao invalida digite o ID de uma task valida\n")
            continue
            

def updateTask():
    while True: 
        print("\nDeseja editar o status ou o texto? \n")
        print("[1] - Alterar Status da Task")
        print("[2] - Alterar Texto da Task")
        print("[3] - Voltar")
  
        opcao = leitorCoringa(int, "\nInforme uma das opcoes: ", "Erro! Opcao invalida, tente novamente!")
    
        if opcao < 1 or opcao > 3:
            print("\nOpcao invalida digite uma opcao entre 1 e 3.\n")
            continue
        else :
            x()
            match opcao : 
                case 1 : 
                    updateStatus()
                case 2 : 
                    updateName()
                case 3 : 
                    break