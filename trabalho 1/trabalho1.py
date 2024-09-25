# Dicionário com os carros e seus valores
carros = {
    'Ford Mustang': 300000,
    'Chevrolet Camaro': 250000,
    'Toyota Corolla': 120000,
    'Honda Civic': 110000,
    'BMW X5': 400000
}

def atendimento_loja():
    while True:
        print("\nBem-vindo à loja de veículos")
        print("Por favor, escolha uma das opções abaixo:")
        print("1. Ver carros disponíveis")
        print("2. Consultar preço de um carro específico")
        print("3. Comprar um carro")
        print("4. Encerrar")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            if carros:
                print("\nCarros disponíveis:")
                for carro in carros:
                    print(f"- {carro}")
            else:
                print("\nNão há carros disponíveis no momento.")
        
        elif opcao == '2':
            carro_desejado = input("\nDigite o nome do carro que deseja consultar: ")
            if carro_desejado in carros:
                print(f"O preço do {carro_desejado} é R${carros[carro_desejado]:,.2f}.")
            else:
                print("Desculpe, este carro não está disponível em nosso estoque.")
        
        elif opcao == '3':
            carro_compra = input("\nDigite o nome do carro que deseja comprar: ")
            if carro_compra in carros:
                print(f"Você escolheu comprar o {carro_compra} por R${carros[carro_compra]:,.2f}.")
                print("Um de nossos vendedores entrará em contato com você em breve para finalizar a compra.")
                del carros[carro_compra]
                print("Conexão encerrada. Obrigado por visitar")
                break
            else:
                print("Desculpe, este carro não está disponível em nosso estoque.")
        
        elif opcao == '4':
            print("Encerrando a conexão. Obrigado por visitar")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
    
    print("Conexão encerrada.")

# Executa o chatbot
atendimento_loja()
