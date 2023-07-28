import time
import getpass
import os
from datetime import datetime
import re
data_atual = datetime.now()

print("-----BEM VINDO A CODIGOS AND DRAGONS-----")

print("--------CADASTRO--------")
time.sleep(1)

while True:
    name = input("Nome completo: ")
    if name.strip(): 
        break  
    else:
        print("Por favor, insira um nome válido.")

while True:
    date_born = input("Digite a data de nascimento (DD/MM/AAAA): ")
    try:
        date_born = datetime.strptime(date_born, "%d/%m/%Y")
        break 
    except ValueError:
        print("Data de nascimento inválida. Certifique-se de digitar no formato DD/MM/AAAA.")
while True:
    email=input("Seu E-mail: ")
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
   
    if re.match(email_pattern, email):
        break
    else:
        print("E-mail inválido. Por favor, insira um e-mail válido.")

while True:
    password = getpass.getpass("Escolha uma senha: ")
    confirm_password = getpass.getpass("Confirme sua senha: ")
    
    if password == confirm_password and password != "":
        print("Senha definida com sucesso!")
        break
    else:
        if password == "":
            print("Você deve inserir uma senha.")
        else:
            print("As senhas não são iguais. Tente novamente!")

age = data_atual.year - date_born.year - ((data_atual.month, data_atual.day) < (date_born.month, date_born.day))
if age < 18:
    print("É necessário ter no mínimo 18 anos para se cadastrar.")
    exit(1)
    
print("Voce sera direcionado para a tela de Login")
os.system('cls')
print("AGUARDE. . .")
time.sleep(1)
os.system('cls')

print("--------LOGIN--------")
time.sleep(1)

attempts = 0
attempts_max = 3

while attempts < attempts_max:
    email_login = input("E-mail: ")
    senha_login = getpass.getpass("Senha: ")
    
    if email_login == email and senha_login == password:
        print("Login bem-sucedido!")
        time.sleep(1)
        break
    else:
        attempts += 1
        remaining_attempts = attempts_max - attempts
        if remaining_attempts > 0:
          print(f"Email ou senha incorretos. Você ainda tem {remaining_attempts} tentativa(s).\n")
        
    if attempts == attempts_max:
        print("Você excedeu o número máximo de tentativas permitidas. O jogo será finalizado.")
        exit(1)

print("Você esta sendo direcioado par ao jogo")
os.system('cls')
time.sleep(1)

print("--------Codigos and Dragons--------")

print("[1] Paladino")
print("[2] Atirador")
print("[3] Guerreiro")
print("[4] Bárbaro")
print("[5] Arqueiro")

while True:
    class_choice = input("Escolha o número do seu Herói: ")

    if class_choice == "1":
        print("Você escolheu o Paladino.")
        vida = 85
        mana = 35
        velocidade_ataque = 1.25
        break
    elif class_choice == "2":
        print("Você escolheu o Atirador.")
        vida = 80
        mana = 25
        velocidade_ataque = 1.75
        break
    elif class_choice == "3":
        print("Você escolheu o Guerreiro.")
        vida = 100
        mana = 20
        velocidade_ataque = 1.0
        break
    elif class_choice == "4":
        print("Você escolheu o Bárbaro.")
        vida = 110
        mana = 10
        velocidade_ataque = 0.8
        break
    elif class_choice == "5":
        print("Você escolheu o Arqueiro.")
        vida = 75
        mana = 30
        velocidade_ataque = 2.0
        break
    else:
        print("Opção inválida, por favor escolha um número entre 1 e 5.")

os.system('cls')

print("---Defina as caracteristicas fisicas do seu Herói---")

caracteristicas_fisicas = []

while True:
    caracteristica = input("Escreva uma característica física (Ex. Olhos castanhos) (ou 'sair' para finalizar): ")

    if caracteristica.lower() == 'sair':
        break
    if not caracteristica.strip():
        print("Erro: Característica inválida. Por favor, insira uma característica válida.")
    else:
        caracteristicas_fisicas.append(caracteristica)

os.system('cls')

print("-------- O GRANDE DIFERENCIAL ESTA NAS FERRAMENTAS DE BATALHA --------")

if class_choice == "1":  
    print("[1] Lança")
    print("[2] Escudo")
    while True:
        arma_choice = input("Escolha o número da arma: ")
        if arma_choice == "1":
            arma_escolhida = "Lança"
            break
        elif arma_choice == "2":
            arma_escolhida = "Escudo"
            break
        else:
            print("Opção inválida, por favor escolha um número entre 1 e 2.")

elif class_choice == "2": 
    print("[1] Arma")
    while True:
        arma_choice = input("Escolha o número da arma: ")
        if arma_choice == "1":
            arma_escolhida = "Arma"
            break
        else:
            print("Opção inválida, por favor escolha o número 1.")

elif class_choice == "3":  
    print("[1] Espada e escudo")
    while True:
        arma_choice = input("Escolha o número da arma: ")
        if arma_choice == "1":
            arma_escolhida = "Espada e escudo"
            break
        else:
            print("Opção inválida, por favor escolha o número 1.")

elif class_choice == "4":  
    print("[1] Machado")
    print("[2] Marreta")
    while True:
        arma_choice = input("Escolha o número da arma: ")
        if arma_choice == "1":
            arma_escolhida = "Machado"
            break
        elif arma_choice == "2":
            arma_escolhida = "Marreta"
            break
        else:
            print("Opção inválida, por favor escolha um número entre 1 e 2.")

elif class_choice == "5":  
    arma_escolhida = "Arco"

else:
    print("inválido!")

print(f"Você escolheu a arma: {arma_escolhida}")
os.system('cls')

print(" ----- UM GRANDE GUERREIRO PRECISA DE UMA GRANDE MONTARIA ----- ")
print("[1] - Cavala do guerra")
print("[2] - Panda")
print("[3] - Lobo Gigante")
print("[4] - Dragão pequeno")
print("[5] - Hipogrifo ")

while True:
    ride_choice = input("Escolha o número da sua montaria: ")

    if ride_choice == "1":
        print("Você escolheu o Cavalo de Guerra.")
        velocidade_montaria = "3.0 m/s"
        tempo_descanso = "5 minutos"
        break
    elif ride_choice == "2":
        print("Você escolheu o Panda.")
        velocidade_montaria = "2.5 m/s"
        tempo_descanso = "6 minutos"
        break
    elif ride_choice == "3":
        print("Você escolheu o Lobo Gigante.")
        velocidade_montaria = "3.2  m/s"
        tempo_descanso = "4 minutos"
        break
    elif ride_choice == "4":
        print("Você escolheu o Dragão Pequeno.")
        velocidade_montaria = "4.5 m/s"
        tempo_descanso = "8 minutos"
        break
    elif ride_choice == "5":
        print("Você escolheu o Hipogrifo.")
        velocidade_montaria = "3.8 m/s"
        tempo_descanso = "7 minutos"
        break
    else:
        print("Opção inválida, por favor escolha um número entre 1 e 5.")

os.system('cls')
time.sleep(1)

print(" ----- PARABENS VIAJANTE SEU HERÓI ESTA PRONTO ----- ")

print(" ---- Heroi ---- ")
print(f" -> Classe: {'Paladino' if class_choice == '1' else 'Atirador' if class_choice == '2' else 'Guerreiro' if class_choice == '3' else 'Bárbaro' if class_choice == '4' else 'Arqueiro'}")
print(f" -> Vida: {vida}")
print(f" -> Mana: {mana}")
print(f" -> Velocidade de Ataque: {velocidade_ataque}")
print(" -> Características do Herói:")
for caracteristica in caracteristicas_fisicas:
    print("    -", caracteristica)
print(f" -> Arma do Herói: {arma_escolhida}")
print(f" -> Montaria: {'Cavalo de Guerra' if ride_choice == '1' else 'Panda' if ride_choice == '2' else 'Lobo Gigante' if ride_choice == '3' else 'Dragão Pequeno' if ride_choice == '4' else 'Hipogrifo'}")
print(f" -> Atributos da Montaria: Velocidade - {velocidade_montaria}, Tempo para descanso - {tempo_descanso}")

print(" ----- OBRIGADO POR JOGAR ----- ")


time.sleep(2)

input("Pressione Enter para sair...")







