from algo1 import *


### Defino una lista enlazada que solo tendra un puntero
class LinkedList:
    head = None


### Defino un nodo como dos punteros, uno al siguiente
### nodo y el otro con nuestro valor de interes.
class Node:
    value = None
    nextNode = None


### Esta funcion agrega un elemento element al
### principio de la lista listL es la lista
def add(listL, element):
    ### Creo un nuevo nodo
    newHead = Node()
    ### Le agrego el valor a agregar.
    newHead.value = element
    ### Conecto el nuevo nodo al resto de la lista.
    newHead.nextNode = listL.head
    ### Cambio el valor inicial de la lista
    listL.head = newHead
    ### devuelvo "nada" al final de la funcion.
    return


### Esta funcion busca el elemento un element en la
### lista listL. Si lo encuentra devuelve la posicion
### Sino devuelve None
def search(listL, element):
    ### agarro la cabecera de la lista
    currentNode = listL.head
    ### Inicio la posicion a devolver  en 0 por si esta
    ### al principio de la lista
    currentPosition = 0
    ### Si el nodo no esta vacio y el nodo no contiene
    ### element busco en el siguiente.
    while currentNode != None and element != currentNode.value:
        ### Buscolo el siguiente nodo
        currentNode = currentNode.nextNode
        ### La nueva posicion sera la anterior mas uno
        currentPosition += 1
    ### Al final del ciclo pudo haber recorrido todo la
    ### la lista. En ese caso currentNode seria None
    if currentNode == None:
        ### Si es None, la busqueda fallo, devuelvo None
        return None
    ### Si salio porque encontro element, devuelvo la
    ### posicion donde esta element.
    return currentPosition


### Esta funcion inserta un nodo con el elemento element
### en la posicion position de la lista listL
### Si no encuentra la posicion devuelve None
def insert(listL, element, position):
    ### Si position es 0, es lo mismo que hacer add.
    if position == 0:
        ### Llamamos a add, entonces
        add(listL, element)
        ### Devolvemos 0 como se pide.
        return 0
    ### Si no agregamos al principio
    ### debemos iterar la lista.
    firstNode = listL.head
    ### Si la lista esta vacia, no podemos insertar
    if firstNode == None:
        ###  Devolvemos None en este casos como error
        return None
    ### Miraremos el siguiente nodo,
    nextNode = firstNode.nextNode
    ### Vamos a crear un nueva lista.
    newList = LinkedList()
    ### Esta lista empezara con nuestro segundo nodo
    newList.head = nextNode
    ### Si tuvieramos que insertar el elemento en esta
    ### nueva lista seria e la posicion position - 1
    newposition = position - 1
    ### Ahora intentamos insertar element en esta nueva
    ### lista en la nueva posicion.
    ### Si la insercion fuera exitosa, obenemos la nueva
    ### posicion, sino None.
    if newposition != insert(newList, element, newposition):
        ### Si fallo, tenemos un None así que no se puede
        ### Insertar, devolvemos None
        return None
    ### Si la insercion es exitosa, entonces tenemos una
    ### lista actualizada, vemos enganchar esta lista
    ### nueva con la cabecera vieja.
    firstNode.nextNode = newList.head
    ### Luego devolvemos la posicion.
    return position


### Esta funcion elimina un nodo con el elemento element
### en la lista listL
### Si no encuentra la posicion devuelve None
def delete(listL, element):
    ### Miremos el primer elemento
    firstNode = listL.head
    ### Si no hay primer nodo, esto ha fallado.
    if firstNode == None:
        ### Devolvemos None.
        return None
    ### Revisamos que tiene el primer elemento.
    ### Queremos ver si el primer elemento tiene element
    if firstNode.value == element:
        ### Si tiene element, cambiamos la cabecera
        ### Por el siguiente nodo
        listL.head = firstNode.nextNode
        ### Y desvinculamos el nodo anterior de la lista
        firstNode.nextNode = None
        ### Como estaba en el primero, devolvemos 0
        return 0
    ### Usamos el mismo truco de insert
    ### Vamos a crear un nueva lista.
    newList = LinkedList()
    ### Esta lista empezara con nuestro segundo nodo
    newList.head = firstNode.nextNode
    ### probamos borrar element en la nueva lista.
    result = delete(newList, element)
    ### Si delete fallo tendremos un None
    if result == None:
        ### En ese caso devolvemos None
        return None
    ### Si delete nos devuelve un entero, entonces se
    ### elimino. Si se elimino debemos actulizar nuesta
    ### lista
    firstNode.nextNode = newList.head
    ### Entonces devolvemos la posicion donde se hizo el
    ### borrado, pero debemos aumentar la posicion en 1,
    ### porque acabamos de agregas un nodo al principio
    return result + 1


### Esta funcion devuelve la cantidad de elementos en
### listL
def length(listL):
    ### El menor tamanio posible es 0
    size = 0
    ### Revisamos que hay al principio de la lista.
    currentNode = listL.head
    ### Mientras el primer elemento que miremos no sea
    ### None, entonces no hemos llegado al final de la
    ### lista. Debemos seguir recorriendola
    while currentNode != None:
        ### Revisamos que hay en el siguiente nodo.
        currentNode = currentNode.nextNode
        ### Debemos aumentar en uno el tamanio, dado que
        ### Al menos hay un elemento mas, si currentNode
        ### no es None
        size += 1
    ### Al final del ciclo tenemos el tamanio
    return size


### Esta funcion devuelve el valor del elemento en la
### posicion position de la lista listL
def access(listL, position):
    ### inicio un entero para ser iterado
    i = 0
    ### Miro que hay la cabecera de la lista
    currentNode = listL.head
    ### Mientras el nodo no este vacio, y el numero de
    ### iteracion es menor a la posicion position que
    ### queremos, entonces no hemos encontraro lo que
    ### queremos
    while currentNode != None and i < position:
        ### Miramos entonces que hay en el siguiente nodo
        currentNode = currentNode.nextNode
        ### Aumentamos nuestro entero
        i += 1
    ### Al final del ciclo anterior, puede que
    ### tengamos un None. En ese caso, la posicion position
    ### no existe en esta lista.
    if currentNode == None:
        ### Si no existe, devolvemos None
        return None
    ### Si el valor no es vacío, entonces hemos encontrado
    ### la posicion de interes, asi que imprimimos su valor
    return currentNode.value


### Esta funcion cambia el valor del elemento en la
### posicion position de la lista listL por el nuevo
### valor element
def update(listL, element, position):
    ### inicio un entero para ser iterado
    i = 0
    ### Miro que hay la cabecera de la lista
    currentNode = listL.head
    ### Mientras el nodo no este vacio, y el numero de
    ### iteracion es menor a la posicion position que
    ### queremos, entonces no hemos encontraro lo que
    ### queremos
    while currentNode != None and i < position:
        ### Miramos entonces que hay en el siguiente nodo
        currentNode = currentNode.nextNode
        ### Aumentamos nuestro entero
        i += 1
    ### Al final del ciclo anterior, puede que
    ### tengamos un None. En ese caso, la posicion position
    ### no existe en esta lista.
    if currentNode == None:
        return None
    ### Si no es vacio, entonces econtramos el elemento de ### interes, asi que lo actualizamos.
    currentNode.value = element
    ### Devolvemos la posicion actualizada si la
    ### actualizacion fue exitosa
    return position

    ### Todas seran O(n), excepto add()
    ### En array eran todas O(n), excepto access y update
