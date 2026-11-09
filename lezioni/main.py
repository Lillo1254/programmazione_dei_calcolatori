a= 10
print(a)

print(a >> 1)

n= 15
print(n >> 1)
print(n & 1)
print(72 & 1)
print(f"{a:b}")
a = a>>1
print(a)

n = 10

while n > 0:
    print( n&1 )
    n = n>>1

n = 10

n_w = n
n_bin=""
while n_w > 0:
    b = str(n_w&1)
    n_bin = b+n_bin
    n_w = n_w>>1

print(n_bin)

def int_to_bin(n):
    n_bin = ""
    while n > 0:
        b=str(n&1)
        n_bin=b+n_bin
        n=n>>1
    return n_bin

N = 12
print(int_to_bin(N))

def binary(v):
    binary_str = f"{v:b}"
    print(binary_str)

    return binary_str


h=3000
stringa_binary=binary(h)

def reverseBinary(v):
    v_reverse = int(f"{v}",2)
    print(v_reverse)

reverseBinary(stringa_binary)

#%%
x = 0
print(type(x))
print("oggetto x 1",id(x))
x = x/2
print(type(x))
print("oggetto x 2",id(x))
# %%
a,b,pi=10,5,3.14
c= a+b
d= c+pi
print(c)
print(type(c))
print(d)
print(type(d))

#%%
a,b = 9, 2
df= a/b # divisione restituisce sempre un float
d= a//b # divisione intera restituisce un int escludendo la parte decimale 4,8=4
print(type(df))
print(type(d))
print(a%b) # modulo restituisce il resto della divisione 9/2=4 resto 1


# %%
a = "programmazione"
b= "python"
print(a+" "+b) # concatenazione di stringhe possibile solo tra stringhe
print((a+" ")*3) # ripetizione di stringhe
print(len(a)) # lunghezza di una stringa
print(a[0]) # accesso agli elementi di una stringa
# %% Operatori relazionali
a, b, c = 10, 5.5, "stringa"
print(a==b) # uguaglianza
print(a!=b) # disuguaglianza
print(a>b) # maggiore
print(a<b) # minore
print(a>=b) # maggiore o uguale
print(a<=b) # minore o uguale
print(a==c) # confronto tra tipi diversi restituisce False
print(a!=c) # confronto tra tipi diversi restituisce True
#  confronto lessicografico alfabetico esteso tiene conto della codfiica ASCII dei caratteri
print(c == "stringa") # confronto tra stringhe restituisce True
print(c == "Stringa") # confronto tra stringhe restituisce False
print(c != "Stringa") # confronto tra stringhe restituisce True
print(c > "Stringa") # confronto tra stringhe restituisce True
print(c < "Stringa") # confronto tra stringhe restituisce False
print(ord('p')) # restituisce il codice ASCII del carattere
print(112 == ord('p')) # confronto tra intero e codice ASCII del carattere restituisce True
# restituiscono un valore booleano True o False
# %% Operatori booleani
b0 = a>2*a # senza dichiarazione della variabile a il confronto restituisce il valore dell'operazione logica matematica
print(b0)
print(b0 and True)
print(b0 or True)
print(not b0)
print(b0 or 7>21/2)
# una stringa vuota restituisce False, una stringa non vuota restituisce True, un intero 0 restituisce False, un intero non 0 restituisce True, un float 0.0 restituisce False, un float non 0.0 restituisce True, un booleano False restituisce False, un booleano True restituisce True, un oggetto None restituisce False, un oggetto non None restituisce True, una lista vuota restituisce False, una lista non vuota restituisce True, un dizionario vuoto restituisce False, un dizionario non vuoto restituisce True, una tupla vuota restituisce False, una tupla non vuota restituisce True

# %% Operatori bit-a-bit
n = 5 # binario 101 = 1*2^2 + 0*2^1 + 1*2^0 = 4+0+1=5
m = 3 # binario 011 = 0*2^2 + 1*2^1 + 1*2^0 = 0+2+1=3
print(n&m) # operatore AND bit a bit confronta i bit di due numeri e restituisce 1 se entrambi i bit sono 1, altrimenti restituisce 0
print(n|m) # operatore OR bit a bit confronta i bit di due numeri e restituisce 1 se almeno uno dei due bit è 1, altrimenti restituisce 0
print(n^m) # operatore XOR bit a bit confronta i bit di due numeri e restituisce 1 se i due bit sono diversi, altrimenti restituisce 0
print(~n) # operatore NOT bit a bit inverte i bit di un numero e restituisce 1 se il bit e' 0, altrimenti restituisce 0
print(n>>1) # operatore di shift a destra bit a bit sposta i bit di un numero di posizioni a destra e restituisce il numero risultante
print(n<<2) # operatore di shift a sinistra bit a bit sposta i bit di un numero di posizioni a sinistra e restituisce il numero risultante


# %% esercizio
# dato un intero n creare una stringa che contiene la rappresentazione binaria di n con spiegazioen dei passaggi passo per passo

n=25

n_w = n # variabile temporanea per la rappresentazione binaria
n_bin="" # stringa vuota 
while n_w > 0: # fin quando n_w non e' 0 (effettua il blocco fino a che la condizione è vera)
    b = str(n_w&1) # operatore AND bit a bit confronta i bit di due numeri e restituisce 1 se entrambi i bit sono 1, altrimenti restituisce 0
    n_bin = b+n_bin # aggiunge il bit ottenuto alla stringa binaria
    n_w = n_w>>1 # operatore di shift a destra bit a bit sposta i bit di un numero di posizioni a destra e restituisce il numero risultante
print(n_bin)
print(type(n_bin)) # stampa il tipo della variabile n_bin
binary = bin(n) # funzione built-in che restituisce la rappresentazione binaria di un numero intero
print(binary[2:]) # stampa la rappresentazione binaria senza il prefisso '0b'
print(type(binary[2:])) # stampa il tipo della variabile binary
# %% Funzioni

N_int=33
def int_to_bin(a): # i parametri sono dei segnaposto per i dati/variabile che vengono inseriti al momento dell'invocazione
    n_bin = "" # stringa vuota
    while a > 0: # fin quando a non e' 0 (effettua il blocco fino a che la condizione è vera)
        b = str(a&1) # operatore AND bit a bit confronta i bit di due numeri e restituisce 1 se entrambi i bit sono 1, altrimenti restituisce 0
        n_bin = b+n_bin # aggiunge il bit ottenuto alla stringa binaria
        a = a>>1 # operatore di shift a destra bit a bit sposta i bit di un numero di posizioni a destra e restituisce il numero risultante
    return n_bin # stabilisce qual'è il valore della funzione e restituisce il valore calcolato sul parametro " (a) "

a_binary = int_to_bin(N_int) # invocazione della funzione con il parametro N_int 

print(a_binary)

# %% Condizione IF

Number = 21
def int_to_bin(n, stampa=False): #parametri di default indicando un valore iniziale del parametro
    n_bin = ""

    while n> 0:
        b= str(n&1)
        n_bin = b+n_bin
        n = n>>1
    if stampa:
        print(n_bin)

    return n_bin
# int_to_bin(Number) genera errore perché la funzione richiede due parametri, quindi bisogna passare anche il secondo parametro. 
int_to_bin(Number, True)
int_to_bin(n=Number+5, stampa=1) # invocazione della funzione con i parametri passati per nome, quindi non è necessario rispettare l'ordine dei parametri
int_to_bin(Number, "") # ogni valore false o vuoto viene interpretato come False, quindi la funzione non stampa nulla
int_to_bin(Number, "a") #ogni valore true o non vuoto viene interpretato come True, quindi la funzione stampa la rappresentazione binaria di Number
#%% Condizione IF Else

def int_to_bin(n, stampa=False):
    """
    
    Funzione che restituisce la rappresentazione binaria di un intero
    :param n: intero da convertire in binario
    :param stampa: booleano che indica se stampare o meno la rappresentazione binaria
    
    """
    
    n_bin = ""

    while n> 0:
        b= str(n&1)
        n_bin = b+n_bin
        n = n>>1

    if stampa:
        print(n_bin)
        return None
    else:
        print("La funzione non stampa nulla perché il parametro 'stampa' è impostato su False o vuoto.")
        return n_bin


N = 42

int_to_bin(N)
int_to_bin(N, True)

# %% if-elif-else

def int_to_bin(n, stampa=False):
    """
    
    Funzione che restituisce la rappresentazione binaria di un intero
    :param n: intero da convertire in binario
    :param stampa: booleano che indica se stampare o meno la rappresentazione binaria
    
    """
    n_bin = ""

    while n> 0:
        b= str(n&1)
        n_bin = b+n_bin
        n = n>>1

    if stampa:
        print(n_bin)
        return None
    elif stampa == "" or stampa == 0:
        print("La funzione non stampa nulla perché il parametro 'stampa' é impostato su un valore false.")
        
    else:
        print("Il parametro 'stampa' non è un booleano, quindi la funzione non stampa nulla.")
        


N = 33

int_to_bin(N)
int_to_bin(N, True)
int_to_bin(N, "")

# %%

def int_to_bin(n, stampa=False):

    n_bin = ""
# sia t la lunghezza della rappresentazione binaria di n
    t = 0    
    while n> 0:
        b= str(n&1)
        n_bin = b+n_bin
        t += 1
        n = n>>1
    print(f"La lunghezza/costo è {t} cicli.")
    if stampa:
        print(n_bin)
        return None
    elif stampa == "" or stampa == 0:
        print("La funzione non stampa nulla perché il parametro 'stampa' é impostato su un valore false.")
        
    else:
        print("Il parametro 'stampa' non è un booleano, quindi la funzione non stampa nulla.")
        


N = 31111

int_to_bin(N)
int_to_bin(N, True)

# %%
N = 42

print(bin(N)[2:])
# %%

def int_to_bin(n, stampa=False):

    t = 0
    n_bin=""
    while n> 0:
        b=str(n&1)
        n_bin = b+n_bin
        t +=1
        n = n>>1

    if stampa:
        print(n_bin)
    else:
        return n_bin, t

N = 42

int_to_bin(N, True)
int_to_bin(N)

# %% esercizio scacchiera

n, m = 10, 7
riga_pari = "#_"*(m//2)
riga_dispari = "_#"*(m//2)

for i in range(n):
    if i%2 == 0:
        print(riga_pari)
    else:
        print(riga_dispari)
# %%
n, m = 10, 7
riga_pari= "#_"*(m//2)

riga_dispari= riga_pari+"#" if m%2 == 0 else "_#"

print(riga_pari)


# %%
n, m = 8,8

riga_pari = "#_"*(m//2)

riga_dispari = riga_pari+"o" if m%2 == 0 else "_#"

while n > 0:
    if n%2 == 0:
        print(riga_pari)
    else:
        print(riga_dispari)
    n = n-1



# %%
n, m = 8, 8

control_cicle = 0
while control_cicle < n:
    control_cicle_2 = 0
    riga = ""
    
    while control_cicle_2 < m:

        if (control_cicle + control_cicle_2) % 2 == 0:
            riga += "#"
        else:
            riga += "_"
        control_cicle_2 += 1
        
    print(riga)
    control_cicle += 1
# %%
n = 8
m = 8

control_var = 0

while control_var < n:
    control_var_2 = 0
    riga = ""

    while control_var_2 < m:
        if (control_var + control_var_2) % 2 == 0:
            riga += "#"
        else:
            riga += "_"
        control_var_2 += 1 
        
    print(riga)
    control_var += 1 
# %%
altezza= 13
larghezza= 15

riga_pari = "# _ "*(larghezza//2)
riga_dispari="_ # "*(larghezza//2)

control_var = 0

while control_var < altezza:
    if control_var%2 == 0:
        print(riga_pari)
    else:
        print(riga_dispari)
    control_var += 1
# %%

def griglia(n,m):
    control_var = 0
    while control_var < n:
        control_var_2 = 0
        riga = ""
        while control_var_2 < m:
            if (control_var + control_var_2) % 2 == 0:
                riga += "#"
            else:
                riga += "_"
            control_var_2 += 1
        print(riga)
        control_var += 1

griglia(13, 15)

# %% generare funzione
# il parametro m non deve essere passato obbligatoriamente all'invocazione della funzione ma se manca deve stampare una griglia quadrata
def griglia(n,m=None):
    if m is None:
        m = n
    riga_pari = "# _ "*(m//2)
    riga_dispari="_ # "*(m//2)

    control_var = 0

    while control_var < n:
        if control_var%2 == 0:
            print(riga_pari)
        else:
            print(riga_dispari)
        control_var += 1

griglia(13)
# %%
def griglia(n,m=None):
    if m is None:
        m = n
    riga_pari = "# _ "*(m//2)
    riga_dispari="_ # "*(m//2)
    if m == 1:
        riga_pari = "#"
        riga_dispari = "_"
    control_var = 0

    while control_var < n:
        if control_var%2 == 0:
            print(riga_pari)
        else:
            print(riga_dispari)
        control_var += 1

griglia(2,2)
griglia(2,1)
griglia(10)
griglia(5,7)

# %%
a = input("Premi un tasto") #il programma viene interrotto e attende un input da parte dell'utente si puo inserire un parametro stringa che indica il messaggio da mostrare all'utente

print(a)
# %%
n = input("numero di righe")
m = input("numero di colonne")

griglia(int(n),int(m))
# %%
n = int(input("numero di righe"))
m = int(input("numero di colonne"))

griglia(n,m)
# %%
f = float("3.14")
print(f, type(f))
# %%
a = "0123456789"

# calcolo lunghezza della stringa
print(len(a))
print("====================")
# stampa a seconda dell'indice
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print("====================")
# slice
print(a[0:5])
print(a[5:10])
print("====================")
# %%
# indicizzazione con stampa in diagonale
print(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9])
print(a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9])
print(a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9])
print(a[3],a[4],a[5],a[6],a[7],a[8],a[9])
print(a[4],a[5],a[6],a[7],a[8],a[9])
print(a[5],a[6],a[7],a[8],a[9])
print(a[6],a[7],a[8],a[9])
print(a[7],a[8],a[9])
print(a[8],a[9])
print(a[9])
# %% stampa in diagonale
a = "0123456789"

n = len(a)

i = 0
while i < n:
    print(" "*i+a[i])
    i += 1
    
# %% stampa in diagonale con ciclo for
a = "0123456789"

n = len(a)
print(type(n))

for i in range(n):
    print(" "*i+a[i])

# %% stampa in diagonale con ciclo for senza len()
a = "0123456789"

i=0
for c in a:
    print(" "*i+c)
    i += 1

# %% stampa in diagonale con ciclo for con enumerate()
a = "0123456789"

# enumerate() restituisce un oggetto di tipo enumerate che contiene la coppia (indice, valore)
print(type(enumerate(a)))
for i,c in enumerate(a):
    print(" "*i+c)

# %% stmapare l'ultimo carattere
a = "0123456789"
# l'utilizzo di indici negativi si utilizza per accedere agli indici partendo dalla fine in python l'ultimo indice letto da destra verso sinistra è -1 poiche -0 matematicamente è uguale a 0
print(a[-1])

# %%
#funzione se stringa palindroma restituisce true altrimenti false
def stringa(a):
    if a == a[::-1]: #[::-1] restituisce la stringa invertita
        return True
    else:
        return False

print(stringa("yamamay"))
print(stringa("yamamay1"))
# %%
#funzione se stringa palindroma restituisce true altrimenti false con ciclo

def stringa(a):
    for i in range(len(a)):
        if a[i] != a[-(i+1)]:
            return False
            
        else:
            print(f"carettere {a[i]} uguale a {a[-(i+1)]}", True)
            

print(stringa("yamamay"))
print(stringa("yamamay1"))

# %%
# funzione se stringa palindroma restituisce true altrimenti false con ciclo ed enumerate()

def stringa(a):
    for i,c in enumerate(a):
        if a[i] != a[-(i+1)]:
            return False
    return True

print(stringa("yamamay"))
print(stringa("yamamay1"))
# %%
def palindromo(a):
    if a == a[::-1]:
        return True
    else:
        return False

def palindromo_2(a):
    stringa_1 =""
    stringa_2 =""
    for i in range(len(a)):
        stringa_1 += a[i]
        stringa_2 += a[-(i+1)]
    if stringa_1 == stringa_2:
        return True
    else:
        return False

print(palindromo("yamamay"))
print(palindromo("yamamay1"))

print(palindromo_2("yamamay"))
print(palindromo_2("yamamay1"))
# %%

a = "kayak"

n =len(a)
i , j = 0, n-1

while i  < j and a[i] == a[j]:
    i += 1
    j -= 1

if a[i] == a[j]:
    print("palindromo")
else:
    print("non palindormo")

# %%
def palindormo (a):
    i, j = 0,-1
    while i< len(a)//2 and a[i] == a[j]:
        i += 1
        j -= 1

    if a[i] == a[j]:
        return True
    else:
        return False

print(palindormo("yamamay"))
# %%

a = "0123456789"

b = a[2:8] #da l'indice 2 fino all'indice 7
print(b)

b = a[2:] #da l'indice 2 fino alla fine
print(b)

b = a[:8] #da l'inizio fino all'indice 7
print(b)

b = a[:] #da l'inizio fino alla fine
print(b)

b= a[2:8:2] #da l'indice 2 fino all'indice 7 con passo 2
print(b)

b= a[8:2:-2] #dall'indice 8 fino all'indice 2 con passo -2
print(b)

b= a[::2] #da l'inizio fino alla fine con passo 2
print(b)

b= a[::-1] #inverte la stringa dalla fine all'inizio
print(b)


# %%
a ="kayak7"
a[::-1] == a

def palindromo2(a):
    return a == a[::-1]

print(palindromo2("kayak"))
print(palindromo2("kayak7"))
# algoritmo non efficenze poiche crea una copia della stringa allocando memoria tanto quanto la lunghezza della stringa stessa ed effettuando un confronto diretto pertanto viene utilizzata memoria e tempo


# %%
# le stringhe in python sono immutabili pertanto non possiamo modificarle direttamente

a = "Programmazione dei calcolatori"
# a[1] = "R" # TypeError: 'str' object does not support item assignment 

b =""
for c in a:
    if c >= "a" and c <= "z": # caratteri minuscoli
        k= ord(c)-ord("a") # converte il carattere in numero
        
        c= chr(ord("A")+k) # la funzione chr() converte un numero in carattere
        
    b += c
# quindi questa funzione converte le lettere in numeri ascii poi fa il confronto tra i numeri ascii e i corrispettivi numeri ascii delle lettere maiuscole


print(b)
print(a.lower())
print(a.upper())

# %%
def pal(a):

    n = len(a)
    for i in range(n//2):
        if a[i] != a[-1-i]:
            return False
    return True

a = input("inserisci una stringa: ")

p= pal(a)
if p:
    print("la stringa è palindroma")
else:
    print(f"la stringa non é palindroma - {a}- ")
# %%
def pal(a):

    n = len(a)
    for i in range(n//2):
        if a[i] != a[-1-i]:
            return 1
    return -1

a = input("inserisci una stringa: ")

p= pal(a)
if p<0:
    print("la stringa è palindroma")
else:
    print(a)
    n = len(a)
    q= n-1-p
    b= " "*p+"^"+" "*(q-p-1)+"^"
    print(b)
# %%

# %%
permessi = "warr"
bm = 0
bitarray = 0

if "r" in permessi:
    print("SI")
else:
    print("NO")

if "r" in permessi:
    bitarray = bitarray|1

if "w" in permessi:
    bitarray = bitarray|0b10

print(bitarray)
print(f"{bitarray: b}") #formattazione della stringa con f-string e specifica il formato binario - float, int, str, bool, list, dict, tuple, set, complex, bytes, bytearray, memoryview, range, frozenset
print(f"{bitarray: 10.2f}")
print(f"{bitarray:08b}") #

if "x" in permessi:
    bitarray = bitarray|0b100

if "a" in permessi:
    bitarray = bitarray|0b1000

print(f"La sequenza è: {bitarray: 04b}")

# %%
def pal(a):
    """
    input: a una stringa
    Output: -1 se la stringa è palindroma oppure (i,j) se il carattere in posizione i differisce dal suo simmetrico in posizione  j
    """
    i,j = 0,len(a)-1

    while i < len(a)//2 and a[i] == a[j]:
        i += 1
        j -= 1

    if a[i] == a[j]:
        return -1
    else:
        return (i,j)


print(pal("kayak"))
print(pal("kayAk"))

t = pal("kayAk")
print(type(t)) # t è una tupla cioe un insieme di elementi separati da virgola e racchiusi tra parentesi tonde, le tuple sono immutabili e possono contenere elementi di tipo diverso accedendo alla tupla con l'indice
print(t[:])
print(int(t[0]), int(t[1])) # conversione dei valori della tupla in interi




# %%
t = (0,3.14,"stringa",True, (7,9,"stringa2"))
for x in t:
    print(x, type(x))
# %%
def pal(a):
    """
    input: a una stringa
    Output: -1 se la stringa è palindroma oppure (i,j) se il carattere in posizione i differisce dal suo simmetrico in posizione  j
    """
    i,j = 0,len(a)-1

    while i < len(a)//2 and a[i] == a[j]:
        i += 1
        j -= 1

    if a[i] == a[j]:
        return -1
    else:
        return (i,j)

t = pal("kayAk")
p, q = pal("kayAk") # spacchettamento della tupla in due variabili p e q, se la funzione restituisce una tupla di due elementi, p e q conterranno i valori della tupla restituita dalla funzione
print(p,q)

# %%
#      J
# |10,11,12,13|
# |20,21,22,23| I
# |30,31,32,33|

i,j = 1,2
n_cols = 4

M = (10,11,12,13,20,21,22,23,30,31,32,33,34)

# elemento i, j in M si trova in posizione j+posizione del primo elemento della riga i
# j+posizione del primo elemento della iga i = j+i*n_cols

# %%
#funzioni

Tupla_di_elementi = (1,2,3,4,5,6,7,8,9,10,11,12)
n_cols = 4
def estrai_riga(M, n_cols, r):
    """
    parametri: M una tabella memorizzata per righe;
    n_cols numero colonne tabella
    r numero intero
    output: ritorna una tupla che contine la riga r di M
    """
    # M viene calcolato con lo slicing tramite gli indici della riga*l colonne
    return M[r*n_cols:(r+1)*n_cols]
# in questo caso specifico M sara sottoposto a uno slicing dall'indice M[2*4] fino all'indice M[3*4] escluso, quindi M[8:12] che corrisponde alla terza riga della tabella memorizzata per righe pertanto sarà M[8:12] dall'indice 8 all'indice 12 della tupla di entrata
print(estrai_riga(Tupla_di_elementi, n_cols, 2))

def estrai_colonna(M, n_cols, r):
    """
    parametri: M una tabella memorizzata per righe;
    n_cols numero colonne tabella
    r numero intero
    output: ritorna una tupla che contine la colonna r di M
    """
    # per estrarre una colonna si procede sempre con uno slicing ma con passo uguale al numero di colonne della tabella in modo da mantenere gli stessi spazi tra gli elementi della colonna 
    # M[c], ;[c+n_cols],M[c+2*n_cols]...
    return M[r::n_cols]

# qui utilizziamo la
print(estrai_colonna(Tupla_di_elementi, n_cols, 3))
# %%
t = (10,20,30,0)
t2 = ( "casa", "barca", "aba")
print(sum(t)) # somma gli elementi della tupla
print(max(t)) # restituisce il valore massimo tra elementi della tupla
print(min(t)) # restituisce il valore minimo tra elementi della tupla
print(len(t)) # lunghezza della tupla
print(t+t2) # concatenazione di tuple
print(max(t2)) # restituisce il massimo elemento della tupla secondo l'ordinamento lessicografico
print(min(t2)) # restituisce il minimo elemento della tupla secondo l'ordinamento lessicografico
# print(sum(t2)) TypeError: unsupported operand type(s) for +: 'int' and 'str' - non è possibile sommare stringhe e numeri
# %%
print(max((10,8), (11,0))) # restituisce il massimo tra due tuple confrontando prima il primo elemento e poi il secondo elemento se i primi elementi sono uguali
print(max((10,9,8), (10,8,0)))
print(max((10,8,"tra"), (10,8,"casa")))
#gli elementi della tupla devono essere confrontabili tra loro altrimenti si ottiene un errore TypeError: '>' not supported between instances of 'str' and 'int'
print(max((10,8,"casa"), (10,8,"d")))
# %%
help(max) # restituisce la documentazione della funzione max
t = ("zero","uno","due","tre","quattro","ottanta")
print(min(t))
print(max(t,key=len)) # restituisce l'elemento della tupla con la lunghezza massima
print(min(t,key=len)) # restituisce l'elemento della tupla con la lunghezza minima
# %%
t = ("zero","uno","due","tre","quattro","ottanta")

def F(e):
    return (len(e),(e))

print(F("casa"))
print(min(t,key=F))
# %%
#funzione lambda utilizzata per creare funzioni anonime, cioè funzioni senza nome, che possono essere utilizzate come argomenti di altre funzioni o come valori di ritorno di altre funzioni. Le funzioni lambda sono utili quando si vuole creare una funzione semplice e veloce senza dover definire una funzione completa con def. o inserire una funzione in una variabile. La sintassi di una funzione lambda è la seguente: lambda arg1, arg2, ... : expression. dove arg1, arg2, ... sono gli argomenti della funzione e expression è l'espressione che viene valutata e restituita come valore della funzione. Le funzioni lambda possono essere utilizzate in combinazione con altre funzioni come map(), filter() e reduce() per creare operazioni complesse su liste e altri oggetti iterabili
t = ("zero","uno","due","tre","quattro","ottanta")
print((lambda x: x+1)(7))
# %% Lista
# struttura dati lineare come le tuple di elementi ordinati accesso tramite indicie e possibilità di essere disomogenea a differenza delle tuple le liste sono mutabili quindi possiamo modificare cancellare o aggiungere elementi all'interno della lista

a =[] # lista vuota
a = [2,3,"python",(1,"9"),["y",9]]

print(a)

a[1]=3.14 # sostituito elemento indice 1

print(a)

a = [0,1,2,3,4,5,6,7,8,9]


print(a[1:3])

a[1:3] = ["uno","due"]# slicing per modificare elementi tanti quanti sono quelli selezionati
print(a)
a[1:3] = ["add-1","add-2","add-3"] # slicing per aggiungere elemente oltre quelli presenti selezionanto l'indice e aggiungere piu elementi del dovuto
print(a)

n = len(a)
a[n-1:] = a[n-1],10 # inserimento di un elemento alla fine della lista
print(a)

a.append(11) # il metodo append inserisce in una lista un elemento alla fine "appende" l'elemento alla fine Per metodo si definisce una speciale funzine derivata dal tipo di dato stesso ogni tipologia di dato ha metodi unici o uguali agli altri
print(a)

# scrivere una funzione che prende in input una tabella con righe e colonne e poi prende in input l'indice di una colonna. La funzione deve modificare tutti gli elementi della colonna selezionata cambiando il valore in 0

M=[1,2,3,4,5,6,7,8,9,10,11,12]
#   1,2,3
#   4,5,6
#   7,8,9
#   10,11,12

n = len(M)
n_cols= 3
print(n)

T = list(range(0,5)) + list(range(10,15))
print(T)





def set_col_zero(M, n_cols, indice):

    for i in range(len(M)//n_cols):
        print(f"i={i}, indice={indice}, n_cols={n_cols}, i*n_cols+indice={i*n_cols+indice}")
        M[i*n_cols+indice] = 0

set_col_zero(M, n_cols, 1)
print(M)

j = 2
n_rows = len(M)//n_cols
M[j::n_cols] = [0]*n_rows
print(M)
# %%
# def calcola_massimi(T,n_n_cols):
    #
    # input: 
    # T tabella numerica memorizzata in una lista con gli elementi disposti per righe;
    # n_cols: numero di colonne di T
    # ritorna:
    # una lista contenente i massimi di ciascuna colonna
    # una lista contenente i massimi di ciascuna riga
    # """
    # sia n = len(T), n_rows = numero di righe, 
    

n_cols= 4
T = [ 4,2,9,1,5,3,8,0,2,1,3,6]

max_colonne, max_righe = [], []
for j in range(n_cols):
    print(T[j::n_cols]) # slicing per estrarre la colonna j
    
    max_colonne.append( max(T[j::n_cols])) # calcola il massimo della colonna j e lo aggiunge alla lista max_colonne

        # Theta(n_rows) per slicing
        # Teheta(n_rows) per max
        # Theta(1) per append
        # il tutto per n_cols => Theta(n)

print("")

print(max_colonne)

for i in range (len(T)//n_cols):
    print(T[i*n_cols:(i+1)*n_cols]) # slicing per estrarre la riga i
    max_righe.append(max(T[i*n_cols:(i+1)*n_cols])) # calcola il massimo della riga i e lo aggiunge alla lista max_righe

    # Theta(n)
    
print("")
print(max_righe)

def calcolo_massimi(T, n_cols):
    max_colonne, max_righe = [], []
    for j in range(n_cols):
        max_colonne.append(max(T[j::n_cols]))
    for i in range(len(T)//n_cols):
        max_righe.append(max(T[i*n_cols:(i+1)*n_cols]))
    return max_colonne, max_righe

print(calcolo_massimi(T, n_cols))

# %%
a = [4,2,9,1,5,3,8,0,2,1,3,6]
k = 2
# cercare k in a
print(k in a)

for i, x in enumerate(a):
    if x == k:
        print(f"trovato in {i}")
        break
# %%
T = [4,2,9,1,5,3,8,0,2,1,3,6]

print( (T[i] for i in range(2,7))) #generatore di sequenza

a = [T[i] for i in range(2,7)] #list comprehension
print(a)
print("ciao")
# %%
