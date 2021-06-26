from mylinkedlist import *

#Ordena una lista utilizando el método de la burbuja
def BubbleSort(L):
    if L==None:
        return None
    else:
        BubbleSortR(L,None)

#Parte recursiva
#Los nodos se mueven en Orden A-B-C
def BubbleSortR(L,End):
    nodeB = nodeA = L.head
    nodeC = nodeB.nextNode

    if nodeC==End:
        return
    while nodeC!=End:
        if nodeB.value>nodeC.value:
            nodeA.nextNode= nodeC
            nodeB.nextNode= nodeC.nextNode
            nodeC.nextNode= nodeB
            if L.head==nodeB:
                L.head = nodeA = nodeC
            nodeA=nodeC
            nodeC=nodeB.nextNode
        else:
            nodeC=nodeC.nextNode
            if L.head!=nodeB:
                nodeA=nodeA.nextNode
            nodeB=nodeB.nextNode

    BubbleSortR(L,nodeB)


#Ordena una lista utilizando el método de Seleccion
def SelectionSort(L):
    if L==None:
        return None
    else:
        SelectionSortR(L,None)

def SelectionSortR(L,lastSorted):
    if lastSorted==None:
        Union=L.head
    else:
        Union=lastSorted.nextNode

    if Union==None:
        return
    else:
        currentNode = leftMin = minNode = Union

        #Busco el menor
        while currentNode.nextNode!=None:
            if currentNode.nextNode.value<minNode.value:
                minNode=currentNode.nextNode
                leftMin=currentNode 
            currentNode=currentNode.nextNode
        
        #Acomodo el menor en la ultima posicion de los ya ordenados
        if minNode!=Union:
            if lastSorted==None:
                leftMin.nextNode=minNode.nextNode
                minNode.nextNode=L.head
                L.head=minNode
                
            else:
                lastSorted.nextNode=minNode
                leftMin.nextNode=minNode.nextNode
                if Union.nextNode==minNode:
                    minNode.nextNode=leftMin
                else:
                    minNode.nextNode=Union

        SelectionSortR(L,minNode)       
        

#Ordena una lista utilizando el método de Inserccion
def InsertionSort(L):
    if L==None:
        return None
    else:
        InsertionSortR(L,L.head)

def InsertionSortR(L,lastSorted):
    Union = lastSorted.nextNode
  
    if Union==None:
        return
    else:
        positioned = False
        currentNode = L.head

        #Busca una posicion posible donde insertar el nodo
        while currentNode.nextNode!=Union:
            if currentNode.value<=Union.value and currentNode.nextNode.value>=Union.value:
                leftNode=currentNode
                rigthNode=currentNode.nextNode
                positioned=True
            currentNode=currentNode.nextNode

        #Inserta en la posicion y aplica recursividad
        if (positioned==False and Union.value<currentNode.value):
            currentNode.nextNode = Union.nextNode
            Union.nextNode = L.head
            L.head = Union
            InsertionSortR(L,lastSorted)   
        elif positioned:
            lastSorted.nextNode = Union.nextNode
            leftNode.nextNode = Union
            Union.nextNode = rigthNode
            InsertionSortR(L,lastSorted)
        else:
            InsertionSortR(L,lastSorted.nextNode)


#Ordena una lista utilizando el método de Ordenamiento Rápido
def QuickSort(L):
    if L==None:
        return None
    else:
        QuickSortR(L,L.head,None,None)


def QuickSortR(L,Start,End,Union):
    #Toma como pivota el primer elemento
    pivot=Start.value
    currentNode=Start.nextNode
    leftNode=Start
    rightNode=Start

    #Acomoda los elementos menores y mayores respecto al pivote
    while currentNode!=None:
        siguiente=currentNode.nextNode
        if currentNode!=End:
            if currentNode.value<pivot:    
                rightNode.nextNode=currentNode.nextNode
                currentNode.nextNode=leftNode
                leftNode=currentNode
            
                if Union!=None:
                    Union.nextNode=currentNode
            else:
                rightNode=currentNode
        currentNode=siguiente

    if Start==L.head:
        L.head=leftNode

    if Start.nextNode!=None:
        QuickSortR(L,Start.nextNode,None,Start)
    if leftNode!=Start:
        QuickSortR(L,leftNode,Start,None)
    
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
            if currentNodeL1.value<currentNodeL2.value:
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

