from sys import argv
from os import listdir, chdir
from os.path import isfile, isdir
from algo1 import String, strcmp, substr, Array
from mylinkedlist import LinkedList
from structure import SIZE_OF_ARRAY, SIZE_OF_HASH, insertArray, HashFunction, StringToIndex
from pickle import dump, load
from utility import printHelp, cleansubstr


if len(argv) != 3:
  printHelp(argv[0])
elif argv[1] == "--create":
  path = argv[2]
  library = open("library.sho","wb")
  words = Array(SIZE_OF_ARRAY,Array(SIZE_OF_HASH,LinkedList())) ### esta es la estructura
  ArrayDocNames = None
  ####################
  ### Esta parte se podría abstraer para hacer una función recursiva y ver si hay una serie de carpetas dentro de carpetas
  if isdir(path):
    documents = listdir(path)
    NumberOfDocuments = len(documents)
    ArrayDocNames = Array(NumberOfDocuments,String(""))
    chdir(path)
    for j in range(len(documents)):
      ArrayDocNames[j] = String(documents[j])
      documentPath = documents[j]
      if isfile(documentPath) and strcmp(substr(documentPath,-3,0),String("txt")):
        document = open(documentPath,"r")
        text = String(document.read())
        prev = 0
        MAX_LEN = len(text)
        for i in range(MAX_LEN):
          if strcmp(text[i],String(" ")) or strcmp(text[i],String("\n"))or strcmp(text[i],String("\t")):
            start = prev
            end = i
            prev = i + 1
            word = cleansubstr(text,start,end, MAX_LEN)
            if len(word) > 0:
              insertArray(words, word, j)
        word = cleansubstr(text,prev,i + 1,MAX_LEN)
        if len(word) > 0:
          insertArray(words, word, j)
        if not document.closed:
          document.close()
    #### ACA TERMINA LO QUE SE PUEDE ABSTRAER
    ####################
    if not library.closed:
      dump(words,library)
      dump(ArrayDocNames,library)
      library.close()
    print("library created successfully")
  else:
    print("Not a valid directory!")
elif  argv[1] == "--search":
  print("Captured word: " + argv[2])
  word = String(argv[2])
  ### Podría intentar con primera en mayusculas
  ### y toda la palabra en mayusculas
  index = StringToIndex(word)
  key = HashFunction(word)
  library = open("library.sho","rb")
  if not library.closed:
    words = load(library)
    ArrayDocNames = load(library)
    library.close()
    candidate = words[index][key]
    if candidate != None:
      node = candidate.head
    else:
      node = candidate
    while node != None:
      if strcmp(node.word,word):
      ### ACA HAY QUE ORDERNAR LA LISTA
      ### OBSERVACIÓN HABRÍA QUE USAR BUCKET SORT
        document = node.documents.head
        while document != None:
          print(word, document.relevance, ArrayDocNames[document.identity])
          document = document.nextNode
        break
      node = node.nextNode
    if node == None:
      print("no document found")

  ### ACA HAY QUE LEVANTAR EL ARCHIVO
  ### ACA HAY QUE BUSCAR
  ### ACA HAY QUE DEVOLVER LA LISTA

else:
  printHelp(argv[0])
