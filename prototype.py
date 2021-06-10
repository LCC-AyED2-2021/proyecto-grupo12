OFFSETa = ord("a")
OFFSETA = ord("A")
OFFSETSPACE = ord(" ")
NUMBEROFDIGITS = 94

def letterNum(char): "&" "g" "G" "_" 
  i = char - OFFSETA (-) (+) (+) (+)
  j = char - OFFSETa (-) (+) (-) (-)
  if j < 0:
    return i
  else:
    return j

### TODO: hacer un TEST
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
    return j*26 + i
  else:
    return 25 * 26 + 25 + 1

### TODO: hacer un TEST
def HashFunction(String):
  length = len(String)
  result = 0
  for i in range(length):
    result = result * 94
    result += String[i] - OFFSETSPACE
    ### TODO: hacer una función de hash propiamente dicha
  return result

###############################################
### Vamos a implementar un array de hashes
### El array de hashes debería tener tamaño 677 26 * 26 + 1
###############################################
class HashNode:
  word = None ### string
  documents = None ### insersion online para asegurar orden

### documents es una lista con nodos "DocumentNode"
class DocumentNode:
  identity = None ### el indice en el que guardamos el nombre del archivo
  relevance = 0 ### cantidad de veces que aparece una palabra

### El nombre del documento se guarda en un array
### los indices de este array son la variable identity en "DocumentNode"

### Necesitamos un for que:
### for document in path
### index = insert(Array,document)
###   for word in document
###     insert(arrayOfHashes,word,index)
###
### def insertArray(arrayOfHashes,word,document):
###     index = StringToIndex(word):
###     insertHash(arrayOfHashes[index], word,document)
###
### def insertHash(arrayOfHashes,word,document):
###     hashNode = search(hash,word)
###     if hashNode == None:
###       node = HashNode()
###       node.word = word
###       node.documents = LinkedList()
###       insert(node.documents,document) ### insertar indice y la relavance o actualiza la relevancia
