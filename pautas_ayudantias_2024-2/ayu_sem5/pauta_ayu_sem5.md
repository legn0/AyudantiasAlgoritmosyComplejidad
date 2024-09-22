# Ayudantia semana 5: Analisis asintotico, Dividir y conquistar.

## Analisis Mejor y Peor caso:

1) Entregar el tiempo de mejor y peor caso del algoritmo shellsort, para un arreglo A de tamano n 

```
1: procedure ShellSort(A):
2:    n <- length(A)
3:    h <- piso(n/2)
4:
5:    while h > 0:
6:       for i <- h + 1 to n:
7:            j <- i - h
8:           while j > 0:
9:               if A[j] > A[j+h]:
10:                   swap(A[j], A[j+h])
11:                   j <- j-h
12:               else:
13:                   j <- 0
14:       h <- piso(h/2)
```


Respuesta:

(a) El mejor caso es el ordenar un arreglo ya ordenado, en ese caso el "if" de la linea 9 siempre sera falso, y por lo tanto el "while" de la linea 8 sera una operacion de tiempo constante.

De esta manera por cada iteracion del while de la linea 5 se realizan n-h operaciones por el for de la linea 6. Como la cantidad de iteraciones del while externo esta dado por dividir el tamano de h (el span de ShellSort) a la mitad hasta que sea menor que 1, este while externo se ejecute log(n) veces. De esta forma  el tiempo de mejor caso del algoritmo es

$ \sum_{i=1}^{log(n)} n-(n/2^i) = -n + nlog(n) + 1 \in \Omega(nlog(n))$

(b) El peor caso se da cuando el arreglo se encuentra en el orden opuesto al deseado.

Cuando esto ocurre el if de la linea 9 sera verdadero hasta que se llegue al principio del arreglo (si esto no hace sentido, recomiendo buscar como funciona ShellSort), y por ende el while interior se sejecuta techo(j/h) veces. El analisis para el for y el while exterior se mantienen del analisis de tiempo de mejor caso. 

Ahora, en lugar de cada interacion del for tomar tiempo constante, se considera que la i-esima iteracion toma tiempo $ (h + i)/ h $. Entonces, para la j-esima iteracion del ciclo while externo, el tiempo de ejecucion del ciclo for es $ \sum_{i=(n/2^j) + 1}^{n} \lceil (n/2^j)+i \rceil /(n/2^j)$

De esta manera el tiempo de peor caso del algoritmo esta dado por:

$\sum_{j=1}^{log(n)} \sum_{i=(n/2^j) + 1}^{n} \lceil (n/2^j)+i \rceil /(n/2^j) \approx (2n-1)(nlog(2)+log(n/2))/log(4) = (2n^2log(2) + 2nlog(n/2) - nlog(2) - log(n/2))/log(4) \in O(n^2) $


## Analisis Amortizado:

2. Analisis amortizado de secuencia de operaciones de monotonic stack.

Una pila monotona (monotonic stack) S es una pila en que los elementos aparecen en orden creciente (de tal manera que el elemento superior es el mayor), las cuales se inicializan como vacias, tiene las siguientes operacioes:

- Pop(S): Borrar y retorar el primer elemento de S. Tiene tiempo $\Theta(1)$
- Push(S,x): Insertar x en S y reestablecer el orden removiedo elementos hasta que x sea el mayor. Tiene tiempo de peor caso O(n) y de mejor caso $\Omega(1)$

Realice el analisis amortizado de n operaciones pop y push.

Respuesta:

Cada operacion que se hace se realiza exactamente una vez por elemento, un elemento solo se agrega una vez y solo se elimina una vez. Como agregar y eliminar toma tiempo constante, cualquiere secuencia de n operaciones toma tiempo O(n), dividido por la cantidad de operaciones obtenemos que el costo amortizado de una operacion Pop y Push es de O(1)


## Dividir y Conquistar:

3. Considere el problema de calcular una aproximacion de $r$ la raiz cuadrada de q, $(q > 1)$. Se requiere realizar la aproximacion con precicion p, se cumple que:

$r-p \le \sqrt{q} \le r + p$

Construya un algoritmo recursivo que permita resolver el problema anterior y calcule la complejidad temporal de este.

Respuesta:

Por simplicidad, el algoritmo se escribira usando python (ver: algoritmo_raiz_cuadrada.py).

El fundamento es que dada la relacion $r-p \le \sqrt{q} \le r + p$, tambien se cumple $(r-p)^2 \le q \le (r+p)^2$. Dado esto podemos  pensar en realizar busqueda binaria sobre un "arreglo" ordenado que parte en 0 y termina en q. Consultamos por la posicion central (que sera el promedio entre los limites superior e inferior), esta sera nuestra $guess$ de la raiz de q, digamos r'. si nuestra $guess$ no es suficientemente buena ajustamos los limites acordemente y tratamos de nuevo.  

Este algoritmo divide el problema en 1 subproblema de tamano n/2, y toma tiempo constante de union (conquistar). Esto corresponde a la recurrencia $T(n) = T(n/2) + O(1)$, que segun el teorema maestro corresponde a tiempo de ejecucion $O(log(n))$.


4. Rebata o apoye lo siguiente: Dado que mergesort usa subdivision del arreglo para ordenar, alguien ha pensado en lograr una mayor eficiencia si en vez de usar 2 pariciones, se usan 4.

Respuesta:

Mergesort es un algoritmo dividir y conquistar, y su tiempo definicion esta dado por la recurrencia $T(n) = 2T(n/2) + O(n)$. Esto resulta segun el teorema maestro un tiempo de ejecucion de $O(nlog(n))$.

Si en lugar de dividir el arreglo en 2 subarreglos lo dividimos en 4, la recurrencia seria $T(n) = 4T(n/4)+O(n)$. Esto segun el teorema maestro corresponde a un tiempo acotado por O(nlog(n)), es decir, el mismo. 

Por lo tanto, usar 4 particiones en vez de 2 no es mejor, al menos asintoticamente.