# Flow-Shop-Scheduling
Es un problema combinacional en el que se necesita organizar el procesamiento de un conjunto de trabajos divididos en operaciones y cada operación se lleva a cabo en un recurso compartido.
En el FSS (Flow Shop Scheduling) se dan tiempos _Pkj_ para cada trabajo _j_ en cada máquina _k_ y una secuencia de trabajo _S=(s1,s2,...,sn)_ donde _n_ trabajos _(j = 1,2,...,n)_ serán procesados por _m_ máquinas _(k = 1,2,...,m)_ por lo que el objetivo de FSSP es encontrar un
orden de secuencia para el procesamiento de operaciones con el valor mínimo para el *_MakeSpan._*

El _*MakeSpan*_ para una organización de trabajo en particular se compone del total tiempo transcurrido desde el comienzo del primer trabajo hasta el término del último trabajo. El *_MakeSpan_* es por lo tanto un característica de todo el problema.

El FSSP se resume a determinar la permutación optima para minimizar el _MakeSpan_, es decir, minimizar la suma del tiempo en el que se completa cada trabajo. Con 2 máquinas, el problema se puede resolver en un tiempo _ø(nlogn)_ usando el algoritmo de _Johnson_, sin embargo, para más de 2 máquinas, el problema se convierte en _NP Hard_. 

# Datos del problema
$n$ :  Número total de trabajos

$m$ :  Número de máquinas

$W_j$ Peso del trabajo $j$, $j = 1, 2,..., n$

# Variables

$P_{ij}$ : Tiempo de procesamiento. Indica el tiempo requerido para procesar el trabajo $i$ en la máquina $j$.

$S_{ikj} $ : Tiempo de configuración de un trabajo $i$ a un trabajo $k$ en la máquina $j$ ($i = 0$ se refiere al tiempo de configuración inicial del trabajo programado).

$C_{i,j}$ : Tiempo de finalización del trabajo $i$ en la máquina $j$.

$X_{ik}$ : Si el trabajo $i$ es procesado antes que el trabajo $k$, es igual a $1$; se otra forma, es igual a $0$.


# Modelo
El problema de Flow Shop es generalmente entendido como un problema de permutaciones.

# Función Objetivo
El objetivo del problema es disminuir el tiempo total de procesamiento desde el inicio de la tarea 1 del trabajo 1 hasta la tarea n del trabajo n.

$ Minimize \sum_{j=1}^{n} w_j C_j^2$

# Restricciones
Garantizar que todos los trabajos han sido asignados y que el tiempo de completado del trabajo $i$ en la máquina $1$ es al menos tan grande como el tiempo de procesamiento de ese trabajo en la máquina:

$p_{i1} \geq  c_{i1}; i=1,...,n.$

El trabajo $j$ no puede empezar en la máquina $j$ a menos que haya finalizado en la máquina $j-1$. La restricción 2 garantiza que el tiempo de completado del trabajo $i$ en la máquina $j$ debe ser al menos tan grande ocmo el tiempo de procesamiendo en la máquina $j$, uno más grande que el tiempo de completado en la máquina $j-1$.

$p_{i1} + c_i [j-1] \geq c_{ij}, i=1,...,n; j=1,...,m. $

Las restricciones 3 y 4 aseguran que solo hay una restricción para cada secuencia de trabajos. Este caso muestra la relación entre la precedencia y latencia entre trabajos.

$c_{ij} - c_{kj} + Mx_{ik} \geq s_{kij} + p_{ij}$

$c_{ij} - c_{kj} + M[1 - x_{ik}] \geq s_{kij} + p_{ij}$

donde $k \gt i \geq 1$ y $i=1,...,n;k=1,...,n; j=1,...,m. $
También, $M$ es un número muy grande.

Las restricciones 5 y 6 garantizan que solo un trabajo puede ser seguido de otro trabajo en cada planificación:

$\sum_{i=1}^{n} x_{ik}=1; k = 1,2,...,n$ para $i \ne k,$

$\sum_{k=1}^{n} x_{ik}; k = 1,2,...,n$ para $i \ne k.$

# Suposiciones
1. Hay un cierto numero de trabajos que puede ser asignado a una estacion.
2. Cada operacion es realizada en su propia maquina.
3. El tiempo de cada trabajo esta determinado.
4. Los prerequisitos para cada trabajo han sido determinados. Por lo tanto, una tarea es ejecutable cuando su prerequisito ha sido completamente completado.

# Representación de la solución 
La representación de dato usada fue directa, un arreglo de enteros que representan la secuencia de los trabajos a realizar que minimiza el tiempo de procesamiento. El arreglo sera tan grande como cantidad de trabajos tenga el problema.

# Solución inicial

_Aleatoria_
La solución inicial que se propone esta ordenada de forma aleatoria, para n trabajos.
 |  |  |  |  |  |
 | :---: | :---: | :---: | :---: | :---: |
 | 2 | 1 | n | n-1 | ... |
 
 # Solución Vecina
 
 _Intercambio de orden de trabajos, mediante permutaciones_
 
 Inicial:
 
 |  |  |  |  |  |
 | :---: | :---: | :---: | :---: | :---: |
 | _2_ | 1 | n | _n-1_ | ... |
 
 Vecina:
 Solución obtenida a partir de la permutación de dos elementos diferentes entre sí del arreglo, 
 
 |  |  |  |  |  |
 | :---: | :---: | :---: | :---: | :---: |
 | __n-1__ | 1 | n | __2__ | ... |

# Aplicaciones

Su aplicación es amplia:

  → para programar el despacho de vuelos en aeropuertos
  
  → programar líneas de producción en un fábrica
  
  → programación de cirugías
  
  → reparación de equipos o maquinarias de un taller

# Ejemplo
|Trabajos|M1|M2|M3|M4|
| :---: | :---: | :---: | :---: | :---: |
|T1|5|10|6|8|
|T2|8|15|5|7|
|T3|8|5|7|9|

## Vector inicial propuesto 
Se genera un vector inicial de orden aleatorio 
|  |   |   |
| :---: | :---: | :---: |
|2|1|3|
## Ilustración de la solución optima 
![image](https://user-images.githubusercontent.com/93891210/162112069-e758b97f-e035-4961-8808-46f18bf2c857.png)



## Resultados obtenidos
Resultados del ejemplo
|Iteraciones | Resultado | Costo | Tiempo | Temperatura|
| :---: | :---: | :---: | :---: | :---: |
|61|1,3,2|48|0.0276|6|


# Generación de solución Vecina

```python
		
def solucionVecina(self,state,t=1):
    index=list(range(len(state)))	
    random.shuffle(index)
    a, b = index.pop(), index.pop()
    newSolution=list(state)
    newSolution[a], newSolution[b] = newSolution[b], newSolution[a]
    return tuple(newSolution)
		
```

# Función de Costo

```python
def makespan(self,state):
    temp=[]
    for i in state:
      temp.append(np.array(self.d_jobs[i]))
    cost=np.array(temp)
    for i in range(self.d_process):
      for j in range(self.n_jobs):
        temp=cost[0:j+1,0:i+1].copy()
        temp[-1][-1]=0
        cost[j][i]+=np.max(temp)
    return cost[-1][-1]

```

# Instancias
Las dos ultimas instancias de este problema se encuentran en la carpeta data. 
## Instancia 1
## 5 Trabajos

| Trabajos |  M1  |  M2  |  M3  |  M4  |
| :---: | :---: | :---: | :---: | :---: |
| Trabajo 1 |  5  |  4  |  4  |  3  |
| Trabajo 2 |  5  |  4  |  4  |  6  |
| Trabajo 3 |  3  |  2  |  3  |  3  |
| Trabajo 4 |  6  |  4  |  4  |  2  |
| Trabajo 5 |  3  |  4  |  1  |  5  |

## Instancia 2
## 50 Trabajos
|Instancia 2|M1|M2|M3|M4|
| :---: | :---: | :---: | :---: | :---: |
|T1|269|428|249|135|
|T2|187|276|177|293|
|T3|356|263|253|218|
|T4|281|480|285|98|
|T...|...|...|...|...|
|T49|383|174|264|71|
|T50|8|121|194|296|

## Instancia 3
## 1000 tabajos

| Trabajos |  M1  |  M2  |  M3  |  M4  |
| :---: | :---: | :---: | :---: | :---: |
| Trabajo  1  |   3   |   14   |   11   |   1   |
| Trabajo  2  |   12   |   14   |   11   |   15   |
| Trabajo  3  |   8   |   9   |   14   |   8   |
| Trabajo  4  |   13   |   6   |   12   |   7   |
| Trabajo  5  |   12   |   12   |   2   |   6   |
| Trabajo  ... |   ...   |   ...   |   ...   |   ...   |
| Trabajo  1000  |   4   |   12   |   15   |   5   |


## Instancia 4
## 3000 tabajos

| Trabajos |  M1  |  M2  |  M3  |  M4  |   M5  |  M6  |  M7  |  M8  |   M9  |  M10  |  M11  |  M12  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Trabajo  1 |128|487|58|96|346|352|209|86|21|267|73|182|
| Trabajo  2 |272|175|306|112|243|465|182|209|356|482|347|175|
| Trabajo  3 |11|122|135|240|74|496|17|259|262|66|384|403|
| Trabajo  4 |36|153|177|11|363|99|2|251|231|84|370|214|
| Trabajo  ... |...|...|...|...|...|...|...|...|...|...|...|...|
| Trabajo  3000  |  79|372|48|281|52|137|91|280|358|204|350|282|



### La lectura de los datos se realiza con la siguiente función.
```python
data = pandas.read_csv('/content/Instancia2.csv', header=None)
intancia1 = np.array(data)

```
