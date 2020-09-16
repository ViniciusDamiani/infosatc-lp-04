#TUPLAS
#Sintaxe de criação da tupla
minhaTupla = ("Açai", "Leite Ninho","Nutella","Tupla")
print("Mostrar a tupla: ",minhaTupla)
print("Mostrar um item na posição específica: ",minhaTupla[2])
print("Mostrar o último item da tupla: ",minhaTupla[-1])
print("Mostra o intervaloi de itens: ",minhaTupla[1:2])
#Tentando alterar item na tupla
#minhaTupla[1]= "Leite em pó"
#print(minhaTupla)
#Burlando alteração de dados na tupla
listaClandestina = list(minhaTupla)
listaClandestina.index
print("Lista clandestina: ",listaClandestina)
listaClandestina[2] = "Leite condesado"
print("Lista clandestinacom dado alterado: ",listaClandestina)
minhaTupla = tuple(listaClandestina)
#Criando a tupla com apenas um item (Tem que ter vírgula)
minhaTuplaDois =('tupla',)
print("Verificando tipo de dado: ", type(minhaTuplaDois))
print("Acessando pela posição ordenada: ", minhaTuplaDois[0])
print("Acessando indexação negativa: ", minhaTuplaDois[-1])
#Excluindo completamente a Tupla
#del minhaTuplaDois
#print("Adeus Tupla", minhaTuplaDois)
#Juntando tuplas
minhaTuplaTres = minhaTupla + minhaTuplaDois
print("Juntando as tuplas: ",minhaTuplaTres)
#Função count() serve para contar a quantidade de vezes que se repete o item
quantidadeQueRepete = minhaTuplaTres.count('tupla')
print("Usando função count: ", quantidadeQueRepete)
#Função index() serve para retornar primeira ocorrência do item
posicaoDoItem = minhaTuplaTres.index('tupla')
print("Usando função index (Retorna primeira posição): ", posicaoDoItem)