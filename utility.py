from algo1 import substr,strcmp,String

def printHelp(name):
  print(f"""USAGE:
  {name} --create <path_name>: creates library structure using directory <path_name>.
  Files must be *.txt
  {name} --search <word>: searches <word> in library
  {name} --help: shows this message""")

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

#Ordena una lista utilizando el metodo Merge Sort
def MergeSort(L):
    n=length(L)
    if n<=1:
        return L
    else:
        currentNode=L.head
        for i in range(0,n//2-1):
            currentNode=currentNode.nextNode
        StartL2=currentNode.nextNode
        #creo la primer lista que ira hasta la mitad
        StartL1=L.head  
        L1=LinkedList()
        L1.head=StartL1
        currentNode.nextNode=None

        #creo la segunda lista que ira desde la mitad hasta el final
        L2=LinkedList()
        L2.head=StartL2

        #Hago recursion hasta que queden solo nodos de tamaño 1
        L1=MergeSort(L1)
        L2=MergeSort(L2)

        #Rearmo la lista
        L.head=None
        currentNodeL1=L1.head
        currentNodeL2=L2.head

        while currentNodeL1!=None and currentNodeL2!=None:
            if currentNodeL1.relevance<currentNodeL2.relevance:
                if  L.head==None:
                    L.head=currentNodeL1
                    currentNode=L.head
                else:
                    currentNode.nextNode=currentNodeL1
                    currentNode=currentNode.nextNode    
                currentNodeL1=currentNodeL1.nextNode
            else:
                if  L.head==None:
                    L.head=currentNodeL2
                    currentNode=L.head
                else:
                    currentNode.nextNode=currentNodeL2
                    currentNode=currentNode.nextNode    
                currentNodeL2=currentNodeL2.nextNode

        #Agrego los nodos restantes        
        if currentNodeL1==None:
            currentNode.nextNode=currentNodeL2
        else:
            currentNode.nextNode=currentNodeL1
        return L
