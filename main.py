  import random
      
  naipes= ['ouro', 'espada', 'pau', 'copas']
  números= ['Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]      cartas= []
    #para os naipes
  for i in range(4): 
    #for para números
  for u in range(13):
  cartas.append(str(numeros[u])+" de "+naipes[i])
      
  quantidade = int(input("digite a quantidade de cartas:"))
  
  random.shuffle(cartas)
  
  for i in range(quantidade):
  print(cartas)[s]













