# Ayudantia Semana 7: Ejercicios Pre-Certamen 1

## Correctitud de Algoritmos:

### 1. Suma de elementos en array:

Pruebe con invarientes de ciclos que el siguiente algoritmo suma correctamente los elementos de un array:

```
1: function sumArray(A[1..n], n)
2: 
3: sum ← 0
4: for i <- 1 to n do
5:     sum ← sum+A[i]
7: end for
7: return sum 
```

Respuesta:

Primero, tenemos que la suma de los primeros i elementos del array es

$sum = \sum_{k=1}^{i} A[k]$

1) $sum$ se incializa como 0 y $i$ como 1, la suma de los primeros 0 elementos es 0, por lo tanto antes de la primera iteracion se cumple.

2) Suponemos que para alguna iteracion del loop con i, es decir, se cumple $sum = \sum_{k=1}^{i} A[k]$

3) La invariante es correcta al principio de la siguiente operacion, por lo que tenemos $sum_i = \sum_{k=1}^{i} A[k]$. Para i+1, por la suma de la linea 5, tenemos 

    $sum_{i+1} = sum_i + A[i+1] = \sum_{k=1}^{i} A[k] + A[i+1] = \sum_{k=1}^{i+1} A[k]$

    Lo cual hace que se cumpla la invariante.

4) Cuando el loop termina, tenemos i=n, y como se cumple la invariante, sum guarda el valor de la suma de los primeros n elementos del array, y por lo tanto, la suma de todos los elementos del arreglo.


### 2. Numeros Primos:

Pruebe con invariantes de ciclos que el siguientr algoritmo correctamente idenntifica numeros primos.

```
 1: function isPrime(n)
 2: for i = 2 to √n do
 3:     if n divisible por i then
 4:         return false
 5:     end if
 6: end for
 7: return true 
```

Respuesta:

Primero, la invariante es que para cada iteracion, si n es divisible por i, entonces n no es primo.

1) Antes de la primera iteracion, no se ha comprobado ningun numero por lo que como no conozco ningun numero que divida a n, aun no lo descarto como primo.

2) Para un i en el rango, asumismos que se cumple la invarianza, es decir, n no es divisible por ningun numero entre 2 y i, y por lo tanto aun no decimos que no es primo.

3)  caso a. Si n es divisible por i+1, retornamos falso y salimos del loop.
    
    caso b. Si n no es divisibble por i+1, entonces como no era divisible por numeros entre 1 y i (por hipotesis inductiva), no es divisible por numeros entre 1 y i+1, por lo que no decimos que no es primo y seguimos avanzando en el loop.

4) El loop termina cuando i = $\sqrt{n}$. Si n no es divisible entre ningun numero entre 1 y $\sqrt{n}$, entonces es primo, pues para ser divisible por numeros entre $\sqrt{n}$ y $n-1$, tiene que serlo tambien por numeros menores, que ya hemos visto no es el caso. (salvo dividirlo por si mismo y 1, claro) (see: si $a<b$ entonces $a^2 < a \times b$). Por otra parte, si se salio del loop antes de tiempo, es porque pudimos encontrar un numero que divide a n fuera de 1 y si mismo, y por ende, no es primo. De esta manera, el algoritmo correctamente identifica numeros primos.

## Analisis de algoritmos.

### 3. Karatsuba:

Determine el tiempo de ejecucion del algoritmo de multiplicacion de karatsuba.

```
1: function Karatsuba(num1, num2)
 2: if num1 < 10 or num2 < 10 then
 3:     return num1 * num2
 4: end if
 
 5: m ←max(largo(num1),largo(num2))
 6: m2 ←⌊m/2⌋ {Floor division by 2}
 
 7: high1,low1 ← split_at(num1,m2)
 8: high2,low2 ← split_at(num2,m2)
 
 9: z0 ←Karatsuba(low1,low2)
 10: z1 ←Karatsuba(low1 +high1,low2 +high2)
 11: z2 ←Karatsuba(high1,high2)
 
 12: return (z2 *10^(m2*2)) +((z1 −z2−z0)*10^m2)+z0 

```

Respuesta:

Vemos que en m2 se divide el problema en subproblemas de tamano m/2.

Vemos que entre las lineas 9 a 11 hacemos 3 llamadas recursivas, las 3 de tamano n/2.

Vemos que el tiempo destinado a "conquistar" es constante, pues se hace en la linea 12, y no depende del tamano de los numeros.

Con esto, vemos que este algoritmo tiene el tiempo correspondiente a la recursion:

$T(n) = 3T(n/2) + O(1)$

Viendo el teorema maestro, tenemos $a=3$, $b=2$, $d=0$, como $\log_b a = \log_2 3 \approx 1.58 > d = 0 $, por lo tanto, nos encontramos en el tercer caso:

$T(n) = O(n^{\log_b a}) = O(n^{\log_2 3}) \approx O(n^{1.58})$