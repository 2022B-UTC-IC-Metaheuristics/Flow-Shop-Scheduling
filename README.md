# Flow-Shop-Scheduling

## Definición del problema
El problema de Flow-Shop-Scheduling (FSS) es un desafío de optimización en el ámbito de la gestión de operaciones y la planificación de la producción. En este problema, se trata de determinar el orden de procesamiento óptimo para un conjunto de trabajos en una serie de máquinas, conocidas como etapas o estaciones, de tal manera que se minimice el tiempo total de finalización de todos los trabajos. Cada trabajo debe pasar por todas las máquinas en el mismo orden, y una vez que comienza su procesamiento en una máquina, no puede interrumpirse hasta su finalización.

El objetivo del FSS es encontrar una secuencia de trabajos que minimice el tiempo total necesario para completar todos los trabajos, conocido como el tiempo de flujo total. Esto implica optimizar el tiempo de finalización del último trabajo, lo que a menudo se denomina como la métrica $MakeSpan$. El FSS es un problema NP-duro, lo que significa que no se conoce un algoritmo que pueda resolverlo en tiempo polinomial para todas las instancias del problema, por lo que generalmente se utilizan enfoques heurísticos y algoritmos de búsqueda para encontrar soluciones aproximadas en un tiempo razonable.

Con 2 máquinas, el problema se puede resolver en un tiempo _ø(nlogn)_ usando el algoritmo de _Johnson_, sin embargo, para más de 2 máquinas, el problema se convierte en _NP Hard_. 

# Datos del problema
$n$ :  Número total de trabajos

$m$ :  Número de máquinas

$W_j$ Peso del trabajo $j$, $j = 1, 2,..., n$

# Variables

$P_{ij}$ : Tiempo de procesamiento. Indica el tiempo requerido para procesar el trabajo $i$ en la máquina $j$.

$S_{ikj}$ : Tiempo de configuración de un trabajo $i$ a un trabajo $k$ en la máquina $j$ ($i = 0$ se refiere al tiempo de configuración inicial del trabajo programado).

$C_{i,j}$ : Tiempo de finalización del trabajo $i$ en la máquina $j$.

$X_{ik}$ : Si el trabajo $i$ es procesado antes que el trabajo $k$, es igual a $1$; se otra forma, es igual a $0$.


# Modelo
El problema de Flow Shop es generalmente entendido como un problema de permutaciones.

# Función Objetivo
El objetivo del problema es disminuir el tiempo total de procesamiento desde el inicio de la tarea 1 del trabajo 1 hasta la tarea n del trabajo n.

$Minimize \sum_{j=1}^{n} w_j C_j^2$

# Restricciones
Garantizar que todos los trabajos han sido asignados y que el tiempo de completado del trabajo $i$ en la máquina $1$ es al menos tan grande como el tiempo de procesamiento de ese trabajo en la máquina:

$p_{i1} \geq  c_{i1}; i=1,...,n. (1)$

El trabajo $j$ no puede empezar en la máquina $j$ a menos que haya finalizado en la máquina $j-1$. La restricción 2 garantiza que el tiempo de completado del trabajo $i$ en la máquina $j$ debe ser al menos tan grande ocmo el tiempo de procesamiendo en la máquina $j$, uno más grande que el tiempo de completado en la máquina $j-1$.

$p_{i1} + c_i [j-1] \geq c_{ij}, i=1,...,n; j=1,...,m. (2)$

Las restricciones 3 y 4 aseguran que solo hay una restricción para cada secuencia de trabajos. Este caso muestra la relación entre la precedencia y latencia entre trabajos.

$c_{ij} - c_{kj} + Mx_{ik} \geq s_{kij} + p_{ij} (3)$

$c_{ij} - c_{kj} + M[1 - x_{ik}] \geq s_{kij} + p_{ij} (4)$

donde $k \gt i \geq 1$ y $i=1,...,n;k=1,...,n; j=1,...,m. $
También, $M$ es un número muy grande.

Las restricciones 5 y 6 garantizan que solo un trabajo puede ser seguido de otro trabajo en cada planificación:

$\sum_{i=1}^{n} x_{ik}=1; k = 1,2,...,n$ para $i \ne k,(5)$

$\sum_{k=1}^{n} x_{ik}; k = 1,2,...,n$ para $i \ne k.(6)$

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


# Generar la primera solución
```python
def create_first_solution(self):
return np.random.permutation(self.num_tasks)
```
# Generación de solución Vecina

```python
		
def create_neighbor_solution(self, solution):
        neighbor = solution.copy()
        swap1 = np.random.randint(len(solution))
        swap2 = 0
        while(1):
            swap2 = np.random.randint(len(solution))
            if swap1 != swap2: break
        copy = neighbor[swap1]
        neighbor[swap1] = neighbor[swap2]
        neighbor[swap2] = copy
        return neighbor
		
```

# Función de Costo

```python
def makespan(self, matrix, solution):
        # Ordenar la matriz de acuerdo a la solución
        processing_times = [matrix[i] for i in solution]
        n_jobs = len(matrix)
        n_machines = len(matrix[0])
        completion_times = np.zeros((n_jobs, n_machines))
        job_order = np.zeros((n_jobs, n_machines), dtype=np.int32)
        start_times = np.zeros(n_machines)
        for i in range(n_jobs):
            for j in range(n_machines):
                # Si es la primera máquina, empieza en el tiempo 0
                if j == 0:
                    start_times[j] = completion_times[i-1, j] if i > 0 else 0
                else:
                    start_times[j] = max(completion_times[i, j-1], completion_times[i-1, j])
                # Actualiza el tiempo de completado y el orden de trabajo para el trabajo en la máquina actual
                completion_times[i, j] = start_times[j] + processing_times[i][j]
                job_order[i, j] = i
        last_machine_times = completion_times[:, -1]
        job_order = job_order[np.argsort(last_machine_times)]
        return completion_times[-1, -1]
```

# Instancias
## Instancia 1
## 11 Trabajos



| Trabajos |  M1  |  M2  |  M3  |  M4  |  M5  |
| :---: | :---: | :---: | :---: | :---: |:---: |
| Trabajo 1 |  375  |  12  |  142  |  245   | 412  |
| Trabajo 2 |  632  |  452  |  758  |  278  | 398  |
| Trabajo 3 |  12   |  876  |  124  |  534  | 765  |
| Trabajo 4 |  460  |  542  |  523  |  120  | 499  |
| Trabajo 5 |  528  |  101  |  789  |  124  | 999  |
| Trabajo 6 |  796  |  245  |  632  |  375  | 123  |
| Trabajo 7 |  532  |  230  |  543  |  896  | 452  |
| Trabajo 8 |  14   |  124  |  214  |  543  | 785  |
| Trabajo 9 |  257  |  527  |  753  |  210  | 463  |
| Trabajo 10 |  896  |  896  |  214  |  358  | 259  |
| Trabajo 11 |  532  |  302  |  501  |  765  | 988  |



## Instancia 2
## 13 Trabajos

  | Trabajos |  M1  |  M2  |  M3  |  M4  |
| :---: | :---: | :---: | :---: | :---: |
|Trabajo|654|147|345|447|
|Trabajo|321|520|789|702|
|Trabajo| 12|147|630|255|
|Trabajo|345|586|214|866|
|Trabajo|678|532|275|332|
|Trabajo|963|145|302|225|
|Trabajo| 25| 24|142|589|
|Trabajo|874|517| 24|996|
|Trabajo|114|896|520|541|
|Trabajo|785|543|336|234|
|Trabajo|203|210|699|784|
|Trabajo|696|784|855|512|
|Trabajo|302|512|221|345|

## Instancia 3
## Reeves 30x10 type C instance
|Trabajos |  M1  |  M2  |  M3  |  M4  |   M5  |  M6  |  M7  |  M8  |   M9  |  M10  |
| :---:|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |   :---:  |  :---:  |  :---:  |  :---:  |  :---: |
  | Trabajo | 54  |  2  |  2  | 75  | 39  | 97  | 70  |  5  | 40  | 16|
  | Trabajo | 51  | 69  | 31  |100  | 25  | 58  | 30  |  3  | 18  | 64|
  | Trabajo | 44  | 18  |  6  |  6  |  9  | 96  | 52  | 31  | 52  | 14|
  | Trabajo | 66  | 95  | 42  |  1  | 21  | 65  | 24  | 78  | 20  | 81|
  | Trabajo | 18  | 53  | 28  | 61  | 84  | 52  | 33  | 31  | 14  | 35|
  | Trabajo | 100 |  39 |  72 |  19 |  44 |  66 |   8 |  59 |  80 | 94|
  | Trabajo | 51  | 86  | 28  | 56  | 13  | 22  | 51  | 99  | 51  |  8|
  | Trabajo | 88  | 95  | 45  | 83  |  5  | 30  | 81  | 49  | 86  | 46|
  | Trabajo | 41  | 24  | 93  | 33  | 70  | 84  | 66  | 50  | 11  | 87|
  | Trabajo | 92  | 78  |  9  | 47  | 39  | 48  | 65  | 79  | 49  |  4|
  | Trabajo | 12  | 95  | 32  | 60  | 53  | 44  | 63  | 28  | 66  | 53|
  | Trabajo | 98  | 31  | 39  | 91  |  7  | 38  | 10  |  2  |  4  | 60|
  | Trabajo | 11  | 53  | 83  | 29  | 85  | 31  | 55  |100  | 16  | 10|
  | Trabajo | 16  | 22  | 32  | 21  | 96  | 42  | 88  |100  | 12  | 31|
  | Trabajo | 13  | 80  |  5  | 57  | 15  | 99  | 76  | 56  | 85  | 87|
  | Trabajo | 83  | 41  | 11  | 64  | 16  | 26  | 98  | 77  | 59  | 60|
  | Trabajo | 17  | 78  | 85  | 87  | 16  | 29  | 88  | 16  | 20  | 41|
  | Trabajo | 59  |  8  | 26  | 77  |  4  | 84  | 64  | 62  | 56  | 14|
  | Trabajo | 44  | 79  | 34  | 85  | 86  | 25  | 76  | 21  | 94  | 49|
  | Trabajo | 31  | 63  | 50  | 39  | 20  | 32  | 34  |  9  | 39  | 85|
  | Trabajo | 44  | 37  | 88  | 43  | 50  | 17  | 52  | 38  |  8  | 17|
  | Trabajo |  9  | 74  | 81  | 55  | 50  | 13  | 82  |100  | 69  | 89|
  | Trabajo | 90  | 31  |  8  | 79  | 55  | 59  | 52  | 59  | 83  | 75|
  | Trabajo | 29  | 33  | 42  | 54  |  5  | 93  |  5  | 38  | 32  | 70|
  | Trabajo | 81  | 66  | 79  | 36  | 75  | 32  | 36  |  2  | 68  | 77|
  | Trabajo | 53  | 58  | 82  | 91  | 21  | 65  | 28  | 53  | 39  | 95|
  | Trabajo | 40  | 72  | 13  | 79  |  9  | 39  | 90  |  9  | 37  |  3|
  | Trabajo | 66  | 90  | 75  | 45  | 59  | 46  | 98  | 99  | 26  | 55|
  | Trabajo | 16  |  3  | 46  |  2  | 79  | 11  | 26  | 47  | 88  | 58|
  | Trabajo | 78  | 97  | 19  | 22  |  5  | 79  | 90  | 57  | 54  | 68|
## Instancia 4
## Reeves 75x20 type C instance  


|Trabajos |  M1  |  M2  |  M3  |  M4  |   M5  |  M6  |  M7  |  M8  |   M9  |  M10  |  M11  |  M12  | M13  |  M14  |   M15  |  M16  |  M17  |  M18  |   M19  |  M20|
| :---:|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |   :---:  |  :---:  |  :---:  |  :---:  |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---:|   :---: |  :---: |  :---: |  :---: |
  |Trabajo |  88  |  49  |  15  |  75  |  21  |   6  |  79  |  74  |  45  |  63 |  20 |  18 |  13 |  64 |   3 |  13 |   1 |  80 |  15 |  93 |
  |Trabajo |  50  |  16  |  58  |  11  |  21  |  82  |  23  |  33  |   2  |  95 |  19 |  36 |  18 |  76 |  87 |   1 |  21 |  71 |  89 |  36 |
  |Trabajo |  49  |  45  |  92  |  46  |  99  |   1  |   9  |  37  |  99  |  79 |  38 |  68 |  53 |  73 |  92 |  98 |  86 |   3 |  11 |  10 |
  |Trabajo |  66  |  95  |  36  |  29  |   8  | 100  |  32  |   8  |  68  |  25 |  44 |  14 |  23 |  40 |  61 |  80 |  74 |  40 |  98 |  63 |
  |Trabajo |   6  |  54  |  31  |  33  |  28  |  40  |   7  |  96  |  62  |  70 |  29 |  97 |  57 |  88 |  61 |  43 |  91 |  65 |  92 |  68 |
  |Trabajo |  97  |  31  |  45  |  56  |  65  |   7  |  78  |  74  |  61  |  74 |  11 |  65 |  11 |  54 |  85 |  13 |  67 |  90 |  62 |  24 |
  |Trabajo |  95  |  63  |  69  |  23  |  47  |  11  |  10  |  40  |  70  |  24 |  32 |  92 |  63 |  98 |  48 |  36 |  55 |  51 |  98 |  55 |
  |Trabajo |  80  |  11  |  21  |  82  |  30  |  89  |  97  |  18  |  18  |  31 |  59 |  76 |  20 |   6 |  94 |  86 |  36 |  10 |  18 |   8 |
  |Trabajo |  55  |  61  |  42  |   5  |  93  |   1  |  56  |  57  |  61  |  29 |  84 |  40 |   9 |  89 |  90 |  63 |  15 |  51 |  65 |  57 |
  |Trabajo |  52  |  23  |   2  |  91  |  41  |  34  |  28  |  29  |  77  |  81 |  24 |  34 |  86 |  83 |  28 |  88 |  20 |  86 |   5 |   1 |
  |Trabajo |  24  |  33  |  90  |  65  |   4  |  98  |  81  |  33  |  73  |  72 |  22 |  29 |  32 |  49 |  25 |  12 |   8 |  51 |  30 |  63 |
  |Trabajo |  51  |  53  |  25  |  73  |  36  |  29  |   8  |  93  |  76  |  13 |  44 |  26 |  49 |  73 |  23 |   7 |  56 |   7 |  59 |  92 |
  |Trabajo |  38  |  69  |  49  |  91  |  16  |  89  |  25  |  57  |  43  |  40 |  83 |  47 |  69 |  66 |  90 |  71 |  71 |  39 |  32 |  61 |
  |Trabajo |  15  |  91  |  29  |  15  |  51  |  63  |  74  |  98  |  52  |  14 |  57 |  41 |  45 |  64 |  17 |  28 |  82 |  59 |  18 |  67 |
  |Trabajo |  35  |  55  |  57  |  70  |  68  |  61  |  23  |  15  |   8  |  20 |   7 |  81 |  58 |  27 |  22 |  27 |  43 |   2 |   8 |  36 |
  |Trabajo |  80  |  22  |  50  |   5  |  24  |  21  |  64  |  31  |  42  |  71 | 100 |  66 |  11 |  42 |  47 |  41 |  34 |  30 |  20 |  15 |
  |Trabajo |  54  |  78  |  51  |  91  |  97  |   3  |  14  |  95  |   7  |   2 |  28 |  19 |  36 |  20 |  59 |  69 |  60 |  28 |  95 |  78 |
  |Trabajo |  85  |  35  |  27  |  28  |  93  |  93  |  15  |  81  |  84  |  73 |  10 |  88 |  86 |  96 |  51 |  33 |  51 |   8 |   2 |  23 |
  |Trabajo |  30  |  28  |  69  |  40  |  40  |   1  |  35  |  86  |  77  |  71 |  87 |  47 |  41 |  32 |  39 |  82 |  60 |   5 |  31 |  73 |
  |Trabajo |  67  |  17  |  96  |  75  |  95  |  64  |  65  |  34  |  16  |   6 |  26 |  95 |   7 |  13 |  66 |  90 |  69 |  80 |   1 |  77 |
  |Trabajo |   2  |  90  |  49  |   5  |  36  |  43  |  23  |  73  |  55  |  15 |  19 |  54 |  11 |  50 |  99 |  55 |  82 |  19 |  53 |   9 |
  |Trabajo |  64  |  56  |  95  |  31  |  68  |  24  |  51  |  78  |  74  |  59 |  84 |  74 |  10 |  80 |  30 |   1 |  27 |  34 |  56 |  67 |
  |Trabajo |   7  |  52  |  27  |  74  |  20  |  17  |  17  |  46  |  78  |  23 |  62 |  27 |  83 |  63 |  77 |  75 |  61 |  59 | 100 |  74 |
  |Trabajo |  12  |  39  |  61  |  84  |  49  |  59  |  12  | 100  |  97  |  18 |  22 |  12 |  35 |  85 |  81 |  53 |  62 |  57 |   3 |  79 |
  |Trabajo |  83  |   3  |  41  |  34  |  32  |  11  |  53  |  90  |  85  |  80 |  54 |  53 |  94 |  57 |   9 |  31 |  36 |  12 |   7 |  55 |
  |Trabajo |  50  |  54  |  33  |  22  |  75  |  57  |  83  |  89  |  22  |  71 |  77 |  98 |  17 |  16 |  55 |  33 |  12 |  36 |  80 | 100 |
  |Trabajo |  67  |  28  |  30  |  72  |   8  |  10  |  69  |  95  |  13  |  76 |  33 |  21 |  83 |  21 |  35 |   8 |  45 |  65 |  13 |  39 |
  |Trabajo |  15  |  87  |  47  |  32  |  85  |   6  |   4  |  31  |  87  |   6 |  88 |  19 |  95 |  59 |  91 |  29 |  13 |  60 |  25 |  19 |
  |Trabajo |  97  |  17  |  29  |  76  |  86  |   4  |   3  |  46  |  98  |  97 |  35 |  17 |  85 |  41 |  90 |  95 |  24 |   6 |  56 |  14 |
  |Trabajo |  44  |  28  |  42  |   2  |  16  |  92  |  10  |  14  |  28  |  10 |  92 |  62 |   7 |   3 |  25 |  29 |   4 |  15 |  74 |  23 |
  |Trabajo |  10  |  56  |  78  |  34  |   4  |  80  |  92  |  33  |  80  |  31 |  99 |  29 |  40 |   5 |  13 |  80 |  11 |  22 |  72 |  68 |
  |Trabajo |  75  |  62  |  54  |  19  |   5  |   4  |  41  |  26  |  84  |  71 |  25 |  15 |  89 |  34 |  96 |  20 |  22 |  89 |  67 |  99 |
  |Trabajo |  44  |  33  |  12  |  32  |  98  |  25  |  73  |  41  |  94  |  66 |  62 |  44 |  84 |   1 |  41 |  49 |  44 |   2 | 100 |  88 |
  |Trabajo |  46  |  79  |  21  |  71  |  89  |  28  |  33  |  53  |  91  |  76 |  26 |  65 |  79 |  41 |  40 |  89 |   5 |  70 |  39 |  34 |
  |Trabajo |  36  |  35  |  71  |  60  |   7  |  26  |  85  |  60  |  80  |  88 |  60 |  51 |  55 |  16 |  11 |  90 |  60 |  31 |  77 |  61 |
  |Trabajo |  93  |  64  |  80  |  46  |   7  |  53  |  23  |  84  |  89  |  12 |  32 | 100 |  16 |  11 |  96 |  25 |  89 |  46 |  29 |  17 |
  |Trabajo |  23  |  51  |  91  |   3  |  68  |  71  |  64  |  76  |  73  |  85 |  33 |  36 |  91 |  38 |  62 |  92 |  97 |  99 |  40 |  76 |
  |Trabajo |  55  |   6  |  70  |  30  |  95  |  66  |  50  |   7  |  13  |  68 |  81 |   7 |  35 |  32 |   1 |  14 |  13 |   2 |  75 |  35 |
  |Trabajo |  44  |  66  |  10  |  50  |  18  |  49  |  48  |  76  |  12  |  46 |  17 |  87 |  28 |  54 |  30 |  40 |  92 |  92 |  26 |  18 |
  |Trabajo |  69  |  92  |  27  |  11  |  92  |  55  |  51  |   7  |   1  |  30 |  10 |  74 |  75 |  90 |  92 |  44 |  14 |  28 |  12 |  75 |
  |Trabajo |  36  |  70  |  65  |  87  |  96  |  45  |  75  |  49  |  35  |  57 |  50 |  92 |   5 |  51 |  53 |  23 |  83 |  98 |  75 |  77 |
  |Trabajo |  73  |  10  |  90  |  77  |  34  |   6  |  63  |  74  |  92  |  87 |  56 |  88 |  73 |  73 |   7 |   2 |  29 |  11 |  80 |  24 |
  |Trabajo |  35  |  49  |  94  |   4  |  37  |  48  |  82  |  81  |  78  |   6 |  69 |  37 |  59 |  18 |  69 |  29 |   7 |   4 |  21 |  40 |
  |Trabajo |   3  |  47  |  95  |  15  |  60  |   7  |  24  |  94  |  22  |  25 |  57 |  37 |  67 |  70 |  83 |  77 |  96 |  38 |  16 |  71 |
  |Trabajo |  81  |  90  |  34  |  86  |  81  |  45  |   7  |  61  |  79  |  80 |  12 |  11 |  27 |  41 |  15 |  44 |   1 |  98 |   5 |  93 |
  |Trabajo |  98  |  90  |  80  |  14  |   6  |  47  |  71  |  55  |  29  |  32 |  51 |   8 |  94 |  67 |  58 |  55 |  52 |  96 |  56 |   3 |
  |Trabajo |  10  |  83  |  23  |  22  |  64  |  24  |  86  |  76  |  76  |  67 |  17 |   1 |  47 |   8 |  29 |  57 |   4 |  68 |  62 |  25 |
  |Trabajo |  95  |  28  |  82  |  59  |  10  |  12  |  43  |  45  |  50  |  96 |  75 |  89 |  92 |  52 |  69 |  24 |  36 |  74 |  39 |   7 |
  |Trabajo |  59  |  13  |  99  |  99  |  24  |  71  |  58  |  12  |   6  |  55 |  20 |  95 |  57 |   7 |  47 |  54 |  53 | 100 |  30 |  23 |
  |Trabajo |  31  |  47  |  40  |  39  |  10  |  89  |  75  |  51  |  24  |   4 |  67 |  67 |  98 |  12 |  55 |  71 |  84 |  58 |   2 |  71 |
  |Trabajo |  66  |  68  |  98  |   4  |  99  |  76  |  60  |  59  |   7  |  30 |  59 |  80 |  94 |  25 |   9 |  24 |  84 |  83 |  47 |  74 |
  |Trabajo |  44  |  36  |  90  |  42  |  44  |  67  |   6  |  60  |  87  |  44 |  64 |  30 |  49 |  35 |  51 |  85 |  34 |  36 |  83 |  82 |
  |Trabajo |  70  |  36  |  59  |  25  |  25  |  25  |  30  |   3  |  16  |  81 |  73 |  43 |  95 |  50 |  50 |  53 |  37 |   4 |  51 |  67 |
  |Trabajo |  72  |  81  |  70  |  54  |  48  |  33  |  74  |  60  |  76  |   2 |   3 |  66 |  84 |   8 |  97 |  52 |  23 |  96 |  19 |  28 |
  |Trabajo |   6  |   5  |  18  |  50  |  41  |   5  |   5  |  31  |  71  |  94 |  97 |  72 |  98 |  69 |   9 |  30 |  48 |  50 |  78 |  88 |
  |Trabajo |  52  |  70  |  18  |  63  |  60  |  75  |  15  |  39  |  31  |  68 |  22 |  61 |  40 |  19 |  28 |  60 |  90 |  25 |  47 |  96 |
  |Trabajo |  13  |  62  |  14  |  66  |  84  |   4  |  22  |  32  |   9  |  58 |  71 |  55 |  40 |  70 |  22 |  41 |  54 |   9 |  67 |  25 |
  |Trabajo |  21  |  91  |  71  |  57  |  18  |  79  |  68  |  84  |  87  |  27 |  59 |   3 |  54 |  56 |  84 |  97 |  70 |  11 |   5 |  74 |
  |Trabajo |  29  |  94  |  83  |  61  |  91  |  10  |  20  |  93  |  68  |  60 |  30 |  78 |  60 |  39 |  29 |  75 |  94 |  68 |  55 |  65 |
  |Trabajo |  17  |  31  |  67  |  24  |  59  |  34  |  70  |  82  |  82  |  69 |  51 |  80 |  63 |   6 |   1 |  49 |   3 |  41 |  31 |  49 |
  |Trabajo |  90  |  89  |  64  |  21  |   1  |  10  |  35  |   1  |  85  |  88 |  14 |  31 |  94 |  66 |  66 |  18 |   4 |  15 |  78 |  97 |
  |Trabajo |  77  |  78  |  42  |  50  |  21  |  26  |  58  |  22  |  55  |  79 |  36 |  79 |   6 |  56 |  16 |   6 |  25 |   2 |  63 |   9 |
  |Trabajo |  34  |  34  |  94  |  35  |  50  |  92  |   5  |  43  |  98  |  28 |  59 |  99 |  80 |  36 |  70 |  59 |  22 |  38 |  76 |   7 |
  |Trabajo |  40  |  19  |  36  |  24  |  41  |  44  |  69  |  90  |  42  |  46 |  51 |  88 |  19 |  94 |  68 |  53 |  75 |  83 |  36 |  41 |
  |Trabajo |  99  |  17  |  10  |  90  |  75  |  43  |  68  |   8  |  43  |  69 |   3 |  71 |  55 |  38 |  79 |  85 |  87 |  23 |  85 |  83 |
  |Trabajo |  42  |  41  |  84  |  32  |  57  |  75  |  43  |  73  |  81  |  57 |  33 |  95 |  41 |   7 |  94 |  78 |  88 |  70 |  90 |  33 |
  |Trabajo |  22  |  26  |  50  |  73  |  15  |  51  |  61  |  83  |  60  |  97 |  83 |  33 |  57 |  60 |  31 |  82 |  34 |  59 |  43 |  13 |
  |Trabajo |  20  |  33  |  25  |  63  |   6  |   6  |  14  |  61  |  10  | 100 |  20 |  86 |   8 |  83 |  31 |  70 |   4 |  52 |  61 |  72 |
  |Trabajo |  41  |  47  |  51  |  73  |   8  |   3  |  21  |  55  |  85  |   1 |  37 |  75 |  24 |  88 |  63 |  40 |   2 |  33 |  87 |  83 |
  |Trabajo |  14  |  81  |  96  |   3  |  25  |  25  |  23  |  39  |  65  |  62 |  50 |  49 |  59 |  10 |  17 |  15 |  59 |  15 |  88 |  46 |
  |Trabajo |  93  |  69  |  51  |  76  |  89  |  86  |  86  |  12  |  55  |  68 |   2 |  82 |  93 |  10 |  12 |  45 |  28 |  32 |  55 |  82 |
  |Trabajo |  59  |  73  |  34  |  40  |  53  |  20  |   5  |  96  |  85  |  30 |  60 |  72 |  30 |  74 |  89 |   1 |  91 |  47 |   7 |  42 |
  |Trabajo |  16  |  79  |  87  |  70  |  98  |  88  |  95  |  41  |   9  |  85 |  16 |  43 |   1 |  13 |  17 |  84 |  50 |  44 |  85 |  97 |
  |Trabajo |  94  |  97  |  78  |  63  |  27  |  77  |  98  |  19  |   7  |  93 |  88 |  43 |  59 |  64 |  86 |  16 |  37 |  36 |  56 |  48 |
  |Trabajo |  47  |  64  |  98  |  43  |  71  |  98  |  83  |  30  |  83  |  40 |  17 |  45 |  86 |  86 |  14 |  46 |   6 |  57 |  13 |  16 |


### La lectura de los datos se realiza con la siguiente función.
```python
def read_cost_matrix_from_csv(self, filename):
        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            cost_matrix = [list(map(int, row)) for row in reader]
            self.num_tasks = len(cost_matrix)
            self.num_machines = len(cost_matrix[0])
        return cost_matrix

```

### Implementación.
```python
from SAnnealingFlowShop import SAnnealingFlowShop
import matplotlib.pyplot as plt
import time
from tabulate import tabulate

sa = SAnnealingFlowShop()
cost_matrix = sa.read_cost_matrix_from_csv('C:\\Users\\jairo\\Documents\\UTM\\Decimo\\Metaheurística\\RECOCIDO_SIMULADO_COP\\prueba.csv')
best_solution, best_cost, elapsed_time, iterations, final_temperature = sa.fit(cost_matrix)
best_solution = [task + 1 for task in best_solution]
elapsed_time_formatted = f"{time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}:{str(elapsed_time - int(elapsed_time))[2:5]}"
data = []
data.append([iterations, best_solution, best_cost, elapsed_time_formatted, final_temperature])
headers = ["Iteraciones", "Mejor Solución", "Costo", "Tiempo", "Temperatura Final"]
print(tabulate(data, headers=headers, tablefmt="grid"))

```
