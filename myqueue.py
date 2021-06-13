from linkedlist import Node

"""
Implmentaremos nuestas colas como listas circulares.
Esta implmentacion es una de las alternativas 
propuestas en el libro de Alfred Aho. Al implmentar
las colas de esta forma la insercion y la extraccion
son de complejidad O(1)

Llamemos queueQ a nuesta cola. Esta esta implmentada 
con una lista. el cabezal de nuestra lista es 
queueQ.head. Sin embargo, en nuestra implmentacion,
este cabezal apuntara al ultimo elemento (es decir, es 
mas un rabo que un cabezal). De esta manera, insertar 
el proximo elemento se puede hacer en tiempo O(1), 
pues corresponde al primer elemento. Adicionalmente, 
hacemos que nuestro rabo apunte al primer elemento 
insertado. De esta manera, la extraccion tambien se 
hace en tiempo O(1) porque es siempre insertar en la 
posicion 1
"""
### Encolamos el elemento element en la cola queueQ
def enqueue(queueQ, element):
  ### Nuestro primer elmento es en realidad el ultimo
  ### por eso lo llamamos tail
  tail = queueQ.head
  ### Si no hay ningun elemento, tenemos que insertar
  ### un primer elemento
  if tail == None:
    ### Para insertar un primer elemento, primero
    ### creamos un nodo
    head = Node()
    ### En este nodo ponemos el valor del elemento a 
    ###isertar
    head.value = element
    ### Como nuestas colas son listas ciclicas, hacemos
    ### que el siguiente nodo sea si mismo.
    head.nextNode = head
    ### Luego asignamos este nodo como nuestro primer 
    ### elemento
    queueQ.head = head
    ### Terminamos nuestra funcion
    return
  ### Como dijimos, nuestro ultimo elemento apunta al 
  ### primero, asi que al insertar un nuevo elemento 
  ### tenemos que vincularlo al ultimo y hacer que el 
  ### nuevo apunte al primero. Por esto necesitamos 
  ### guardar el primer nodo.
  firstNode = tail.nextNode
  ### Creamos el nuevo nodo a insertar en la cola
  newTail = Node()
  ### Lo cargamos con el elemento a insertar.
  newTail.value = element
  ### Ahora hacemos que el nuevo final apunte al nuevo 
  ### final
  tail.nextNode = newTail
  ### Y que el nuevo final apunte al primero
  newTail.nextNode = firstNode
  ### Por ultimo hacemos que el cabezal de nuesta lista
  ### apunte al nuevo final
  queueQ.head = newTail
  ### Terminamos la funcion.
  return

### Extraemos el primer elemento de nuestra cola queueQ
def dequeue(queueQ):
  ### Como dijimos el primer elemento apunta al final
  tail = queueQ.head
  ### Si el final esta vacio...
  if tail == None:
    ### ... devolvemos un None
    return None
  ### Caso contrario, buscamos el primer nodo, que es
  ### el siguiente al ultimo.
  firstNode = tail.nextNode
  ### Guardamos el valor del primer nodo para
  ### devolverlo despues.
  result = firstNode.value
  ### Guardamos tambien el segundo nodo, esto es para
  ### poder eliminar el primer nodo
  secondNode = firstNode.nextNode
  ### Ahora asociamos el final de la cola al segundo
  ### de esta manera eliminamos el primer nodo-
  tail.nextNode = secondNode
  ### Hasta aqui no hemos considerado un caso limite,
  ### cuando hay un solo elemento. En ese caso el 
  ### primer nodo es el ultimo.
  if firstNode == tail:
    ### Si ese fuera el caso vaciamos la lista
    queueQ.head = None
  ### luego desvinculamos el nodo del resto de la lista
  firstNode.nextNode = None
  ### y devolvemos el resultado.
  return result

"""
OBSERVACION:
la funcion insert implementada anteriormente puede 
usarse para implementar enqueue. La funcion enqueue 
corresponde a seria un insert en la posicion 1 y luego 
un cambio de cabezal. hay que aclarar que al usar 
siempre un mismo valor de position, la funcion insert 
se vuelve O(1). En el caso de un elemento, habría que 
asignar correctamente el siguiente nodo. En cualquier 
caso enqueue y dequeue son O(1)
"""