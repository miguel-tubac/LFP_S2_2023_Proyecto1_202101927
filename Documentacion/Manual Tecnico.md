# LENGUAJES FORMALES Y DE PROGRAMACIÓN
## Manual Tecnico, Proyecto 1
### SEGUNDO SEMESTRE 2023
```js
Universidad San Carlos de Guatemala
Programador: Miguel Adrian Tubac agustin
Carne: 202101927
Correo: mgtubac@gmail.com
```
---
## Descripción del Proyecto
El programa fue desarrollado en el lenguaje de programación Python, el mismo permite la lectura de código fuente, el cual tendrá un formato JSON, posteriormente el programa es capaz de identificar un lenguaje dado, identificando los errores léxicos y ejecutando las instrucciones correspondientes. Los errores son almacenados en un archivo JSON. 


## Objetivos
* Objetivos
    * Implementar por medio de estados un analizador léxico.
    * Utilizar funciones de manejo de cadenas de caracteres en lenguaje Python.
    * Programar un Scanner para el análisis léxico.
    * Construir un scanner basándose en un autómata finito determinístico.
    * Crear una herramienta para interactuar de forma visual con el usuario con Tkinter
    * Crear diagramas con la librería Graphviz 

---
## Elaboración de la practica
En la práctica se utilizaron las siguientes clases:

Clase Ventana() utilizada para inicializar las variables y mostrar la ventana del texto a ingresar y posteriormente a ser analizado:

![ImagenesDeMarcdown](https://i.ibb.co/NpHX9kv/image.png)

La Clase TextLineNumbers() permite que en el area de texto se muestre la numeracion de las lineas ingresadas y al mismo tiempo se actualiza con el ingreso de archivos json al mismo:

![ObtenerLink](https://i.ibb.co/vJHtXJV/image.png)

La Clase ExpresionAritmetica() permite que las operaciones de aritmetica se ejecuten sin ningun proble:

![ObtenerLink](https://i.ibb.co/vXFKK0z/image.png)

La Clase ExpresionTrigonometrica() permite que las instruciones del json que indique alguna operacion Trigonometrica, esta pueda ser operada por esta clase: 

![ObtenerLink](https://i.ibb.co/x8z8kKS/image.png)

La Clase Arbol() permite que se almacenen los nodos de cada operacion y al finalizar la carga de archivos se pueda generar la grafica, a travez de la libreria de graphviz: 

![ObtenerLink](https://i.ibb.co/94FBjc5/image.png)

Tabla con las funciones que se encuentran dentro del sistema de analisis:
| Función                          | Especificación                                                                                                 |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `ScrollText(tk.Frame)`      | Permite que en area de texto se pueda navegar y con la misma actualizar los numeros de lineas.                                          |
| `TextLineNumbers(tk.Canvas)`           | Permite mostrar la numeracion de las lineas que se esten utilizando en el area de texto.            |
| `Ventana(tk.Tk)`| En esta clase se declaran los atributos generales de la ventana que el usuario tendra acceso  y edicion sobre el mismo.    |
| `Error()`  | La clase establece la estructura de los errores que se almacenaran en el archivo de salida.         |
| `Arbol()`  | Muestra la información ingresada. Esta clase ademas genera los nodos correspondientes a la grafica que se genera.         |
| `ExpresionAritmetica(Expresion)`  | La clase analiza el analisis de las antradas cuyas operaciones corresponden a operaciones Aritmeticas.         |
| `ExpresionTrigonometrica(Expresion)`  | Esta clase analiza las operaciones Trigonometricas que se establecen en el archivo de entrada.         |