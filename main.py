def printHelp():
  print(f"""USAGE:
  {argv[0]} --create <path_name>: creates library structure using directory <path_name>.
  Files must be *.txt
  {argv[0]} --search <word>: searches <word> in library
  {argv[0]} --help: shows this message""")

def cleansubstr(text,start,end,max):
  if start >= max:
    return String("")
  unproperEnd = String(")]}>\"!?.,:;")
  unproperStart = String("([{<\"")
  for i in range(len(unproperEnd)):
    if strcmp(text[end-1],unproperEnd[i]):
      end -= 1
      return cleansubstr(text,start,end,max)
  for i in range(len(unproperStart)):
    if strcmp(text[start],unproperStart[i]):
      start += 1
      return cleansubstr(text,start,end,max)
  return substr(text,start,end)

def panic():
  exit(1)

from sys import argv
from os import listdir, chdir
from os.path import isfile, isdir
from algo1 import String, strcmp, substr, Array
from linkedlist import LinkedList
from myqueue import enqueue,dequeue

if len(argv) != 3:
  printHelp()
elif argv[1] == "--create":
  path = argv[2]
  words = LinkedList() ### esta es la estructura
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
      if isfile(documentPath):
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
            ##### ACA HAY QUE INSERTAR EN LA ESTRUCTURA
            ### ACA HAY QUE PASAR CORRECTAMENTE
            ### LOS NODOS QUE USAMOS
            enqueue(words, word)
            enqueue(words, j)
      word = cleansubstr(text,prev,i + 1,MAX_LEN)
      if len(word) > 0:
        ##### ACA HAY QUE INSERTAR EN LA ESTRUCTURA
        ### ACA HAY QUE PASAR CORRECTAMENTE
        ### LOS NODOS QUE USAMOS
        enqueue(words, word)
        enqueue(words, j)
      if not document.closed:
        document.close()
    #### ACA TERMINA LO QUE SE PUEDE ABSTRAER
    ####################
    s = dequeue(words)
    t = dequeue(words)
    #### Esto es código para verficar la inserción
    ### Se puede eleminar
    while s != None:
      print(f"{len(s):3d}",s,ArrayDocNames[t]) ##DEBUG
      s = dequeue(words)
      t = dequeue(words)
    for i in range(len(ArrayDocNames)):
      print(ArrayDocNames[i])
    ### ACA HAY QUE GUARDAR A DISCO
    print("library created successfully")
  else:
    print("Not a valid directory!")
elif  argv[1] == "--search":
  print("Captured word: " + argv[2])
  ### ACA HAY QUE LEVANTAR EL ARCHIVO
  ### ACA HAY QUE BUSCAR
  ### ACA HAY QUE ORDERNAR LA LISTA
  ### OBSERVACIÓN HABRÍA QUE USAR BUCKET SORT
  ### ACA HAY QUE DEVOLVER LA LISTA
  print("SEARCH OK")
else:
  printHelp()
