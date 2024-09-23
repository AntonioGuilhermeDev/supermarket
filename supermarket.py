import os

items = {"Abacate" : 3.50,
         "Maca" : 2.00,
         "Biscoito" : 1.50,
         "Bolacha" : 2.00,
         "Cafe" : 4.00,
         "Acucar" : 3.00,
         "Pirulito" : 1.00,}

users = {'Admin' : 'admin'
}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_items():
    if items:
        print("Lista de Produtos:\n")
        for item, preco in items.items():
            print(f'{item}: R$ {preco:.2f}')
    else:
        print("A lista de produtos está vazia.")

def add_items():
  while True:
    item = input("Digite o nome do item que deseja adicionar (Digite 1 para parar)\n").capitalize()
    if item == '1':
      break
    if item in items:
      print('Este item já foi adicionado')
      continue
    elif len(item) == 0:
      print('O nome de item não pode estar vazio.')
      continue
    try:
      price = float(input(f'Digite o preço de {item}\n'))  # Recebe o preço e converte para float
    except ValueError:
      print("Por favor, insira um número válido para o preço.")
      continue
    items[item] = price
    print(f'{item} foi adicionado a lista de items')

def consult_item():
  item = input("Digite o item que deseja procurar\n").capitalize()
  if item in items:
    return f"O valor de {item} é R$ {items[item]:.2f}"
  else:
    return 'Este item não está na lista.'

def change_price():
  item = input("Digite o item que deseja atualizar o valor\n").capitalize()
  if item in items:
    new_price = float(input(f'Digite o novo valor de {item}\n'))
    items[item] = new_price
    return 'O valor do item foi alterado com sucesso!'
  else:
    return 'O item não está na lista'
  
def remove_item():
  item = input('Digite o item que deseja remover da lista\n').capitalize()
  if item in items:
    del items[item]
    return f'{item} foi removido da lista de produtos'
  else:
    return f'{item} não está na lista de produtos'
  
def register():
  sucessful_register = False
  while True:
    name = input('Digite seu nome\n').capitalize()
    if name in users:
      print('Esse usuário já está cadastrado!')
    elif len(name) == 0:
      print('O nome de usuario não pode estar vazio.')
    else:
      while True: 
        password = input('Digite uma senha\n')
        confirm_password = input('Confirme sua senha\n')
        if password == confirm_password:
          users[name] = password
          print(f'{name} foi cadastrado com sucesso!')
          input("\nPressione Enter para continuar...")
          sucessful_register = True
          break
        else:
          print('As senhas não coincidem. Por favor, tente novamente.')
    if sucessful_register == True:
      break

def login():
  attempts = 0
  max_attempts = 3

  while attempts < max_attempts:
    name = input('Digite seu nome de usuario\n').capitalize()
    password = input('Digite sua senha\n')
    if name in users and users[name] == password:
      print('Acesso autorizado!')
      return True
    else:
      attempts += 1
      print('O usuario ou a senha estão incorretas.')
      if attempts < max_attempts:
        print(f'tentativa {attempts}/{max_attempts}.')
      else:
        register_user = input('Talvez você não esteja registrado. Você gostaria de se registrar? (s/n)\n')
        if register_user.lower() == 's':
          register()
        else:
          print('Voce excedeu o limite de tentativas de login. Tente novamente mais tarde.')
          return False
        
while True:
  clear_terminal()

  while True:
    try:
      print('Seja bem-vindo ao supermercado\n') 
      user_type = int(input('Voce é um cliente ou um funcionario? \n 1. Funcionario \n 2. Cliente \n'))
      if user_type not in [1, 2]:
        clear_terminal()
        print('Opção inválida. Por favor, escolha 1 ou 2.')
      break
    except ValueError:
      print('Entrada inválida. Por favor, insira 1 ou 2.')
      input("\nPressione Enter para tentar novamente...")
      clear_terminal()


  if user_type == 1:
    while True:
      clear_terminal()
      try:
        opcao_autenticacao = int(input('Escolha uma opção:\n 1. Registrar-se\n 2. Fazer Login\n'))
        match opcao_autenticacao:
          case 1: 
            register()
          case 2:
            if login():
              break
          case _:
            print("Opção invalida!")
      except ValueError:
        print('Por favor digite uma opção valida.')
        input("\nPressione Enter para tentar novamente...")

    while True:
      clear_terminal()
      try: 
        opcao = int(input('Escolha uma opção:\n 1. Ver Lista de Produtos \n 2. Consultar preço\n 3. Alterar preço \n 4. Adicionar um produto \n 5. Remover um produto \n 6. Sair \n'))
        match opcao:
          case 1:
            clear_terminal()
            list_items()
          case 2:
            clear_terminal()
            print(consult_item())
          case 3: 
            clear_terminal()
            print(change_price())
          case 4:
            clear_terminal()
            add_items()
          case 5:
            clear_terminal()
            print(remove_item())
          case 6:
            print('Saindo...')
            break
          case _:
            print("Opção invalida!")
        input("\nPressione Enter para continuar...")
      except ValueError:
        print('Por favor digite uma opção valida.')
        input("\nPressione Enter para tentar novamente...")
  else:
    while True:
      clear_terminal()
      opcao = int(input('Escolha uma opção:\n 1. Ver Lista de Produtos \n 2. Consultar preço\n 3. Sair \n'))
      match opcao:
        case 1:
          list_items()
        case 2:
          print(consult_item())
        case 3:
          print('Saindo...')
          break
        case _:
          print("Opção invalida!")

      input("\nPressione Enter para continuar...")

  input("\nPressione Enter para continuar...")


