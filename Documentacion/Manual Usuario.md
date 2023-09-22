# LENGUAJES FORMALES Y DE PROGRAMACIÓN
## Manual De Usuario, Proyecto 1 
### SEGUNDO SEMESTRE 2023
```js
Universidad San Carlos de Guatemala
Programador: Miguel Adrian Tubac agustin
Carne: 202101927
Correo: mgtubac@gmail.com
```
---
## Descripción del Proyecto
El programa permite la lectura de código fuente, el cual tendrá un formato JSON, posteriormente el programa es capaz de identificar un lenguaje dado, identificando los errores léxicos y ejecutando las instrucciones correspondientes. Los errores son almacenados en un archivo JSON. 


## Objetivos
* Objetivos
    * Implementar por medio de estados un analizador léxico.
    * Construir un scanner basándose en un autómata finito determinístico.
    * Crear una herramienta para interactuar de forma visual con el usuario con Tkinter
    * Crear diagramas con la librería Graphviz 

---
## Utilización de la interfaz 
En la ejecucion de la aplicaion seran visibles y accedibles los siguientes objetos graficos:

La ventana principal cuanta con la siguiente apariencia:
![ImagenesDeMarcdown](https://i.ibb.co/LvPGGN1/image.png)
Los botones de Errores y Reporte(Grafica) aparecen desabilitadas al principio ya que al ingresar texto y presionar Analizar, estos seran avilitados. Las funciones son las siguientes:
* Archivo:
    * Abrir: Permite abrir un archivo para poder seguir editándolo en la aplicación
    * Guardar: Permite guardar el archivo que está siendo editado con el nombre actual.
    * Guardar como: Permite guardar el archivo que está siento editado con otro nombre.
    * Salir: Con esta opción se cerrará la aplicación
* Analizar: Analizará el texto y mostrará los elementos reconocidos.
* Errores: Muestra los errores con el formato que más adelante se detalla del último archivo compilado. 
* Reporte: Generar los diagramas de las operaciones previamente analizadas 

Al ingresar un archivo json, este se mostrara en el area de texto y posteriormente al presionar el boton de `Analizar` este producira un mensaje indicando que se anilizo el texto exitosamente:
![ObtenerLink](https://i.ibb.co/HdXBzXB/image.png)

Posteriormete de analizar el texto, se seleciona el boton de `Errores` y el mismo mostrara el mensaje indicando que el archivo fue creado con exito y al mismo tiempo se almaceno en la carpeta raiz del proyecto:
![ObtenerLink](https://i.ibb.co/nj6m9Fs/image.png)

Al abrir el archivo de errores.json con el mismo programa muestra la estructura siguiente: 
![ObtenerLink](https://i.ibb.co/nMTBJm3/image.png)

Al presionar el boton de `Reporte(Grafica)`, este generara la grafica y los nodos que se conectan apareceran en el mismo, el archivo generado corresponde a un archivo pdf:
![ObtenerLink](https://i.ibb.co/997JP7p/image.png)

Posteriormente al seleccionar el boton `salir` el programa terminara si ejecucion y se cerrara.
