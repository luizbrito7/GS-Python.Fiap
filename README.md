# GS-Python

Este repositório implementa um sistema simples de gerenciamento de tasks via terminal usando Python. Ele utiliza operações CRUD para adicionar, remover, listar, procurar e atualizar tasks, permitindo a alteração tanto do status quanto do texto de cada task.

## Estrutura do Repositório

- **functions.py**  
  Contém funções utilitárias, como a função para limpar o terminal, aguardar um tempo determinado e ler entradas do usuário com validação.  
  Veja: [`functions.x`](functions.py), [`functions.leitorCoringa`](functions.py)
  
- **crud.py**  
  Implementa as operações CRUD (Criar, Remover, Atualizar, Buscar) para gerenciar as tasks.  
  Veja: [`crud.addTask`](crud.py), [`crud.removeTask`](crud.py), [`crud.updateName`](crud.py), [`crud.updateTask`](crud.py)
  
- **main.py**  
  Arquivo principal que executa o loop do programa, exibindo o menu e direcionando para as funções do CRUD conforme a escolha do usuário.  
  Veja: [`main.py`](main.py)

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. No terminal, dentro do diretório do repositório, execute:
   
   ```sh
   python main.py