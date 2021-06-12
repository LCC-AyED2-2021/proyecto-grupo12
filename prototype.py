from algo1 import *

OFFSETa = ord("a")
OFFSETA = ord("A")
OFFSETSPACE = ord(" ")

class HashNode:
  word = None 
  documents = None
  nextNode = None

class DocumentNode:
  identity = None 
  relevance = 0 
  nextNode = None

class LinkedList():
    head=None

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

    if i > -1 and i < 26 and j > -1 and j < 26:
        return i*26 + j
    else:
        return 25 * 26 + 25 + 1


#Array of Hashes size 676x128
arrayOfHashes = Array(676,Array(128,LinkedList()))


#Funcion Hash para cada hash del Array de hashes
#Utiliza el método de multiplicación con A de Knut
SIZE_OF_HASH =  128
A = ((5**(1/2))-1)/2

def HashFunction(String):
  length = len(String)
  if length<2:
      return -1
  result = 0

  for i in range(length):
    result = result * 94
    result += String[i] - OFFSETSPACE

    result = result * A
    floorS = result % 1
    return int(SIZE_OF_HASH * floorS)
  return result

#Inserta el String en el indice correspondiente del Array de Hash
def insertArray(arrayOfHashes,word,document):
    index = StringToIndex(word)
    insertHash(arrayOfHashes[index], word,document)

#Inserta el String en el Hash
#Resuelve colisiones por encadenamiento
def insertHash(HashWord,word,document):
    hashNode = HashWord[HashFunction(String)] #Existencia en slot
    if hashNode == None:

        #Crea un nuevo contenido
        hashNode = LinkedList()         
        node = HashNode()
        node.word = word

        #Añade a la lista de documentos de la palabra el documento
        node.documents = LinkedList()
        nodeD = DocumentNode()
        nodeD.identity = document
        nodeD.relevance = 1
        node.documents.head = nodeD

        hashNode.head = node
    else:
        
        currentNode = hashNode.head   #Caso que exista algo en el slot
                                        #Recorre las palabras en un mismo slot del hash
        while currentNode!=None:      
            if currentNode.word == word:   #Caso de que exista la palabra

                documentNode = currentNode.document.head

                while documentNode!=None:
                    if documentNode.identity == document:
                        documentNode.relevance += 1
                        break
                    documentNode = documentNode.nextNode
                if documentNode == None:
                    nodeD = DocumentNode()
                    nodeD.identity = document
                    nodeD.relevance = 1
                    nodeD.nextNode = currentNode.document.head
                    currentNode.document.head = nodeD
                break
            currentNode == currentNode.nextNode
        if currentNode == None:                     #Caso de que no exista la palabra en el hasNode
            node = HashNode()
            node.word = word
            node.documents = LinkedList()

            nodeD = DocumentNode()
            nodeD.identity = document
            nodeD.relevance = 1
            
            node.documents.head = nodeD
            hashNode.head = node

#TODO
def levantarDedisco(nomArchivo,estruc_path):
    #Levanta desde disco la estructura
    return True

"""
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
