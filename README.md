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

# Solución inicial

_Aleatoria_

 |  |  |  |  |
 | :---: | :---: | :---: | :---: |
 | 3 | 1 | 4 | 2 |
 
 # Solución Vecina
 
 _Intercambio de orden de trabajos_
 
 Inicial:
 
 |  |  |  |  |
 | :---: | :---: | :---: | :---: |
 | 3 | 1 | 4 | 2 |
 
 Vecina:
 
 |  |  |  |  |
 | :---: | :---: | :---: | :---: |
 | 2 | 1 | 4 | 3 |

# Aplicaciones

Su aplicación es amplia:

  → para programar el despacho de vuelos en aeropuertos
  
  → programar líneas de producción en un fábrica
  
  → programación de cirugías
  
  → reparación de equipos o maquinarias de un taller

# Ejemplo

| Trabajos |  M1  |  M2  |  M3  |  M4  |
| :---: | :---: | :---: | :---: | :---: |
| Trabajo 1 |  5  |  4  |  4  |  3  |
| Trabajo 2 |  5  |  4  |  4  |  6  |
| Trabajo 3 |  3  |  2  |  3  |  3  |
| Trabajo 4 |  6  |  4  |  4  |  2  |
| Trabajo 5 |  3  |  4  |  1  |  5  |

 ![EjemploFSS](https://user-images.githubusercontent.com/56168289/160938652-5fa3ea8b-89a2-4a4b-abee-2bdf0da8e2dd.png)

# Instancias
2

5

10
