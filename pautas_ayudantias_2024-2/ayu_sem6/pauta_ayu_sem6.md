# Ayudantia semana 6: Correctitud, Caso Promedio + Ejercicio extra de Analisis amortizado.

## Correctitud de algoritmos:

### 1) Realice el analisis de correctitud de InsertionSort, utilizando el metodo de "loop invariants" (i.e: la induccion que se realiza sobre loops).

```
1:  procedure InsertionSort(A,n):
2:      for j <- 2 to n do:
3:          key <- A[j]
4:          i <- j - 1
5:          while i > 0 and A[i] > key do:
6:              A[i+1] <- A[i]  
7:              i <- i - 1 
8:          A[i+1] <- key
```

Se recomienda estudiar bien como funciona insertion sort antes de realizar este ejercisio (un video que muestre como se ordena un arreglo con este algritmo puede ser util).

Respuesta:

Recordar que los pasos para probar cor induccion son:

1) Definir un **caso base** para el que lo que se quiere demostrar se cumple. En general, que se cumple en la primera iteracion o antes de la primera iteracion.

2) Definir la **hipotesis inductiva**, es decir, un escenario arbitrario en el que se cumple lo que se queire probar, digamos para la i-esima iteracion.

3) **Probar mantendion**, dado que la hipotesis inductiva se cumple, para iteraciones posteriores tambien se cumple. Si lo conseguimos, hemos probado que esto es correcto antes, durante y despues del loop, y por lo tanto, nuestro algoritmo es correcto.

4) **Probar terminacion**: dado que se completan todas las iteraciones del loop, el resultado final es el esperado.


Primero, hay que notar que el "while" de la linea 5 toma el elemento siguiente al sub arreglo ordenado y lo inserta en la posicion correcta dentro del sub arreglo, es decir, produce un nuevo sub-arreglo ordenado (Esto tambien es probable con loop invariants, seria tambien un buen ejercicio para estudiar, recomiendo tratar de hacerlo).

Ahora, en InsertionSort:

1) Al principio del loop, con j=2, el sub-arreglo A[1...j-1] se encuentra ordenado. 

    Vemos que al principio del loop, este sub-arreglo contiene un unico elemento, A[1], que de manera trivial esta ordenado.

2) Asumimos que en cualquier iteracion j, A[1..j-1] (el sub-arreglo de la izquierda) se encuentra ordenado. 

3) Para la siguiente iteracion, con j+1, se paso por while que colocaba A[j] en la posicion correcta, por lo tanto, A[1..j] ahora esta ordenado. De esta manera, incremetar j en el loop mantiene la invarianza del loop.

4) Al final del loop, con j = n+1, por invarianza del loop A[1..n] esta ordenado. Esto es lo que queriamos probar, por lo tanto, hemos probado que InsertionSort es correcto.


## Caso promedio:

### 2) Calcule el tiempo de ejecucion asintotico de caso promedio del algoritmode busqueda siguiente:

```
1:  BuscarOrdenado(A[1..n], x):
2:      if x <= A[piso(n/2)]:
3:          i <- 1
4:          d <- piso(n/2)
5:      else:
6:          i <- piso(n/2)+1
7:          d <- n
8:      while i <= d do:
9:          if x <= A[i]:
10:             break
11:         i <- i+1
12:     if i <=d and x = A[i]:
13:         return i
14:     else:
15:         return n+1
```

Recordar que se asume que los casos son equiprobables

Respuesta:

Primero, hay que entender lo que hace el algoritmo.

Este algoritmo de busqueda realiza busqueda lineal en una de las dos mitades de un arreglo ordenado.

En este algoritmo los casos posibles corresponden a las distintas posiciones donde se sale del loop while de la linea 8, es decir, cada posicion en el arreglo en el que puede estar x o cada "espacio" entre posiciones en el que x debiese estar en caso de que x no se encuentre en el arreglo.

Para el analisis primero nos damos cuenta que solo necesitamos hacer el analisis para una mitad del arreglo y luego duplicarlo, ya que el comportamiento es exactamente igual en ambas mitades. Para este analisis, veremos la primera mitad.

Veamos un pequeno ejemplo de como se puede ver la mitad del sub arreglo, marco con [] las casillas del arreglo y con {} los espacios infructuosos, | representa la mitad del arreglo 

{ }[ 1 ]{ }[ 2 ]{ }[ 4 ]{ }[ 7 ]{ }[ 9 ]{ }[ 15 ] | { } [ 21 ] { } ...

Notamos que en cada mitad hay n posibles posiciones, para un total de 2n+1 posiciones posibles en todo el arreglo, antes de cada casilla y en la casilla siguiente a la ultima.

Notamos tambien que para x perteneciente al arreglo en la posicion k, se realizan $\approx k$ comparaciones + un par mas para comprobar en que mitad se encuentra y si se salio del loop porque se encontro o porque se paso (esto no es importane pues asintoticamente esto crea constantes y factores que no se anotan en notacion asintotica).

Para los casos en que x no esta en el arreglo, esto se descubre al comparar la posicion siguiente, es decir, no se requieren comparaciones adicionales.

Asi, el tiempo de caso promedio esta dado por:

$ T(n) \approx  \frac{1}{2n} \times 2\sum_{i=1}^{piso(n/2)} i \approx (1/n) \times (1/8)(n^2+2n) = \frac{n}{8}+\frac{1}{4} \in \Theta(n)$



## Otro ejercicio de Analisis Amortizado:

### 3) Los arreglos de tamano $2^i$

Considere una estructura de datos de $n$ elementos. Sea $k = \lceil \lg(n+1) \rceil$, y $(n_{k-1}, n_{k-2},...,n_0)$ la representacion binaria de n. La estructura de datos consiste en k arreglos **ordenados** A_0, ... , A_{k-1}, siendo el tamano de A_i 2^i. El arreglo A_i se encuentra **lleno** si n_i = 1, y **vacio** en caso contrario. Ojo: Aunque cada arreglo se encuentra ordenado, no hay relaciones de orden entre cada arreglo.

1) Proponga una operacion Search e indique su tiempo de peor caso.

2) Proponga una operacion Insert, indique su tiempo de peor caso, y haga el analisis amortizado de una secuencia de operaciones Insert.


*Nota: Para el analisis amortizado, puede resultar util considerar que el arreglo se inicializa como vacio antes de la secuencia de operaciones.*
*Hint: Recuerde el analisis amortizado de contador binario.*

Respuesta:

1) La operacion Search consiste en iterar sobre cada arreglo que no este vacio, realizar busqueda binaria desde el arreglo mas pequeno hasta el mas grande, hasta que se encuentre el elemento o hasta el final si no se encuentra.

    En el peor de los casos, se busca un elemento que no se encuentra en el arreglo, en un caso con todos los arreglos llenos $(n = 2^m-1)$, en este caso se deben hacer k busquedas binarias, cada una con costo $O(\lg(2^i)) = O(i)$, es decir, el costo de peor caso para la operacion Search es:

    $O(0 + 1 + 1 + ... + (k-1)) = O(\frac{k(k-1)}{2}) = O(k^2) = O(\lg^2(n))$

2) La operacion Insert tratara de insertar en el arreglo $A_0$, si el arreglotiene un elemento se hace Merge (el mismo de MergeSort), se inserta en $A_1$ y se borra de $A_0$. En caso de este estar tambien lleno se repite el proceso hasta que se llegue a un arreglo vacio, o se cree un nuevo arreglo al final en caso de estar todos los arreglos llenos. Cada operacion Merge para insertar en el arreglo i (y por lo tanto, con elementos de i-1 hacia artras) toma tiempo $O(2^i)$. Notar que el timepo de insercion esta dado por el tiempo de realizar la operacion merge, pues el tiempo de mover los elementos al siguiente arreglo toma tiempo lineal respecto al tamano del arreglo anterior, el cual es menor al tiempo que toma merge y por lo tanto asintoticamente ignorable.

    **En el peor de los casos**, se trata de hacer insercion en un caso con todos los arreglos llenos $(n = 2^m-1)$. Hacer merge en los k arreglos, y por lo tanto insertar en la estructura en peor caso toma tiempo:

    $O(2^0 + 2^1 + 2^2 + ... + 2^{k-1}) = O(\sum_{i=0}^{k-1} 2^i) = O(2^k - 1) = O(2^k) = O(2^{\lg(n+1)}) = O(n)$


    **Para el analisis amortizado** tenemos que considerar que no todas las inserciones van a generar una casacada de Merges, y cuando ocurre una casacada van a haber varias operaciones en las que no va a ocurrir nuevamente, pues los arreglos que estaban antes del arreglo en que acabo el cascadeo estan vacios.

    Veamos una secuencia de inserciones con su costo para entender mejor:

    **Primera insercion**

    $A_0$:  [x]
    
    $A_1$:  [][]
    
    $A_2$:  [][][][]
    
    Costo: 1

    **Segunda insercion**

    $A_0$:  []
    
    $A_1$:  [x][x]
    
    $A_2$:  [][][][]
    
    Costo: 1+2

    **Tercera insercion**

    $A_0$:  [x]
    
    $A_1$:  [x][x]
    
    $A_2$:  [][][][]
    
    Costo: **1**

    **Cuarta insercion**

    $A_0$:  []
    
    $A_1$:  [][]
    
    $A_2$:  [x][x][x][x]
    
    Costo: 1+2+4

    Vemos que la __cantidad de merges__ se comporta igual que un contador binario. Con $l$ operaciones El arreglo $A_0$ tiene $l$ merges, el arreglo $A_1$ tiene un merge cada 2 inseciones, es decir, $l/2$ merges, $A_2$ tiene $l/4$ merges, y $A_i$ tiene $l/2^i$ merges.

    Entonces, como cada merge toma tiempo $O(2^i)$, tenemos que la suma de tiempo de las operaciones es:

    $O( \frac{l}{2^0}(2^0) + \frac{l}{2^1}2^1 + ... + \frac{l}{2^{k-1}}2^{k-1}) = O(\sum_{i=0}^{\lg n} l) = O(l \lg 2n) = O(l \lg n)$

    Entonces, dividido por la cantidad de operaciones realizadas, $l$, el costo  amortizado de operaciones Insert en esta estructura de datos es $O(\lg n)$

    