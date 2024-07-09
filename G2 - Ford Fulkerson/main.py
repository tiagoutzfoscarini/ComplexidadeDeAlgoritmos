#
from collections import defaultdict


class Graph:
	def __init__(self, graph):
		self.graph = graph # residual graph
		self.ROW = len(graph)
		self.case = {0: 'S', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'T'}


	def BFS(self, s, t, parent):
		# Inicializa todos os nodos como não visitados
		visited = [False]*(self.ROW)

		# Inicializa fila para a busca em largura
		queue = []

		# Define o nodo de origem como visitado e o coloca na fila
		queue.append(s)
		visited[s] = True

		# Busca em largura
		while queue:
			# Define u como o nodo atual e o remove da fila
			u = queue.pop(0)

			# Lista os nodos adjacentes ao nodo u
			for ind, val in enumerate(self.graph[u]):
				# Se o nodo não foi visitado e o valor residual é maior que 0, então marca como visitado e coloca na fila
				# Define armazena o nodo pai do nodo atual
				if visited[ind] == False and val > 0:
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u

					# Se o nodo é o destino, retornar verdadeiro
					if ind == t:
						return True

		# Se não foi possível chegar ao destino através da busca, retorna falso
		return False
			
	
	def FordFulkerson(self, source, sink):
		# Vetor para armazenar o caminho
		# Cada valor indica o pai do nodo atual (índice do vetor)
		parent = [-1]*(self.ROW)

		max_flow = 0

		# Enquanto existe um caminho entre origem e destino, chama a busca em largura
		while self.BFS(source, sink, parent) :
			# Inicializa fluxo do caminho atual e define o nodo de destino
			path_flow = float("Inf")
			s = sink

			# Enquando nodo atual não é origem, procura a capacidade residual mínima do caminho 
			while(s != source):
				path_flow = min(path_flow, self.graph[parent[s]][s])
				s = parent[s]

			# Adiciona o fluxo do caminho calculado ao fluxo máximo
			max_flow += path_flow

			# Atualiza a capacidade residual entre os nodos do caminho
			# v é o nodo de destino
			# u é o nodo pai de v
			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow

				# print("u -> v: ", self.case[u], " -> ", self.case[v], " = ", path_flow)

				v = parent[v]

		return max_flow, self.graph
	
	
	def printGraph(self):
		print("  |  S |  A |  B |  C |  D |  T |")
		print("---------------------------------")
		for i in range(self.ROW):
			print(self.case[i], end=' | ')

			for j in range(self.ROW):
				print(str(self.graph[i][j]).zfill(2), end=' | ')
			print("\n---------------------------------")
		print("\n")


	def printDefinition(self):
		print("GRAPH DEFINITION")
		for i in range(self.ROW):
			for j in range(self.ROW):
				if (self.graph[i][j] > 0):
					print(self.case[i], " -> ", self.case[j], " = ", self.graph[i][j])
		print("\n")
			

if __name__ == "__main__":
	print()

	# Cria um grafo com a matriz abaixo, demonstrando a capacidade de cada caminho
	# Matriz 6x6 para 6 nodos e a capacidade de cada caminho entre eles
	# graph = [
	# 	[0, 16, 13, 0, 0, 0], # S
	# 	[0, 0, 10, 12, 0, 0], # A
	# 	[0, 4, 0, 0, 14, 0], # B
	# 	[0, 0, 9, 0, 0, 20], # C
	# 	[0, 0, 0, 7, 0, 4], # D
	# 	[0, 0, 0, 0, 0, 0] # T
	# ]

	# graph = [
	# 	[0, 10, 0, 10, 0, 0], # S
	# 	[0, 0, 4, 2, 8, 0], # A
	# 	[0, 0, 0, 0, 0, 10], # B
	# 	[0, 0, 0, 0, 9, 0], # C
	# 	[0, 0, 6, 0, 0, 10], # D
	# 	[0, 0, 0, 0, 0, 0], # T
	# ]

	# Grafo do exemplo no documento
	graph = [
		[0, 8, 0, 0, 3, 0], # S
		[0, 0, 9, 0, 0, 0], # A
		[0, 0, 0, 0, 7, 2], # B
		[0, 0, 0, 0, 0, 5], # C
		[0, 0, 7, 4, 0, 0], # D
		[0, 0, 0, 0, 0, 0], # T
	]

	# Define a origem e o destino
	source = 0; sink = 5

	# Cria um objeto do tipo Graph
	g = Graph(graph)

	# Imprime a definição do grafo
	g.printDefinition()

	# Imprime o grafo inicial
	print("GRAFO INICIAL")
	g.printGraph()

	# Chama o método FordFulkerson para calcular o fluxo máximo
	resultado, graphFinal = g.FordFulkerson(source, sink)

	# Imprime o grafo final
	print("GRAFO FINAL")
	gFinal = Graph(graphFinal)
	gFinal.printGraph()

	print ("Fluxo máximo é %d " % resultado)
