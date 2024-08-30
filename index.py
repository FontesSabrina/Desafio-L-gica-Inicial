def condicao(lvl):  
    if lvl < 1.000:  
        return 'Ferro'  
    elif lvl <= 2.000:  
        return 'Bronze'  
    elif lvl <= 5.000:  
        return 'Prata'  
    elif lvl <= 6.000:  
        return 'Ouro'  
    elif lvl <= 8.000:  
        return 'Platina Diamante'  
    elif lvl <= 9.000:  
        return 'Ascendente'  
    elif lvl <= 10.000:  
        return 'Imortal'  
    return 'Classificação Desconhecida'

opcao = 0  
L = []  

while opcao != 3:  
    print('1 - Cadastrar Herói:')  
    print('2 - Classificação:')  
    print('3 - Sair:')   
    
    opcao = int(input('Digite uma opção: '))  
    
    if opcao == 1:  # Cadastrar Herói  
        nome = input("Digite o nome do seu Herói: ")  
        lvl = float(input("Digite o seu XP: "))  
        cadastro = {"Nome do Herói": nome, "XP": lvl}  
        L.append(cadastro)  
        print("Cadastro com sucesso!")  
    
    if opcao == 2:  # Classificação do Herói  
        if L:  # Verifica se há heróis cadastrados  
            for hero in L:  
                xp_str = format(hero["XP"], '.3f')  # Formata o XP como string com 3 casas decimais  
                classificação = condicao(hero["XP"])  # Usa o valor numérico para a classificação  
                print(f"Herói: {hero['Nome do Herói']}, XP: {xp_str}, Classificação: {classificação}")  
        else:  
            print("Nenhum herói cadastrado.")   
    
    if opcao == 3:  # Sair  
        print("Adeus, herói! Até a próxima aventura!")  
        break  
        
    else:  
        print('Opção inválida, tente novamente.')