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