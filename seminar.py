def provjeriElementeNiza(n,niz):
    temp = True
    for element in niz:
        if element < 1 or element > n:
            temp = False
            break
    return temp

def pronadiGraf(N,a,b):
    m = len(a)
    prviNiz = []
    drugiNiz = []
    graf = {}
    for i in range(m):
        for j in range(1,N+1):
            if a[i] * j <= N:
                prviNiz.append((i,a[i]*j))
            if b[i] * j <= N:
                drugiNiz.append((i,b[i]*j))
    for i in prviNiz:
        for j in drugiNiz:
            if i[0] == j[0] and i[1] != j[1]:
                if i[1] not in graf.keys():
                    graf[i[1]] = [j[1]]
                else:
                    graf[i[1]].append(j[1])
    return graf

def najkracaRuta(graf, S, T, istrazeneTocke):
    if(len(graf) == 1):
        print(-1)
        return
    red = [[S]]
    while len(red) != 0:
        listaTocki = red[0]
        red = red[1:]
        tocka = listaTocki[-1]
        if tocka not in istrazeneTocke:
            for susjed in graf[tocka]:
                if susjed in graf:
                    temp = list(listaTocki)
                    temp.append(susjed)
                    red.append(temp)
                    if susjed == T:
                        ispis(temp)
                        return
            istrazeneTocke.append(tocka)
    print(-1)
    return

def ispis(lista):
    putanja = ""
    for i in lista:
        if i != lista[-1]:
            putanja += str(i) + " - "
        else:
            putanja += str(i)
    print(putanja)
    print("Duljina putanje: " + str(putanja.count('-')))

    
def provjeriValjanostParametara(N,S,T,a,b):
    if N < 2 or N > 10**9:
        print("Broj gradova nije dobro unesen!")
        return
    elif S < 1 or S > N:
        print("Pocetni grad nije dobro unesen!")
        return
    elif T < 1 or T > N:
        print("Krajni grad nije dobro unesen!")
        return
    elif len(a) != len(b):
        print("Niz a sadrzi razlicit broj elemenata od niza b")
        return
    elif len(a) < 1 or len(a) > 1000:
        print("M nije dobro unesen")
        return
    elif provjeriElementeNiza(N,a) == False:
        print("Niz a sadrzi elemente koji su izvan intervala")
        return
    elif provjeriElementeNiza(N,b) == False:
        print("Niz b sadrzi elemente koji su izvan intervala")
        return
    else:
        graf = pronadiGraf(N,a,b)
        return graf

istrazeneTocke = []
#graf = provjeriValjanostParametara(11,9,6,[3,10],[5,2])
#if graf != None:
#    najkracaRuta(graf,9,6,istrazeneTocke)

#graf = provjeriValjanostParametara(77,10,62,[2,5,7,4,17,26],[25,7,11,13,31,34])
#if graf != None:
#    najkracaRuta(graf,10,62,istrazeneTocke)

graf = provjeriValjanostParametara(60,30,8,[16,15,12],[2,20,5])
if graf != None:
    najkracaRuta(graf,30,8,istrazeneTocke)

#graf = provjeriValjanostParametara(100,90,40,[20,30,100,99,100],[10,30,100,100,99])
#if graf != None:
#    najkracaRuta(graf,90,40,istrazeneTocke)

#graf = provjeriValjanostParametara(2,1,2,[2],[1])
#if graf != None:
#    najkracaRuta(graf,1,2,istrazeneTocke)
