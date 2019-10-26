# tryAppend() testa se tem espaco em algum lado (2 opções) da criança
def tryAppend(a, b, grafo):
	if b not in grafo[a]:
		if len(grafo[a]) == 2:
			return False
		else:
			grafo[a].append(b)
			grafo[b].append(a)
	return True

# main()
def main():
	k, w = map(int, input().split())
	while k >=3 and k <= 10**9 and w>=0 and w<=10**5:
		if w<=2:
			print("Y")
		else:

			grafo = {x:[] for x in range(1,k+1)}
			for i in range(w):
				a, b = map(int, input().split())
				sucesso = tryAppend(a,b,grafo) # guarda se {deu pra inseir ou ja inseriu} (True) ou {não} (False)
				if not sucesso:
					break

			if sucesso:
				ListaDeFora = []
				ListaTemEspaco = []
				for i in range(1,len(grafo)+1):
					if len(grafo[i])==0:
						ListaDeFora.append(i)
					elif len(grafo[i])==1:
						ListaTemEspaco.append(i)
				if len(ListaTemEspaco) < 1 and len(ListaDeFora) > 0:
					sucesso = False

			if sucesso:
				print("Y")
			else:
				print("N")

		k, w = map(int, input().split())

main()
