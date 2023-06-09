# PythonConObjetos
Este repositorio corresponde al proyecto de Javier Sánchez y Julio Gutiérrez para la materia de Diseño de compiladores.

## Primer avance (léxico y sintaxis)
Realizamos el léxico y la sintaxis de nuestro lenguaje. Decidimos tomar como base la tarea del lenguaje patito y la adaptamos a los requerimientos del proyecto. Nos enfocamos principalmente en agregar la funcionalidad de un lenguaje orientado a objetos para que nuestra sintaxis pueda leer las clases. Hasta el momento, todas nuestras pruebas han sido exitosas y el proyecto funciona como se esperaba.

## Segundo avance (semántica básica de variables y cubo semántico)
Comenzamos a trabajar en el cubo semántico, aunque tenemos dudas de si es necesario declarar variables de tipo booleano en el léxico para poder hacer uso de los operadores && y ||. También tenemos la duda de si podemos regresar un string cuando haya un error de type mismatch. Para el directorio de procedimientos, solamente creamos una plantilla en donde se crean las tablas y las pilas vacías. Ya están declaradas, pero no tienen funcionamiento alguno.

## Tercer avance (semántica, generación de código de expresiones y estatutos lineales)
Modificamos el cubo semántico para que haga uso de números enteros en lugar de strings para los tipos, operadores y errores. Esta mejora permite un manejo más sencillo del cubo que con el uso de strings. También completamos la tabla de variables con sus métodos para declarar las variables y sus valores, además de poder buscar las variables por ID y cuál es su tipo. Nos queda pendiente terminar el directorio de procedimientos y el uso de los cuádruplos.

## Cuarto avance (generación de código de estatutos condicionales y cíclicos)
Creamos las clases que teníamos pendientes del directorio de funciones, el avail y los cuádruplos con sus constructores y métodos para manejar los datos. Refactorizamos la tabla de variables para facilitar su uso en el directorio de procedimientos. Al intentar leer las funciones para guardarlas en el directorio, estamos teniendo problemas para guardar las variables en la parte de los tipos y las comas.

## Quinto avance (generación de código de funciones)
Nos enfocamos en la generación de los cuádruplos para las expresiones aritméticas y los estatutos lineales, implementándolos dentro de la sintaxis y guiándonos con los puntos neurálgicos de las presentaciones. Sin embargo, los cuádruplos generados no son los correctos. También resolvimos un error en el cubo semántico que no nos permitía hacer uso de la tabla porque estaba mal declarado el init. Continuaremos trabajando en resolver los errores en la generación de los cuádruplos y la validación para prevenir que las variables y las funciones puedan estar duplicadas.

## Sexto avance (mapa de memoria de ejecución para la máquina virtual y ejecución de expresiones)
Agregamos los métodos para el manejo de las direcciones virtuales en nuestra clase avail.py, en el cual se pueden generar direcciones globales, locales, temporales y constantes para cada uno de los tipos de variables. También creamos la clase constantes.py para el manejo de las constantes y sus direcciones correspondientes. En la clase de cuadruplos.py, agregamos un método para llenar los cuádruplos pendientes de los saltos como GoTo, GoToF y GoToV.

## Séptimo avance (código de arreglos y ejecución de estatutos)
Refactorizamos el directorio de procedimientos para crear métodos menos complejos y más limpios que nos permitieran pasarle los datos de la sintaxis, ya que se nos estaba complicando mucho guardarlos de manera correcta en la tabla. Simplificamos el caso de prueba de Archivo.txt con el ejemplo que venía en el ejercicio de repaso para el último examen porque el que diseñamos nosotros estaba demasiado extenso como para revisarlo en cada prueba individual. Cambiamos la declaración de los puntos neurálgicos en la sintaxis con el uso de índices negativos para acceder a datos que se encontraban en posiciones anteriores a su declaración.

## Octavo avance (código y ejecución de aplicación particular)
Realizamos las validaciones en el directorio de procedimientos para que no se puedan declararar más de una vez las funciones, las variables dentro del mismo contexto y los parámetros dentro de la misma función. De igual manera, realizamos las validaciones para las variables y las funciones que no han sido declaradas. Se modificó el código de los puntos neurálgicos para la generación de los cuádruplos de las expresiones aritméticas, pero todavía se siguen pasando los datos de manera incorrecta.

## Noveno avance
Agregamos los puntos neurálgicos para generar los cuádruplos de las expresiones aritméticas, los estatutos lineales y los estatutos condicionales (if...else y while). Todos los cuádruplos anteriores ya se generan correctamente. Refactorizamos la tabla de constantes para que fuera menos compleja y ya se hace un uso correcto de ella. Modificamos el cubo semántico para que volviera a hacer uso de texto en lugar de enteros porque estamos guardando los tipos de los operandos como texto en las pilas, por lo que el cubo no estaba funcionando anteriormente.

## Décimo avance
Agregamos el código intermedio para la declaración y la llamada de funciones. En la parte de la declaración, ya generamos la firma de la función y se guarda en el directorio de procedimientos, junto con sus cuádruplos correspondientes y la liberación de la memoria local al salir de la función. También validamos que se respete el número de retornos que puede haber por función en caso de que la función contenga condiciones, ya que puede haber más de un retorno. En la parte de la llamada, ya se generan sus cuádruplos correspondientes y se valida que la firma de la llamada concuerde con la firma de la declaración.

## Decimoprimer avance
Implementamos el parche guadalupano en los GoSub para guardar el resultado regresado por las funciones en memoria y poder aplicarle más operadores sin que se pierda el dato. Después, agregamos el uso de direcciones virtuales para las variables, las funciones, los parámetros y las constantes. En el caso de las constantes, tuvimos que manejarlas como strings para separar a los enteros de los flotantes en la tabla. Posteriormente, resolvimos unos problemas que teníamos con las pilas porque nos seguían quedando datos adentro de ellas al terminar de analizar el programa. Descubrimos que el error estaba en nuestro manejo de las asignaciones y las constantes duplicadas. También agregamos los saltos de línea en las escrituras al léxico y a la sintaxis. Finalmente, ya tenemos un primer avance de la máquina virtual, donde tenemos una clase que ya puede leer los cuádruplos e identificar qué lógica debe ejecutar. Por el momento, solo lee operaciones aritméticas y asignaturas. También guarda en memoria los valores de las constantes.
