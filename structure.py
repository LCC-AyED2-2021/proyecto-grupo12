from algo1 import Array, String, strcmp
from mylinkedlist import LinkedList


LATIN_ALPHABER_SIZE = 26
ALPHABER_SIZE = 94
SIZE_OF_ARRAY = 677
SIZE_OF_HASH =  128
OFFSETa = ord("a")
OFFSETA = ord("A")
OFFSETSPACE = ord(" ")
A = ((5**(1/2))-1)/2

class HashNode:
  word = None 
  documents = None
  nextNode = None

class DocumentNode:
  identity = None 
  relevance = 0 
  nextNode = None


#Diferencia entre caracteres speciales y comunes
def letterNum(char): 
    i = ord(char) - OFFSETA #(-) (+) (+) (+)
    j = ord(char) - OFFSETa #(-) (+) (-) (-)
    if j < 0:
        return i
    else:
        return j

#Otorga un indice para el Array de Hashes
#Considera los dos primeros caracteres del String
def StringToIndex(String):
  
    length = len(String)
    if length == 0:
        return None
      
    i = letterNum(String[0])
    j = 0
    if length == 1:
        j = i
    else:
        j = letterNum(String[1])

    if i > -1 and i < LATIN_ALPHABER_SIZE and j > -1 and j < LATIN_ALPHABER_SIZE:
        return i * LATIN_ALPHABER_SIZE + j
    else:
        return SIZE_OF_ARRAY - 1

#Funcion Hash para cada hash del Array de hashes
#Utiliza el método de multiplicación con A de Knut
def HashFunction(String):
  length = len(String)
  if length < 2:
      return -1
  result = 0

  for i in range(length):
    result = result * ALPHABER_SIZE
    result += ord(String[i]) - OFFSETSPACE

    result = result * A
    result = result % 1
  return int(SIZE_OF_HASH * result)
  
#Array of Hashes size 677x128
arrayOfHashes = Array(SIZE_OF_ARRAY,Array(SIZE_OF_HASH,LinkedList()))
  
#Inserta el String en el indice correspondiente del Array de Hash
def insertArray(arrayOfHashes,word,document):
    index = StringToIndex(word)
    insertHash(arrayOfHashes[index], word,document)
    return

#Inserta el String en el Hash
#Resuelve colisiones por encadenamiento
def insertHash(HashWord,word,document):
    index = HashFunction(word)
    hashNode = HashWord[index] #Existencia en slot
    if hashNode == None:
### Lo que está entre ####### podría abstraerse en una o dos funciones
#############
        #Crea un nuevo contenido
        HashWord[index] = LinkedList()         
        node = HashNode()
        node.word = String(word)

        #Añade a la lista de documentos de la palabra el documento
        node.documents = LinkedList()
        nodeD = DocumentNode()
        nodeD.identity = document
        nodeD.relevance = 1
        node.documents.head = nodeD

        HashWord[index].head = node
#############
    else:
        
        currentNode = hashNode.head   #Caso que exista algo en el slot
                                        #Recorre las palabras en un mismo slot del hash
        while currentNode != None:      
            if strcmp(currentNode.word,word):   #Caso de que exista la palabra

                documentNode = currentNode.documents.head

                while documentNode!=None:
                    if documentNode.identity == document:
                        documentNode.relevance += 1
                        break
                    documentNode = documentNode.nextNode
                if documentNode == None:
            ### Lo que está entre ####### podría abstraerse en una o dos funciones
            #############
                    nodeD = DocumentNode()
                    nodeD.identity = document
                    nodeD.relevance = 1
                    nodeD.nextNode = currentNode.documents.head
                    currentNode.documents.head = nodeD
            #############
                break
            currentNode = currentNode.nextNode
        if currentNode == None:                     #Caso de que no exista la palabra en el hasNode
    ### Lo que está entre ####### podría abstraerse en una o dos funciones
    #############
            node = HashNode()
            node.word = String(word)
            node.documents = LinkedList()

            nodeD = DocumentNode()
            nodeD.identity = document
            nodeD.relevance = 1
            
            node.documents.head = nodeD
            node.nextNode = HashWord[index].head
            HashWord[index].head = node
    #############
    return
#TODO
def levantarDedisco(nomArchivo,estruc_path):
    #Levanta desde disco la estructura
    return True

##### Codigo de prueba!
nombres = ["nombre0", "nombre1", "nombre2"]
test1 = ["aa","una","una","una","palaba","a","ver","si", "entra"]
test2 = [0,1,1,0,1,0,2,1,1]

Structure = Array(SIZE_OF_ARRAY,Array(SIZE_OF_HASH,LinkedList()))

for i in range(len(test1)):
  insertArray(Structure,String(test1[i]),test2[i])

for i in range(SIZE_OF_ARRAY):
  for j in range(SIZE_OF_HASH):
    hash = Structure[i][j]
    if hash != None:
      node = hash.head
      while node != None:
        docnode = node.documents.head
        while docnode != None:
          print(node.word, docnode.identity, docnode.relevance)
          docnode = docnode.nextNode  
        node = node.nextNode

""""
print("Test of letterNum")
#test with [
#test with k
#test with K
#test with |
#test with !
#test with =
print(letterNum("["))
print(letterNum("k"))
print(letterNum("K"))
print(letterNum("|"))
print(letterNum("!")) #return -
print(letterNum("=")) #return -

print("Test of StringToIndex")
print("aa: ",StringToIndex("aa"))
print("ab: ",StringToIndex("ab"))
print("ba: ",StringToIndex("ba"))
print("b: ",StringToIndex("b"))
print("a|: ",StringToIndex("a|"))
print("{: ",StringToIndex("{"))
print("asyw2",StringToIndex("asyw2"))
"""
