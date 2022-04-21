# Flow-Shop-Scheduling
Es un problema combinacional en el que se necesita organizar el procesamiento de un conjunto de trabajos divididos en operaciones y cada operación se lleva a cabo en un recurso compartido.
En el FSS (Flow Shop Scheduling) se dan tiempos _Pkj_ para cada trabajo _j_ en cada máquina _k_ y una secuencia de trabajo _S=(s1,s2,...,sn)_ donde _n_ trabajos _(j = 1,2,...,n)_ serán procesados por _m_ máquinas _(k = 1,2,...,m)_ por lo que el objetivo de FSSP es encontrar un
orden de secuencia para el procesamiento de operaciones con el valor mínimo para el *_MakeSpan._*

El _*MakeSpan*_ para una organización de trabajo en particular se compone del total tiempo transcurrido desde el comienzo del primer trabajo hasta el término del último trabajo. El *_MakeSpan_* es por lo tanto un característica de todo el problema.

El FSSP se resume a determinar la permutación optima para minimizar el _MakeSpan_, es decir, minimizar la suma del tiempo en el que se completa cada trabajo. Con 2 máquinas, el problema se puede resolver en un tiempo _ø(nlogn)_ usando el algoritmo de _Johnson_, sin embargo, para más de 2 máquinas, el problema se convierte en _NP Hard_. 

# Datos del problema
_n:_  Número total de trabajos a programar

_m:_  Número de máquinas en el sistema

_Wj:_ Peso del trabajo _j_, _j = 1, 2,..., n_

_Pi,j:_  Tiempo de procesamiento del trabajo _j, j = 1, 2,..., n_, en la máquina _i, i = 1, 2,..., m_

_Ci,j:_  Tiempo de finalización del trabajo _j, j = 1, 2,..., n_, en la máquina _i, i = 1, 2,..., m_

_Cj:_  Tiempo de finalización del trabajo _j, j = 1, 2,..., n_, en la última máquina _( = C m,j)_

# Modelo
El problema de Flow Shop es generalmente entendido como un problema de permutaciones. El retraso entre el inicio de una tarea y otro es:

# Función Objetivo
max f(S,x) EL objetivo al solucionar el problema es disminuir el tiempo total de procesamiento desde el inicio de la tarea 1 del trabajo 1 hasta la tarea n del trabajo n.

![objFunction](https://user-images.githubusercontent.com/56168289/160326128-09805bfd-a54d-4067-9d44-83431d6d2835.png)

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

### La lectura de los datos se realiza con la siguiente función.
```python
data = pandas.read_csv('/content/Instancia2.csv', header=None)
intancia1 = np.array(data)

```
