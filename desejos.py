def tryAppend(a, b, grafo):
    if b not in grafo[a]:
        if len(grafo[a]) == 2:
            return False
        else:
            grafo[a].append(b)
            grafo[b].append(a)
    return True

def RIPdream():
    k, w = map(int, input().split())
    while k >=3 and k <= 10**9 and w>=0 and w<=10**5:
        if w<=2:
            print("Y")
        else:
            grafo = {x:[] for x in range(1,k+1)}
            for i in range(w):
                a, b = map(int, input().split())
                sucesso = tryAppend(a,b,grafo)
                if not sucesso:
                    break
            #print(grafo)
            osDeFora = []
            temEspaco = []
            if sucesso:
                for i in range(1,len(grafo)+1):
                    if len(grafo[i])==0:
                        osDeFora.append(i)
                    if len(grafo[i])==1:
                        temEspaco.append(i)
                if len(temEspaco) < 1 and len(osDeFora) > 0:
                    sucesso = False
            
            if sucesso:
                print("Y")
            else:
                print("N")
                
                

        k, w = map(int, input().split())

RIPdream()
