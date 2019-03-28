import time

def pertence(vertice, fila):
	if(fila.count(vertice) == 0):
		return False
	return True

def bidirecional_bel(grafo, origem, destino):
	f_ori = []
	f_dest = []

	vis_o = []
	vis_d = []
	
	f_ori.append(origem)									# Coloca o vértice de origem e destino em suas respectivas filas
	vis_o.append(origem)									# e os marca como visitados
	
	f_dest.append(destino)
	vis_d.append(destino)
	# visitados.append(origem)
	
	while(f_ori and f_dest):
		if(f_ori):											# Enquanto a fila não estiver vazia
			x1 = f_ori.pop(0)								# Retira o primeiro "vértice" da fila
			if(x1 == destino or pertence(x1, f_dest)):		# Verifica se x1 é o vértice de destino ou se ele pertence a fila de destino
				return "Intersecção em {}".format(vis_o[vis_o.count(x1)]) # Retorna o vértice de intersecção
			for v_x1 in grafo.get(x1[0]):					# Para todos os vizinhos v_x1 de x1, faça:
				if(vis_o.count(v_x1) == 0):					# se v_x1 não foi visitado, marcar como visitado
					vis_o.append(v_x1)						# e colocá-lo na fila
					f_ori.append(v_x1)

		if(f_dest):											# Repetição do código acima para a bel(Busca em Largura) a partir do vértice de destino
			x2 = f_dest.pop(0)
			if(x2 == origem or pertence(x1, f_ori)):
				return "Intersecção em {}".format(vis_d[vis_d.count(x1)]) # Sucesso
			for v_x2 in grafo.get(x2[0]):
				if(vis_d.count(v_x2) == 0):
					vis_d.append(v_x2)
					f_dest.append(v_x2)
	return "Não há intersecção"								# Caso não haja intersecção entre entre os dois vértices

def main():
	grafo = {
	    'a': ['b', 'd'],
	    'b': ['a', 'c', 'd', 'e'],
	    'c': ['b','e'],
	    'd': ['a', 'b', 'e', 'f'],
	    'e': ['b', 'c', 'd', 'f', 'g'],
	    'f': ['d', 'e', 'g'],
	    'g': ['e', 'f'],
	    'h': ['i'],
	    'i': ['h']
	}

	t = time.time()
	print("Bidirecional => Resultado:", bidirecional_bel(grafo, "a", "g"), "\b. Resolvido em {:02.8f}".format(time.time()-t), "segundo(s)")


if __name__ == '__main__':
	main()