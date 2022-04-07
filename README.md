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
|Trabajos|M1|M2|M3|
| :---: | :---: | :---: | :---: |
|T1|5|8|8|
|T2|10|15|5|
|T3|6|5|7|
|T4|8|7|9|

## Vector inicial propuesto 
Se genera un vector inicial de orden aleatorio 
|  |   |   |
| :---: | :---: | :---: |
|2|1|3|
## Ilustración de la solución optima 
![image](https://user-images.githubusercontent.com/93891210/162112069-e758b97f-e035-4961-8808-46f18bf2c857.png)


## Vector resultado 
Resultado optimo obtenido, minimizando el tiempo de procesamiento de los trabajos.
|  |   |   |
| :---: | :---: | :---: |
|1|3|2|

# Instancias
## Instancia 1
## 5 Trabajos

| Trabajos |  M1  |  M2  |  M3  |  M4  |
| :---: | :---: | :---: | :---: | :---: |
| Trabajo 1 |  5  |  4  |  4  |  3  |
| Trabajo 2 |  5  |  4  |  4  |  6  |
| Trabajo 3 |  3  |  2  |  3  |  3  |
| Trabajo 4 |  6  |  4  |  4  |  2  |
| Trabajo 5 |  3  |  4  |  1  |  5  |

## 50 Trabajos
|Instancia 2|M1|M2|M3|M4|
| :---: | :---: | :---: | :---: | :---: |
|T1|269|428|249|135|
|T2|187|276|177|293|
|T3|356|263|253|218|
|T4|281|480|285|98|
|T5|305|346|49|133|
|T6|274|27|104|254|
|T7|191|420|167|61|
|T8|352|333|201|110|
|T9|24|126|255|218|
|T10|135|205|105|67|
|T11|62|388|92|12|
|T12|228|120|130|173|
|T13|8|305|280|161|
|T14|218|227|63|101|
|T15|278|485|176|202|
|T16|253|362|277|212|
|T17|172|22|36|134|
|T18|164|534|226|250|
|T19|375|257|32|293|
|T20|206|137|247|19|
|T21|339|395|184|179|
|T22|356|461|50|120|
|T23|153|322|154|209|
|T24|65|349|300|189|
|T25|83|355|289|238|
|T26|4|293|132|93|
|T27|248|354|244|81|
|T28|376|265|158|125|
|T29|95|261|242|46|
|T30|93|517|199|188|
|T31|273|446|104|253|
|T32|6|182|26|73|
|T33|22|31|55|256|
|T34|328|115|143|304|
|T35|20|415|112|233|
|T36|372|492|268|96|
|T37|375|66|208|187|
|T38|253|487|324|102|
|T39|360|20|48|138|
|T40|196|278|40|33|
|T41|48|407|180|254|
|T42|328|537|318|36|
|T43|239|208|164|252|
|T44|152|198|124|41|
|T45|130|358|298|199|
|T46|12|165|238|97|
|T47|294|375|78|79|
|T48|34|249|264|194|
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
| Trabajo  6  |   2   |   7   |   2   |   6   |
| Trabajo  7  |   12   |   8   |   7   |   5   |
| Trabajo  8  |   8   |   7   |   1   |   8   |
| Trabajo  9  |   11   |   15   |   6   |   14   |
| Trabajo  10  |   12   |   12   |   13   |   9   |
| Trabajo  11  |   7   |   9   |   13   |   1   |
| Trabajo  12  |   7   |   11   |   3   |   5   |
| Trabajo  13  |   6   |   14   |   9   |   9   |
| Trabajo  14  |   4   |   6   |   3   |   6   |
| Trabajo  15  |   12   |   2   |   14   |   14   |
| Trabajo  16  |   3   |   13   |   2   |   3   |
| Trabajo  17  |   13   |   5   |   8   |   3   |
| Trabajo  18  |   14   |   12   |   13   |   1   |
| Trabajo  19  |   8   |   9   |   15   |   1   |
| Trabajo  20  |   4   |   2   |   5   |   10   |
| Trabajo  21  |   8   |   14   |   3   |   13   |
| Trabajo  22  |   9   |   13   |   4   |   2   |
| Trabajo  23  |   1   |   12   |   3   |   12   |
| Trabajo  24  |   2   |   13   |   3   |   1   |
| Trabajo  25  |   5   |   12   |   15   |   14   |
| Trabajo  26  |   14   |   4   |   11   |   3   |
| Trabajo  27  |   1   |   11   |   1   |   13   |
| Trabajo  28  |   11   |   5   |   13   |   4   |
| Trabajo  29  |   4   |   3   |   1   |   3   |
| Trabajo  30  |   11   |   3   |   8   |   4   |
| Trabajo  31  |   7   |   2   |   2   |   7   |
| Trabajo  32  |   11   |   2   |   15   |   11   |
| Trabajo  33  |   1   |   5   |   10   |   2   |
| Trabajo  34  |   11   |   9   |   5   |   13   |
| Trabajo  35  |   1   |   6   |   9   |   11   |
| Trabajo  36  |   11   |   3   |   9   |   10   |
| Trabajo  37  |   11   |   3   |   12   |   8   |
| Trabajo  38  |   13   |   10   |   7   |   4   |
| Trabajo  39  |   13   |   4   |   10   |   10   |
| Trabajo  40  |   13   |   15   |   5   |   6   |
| Trabajo  41  |   12   |   3   |   4   |   1   |
| Trabajo  42  |   6   |   4   |   13   |   10   |
| Trabajo  43  |   15   |   3   |   6   |   5   |
| Trabajo  44  |   2   |   6   |   14   |   6   |
| Trabajo  45  |   2   |   15   |   1   |   3   |
| Trabajo  46  |   1   |   12   |   9   |   2   |
| Trabajo  47  |   4   |   12   |   7   |   4   |
| Trabajo  48  |   9   |   9   |   14   |   12   |
| Trabajo  49  |   8   |   3   |   5   |   4   |
| Trabajo  50  |   8   |   8   |   5   |   14   |
| Trabajo  51  |   6   |   3   |   7   |   1   |
| Trabajo  52  |   13   |   14   |   5   |   9   |
| Trabajo  53  |   13   |   7   |   4   |   10   |
| Trabajo  54  |   9   |   15   |   12   |   6   |
| Trabajo  55  |   13   |   3   |   10   |   3   |
| Trabajo  56  |   6   |   6   |   8   |   10   |
| Trabajo  57  |   12   |   3   |   9   |   7   |
| Trabajo  58  |   1   |   2   |   3   |   4   |
| Trabajo  59  |   9   |   8   |   1   |   8   |
| Trabajo  60  |   5   |   15   |   1   |   7   |
| Trabajo  61  |   11   |   3   |   2   |   8   |
| Trabajo  62  |   7   |   7   |   2   |   2   |
| Trabajo  63  |   8   |   7   |   4   |   8   |
| Trabajo  64  |   7   |   2   |   11   |   12   |
| Trabajo  65  |   7   |   14   |   1   |   1   |
| Trabajo  66  |   1   |   2   |   9   |   6   |
| Trabajo  67  |   11   |   3   |   6   |   5   |
| Trabajo  68  |   3   |   5   |   11   |   15   |
| Trabajo  69  |   10   |   2   |   13   |   12   |
| Trabajo  70  |   12   |   8   |   1   |   13   |
| Trabajo  71  |   1   |   12   |   13   |   7   |
| Trabajo  72  |   7   |   13   |   12   |   14   |
| Trabajo  73  |   2   |   4   |   5   |   5   |
| Trabajo  74  |   1   |   2   |   4   |   4   |
| Trabajo  75  |   15   |   3   |   8   |   4   |
| Trabajo  76  |   9   |   13   |   9   |   10   |
| Trabajo  77  |   10   |   15   |   4   |   14   |
| Trabajo  78  |   3   |   9   |   11   |   6   |
| Trabajo  79  |   6   |   14   |   7   |   11   |
| Trabajo  80  |   6   |   13   |   9   |   9   |
| Trabajo  81  |   7   |   9   |   7   |   10   |
| Trabajo  82  |   7   |   6   |   10   |   15   |
| Trabajo  83  |   5   |   13   |   12   |   5   |
| Trabajo  84  |   4   |   7   |   14   |   5   |
| Trabajo  85  |   10   |   8   |   9   |   6   |
| Trabajo  86  |   3   |   15   |   10   |   13   |
| Trabajo  87  |   12   |   14   |   10   |   12   |
| Trabajo  88  |   5   |   3   |   2   |   10   |
| Trabajo  89  |   3   |   1   |   10   |   5   |
| Trabajo  90  |   13   |   12   |   6   |   11   |
| Trabajo  91  |   1   |   9   |   1   |   6   |
| Trabajo  92  |   5   |   3   |   2   |   14   |
| Trabajo  93  |   10   |   10   |   15   |   9   |
| Trabajo  94  |   6   |   15   |   2   |   11   |
| Trabajo  95  |   3   |   2   |   11   |   4   |
| Trabajo  96  |   6   |   13   |   3   |   14   |
| Trabajo  97  |   6   |   9   |   5   |   13   |
| Trabajo  98  |   10   |   1   |   12   |   8   |
| Trabajo  99  |   12   |   14   |   13   |   2   |
| Trabajo  100  |   10   |   14   |   2   |   1   |
| Trabajo  101  |   5   |   11   |   2   |   7   |
| Trabajo  102  |   3   |   7   |   10   |   8   |
| Trabajo  103  |   13   |   6   |   9   |   11   |
| Trabajo  104  |   6   |   12   |   8   |   12   |
| Trabajo  105  |   12   |   3   |   4   |   13   |
| Trabajo  106  |   1   |   3   |   3   |   4   |
| Trabajo  107  |   5   |   12   |   9   |   12   |
| Trabajo  108  |   6   |   8   |   2   |   5   |
| Trabajo  109  |   5   |   11   |   7   |   13   |
| Trabajo  110  |   1   |   5   |   7   |   13   |
| Trabajo  111  |   14   |   5   |   6   |   10   |
| Trabajo  112  |   1   |   1   |   5   |   9   |
| Trabajo  113  |   2   |   13   |   6   |   14   |
| Trabajo  114  |   2   |   4   |   8   |   1   |
| Trabajo  115  |   6   |   3   |   7   |   1   |
| Trabajo  116  |   11   |   3   |   7   |   4   |
| Trabajo  117  |   4   |   2   |   13   |   12   |
| Trabajo  118  |   11   |   5   |   10   |   12   |
| Trabajo  119  |   5   |   15   |   10   |   14   |
| Trabajo  120  |   1   |   3   |   2   |   3   |
| Trabajo  121  |   8   |   7   |   12   |   9   |
| Trabajo  122  |   3   |   1   |   15   |   5   |
| Trabajo  123  |   9   |   15   |   12   |   3   |
| Trabajo  124  |   4   |   11   |   15   |   2   |
| Trabajo  125  |   11   |   12   |   3   |   3   |
| Trabajo  126  |   9   |   6   |   8   |   11   |
| Trabajo  127  |   15   |   9   |   3   |   2   |
| Trabajo  128  |   4   |   11   |   10   |   6   |
| Trabajo  129  |   7   |   6   |   13   |   4   |
| Trabajo  130  |   14   |   13   |   11   |   15   |
| Trabajo  131  |   15   |   14   |   12   |   15   |
| Trabajo  132  |   1   |   7   |   3   |   11   |
| Trabajo  133  |   8   |   4   |   15   |   3   |
| Trabajo  134  |   8   |   13   |   15   |   7   |
| Trabajo  135  |   9   |   15   |   7   |   6   |
| Trabajo  136  |   6   |   1   |   1   |   12   |
| Trabajo  137  |   1   |   14   |   2   |   5   |
| Trabajo  138  |   15   |   2   |   3   |   4   |
| Trabajo  139  |   12   |   7   |   10   |   13   |
| Trabajo  140  |   2   |   3   |   3   |   4   |
| Trabajo  141  |   5   |   12   |   4   |   14   |
| Trabajo  142  |   9   |   5   |   3   |   6   |
| Trabajo  143  |   13   |   1   |   1   |   11   |
| Trabajo  144  |   10   |   5   |   11   |   15   |
| Trabajo  145  |   13   |   13   |   13   |   14   |
| Trabajo  146  |   4   |   3   |   6   |   6   |
| Trabajo  147  |   11   |   4   |   6   |   4   |
| Trabajo  148  |   3   |   1   |   9   |   15   |
| Trabajo  149  |   12   |   13   |   3   |   15   |
| Trabajo  150  |   12   |   3   |   3   |   11   |
| Trabajo  151  |   7   |   14   |   8   |   12   |
| Trabajo  152  |   9   |   12   |   12   |   10   |
| Trabajo  153  |   7   |   10   |   12   |   8   |
| Trabajo  154  |   1   |   3   |   11   |   2   |
| Trabajo  155  |   7   |   14   |   6   |   7   |
| Trabajo  156  |   15   |   10   |   9   |   1   |
| Trabajo  157  |   3   |   7   |   4   |   11   |
| Trabajo  158  |   2   |   6   |   11   |   14   |
| Trabajo  159  |   13   |   3   |   7   |   5   |
| Trabajo  160  |   1   |   5   |   9   |   4   |
| Trabajo  161  |   11   |   13   |   10   |   2   |
| Trabajo  162  |   3   |   11   |   1   |   11   |
| Trabajo  163  |   15   |   1   |   8   |   11   |
| Trabajo  164  |   1   |   4   |   15   |   9   |
| Trabajo  165  |   10   |   5   |   12   |   13   |
| Trabajo  166  |   5   |   15   |   8   |   8   |
| Trabajo  167  |   10   |   11   |   7   |   6   |
| Trabajo  168  |   1   |   9   |   14   |   6   |
| Trabajo  169  |   14   |   5   |   9   |   5   |
| Trabajo  170  |   1   |   8   |   13   |   3   |
| Trabajo  171  |   1   |   1   |   3   |   10   |
| Trabajo  172  |   6   |   15   |   13   |   13   |
| Trabajo  173  |   15   |   2   |   7   |   9   |
| Trabajo  174  |   12   |   9   |   8   |   6   |
| Trabajo  175  |   4   |   7   |   9   |   12   |
| Trabajo  176  |   9   |   6   |   7   |   5   |
| Trabajo  177  |   5   |   5   |   11   |   4   |
| Trabajo  178  |   9   |   12   |   4   |   12   |
| Trabajo  179  |   4   |   3   |   13   |   8   |
| Trabajo  180  |   12   |   6   |   12   |   9   |
| Trabajo  181  |   7   |   3   |   4   |   1   |
| Trabajo  182  |   10   |   7   |   6   |   13   |
| Trabajo  183  |   7   |   10   |   8   |   12   |
| Trabajo  184  |   5   |   11   |   6   |   11   |
| Trabajo  185  |   14   |   15   |   15   |   14   |
| Trabajo  186  |   8   |   14   |   7   |   6   |
| Trabajo  187  |   8   |   10   |   11   |   14   |
| Trabajo  188  |   4   |   6   |   4   |   3   |
| Trabajo  189  |   4   |   2   |   10   |   11   |
| Trabajo  190  |   7   |   6   |   15   |   7   |
| Trabajo  191  |   7   |   6   |   3   |   15   |
| Trabajo  192  |   14   |   4   |   5   |   13   |
| Trabajo  193  |   5   |   14   |   13   |   12   |
| Trabajo  194  |   7   |   7   |   9   |   9   |
| Trabajo  195  |   14   |   1   |   11   |   4   |
| Trabajo  196  |   5   |   2   |   9   |   5   |
| Trabajo  197  |   5   |   1   |   10   |   4   |
| Trabajo  198  |   8   |   9   |   7   |   12   |
| Trabajo  199  |   5   |   9   |   1   |   2   |
| Trabajo  200  |   15   |   14   |   5   |   12   |
| Trabajo  201  |   5   |   12   |   8   |   8   |
| Trabajo  202  |   11   |   4   |   13   |   8   |
| Trabajo  203  |   4   |   8   |   7   |   2   |
| Trabajo  204  |   2   |   4   |   9   |   4   |
| Trabajo  205  |   11   |   9   |   6   |   6   |
| Trabajo  206  |   12   |   2   |   3   |   13   |
| Trabajo  207  |   1   |   7   |   1   |   5   |
| Trabajo  208  |   8   |   12   |   14   |   12   |
| Trabajo  209  |   7   |   11   |   10   |   9   |
| Trabajo  210  |   6   |   10   |   8   |   14   |
| Trabajo  211  |   15   |   12   |   9   |   1   |
| Trabajo  212  |   11   |   11   |   10   |   11   |
| Trabajo  213  |   5   |   1   |   15   |   7   |
| Trabajo  214  |   2   |   8   |   3   |   4   |
| Trabajo  215  |   1   |   6   |   12   |   5   |
| Trabajo  216  |   13   |   7   |   5   |   13   |
| Trabajo  217  |   9   |   13   |   12   |   6   |
| Trabajo  218  |   8   |   8   |   12   |   9   |
| Trabajo  219  |   11   |   11   |   8   |   6   |
| Trabajo  220  |   15   |   5   |   13   |   13   |
| Trabajo  221  |   2   |   2   |   8   |   1   |
| Trabajo  222  |   13   |   7   |   12   |   2   |
| Trabajo  223  |   13   |   8   |   14   |   4   |
| Trabajo  224  |   3   |   6   |   8   |   12   |
| Trabajo  225  |   12   |   5   |   2   |   11   |
| Trabajo  226  |   6   |   12   |   13   |   14   |
| Trabajo  227  |   2   |   3   |   10   |   11   |
| Trabajo  228  |   13   |   10   |   6   |   3   |
| Trabajo  229  |   4   |   8   |   6   |   5   |
| Trabajo  230  |   1   |   15   |   7   |   3   |
| Trabajo  231  |   9   |   6   |   12   |   12   |
| Trabajo  232  |   2   |   14   |   1   |   4   |
| Trabajo  233  |   3   |   12   |   14   |   11   |
| Trabajo  234  |   15   |   11   |   1   |   8   |
| Trabajo  235  |   3   |   2   |   13   |   13   |
| Trabajo  236  |   12   |   3   |   11   |   5   |
| Trabajo  237  |   6   |   12   |   11   |   14   |
| Trabajo  238  |   2   |   1   |   1   |   14   |
| Trabajo  239  |   9   |   6   |   15   |   15   |
| Trabajo  240  |   10   |   1   |   11   |   15   |
| Trabajo  241  |   14   |   1   |   4   |   6   |
| Trabajo  242  |   7   |   11   |   3   |   15   |
| Trabajo  243  |   3   |   10   |   4   |   11   |
| Trabajo  244  |   15   |   15   |   13   |   12   |
| Trabajo  245  |   13   |   7   |   2   |   15   |
| Trabajo  246  |   3   |   2   |   7   |   3   |
| Trabajo  247  |   12   |   13   |   1   |   11   |
| Trabajo  248  |   13   |   13   |   12   |   5   |
| Trabajo  249  |   15   |   6   |   3   |   3   |
| Trabajo  250  |   8   |   14   |   10   |   12   |
| Trabajo  251  |   8   |   14   |   9   |   7   |
| Trabajo  252  |   15   |   13   |   12   |   7   |
| Trabajo  253  |   4   |   1   |   14   |   5   |
| Trabajo  254  |   5   |   11   |   11   |   5   |
| Trabajo  255  |   7   |   13   |   9   |   2   |
| Trabajo  256  |   11   |   11   |   5   |   1   |
| Trabajo  257  |   14   |   14   |   10   |   9   |
| Trabajo  258  |   9   |   13   |   8   |   11   |
| Trabajo  259  |   4   |   11   |   2   |   4   |
| Trabajo  260  |   8   |   5   |   4   |   2   |
| Trabajo  261  |   5   |   7   |   9   |   1   |
| Trabajo  262  |   3   |   5   |   4   |   3   |
| Trabajo  263  |   3   |   14   |   1   |   8   |
| Trabajo  264  |   4   |   15   |   15   |   12   |
| Trabajo  265  |   5   |   2   |   2   |   10   |
| Trabajo  266  |   2   |   8   |   13   |   15   |
| Trabajo  267  |   11   |   9   |   13   |   7   |
| Trabajo  268  |   9   |   3   |   3   |   6   |
| Trabajo  269  |   1   |   6   |   13   |   5   |
| Trabajo  270  |   2   |   7   |   6   |   7   |
| Trabajo  271  |   14   |   13   |   4   |   7   |
| Trabajo  272  |   9   |   13   |   12   |   9   |
| Trabajo  273  |   10   |   4   |   7   |   12   |
| Trabajo  274  |   5   |   14   |   11   |   10   |
| Trabajo  275  |   14   |   3   |   4   |   14   |
| Trabajo  276  |   3   |   8   |   11   |   14   |
| Trabajo  277  |   4   |   3   |   6   |   11   |
| Trabajo  278  |   14   |   1   |   12   |   13   |
| Trabajo  279  |   3   |   6   |   12   |   5   |
| Trabajo  280  |   8   |   7   |   7   |   10   |
| Trabajo  281  |   15   |   15   |   12   |   8   |
| Trabajo  282  |   13   |   15   |   2   |   10   |
| Trabajo  283  |   4   |   11   |   12   |   11   |
| Trabajo  284  |   9   |   12   |   15   |   10   |
| Trabajo  285  |   1   |   5   |   9   |   10   |
| Trabajo  286  |   15   |   12   |   4   |   3   |
| Trabajo  287  |   8   |   14   |   2   |   9   |
| Trabajo  288  |   10   |   6   |   14   |   5   |
| Trabajo  289  |   15   |   10   |   13   |   5   |
| Trabajo  290  |   13   |   8   |   4   |   6   |
| Trabajo  291  |   15   |   6   |   15   |   12   |
| Trabajo  292  |   12   |   11   |   9   |   5   |
| Trabajo  293  |   13   |   5   |   10   |   3   |
| Trabajo  294  |   9   |   5   |   9   |   7   |
| Trabajo  295  |   12   |   8   |   5   |   15   |
| Trabajo  296  |   11   |   1   |   10   |   12   |
| Trabajo  297  |   13   |   14   |   4   |   2   |
| Trabajo  298  |   12   |   3   |   2   |   11   |
| Trabajo  299  |   12   |   6   |   10   |   12   |
| Trabajo  300  |   2   |   11   |   11   |   3   |
| Trabajo  301  |   10   |   2   |   9   |   15   |
| Trabajo  302  |   4   |   1   |   5   |   3   |
| Trabajo  303  |   1   |   2   |   4   |   4   |
| Trabajo  304  |   6   |   12   |   1   |   5   |
| Trabajo  305  |   7   |   8   |   2   |   7   |
| Trabajo  306  |   13   |   10   |   12   |   15   |
| Trabajo  307  |   15   |   7   |   5   |   3   |
| Trabajo  308  |   1   |   10   |   1   |   8   |
| Trabajo  309  |   9   |   13   |   11   |   13   |
| Trabajo  310  |   2   |   10   |   15   |   14   |
| Trabajo  311  |   1   |   10   |   9   |   7   |
| Trabajo  312  |   5   |   4   |   15   |   7   |
| Trabajo  313  |   6   |   4   |   5   |   9   |
| Trabajo  314  |   3   |   5   |   11   |   1   |
| Trabajo  315  |   1   |   14   |   9   |   1   |
| Trabajo  316  |   1   |   7   |   15   |   9   |
| Trabajo  317  |   10   |   1   |   2   |   15   |
| Trabajo  318  |   8   |   3   |   13   |   5   |
| Trabajo  319  |   6   |   12   |   12   |   2   |
| Trabajo  320  |   12   |   2   |   8   |   8   |
| Trabajo  321  |   3   |   13   |   8   |   15   |
| Trabajo  322  |   7   |   15   |   2   |   14   |
| Trabajo  323  |   10   |   8   |   4   |   6   |
| Trabajo  324  |   5   |   14   |   10   |   8   |
| Trabajo  325  |   9   |   9   |   1   |   2   |
| Trabajo  326  |   12   |   14   |   11   |   10   |
| Trabajo  327  |   4   |   6   |   14   |   5   |
| Trabajo  328  |   7   |   13   |   9   |   1   |
| Trabajo  329  |   3   |   10   |   14   |   5   |
| Trabajo  330  |   10   |   3   |   3   |   9   |
| Trabajo  331  |   9   |   8   |   4   |   5   |
| Trabajo  332  |   10   |   7   |   14   |   1   |
| Trabajo  333  |   11   |   7   |   15   |   11   |
| Trabajo  334  |   8   |   10   |   8   |   9   |
| Trabajo  335  |   7   |   11   |   7   |   5   |
| Trabajo  336  |   7   |   11   |   7   |   12   |
| Trabajo  337  |   14   |   10   |   10   |   9   |
| Trabajo  338  |   10   |   12   |   3   |   6   |
| Trabajo  339  |   6   |   14   |   12   |   8   |
| Trabajo  340  |   4   |   7   |   2   |   5   |
| Trabajo  341  |   15   |   14   |   5   |   6   |
| Trabajo  342  |   6   |   11   |   9   |   15   |
| Trabajo  343  |   7   |   14   |   1   |   12   |
| Trabajo  344  |   8   |   1   |   11   |   2   |
| Trabajo  345  |   14   |   1   |   15   |   11   |
| Trabajo  346  |   2   |   15   |   9   |   11   |
| Trabajo  347  |   4   |   10   |   2   |   10   |
| Trabajo  348  |   2   |   8   |   4   |   1   |
| Trabajo  349  |   13   |   4   |   14   |   6   |
| Trabajo  350  |   10   |   6   |   5   |   9   |
| Trabajo  351  |   5   |   10   |   13   |   11   |
| Trabajo  352  |   13   |   8   |   10   |   14   |
| Trabajo  353  |   5   |   11   |   10   |   15   |
| Trabajo  354  |   11   |   4   |   10   |   12   |
| Trabajo  355  |   10   |   5   |   1   |   2   |
| Trabajo  356  |   11   |   14   |   9   |   5   |
| Trabajo  357  |   12   |   3   |   15   |   14   |
| Trabajo  358  |   7   |   12   |   7   |   11   |
| Trabajo  359  |   1   |   8   |   12   |   7   |
| Trabajo  360  |   7   |   4   |   12   |   12   |
| Trabajo  361  |   11   |   6   |   14   |   6   |
| Trabajo  362  |   7   |   11   |   2   |   7   |
| Trabajo  363  |   15   |   12   |   7   |   5   |
| Trabajo  364  |   1   |   10   |   12   |   4   |
| Trabajo  365  |   12   |   2   |   12   |   6   |
| Trabajo  366  |   9   |   2   |   6   |   4   |
| Trabajo  367  |   3   |   3   |   15   |   14   |
| Trabajo  368  |   9   |   6   |   13   |   1   |
| Trabajo  369  |   4   |   2   |   13   |   3   |
| Trabajo  370  |   3   |   7   |   14   |   14   |
| Trabajo  371  |   9   |   12   |   3   |   14   |
| Trabajo  372  |   11   |   9   |   15   |   10   |
| Trabajo  373  |   6   |   2   |   2   |   3   |
| Trabajo  374  |   7   |   3   |   8   |   8   |
| Trabajo  375  |   4   |   8   |   5   |   9   |
| Trabajo  376  |   10   |   6   |   14   |   11   |
| Trabajo  377  |   6   |   2   |   5   |   1   |
| Trabajo  378  |   8   |   3   |   14   |   13   |
| Trabajo  379  |   14   |   12   |   10   |   3   |
| Trabajo  380  |   7   |   3   |   14   |   12   |
| Trabajo  381  |   2   |   15   |   15   |   7   |
| Trabajo  382  |   9   |   15   |   11   |   4   |
| Trabajo  383  |   6   |   14   |   5   |   1   |
| Trabajo  384  |   10   |   8   |   9   |   3   |
| Trabajo  385  |   11   |   4   |   15   |   6   |
| Trabajo  386  |   3   |   8   |   12   |   7   |
| Trabajo  387  |   11   |   10   |   15   |   2   |
| Trabajo  388  |   11   |   5   |   11   |   9   |
| Trabajo  389  |   14   |   8   |   4   |   8   |
| Trabajo  390  |   10   |   1   |   9   |   2   |
| Trabajo  391  |   7   |   11   |   4   |   2   |
| Trabajo  392  |   1   |   3   |   2   |   14   |
| Trabajo  393  |   13   |   1   |   3   |   3   |
| Trabajo  394  |   7   |   11   |   14   |   2   |
| Trabajo  395  |   8   |   2   |   1   |   15   |
| Trabajo  396  |   4   |   11   |   3   |   11   |
| Trabajo  397  |   2   |   10   |   10   |   7   |
| Trabajo  398  |   4   |   3   |   12   |   10   |
| Trabajo  399  |   10   |   3   |   6   |   1   |
| Trabajo  400  |   10   |   1   |   1   |   13   |
| Trabajo  401  |   4   |   15   |   13   |   5   |
| Trabajo  402  |   10   |   12   |   11   |   12   |
| Trabajo  403  |   14   |   14   |   15   |   10   |
| Trabajo  404  |   14   |   1   |   11   |   9   |
| Trabajo  405  |   9   |   7   |   6   |   6   |
| Trabajo  406  |   8   |   11   |   5   |   12   |
| Trabajo  407  |   9   |   2   |   4   |   5   |
| Trabajo  408  |   15   |   8   |   6   |   14   |
| Trabajo  409  |   10   |   13   |   8   |   10   |
| Trabajo  410  |   1   |   13   |   8   |   1   |
| Trabajo  411  |   6   |   12   |   13   |   8   |
| Trabajo  412  |   14   |   15   |   6   |   13   |
| Trabajo  413  |   9   |   7   |   10   |   5   |
| Trabajo  414  |   1   |   4   |   1   |   15   |
| Trabajo  415  |   4   |   13   |   7   |   11   |
| Trabajo  416  |   3   |   13   |   11   |   4   |
| Trabajo  417  |   15   |   12   |   5   |   14   |
| Trabajo  418  |   2   |   9   |   12   |   4   |
| Trabajo  419  |   1   |   3   |   11   |   1   |
| Trabajo  420  |   9   |   9   |   13   |   6   |
| Trabajo  421  |   12   |   4   |   12   |   11   |
| Trabajo  422  |   3   |   8   |   3   |   3   |
| Trabajo  423  |   11   |   8   |   9   |   14   |
| Trabajo  424  |   14   |   6   |   7   |   12   |
| Trabajo  425  |   13   |   4   |   9   |   2   |
| Trabajo  426  |   12   |   7   |   4   |   11   |
| Trabajo  427  |   10   |   7   |   1   |   8   |
| Trabajo  428  |   12   |   12   |   9   |   5   |
| Trabajo  429  |   12   |   13   |   11   |   6   |
| Trabajo  430  |   8   |   1   |   3   |   8   |
| Trabajo  431  |   8   |   8   |   15   |   1   |
| Trabajo  432  |   5   |   11   |   6   |   9   |
| Trabajo  433  |   7   |   14   |   4   |   14   |
| Trabajo  434  |   1   |   4   |   15   |   14   |
| Trabajo  435  |   1   |   11   |   8   |   6   |
| Trabajo  436  |   14   |   6   |   7   |   5   |
| Trabajo  437  |   9   |   5   |   13   |   8   |
| Trabajo  438  |   15   |   14   |   12   |   3   |
| Trabajo  439  |   1   |   1   |   15   |   15   |
| Trabajo  440  |   1   |   12   |   14   |   7   |
| Trabajo  441  |   9   |   5   |   13   |   8   |
| Trabajo  442  |   6   |   15   |   15   |   1   |
| Trabajo  443  |   13   |   2   |   6   |   12   |
| Trabajo  444  |   15   |   15   |   8   |   1   |
| Trabajo  445  |   10   |   13   |   7   |   9   |
| Trabajo  446  |   12   |   15   |   15   |   9   |
| Trabajo  447  |   2   |   13   |   8   |   4   |
| Trabajo  448  |   14   |   6   |   8   |   12   |
| Trabajo  449  |   12   |   6   |   11   |   3   |
| Trabajo  450  |   4   |   3   |   12   |   15   |
| Trabajo  451  |   10   |   6   |   6   |   5   |
| Trabajo  452  |   12   |   1   |   9   |   4   |
| Trabajo  453  |   13   |   2   |   14   |   2   |
| Trabajo  454  |   7   |   14   |   10   |   3   |
| Trabajo  455  |   13   |   1   |   2   |   7   |
| Trabajo  456  |   1   |   1   |   5   |   11   |
| Trabajo  457  |   15   |   6   |   3   |   3   |
| Trabajo  458  |   12   |   9   |   9   |   15   |
| Trabajo  459  |   5   |   1   |   8   |   10   |
| Trabajo  460  |   1   |   7   |   9   |   7   |
| Trabajo  461  |   6   |   11   |   9   |   12   |
| Trabajo  462  |   11   |   3   |   8   |   6   |
| Trabajo  463  |   4   |   3   |   14   |   15   |
| Trabajo  464  |   14   |   13   |   14   |   14   |
| Trabajo  465  |   14   |   12   |   2   |   3   |
| Trabajo  466  |   5   |   4   |   15   |   15   |
| Trabajo  467  |   5   |   7   |   13   |   6   |
| Trabajo  468  |   4   |   1   |   14   |   14   |
| Trabajo  469  |   9   |   8   |   5   |   11   |
| Trabajo  470  |   14   |   15   |   15   |   1   |
| Trabajo  471  |   14   |   11   |   10   |   10   |
| Trabajo  472  |   12   |   8   |   8   |   12   |
| Trabajo  473  |   8   |   2   |   6   |   3   |
| Trabajo  474  |   2   |   2   |   3   |   12   |
| Trabajo  475  |   3   |   6   |   1   |   7   |
| Trabajo  476  |   2   |   1   |   8   |   5   |
| Trabajo  477  |   3   |   3   |   4   |   4   |
| Trabajo  478  |   13   |   10   |   12   |   3   |
| Trabajo  479  |   6   |   11   |   7   |   15   |
| Trabajo  480  |   13   |   2   |   5   |   3   |
| Trabajo  481  |   1   |   6   |   3   |   14   |
| Trabajo  482  |   7   |   13   |   7   |   5   |
| Trabajo  483  |   3   |   11   |   12   |   15   |
| Trabajo  484  |   2   |   11   |   10   |   15   |
| Trabajo  485  |   9   |   13   |   1   |   13   |
| Trabajo  486  |   5   |   9   |   5   |   6   |
| Trabajo  487  |   15   |   8   |   15   |   6   |
| Trabajo  488  |   7   |   5   |   5   |   11   |
| Trabajo  489  |   13   |   3   |   15   |   7   |
| Trabajo  490  |   7   |   11   |   4   |   1   |
| Trabajo  491  |   3   |   8   |   11   |   7   |
| Trabajo  492  |   7   |   3   |   6   |   4   |
| Trabajo  493  |   8   |   6   |   13   |   15   |
| Trabajo  494  |   9   |   3   |   4   |   4   |
| Trabajo  495  |   5   |   1   |   12   |   6   |
| Trabajo  496  |   4   |   14   |   7   |   10   |
| Trabajo  497  |   6   |   7   |   8   |   9   |
| Trabajo  498  |   8   |   2   |   6   |   13   |
| Trabajo  499  |   4   |   1   |   2   |   5   |
| Trabajo  500  |   6   |   6   |   13   |   14   |
| Trabajo  501  |   4   |   9   |   10   |   12   |
| Trabajo  502  |   3   |   2   |   15   |   9   |
| Trabajo  503  |   9   |   10   |   6   |   2   |
| Trabajo  504  |   10   |   13   |   1   |   8   |
| Trabajo  505  |   7   |   8   |   2   |   13   |
| Trabajo  506  |   3   |   5   |   8   |   7   |
| Trabajo  507  |   13   |   6   |   3   |   3   |
| Trabajo  508  |   7   |   6   |   12   |   8   |
| Trabajo  509  |   15   |   15   |   15   |   3   |
| Trabajo  510  |   6   |   6   |   10   |   5   |
| Trabajo  511  |   9   |   11   |   2   |   9   |
| Trabajo  512  |   4   |   11   |   6   |   3   |
| Trabajo  513  |   13   |   11   |   1   |   11   |
| Trabajo  514  |   13   |   13   |   6   |   6   |
| Trabajo  515  |   11   |   15   |   9   |   7   |
| Trabajo  516  |   14   |   8   |   9   |   4   |
| Trabajo  517  |   9   |   8   |   4   |   3   |
| Trabajo  518  |   4   |   15   |   1   |   8   |
| Trabajo  519  |   2   |   3   |   15   |   11   |
| Trabajo  520  |   15   |   6   |   12   |   10   |
| Trabajo  521  |   13   |   14   |   5   |   5   |
| Trabajo  522  |   9   |   2   |   6   |   5   |
| Trabajo  523  |   6   |   11   |   6   |   14   |
| Trabajo  524  |   13   |   12   |   14   |   14   |
| Trabajo  525  |   3   |   3   |   8   |   2   |
| Trabajo  526  |   4   |   7   |   15   |   6   |
| Trabajo  527  |   3   |   12   |   11   |   14   |
| Trabajo  528  |   4   |   12   |   10   |   15   |
| Trabajo  529  |   15   |   4   |   8   |   7   |
| Trabajo  530  |   15   |   10   |   7   |   4   |
| Trabajo  531  |   6   |   5   |   10   |   14   |
| Trabajo  532  |   11   |   5   |   9   |   2   |
| Trabajo  533  |   9   |   1   |   10   |   5   |
| Trabajo  534  |   8   |   6   |   3   |   12   |
| Trabajo  535  |   8   |   7   |   5   |   2   |
| Trabajo  536  |   2   |   6   |   10   |   6   |
| Trabajo  537  |   10   |   11   |   8   |   12   |
| Trabajo  538  |   11   |   7   |   11   |   4   |
| Trabajo  539  |   12   |   13   |   5   |   10   |
| Trabajo  540  |   5   |   4   |   13   |   6   |
| Trabajo  541  |   6   |   12   |   6   |   14   |
| Trabajo  542  |   15   |   11   |   3   |   9   |
| Trabajo  543  |   2   |   11   |   6   |   3   |
| Trabajo  544  |   13   |   10   |   10   |   5   |
| Trabajo  545  |   1   |   12   |   13   |   15   |
| Trabajo  546  |   14   |   4   |   12   |   9   |
| Trabajo  547  |   7   |   6   |   13   |   14   |
| Trabajo  548  |   11   |   11   |   8   |   10   |
| Trabajo  549  |   11   |   2   |   9   |   9   |
| Trabajo  550  |   11   |   3   |   13   |   4   |
| Trabajo  551  |   14   |   6   |   12   |   5   |
| Trabajo  552  |   1   |   4   |   9   |   2   |
| Trabajo  553  |   7   |   14   |   11   |   7   |
| Trabajo  554  |   6   |   9   |   3   |   13   |
| Trabajo  555  |   1   |   15   |   6   |   8   |
| Trabajo  556  |   1   |   2   |   12   |   12   |
| Trabajo  557  |   7   |   9   |   9   |   13   |
| Trabajo  558  |   8   |   14   |   5   |   3   |
| Trabajo  559  |   13   |   12   |   10   |   15   |
| Trabajo  560  |   14   |   11   |   3   |   1   |
| Trabajo  561  |   3   |   1   |   13   |   4   |
| Trabajo  562  |   6   |   5   |   7   |   4   |
| Trabajo  563  |   9   |   10   |   6   |   12   |
| Trabajo  564  |   6   |   14   |   13   |   12   |
| Trabajo  565  |   11   |   9   |   8   |   3   |
| Trabajo  566  |   1   |   13   |   13   |   8   |
| Trabajo  567  |   15   |   2   |   6   |   10   |
| Trabajo  568  |   7   |   10   |   12   |   15   |
| Trabajo  569  |   13   |   12   |   2   |   15   |
| Trabajo  570  |   15   |   8   |   12   |   14   |
| Trabajo  571  |   2   |   14   |   13   |   4   |
| Trabajo  572  |   1   |   12   |   1   |   13   |
| Trabajo  573  |   8   |   14   |   8   |   14   |
| Trabajo  574  |   4   |   4   |   3   |   14   |
| Trabajo  575  |   12   |   10   |   6   |   9   |
| Trabajo  576  |   15   |   8   |   10   |   6   |
| Trabajo  577  |   14   |   15   |   14   |   6   |
| Trabajo  578  |   13   |   10   |   1   |   12   |
| Trabajo  579  |   2   |   5   |   1   |   1   |
| Trabajo  580  |   3   |   8   |   4   |   12   |
| Trabajo  581  |   15   |   7   |   15   |   15   |
| Trabajo  582  |   4   |   2   |   14   |   11   |
| Trabajo  583  |   7   |   12   |   10   |   13   |
| Trabajo  584  |   12   |   3   |   9   |   15   |
| Trabajo  585  |   5   |   3   |   15   |   6   |
| Trabajo  586  |   15   |   13   |   2   |   4   |
| Trabajo  587  |   2   |   2   |   11   |   1   |
| Trabajo  588  |   12   |   8   |   3   |   13   |
| Trabajo  589  |   5   |   6   |   13   |   1   |
| Trabajo  590  |   4   |   5   |   1   |   5   |
| Trabajo  591  |   12   |   9   |   1   |   14   |
| Trabajo  592  |   4   |   2   |   9   |   1   |
| Trabajo  593  |   7   |   10   |   14   |   1   |
| Trabajo  594  |   7   |   6   |   5   |   6   |
| Trabajo  595  |   5   |   15   |   12   |   1   |
| Trabajo  596  |   10   |   8   |   15   |   4   |
| Trabajo  597  |   4   |   5   |   2   |   14   |
| Trabajo  598  |   11   |   12   |   10   |   8   |
| Trabajo  599  |   10   |   1   |   3   |   8   |
| Trabajo  600  |   3   |   12   |   12   |   14   |
| Trabajo  601  |   12   |   4   |   9   |   2   |
| Trabajo  602  |   12   |   13   |   8   |   4   |
| Trabajo  603  |   10   |   6   |   10   |   5   |
| Trabajo  604  |   1   |   7   |   7   |   7   |
| Trabajo  605  |   5   |   11   |   4   |   9   |
| Trabajo  606  |   10   |   1   |   14   |   5   |
| Trabajo  607  |   15   |   4   |   5   |   13   |
| Trabajo  608  |   1   |   3   |   2   |   6   |
| Trabajo  609  |   7   |   15   |   4   |   15   |
| Trabajo  610  |   14   |   6   |   14   |   10   |
| Trabajo  611  |   9   |   7   |   8   |   4   |
| Trabajo  612  |   5   |   10   |   9   |   9   |
| Trabajo  613  |   5   |   4   |   7   |   15   |
| Trabajo  614  |   14   |   11   |   8   |   3   |
| Trabajo  615  |   15   |   12   |   11   |   3   |
| Trabajo  616  |   4   |   10   |   12   |   7   |
| Trabajo  617  |   4   |   14   |   15   |   10   |
| Trabajo  618  |   9   |   7   |   5   |   9   |
| Trabajo  619  |   4   |   13   |   8   |   7   |
| Trabajo  620  |   4   |   15   |   4   |   5   |
| Trabajo  621  |   4   |   14   |   14   |   12   |
| Trabajo  622  |   6   |   7   |   2   |   4   |
| Trabajo  623  |   15   |   14   |   4   |   7   |
| Trabajo  624  |   9   |   2   |   11   |   13   |
| Trabajo  625  |   7   |   4   |   4   |   7   |
| Trabajo  626  |   13   |   12   |   4   |   6   |
| Trabajo  627  |   9   |   5   |   2   |   14   |
| Trabajo  628  |   4   |   2   |   11   |   4   |
| Trabajo  629  |   12   |   7   |   10   |   14   |
| Trabajo  630  |   15   |   6   |   5   |   1   |
| Trabajo  631  |   5   |   13   |   14   |   6   |
| Trabajo  632  |   2   |   4   |   15   |   9   |
| Trabajo  633  |   5   |   8   |   5   |   14   |
| Trabajo  634  |   12   |   15   |   3   |   15   |
| Trabajo  635  |   6   |   6   |   9   |   5   |
| Trabajo  636  |   11   |   14   |   11   |   15   |
| Trabajo  637  |   14   |   14   |   3   |   13   |
| Trabajo  638  |   12   |   2   |   15   |   1   |
| Trabajo  639  |   2   |   14   |   5   |   6   |
| Trabajo  640  |   7   |   10   |   13   |   2   |
| Trabajo  641  |   8   |   12   |   3   |   12   |
| Trabajo  642  |   9   |   7   |   9   |   1   |
| Trabajo  643  |   15   |   13   |   5   |   2   |
| Trabajo  644  |   10   |   10   |   10   |   12   |
| Trabajo  645  |   3   |   4   |   11   |   11   |
| Trabajo  646  |   13   |   4   |   4   |   7   |
| Trabajo  647  |   14   |   2   |   9   |   15   |
| Trabajo  648  |   15   |   12   |   6   |   9   |
| Trabajo  649  |   3   |   13   |   11   |   7   |
| Trabajo  650  |   5   |   10   |   7   |   1   |
| Trabajo  651  |   11   |   13   |   9   |   4   |
| Trabajo  652  |   8   |   5   |   5   |   3   |
| Trabajo  653  |   3   |   2   |   3   |   2   |
| Trabajo  654  |   2   |   7   |   4   |   15   |
| Trabajo  655  |   14   |   1   |   9   |   15   |
| Trabajo  656  |   9   |   8   |   4   |   4   |
| Trabajo  657  |   8   |   4   |   6   |   14   |
| Trabajo  658  |   8   |   7   |   6   |   9   |
| Trabajo  659  |   3   |   8   |   11   |   6   |
| Trabajo  660  |   8   |   4   |   14   |   4   |
| Trabajo  661  |   7   |   15   |   9   |   3   |
| Trabajo  662  |   15   |   1   |   9   |   7   |
| Trabajo  663  |   9   |   14   |   3   |   3   |
| Trabajo  664  |   4   |   6   |   4   |   1   |
| Trabajo  665  |   6   |   7   |   1   |   2   |
| Trabajo  666  |   5   |   9   |   5   |   3   |
| Trabajo  667  |   12   |   13   |   10   |   15   |
| Trabajo  668  |   10   |   12   |   8   |   7   |
| Trabajo  669  |   7   |   7   |   11   |   12   |
| Trabajo  670  |   14   |   5   |   10   |   8   |
| Trabajo  671  |   7   |   4   |   1   |   11   |
| Trabajo  672  |   9   |   3   |   13   |   1   |
| Trabajo  673  |   14   |   11   |   13   |   10   |
| Trabajo  674  |   13   |   12   |   12   |   9   |
| Trabajo  675  |   3   |   10   |   11   |   2   |
| Trabajo  676  |   5   |   2   |   6   |   15   |
| Trabajo  677  |   13   |   11   |   8   |   15   |
| Trabajo  678  |   14   |   12   |   14   |   8   |
| Trabajo  679  |   3   |   14   |   3   |   10   |
| Trabajo  680  |   12   |   9   |   1   |   4   |
| Trabajo  681  |   4   |   14   |   3   |   4   |
| Trabajo  682  |   13   |   15   |   6   |   4   |
| Trabajo  683  |   12   |   5   |   13   |   11   |
| Trabajo  684  |   3   |   10   |   8   |   15   |
| Trabajo  685  |   9   |   5   |   8   |   1   |
| Trabajo  686  |   13   |   10   |   8   |   11   |
| Trabajo  687  |   14   |   6   |   5   |   14   |
| Trabajo  688  |   1   |   7   |   5   |   5   |
| Trabajo  689  |   3   |   14   |   2   |   14   |
| Trabajo  690  |   10   |   5   |   3   |   2   |
| Trabajo  691  |   15   |   9   |   11   |   10   |
| Trabajo  692  |   6   |   7   |   6   |   1   |
| Trabajo  693  |   4   |   8   |   11   |   2   |
| Trabajo  694  |   2   |   3   |   7   |   5   |
| Trabajo  695  |   4   |   10   |   5   |   2   |
| Trabajo  696  |   4   |   14   |   11   |   3   |
| Trabajo  697  |   6   |   15   |   4   |   12   |
| Trabajo  698  |   9   |   12   |   10   |   5   |
| Trabajo  699  |   5   |   10   |   1   |   14   |
| Trabajo  700  |   9   |   10   |   7   |   6   |
| Trabajo  701  |   5   |   11   |   5   |   7   |
| Trabajo  702  |   13   |   15   |   1   |   5   |
| Trabajo  703  |   6   |   4   |   9   |   2   |
| Trabajo  704  |   2   |   4   |   2   |   7   |
| Trabajo  705  |   1   |   7   |   13   |   7   |
| Trabajo  706  |   2   |   11   |   4   |   10   |
| Trabajo  707  |   11   |   7   |   4   |   8   |
| Trabajo  708  |   4   |   14   |   15   |   7   |
| Trabajo  709  |   7   |   8   |   15   |   13   |
| Trabajo  710  |   3   |   5   |   13   |   4   |
| Trabajo  711  |   1   |   5   |   1   |   4   |
| Trabajo  712  |   1   |   6   |   9   |   7   |
| Trabajo  713  |   12   |   6   |   6   |   6   |
| Trabajo  714  |   5   |   1   |   3   |   4   |
| Trabajo  715  |   1   |   12   |   10   |   13   |
| Trabajo  716  |   8   |   8   |   13   |   12   |
| Trabajo  717  |   11   |   15   |   15   |   1   |
| Trabajo  718  |   12   |   10   |   5   |   14   |
| Trabajo  719  |   14   |   5   |   2   |   8   |
| Trabajo  720  |   13   |   7   |   3   |   10   |
| Trabajo  721  |   11   |   6   |   11   |   11   |
| Trabajo  722  |   1   |   13   |   9   |   1   |
| Trabajo  723  |   2   |   10   |   4   |   12   |
| Trabajo  724  |   11   |   11   |   10   |   13   |
| Trabajo  725  |   2   |   10   |   12   |   8   |
| Trabajo  726  |   6   |   8   |   3   |   3   |
| Trabajo  727  |   15   |   15   |   6   |   7   |
| Trabajo  728  |   11   |   2   |   1   |   14   |
| Trabajo  729  |   10   |   1   |   10   |   14   |
| Trabajo  730  |   12   |   2   |   7   |   6   |
| Trabajo  731  |   6   |   4   |   11   |   9   |
| Trabajo  732  |   5   |   1   |   13   |   6   |
| Trabajo  733  |   12   |   6   |   4   |   12   |
| Trabajo  734  |   7   |   2   |   6   |   1   |
| Trabajo  735  |   6   |   3   |   14   |   2   |
| Trabajo  736  |   9   |   5   |   10   |   7   |
| Trabajo  737  |   8   |   2   |   4   |   7   |
| Trabajo  738  |   14   |   4   |   11   |   10   |
| Trabajo  739  |   1   |   3   |   11   |   1   |
| Trabajo  740  |   7   |   10   |   10   |   1   |
| Trabajo  741  |   8   |   2   |   7   |   11   |
| Trabajo  742  |   9   |   5   |   13   |   9   |
| Trabajo  743  |   2   |   10   |   15   |   1   |
| Trabajo  744  |   4   |   3   |   12   |   3   |
| Trabajo  745  |   15   |   14   |   10   |   3   |
| Trabajo  746  |   13   |   13   |   1   |   8   |
| Trabajo  747  |   11   |   11   |   5   |   10   |
| Trabajo  748  |   6   |   5   |   4   |   5   |
| Trabajo  749  |   12   |   11   |   6   |   4   |
| Trabajo  750  |   15   |   5   |   14   |   7   |
| Trabajo  751  |   2   |   10   |   11   |   12   |
| Trabajo  752  |   8   |   14   |   14   |   9   |
| Trabajo  753  |   5   |   6   |   15   |   9   |
| Trabajo  754  |   14   |   8   |   1   |   4   |
| Trabajo  755  |   10   |   4   |   2   |   11   |
| Trabajo  756  |   12   |   13   |   9   |   10   |
| Trabajo  757  |   11   |   15   |   4   |   8   |
| Trabajo  758  |   2   |   8   |   13   |   12   |
| Trabajo  759  |   6   |   10   |   8   |   2   |
| Trabajo  760  |   9   |   5   |   5   |   15   |
| Trabajo  761  |   3   |   1   |   14   |   14   |
| Trabajo  762  |   10   |   4   |   14   |   8   |
| Trabajo  763  |   3   |   3   |   6   |   8   |
| Trabajo  764  |   13   |   6   |   3   |   13   |
| Trabajo  765  |   12   |   13   |   12   |   6   |
| Trabajo  766  |   12   |   14   |   12   |   9   |
| Trabajo  767  |   11   |   3   |   4   |   3   |
| Trabajo  768  |   14   |   3   |   1   |   9   |
| Trabajo  769  |   13   |   13   |   1   |   7   |
| Trabajo  770  |   2   |   12   |   15   |   4   |
| Trabajo  771  |   4   |   6   |   14   |   14   |
| Trabajo  772  |   12   |   14   |   10   |   8   |
| Trabajo  773  |   8   |   1   |   11   |   15   |
| Trabajo  774  |   12   |   15   |   10   |   14   |
| Trabajo  775  |   12   |   9   |   14   |   7   |
| Trabajo  776  |   7   |   12   |   8   |   10   |
| Trabajo  777  |   14   |   1   |   5   |   5   |
| Trabajo  778  |   1   |   8   |   6   |   2   |
| Trabajo  779  |   8   |   5   |   12   |   1   |
| Trabajo  780  |   2   |   7   |   7   |   13   |
| Trabajo  781  |   14   |   4   |   5   |   12   |
| Trabajo  782  |   6   |   12   |   3   |   7   |
| Trabajo  783  |   8   |   3   |   9   |   3   |
| Trabajo  784  |   1   |   11   |   14   |   8   |
| Trabajo  785  |   12   |   8   |   7   |   11   |
| Trabajo  786  |   4   |   8   |   12   |   13   |
| Trabajo  787  |   6   |   9   |   15   |   10   |
| Trabajo  788  |   15   |   7   |   10   |   15   |
| Trabajo  789  |   9   |   7   |   15   |   1   |
| Trabajo  790  |   9   |   3   |   10   |   1   |
| Trabajo  791  |   4   |   9   |   8   |   3   |
| Trabajo  792  |   14   |   6   |   1   |   6   |
| Trabajo  793  |   9   |   5   |   6   |   4   |
| Trabajo  794  |   11   |   10   |   4   |   1   |
| Trabajo  795  |   6   |   6   |   13   |   11   |
| Trabajo  796  |   7   |   12   |   2   |   14   |
| Trabajo  797  |   4   |   11   |   5   |   11   |
| Trabajo  798  |   10   |   3   |   8   |   11   |
| Trabajo  799  |   14   |   12   |   9   |   3   |
| Trabajo  800  |   5   |   15   |   13   |   1   |
| Trabajo  801  |   3   |   2   |   11   |   9   |
| Trabajo  802  |   13   |   5   |   3   |   9   |
| Trabajo  803  |   14   |   13   |   7   |   13   |
| Trabajo  804  |   12   |   4   |   6   |   9   |
| Trabajo  805  |   5   |   8   |   2   |   10   |
| Trabajo  806  |   6   |   8   |   10   |   6   |
| Trabajo  807  |   10   |   6   |   4   |   3   |
| Trabajo  808  |   11   |   12   |   6   |   10   |
| Trabajo  809  |   10   |   12   |   13   |   15   |
| Trabajo  810  |   5   |   6   |   3   |   10   |
| Trabajo  811  |   15   |   10   |   6   |   13   |
| Trabajo  812  |   6   |   8   |   14   |   11   |
| Trabajo  813  |   9   |   13   |   9   |   13   |
| Trabajo  814  |   14   |   6   |   10   |   3   |
| Trabajo  815  |   14   |   6   |   8   |   12   |
| Trabajo  816  |   11   |   4   |   13   |   15   |
| Trabajo  817  |   10   |   13   |   4   |   7   |
| Trabajo  818  |   3   |   5   |   11   |   12   |
| Trabajo  819  |   4   |   4   |   14   |   1   |
| Trabajo  820  |   2   |   10   |   4   |   12   |
| Trabajo  821  |   15   |   4   |   13   |   12   |
| Trabajo  822  |   2   |   1   |   12   |   11   |
| Trabajo  823  |   1   |   15   |   13   |   10   |
| Trabajo  824  |   14   |   7   |   3   |   15   |
| Trabajo  825  |   9   |   8   |   1   |   8   |
| Trabajo  826  |   6   |   5   |   7   |   15   |
| Trabajo  827  |   12   |   12   |   6   |   7   |
| Trabajo  828  |   8   |   5   |   2   |   9   |
| Trabajo  829  |   8   |   1   |   9   |   10   |
| Trabajo  830  |   10   |   15   |   15   |   2   |
| Trabajo  831  |   7   |   5   |   8   |   2   |
| Trabajo  832  |   10   |   11   |   11   |   2   |
| Trabajo  833  |   10   |   10   |   8   |   3   |
| Trabajo  834  |   7   |   3   |   12   |   5   |
| Trabajo  835  |   6   |   4   |   7   |   15   |
| Trabajo  836  |   4   |   2   |   12   |   8   |
| Trabajo  837  |   15   |   12   |   7   |   4   |
| Trabajo  838  |   8   |   6   |   11   |   5   |
| Trabajo  839  |   11   |   5   |   4   |   6   |
| Trabajo  840  |   13   |   10   |   4   |   2   |
| Trabajo  841  |   4   |   12   |   15   |   5   |
| Trabajo  842  |   2   |   12   |   10   |   11   |
| Trabajo  843  |   15   |   12   |   7   |   5   |
| Trabajo  844  |   2   |   15   |   4   |   8   |
| Trabajo  845  |   13   |   11   |   9   |   13   |
| Trabajo  846  |   10   |   6   |   15   |   8   |
| Trabajo  847  |   8   |   4   |   2   |   11   |
| Trabajo  848  |   7   |   5   |   1   |   5   |
| Trabajo  849  |   9   |   14   |   14   |   1   |
| Trabajo  850  |   12   |   2   |   3   |   8   |
| Trabajo  851  |   8   |   8   |   11   |   7   |
| Trabajo  852  |   12   |   1   |   4   |   7   |
| Trabajo  853  |   14   |   2   |   1   |   10   |
| Trabajo  854  |   8   |   15   |   12   |   3   |
| Trabajo  855  |   14   |   10   |   8   |   3   |
| Trabajo  856  |   10   |   4   |   12   |   4   |
| Trabajo  857  |   5   |   1   |   5   |   6   |
| Trabajo  858  |   6   |   1   |   3   |   4   |
| Trabajo  859  |   6   |   15   |   11   |   15   |
| Trabajo  860  |   13   |   6   |   9   |   12   |
| Trabajo  861  |   5   |   12   |   12   |   6   |
| Trabajo  862  |   15   |   4   |   9   |   3   |
| Trabajo  863  |   4   |   2   |   4   |   4   |
| Trabajo  864  |   2   |   1   |   1   |   6   |
| Trabajo  865  |   13   |   12   |   14   |   12   |
| Trabajo  866  |   6   |   3   |   14   |   8   |
| Trabajo  867  |   7   |   10   |   2   |   6   |
| Trabajo  868  |   12   |   3   |   12   |   9   |
| Trabajo  869  |   7   |   3   |   9   |   8   |
| Trabajo  870  |   15   |   8   |   8   |   7   |
| Trabajo  871  |   2   |   11   |   12   |   8   |
| Trabajo  872  |   10   |   12   |   10   |   2   |
| Trabajo  873  |   13   |   4   |   14   |   3   |
| Trabajo  874  |   13   |   9   |   15   |   6   |
| Trabajo  875  |   1   |   13   |   6   |   12   |
| Trabajo  876  |   13   |   9   |   14   |   5   |
| Trabajo  877  |   7   |   2   |   6   |   13   |
| Trabajo  878  |   13   |   9   |   4   |   11   |
| Trabajo  879  |   4   |   10   |   13   |   10   |
| Trabajo  880  |   14   |   2   |   13   |   5   |
| Trabajo  881  |   7   |   10   |   9   |   2   |
| Trabajo  882  |   2   |   4   |   9   |   4   |
| Trabajo  883  |   13   |   8   |   4   |   9   |
| Trabajo  884  |   3   |   10   |   4   |   1   |
| Trabajo  885  |   3   |   12   |   13   |   7   |
| Trabajo  886  |   9   |   5   |   9   |   6   |
| Trabajo  887  |   5   |   2   |   3   |   14   |
| Trabajo  888  |   10   |   15   |   2   |   15   |
| Trabajo  889  |   15   |   6   |   12   |   6   |
| Trabajo  890  |   11   |   6   |   2   |   2   |
| Trabajo  891  |   15   |   4   |   13   |   10   |
| Trabajo  892  |   10   |   14   |   3   |   7   |
| Trabajo  893  |   15   |   11   |   15   |   2   |
| Trabajo  894  |   13   |   8   |   1   |   8   |
| Trabajo  895  |   3   |   6   |   12   |   3   |
| Trabajo  896  |   14   |   7   |   4   |   10   |
| Trabajo  897  |   10   |   11   |   9   |   3   |
| Trabajo  898  |   4   |   9   |   12   |   15   |
| Trabajo  899  |   10   |   6   |   9   |   13   |
| Trabajo  900  |   13   |   11   |   5   |   2   |
| Trabajo  901  |   10   |   11   |   2   |   11   |
| Trabajo  902  |   6   |   13   |   1   |   3   |
| Trabajo  903  |   11   |   9   |   8   |   15   |
| Trabajo  904  |   4   |   13   |   5   |   8   |
| Trabajo  905  |   10   |   8   |   10   |   5   |
| Trabajo  906  |   12   |   8   |   8   |   5   |
| Trabajo  907  |   10   |   11   |   6   |   6   |
| Trabajo  908  |   9   |   13   |   15   |   15   |
| Trabajo  909  |   1   |   7   |   5   |   4   |
| Trabajo  910  |   2   |   3   |   9   |   15   |
| Trabajo  911  |   12   |   2   |   7   |   10   |
| Trabajo  912  |   9   |   8   |   12   |   6   |
| Trabajo  913  |   8   |   3   |   2   |   8   |
| Trabajo  914  |   9   |   3   |   4   |   4   |
| Trabajo  915  |   5   |   8   |   4   |   7   |
| Trabajo  916  |   1   |   14   |   2   |   15   |
| Trabajo  917  |   2   |   14   |   6   |   4   |
| Trabajo  918  |   13   |   14   |   10   |   2   |
| Trabajo  919  |   15   |   4   |   14   |   10   |
| Trabajo  920  |   2   |   15   |   7   |   7   |
| Trabajo  921  |   9   |   14   |   1   |   11   |
| Trabajo  922  |   11   |   12   |   10   |   8   |
| Trabajo  923  |   12   |   3   |   13   |   11   |
| Trabajo  924  |   5   |   4   |   10   |   3   |
| Trabajo  925  |   12   |   5   |   6   |   15   |
| Trabajo  926  |   4   |   9   |   15   |   9   |
| Trabajo  927  |   10   |   12   |   15   |   7   |
| Trabajo  928  |   14   |   3   |   5   |   15   |
| Trabajo  929  |   4   |   9   |   9   |   2   |
| Trabajo  930  |   11   |   7   |   12   |   3   |
| Trabajo  931  |   9   |   7   |   1   |   8   |
| Trabajo  932  |   7   |   3   |   1   |   11   |
| Trabajo  933  |   14   |   6   |   13   |   4   |
| Trabajo  934  |   13   |   15   |   15   |   10   |
| Trabajo  935  |   3   |   15   |   12   |   8   |
| Trabajo  936  |   5   |   9   |   3   |   1   |
| Trabajo  937  |   1   |   1   |   11   |   7   |
| Trabajo  938  |   8   |   1   |   8   |   4   |
| Trabajo  939  |   1   |   6   |   13   |   1   |
| Trabajo  940  |   15   |   13   |   5   |   12   |
| Trabajo  941  |   7   |   3   |   14   |   6   |
| Trabajo  942  |   11   |   6   |   10   |   4   |
| Trabajo  943  |   12   |   14   |   4   |   10   |
| Trabajo  944  |   15   |   10   |   3   |   15   |
| Trabajo  945  |   6   |   6   |   3   |   8   |
| Trabajo  946  |   1   |   2   |   2   |   15   |
| Trabajo  947  |   15   |   4   |   11   |   12   |
| Trabajo  948  |   13   |   11   |   11   |   1   |
| Trabajo  949  |   11   |   2   |   2   |   7   |
| Trabajo  950  |   15   |   6   |   1   |   9   |
| Trabajo  951  |   4   |   10   |   2   |   2   |
| Trabajo  952  |   6   |   8   |   5   |   9   |
| Trabajo  953  |   9   |   10   |   6   |   1   |
| Trabajo  954  |   12   |   13   |   2   |   8   |
| Trabajo  955  |   13   |   11   |   11   |   5   |
| Trabajo  956  |   7   |   3   |   13   |   9   |
| Trabajo  957  |   1   |   14   |   3   |   3   |
| Trabajo  958  |   5   |   10   |   3   |   1   |
| Trabajo  959  |   13   |   6   |   14   |   15   |
| Trabajo  960  |   11   |   14   |   1   |   10   |
| Trabajo  961  |   8   |   13   |   14   |   7   |
| Trabajo  962  |   3   |   1   |   10   |   7   |
| Trabajo  963  |   12   |   7   |   15   |   13   |
| Trabajo  964  |   12   |   4   |   2   |   12   |
| Trabajo  965  |   11   |   9   |   3   |   8   |
| Trabajo  966  |   5   |   15   |   7   |   4   |
| Trabajo  967  |   11   |   7   |   15   |   13   |
| Trabajo  968  |   3   |   6   |   4   |   11   |
| Trabajo  969  |   9   |   10   |   12   |   1   |
| Trabajo  970  |   4   |   13   |   10   |   7   |
| Trabajo  971  |   11   |   10   |   12   |   9   |
| Trabajo  972  |   1   |   15   |   6   |   5   |
| Trabajo  973  |   9   |   10   |   5   |   1   |
| Trabajo  974  |   14   |   4   |   5   |   15   |
| Trabajo  975  |   15   |   15   |   12   |   12   |
| Trabajo  976  |   6   |   8   |   14   |   11   |
| Trabajo  977  |   15   |   2   |   1   |   15   |
| Trabajo  978  |   10   |   2   |   9   |   5   |
| Trabajo  979  |   6   |   5   |   14   |   1   |
| Trabajo  980  |   9   |   8   |   6   |   13   |
| Trabajo  981  |   9   |   3   |   12   |   2   |
| Trabajo  982  |   10   |   7   |   14   |   8   |
| Trabajo  983  |   6   |   15   |   8   |   4   |
| Trabajo  984  |   7   |   1   |   13   |   13   |
| Trabajo  985  |   2   |   13   |   14   |   13   |
| Trabajo  986  |   1   |   7   |   3   |   3   |
| Trabajo  987  |   5   |   13   |   15   |   13   |
| Trabajo  988  |   8   |   15   |   15   |   15   |
| Trabajo  989  |   11   |   13   |   12   |   7   |
| Trabajo  990  |   6   |   1   |   13   |   11   |
| Trabajo  991  |   4   |   7   |   4   |   5   |
| Trabajo  992  |   6   |   7   |   8   |   5   |
| Trabajo  993  |   13   |   9   |   2   |   4   |
| Trabajo  994  |   8   |   3   |   4   |   7   |
| Trabajo  995  |   7   |   11   |   1   |   12   |
| Trabajo  996  |   7   |   3   |   2   |   6   |
| Trabajo  997  |   13   |   10   |   10   |   14   |
| Trabajo  998  |   9   |   4   |   1   |   2   |
| Trabajo  999  |   3   |   11   |   14   |   4   |
| Trabajo  1000  |   4   |   12   |   15   |   5   |
