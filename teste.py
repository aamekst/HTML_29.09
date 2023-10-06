class Endereco:
    def __init__(self,rua, numero,complemento,bairro,cidade,uf,cep):
        self.rua=rua
        self.numero=numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade=cidade
        self.uf=uf
        self.cep=cep
    

class Cliente:
    def __init__(self,nome,telefone,endereco):
        self.nome=nome
        self.telefone=telefone
        self.endereco=endereco


class Historico:
    def __init__(self):
        self.__pedidos=[]
    
    def inserir_pedido(self,pedido):
        self.__pedidos.append(pedido)
    
    def calcular_faturamento(self):
        faturamento = 0
        for pedido in self.__pedidos:
            faturamento += pedido.get_valor_total()
        return faturamento
      

class Pedido:
    def __init__(self,cliente,altura,largura,frase,cor_placa,cor_letra):
        self.cliente=cliente
        self.altura=altura
        self.largura=largura
        self.frase=frase
        self.cor_placa=cor_placa
        self.cor_letra=cor_letra
        self.__valor_fixo_material = 147.00
        self.__valor_fixo_letra = 0.35
        self.__valor_total = None


    def __remove(self, frase):
        frase = frase.replace(' ', '')
        return frase

    def get_valor_total(self):
        area = self.altura * self.largura 
        custo_material = area * self.__valor_fixo_material
        custo_desenho = len(self.__remove(self.frase)) * self.__valor_fixo_letra
        valor_placa = custo_material + custo_desenho
        self.__valor_total = valor_placa
        return self.__valor_total



pedidos = []
historico1 = Historico()

while True:
  try:

      print('1 - Pedido')
      print('2 - Historico')
      print('3 - Encerrar')
      opcao = int(input('Escolha uma opção: '))
      for p in range(1):
          if opcao == 1:
              print('Inserira seus dados pessoais \n')
              nome = input('Digite seu nome: ')
              
              while True:
                  telefone=input('Digite o Telefone + (DD): ')
                  if len(telefone) ==11 :
                      break
                  else:
                      print('\nTelefone incorreto...\n')
          
              print('\nEndereço:')
              rua=input('Digite o nome da rua: ')
              numero=input('Digite o numero: ')
              complemento = input('Digite o complemento: ')
              bairro = input('Digite o bairro: ')
              cidade=input('Digite a cidade: ')

              while True:
                  uf=input('Digite o UF: ')
                  if len(uf) ==2 :
                      break
                  else:
                      print('\nUF incorreto...\n')


              while True:
                  cep=input('Digite o CEP: ')
                  if cep.isdigit():
                      break
                  else:
                      print('\nCEP incorreto...\n')

              endereco = Endereco(rua, numero, complemento,bairro,cidade,uf,cep)
              cliente1 =  Cliente (nome,telefone,endereco)


              print('\nEspecifições da placa:\n')
              while True: 
                  try:
                      altura= float(input('Digite a altura da placa: '))
                      largura= float(input('Digite a largura da placa: '))
                      break

                  except ValueError:
                      print('Erro. Valor invalido, apenas número\n')
              
              
              frase= input('Digite a frase que deseja colocar na placa: ')

              while True: 
                  cor_placa= input('Digite a cor da placa BRANCO ou CINZA:: ')
                  if cor_placa in ['branco', 'branca', 'cinza']:
                      break
                  else:
                      print('\nCores indisponíveis, escolha entre BRANCA ou CINZA\n')
      
              while True:
                  cor_letra= input('Digite a cor das letras: ')
                  if cor_letra in ['azul', 'vermelha','vermelho', 'amarela', 'amarelo', 'preta', 'preto', 'verde']:
                      break
                  
                  else:
                      print('\nCores indisponiveis, escolha entre azul, vermelha, amarela, preta, verde')
                  

              print('------------------')
              pedido = Pedido(cliente1, altura, largura,frase,cor_placa,cor_letra)
              pedidos.append(pedido)
              historico1.inserir_pedido(pedido)

              print(f'TOTAL: {pedido.get_valor_total()} \n')
          
          elif opcao ==2: 
              historico1.calcular_faturamento()

              print('Todos pedidos: \n')
              cont=0
              for pedido in pedidos:
                  cont +=1
                  print(f'Pedido {cont}\nNome: {pedido.cliente.nome}  | Telefone: ({pedido.cliente.telefone[:2]}){pedido.cliente.telefone[2:]} \nEndereço: {pedido.cliente.endereco.rua} n° {pedido.cliente.endereco.numero} {pedido.cliente.endereco.complemento}, {pedido.cliente.endereco.bairro}, {pedido.cliente.endereco.cidade} - {pedido.cliente.endereco.uf}, {pedido.cliente.endereco.cep[:5]}-{pedido.cliente.endereco.cep[5:]}\nFrase: {pedido.frase} | Cor da placa: {pedido.cor_placa} | Cor das letras: {pedido.cor_letra} \nAltura: {pedido.altura} | Largura : {pedido.largura} \nvalor da placa: {pedido.get_valor_total()}\n')
              print('----------------')
              print(f'Faturamento total: {historico1.calcular_faturamento():.2f} \n')

          elif opcao == 3:
              print('Programa finalzado')
              exit()
          
          else:
              print('opção errada \n')
  except ValueError:
    print('Erro. Caracter invalido, escolha novamente\n')