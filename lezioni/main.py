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
        k= ord(c)-ord("a")
        
        c= chr(ord("A")+k)
        
    b += c



print(b)
print(a.lower())
print(a.upper())

# %%
