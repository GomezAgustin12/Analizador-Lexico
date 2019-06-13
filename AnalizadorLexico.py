import ply.lex as lex
import os

# resultado del analisis
resultado_lexema = []

reservadas = ['MODULO','DIVISIONENTERA','DISYUNCION','CONJUNCION','NEGACION','LEER',
              'ESCRIBIR','SI','ENTONCES','SINO','FINSI','MIENTRAS','HACER','FINMIENTRAS',
              'REPETIR','HASTAQUE','PARA','HASTA','FINPARA','SEGUN','FINSEGUN','ACCION','ES','FINACCION',
              'PROCESO','AMBIENTE']
tokens = reservadas+['ASIGNACION','NUMERO','ID','SUMA','RESTA','PRODUCTO','DIVISIONREAL','POTENCIA',
    'MENOR','MENORIGUAL','MAYOR','MAYORIGUAL','IGUAL','DISTINTO',
    'PARENTESISI','PARENTESISF','EXIT','IDENTIFICADOR','CADENA'
    ]


t_SUMA = r'\+'
t_RESTA = r'\-'
t_PRODUCTO = r'\*'
t_DIVISIONREAL = r'/'
t_POTENCIA = r'(\*{2} | \^)'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYOR = r'>'
t_MAYORIGUAL = r'>=' 
t_IGUAL = r'='
t_DISTINTO = r'<>'
t_PARENTESISI = r'\('
t_PARENTESISF = r'\)'


#El caracter t antes del nombre de la funcion significa que esa funcion va a obtener un token para poder analizarlo(funcion de libreria lex)
t_ignore =' \t' #Ignora espacios en blanco.

def t_ASIGNACION(t):
    r':='
    return(t)

def t_MODULO(t):
    r'_mod'
    return(t)
def t_DIVISIONENTERA(t):
    r'_div'
    return(t)

def t_DISYUNCION(t):
    r'_o'
    return(t)
def t_CONJUNCION(t):
    r'_y'
    return(t)
def t_NEGACION(t):
    r'_no'
    return(t)


def t_LEER(t): #el nombre de "t_Leer" tiene que estar igual a como se declara en las palabras reservadas o tira error
    r'leer'
    return(t)
def t_ESCRIBIR(t):
    r'escribir'
    return(t)

#SI
def t_SI(t):
    r'si'
    return(t)
def t_ENTONCES(t):
    r'entonces'
    return(t)
def t_SINO(t):
    r'sino'
    return(t)
def t_FINSI(t):
    r'fin_si'
    return(t)

#MIENTRAS
def t_MIENTRAS(t):
    r'mientras'
    return(t)
def t_HACER(t):
    r'hacer'
    return(t)
def t_FINMIENTRAS(t):
    r'fin_mientras'
    return(t)

#REPETIR
def t_REPETIR(t):
    r'repetir'
    return(t)
def t_HASTAQUE(t):
    r'hasta_que'
    return(t)

#PARA
def t_PARA(t):
    r'para'
    return(t)
def t_HASTA(t):
    r'hasta'
    return(t)
def t_FINPARA(t):
    r'fin_para'
    return(t)

#SEGUN
def t_SEGUN(t):
    r'segun'
    return(t)
def t_FINSEGUN(t):
    r'fin_segun'
    return(t)

#ACCION
def t_ACCION(t):
    r'accion'
    return(t)
def t_ES(t):
    r'_es'
    return(t)
def t_FINACCION(t):
    r'fin_accion'
    return(t)

#PROCESO
def t_PROCESO(t):
    r'proceso'
    return(t)

#AMBIENTE
def t_AMBIENTE(t):
    r'ambiente'
    return(t)

#OTROS
def t_COMMENTARIO(t):
    r'\#.*'
    pass
def t_NUMERO(t):
    r'\d+'
    return t
def t_error(t):
    print ("caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t
def t_NUEVALINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



    


cont = int(0)
arc = ''
lista = []
print("#############################################")
print("ESTOS ARCHIVOS SE ENCONTRARON EN LA CARPETA")
print("#############################################")
#CAMBIAR LA RUTA A DONDE TENEMOS EL ARCHIVO DE PRUEBA
for r, d, f in os.walk('E:\Desktop\TP-Teoria de la computacion'):
    for files in f:
        lista.append(files)
for elemento in lista:
    print(cont,": ",elemento)
    cont = cont +1
arc = input("Ingresa el numero del archivo que queres analizar >>>>>>>> ")
s = lista[int(arc)]



 # instanciamos el analizador lexico
archivo = open(s,"r")
cadena = archivo.read()
archivo.close()

def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
       
        if not tok:
            break

        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos))

        resultado_lexema.append(estado)
    return resultado_lexema


analizador = lex.lex()
data = cadena
prueba(data)
for elemento in resultado_lexema:
   print(elemento)
