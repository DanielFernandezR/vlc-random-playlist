## Breve descripción
Construye un software que genere una lista de reproducción aleatoria con las canciones que tienes en la biblioteca de música de tu PC y que invoque a VLC para reproducir las canciones.

## El Reto
- Construye un programa que genere una lista de reproducción aleatoria de las canciones que tienes en tu biblioteca de canciones de tu máquina.
- El script llama a VLC una vez que la lista está creada y la música comienza a sonar en tu MacBookPro de 15 pulgadas portable.
	- Por ejemplo, iTunes dispone de un fichero XML llamado library.xml con una descripción de todas las canciones del equipo. Nosotros/as crearemos en un primer paso nuestra particular library.xml con la descripción de las canciones. Luego, leeremos este fichero XML para generar la lista aleatoria.
- Finalmente, invocaremos desde nuestro programa al reproductor VLC y le pasaremos (en la misma invocación) la lista de canciones para que la reproduzca.
- Durante el desarrollo del proyecto, has de alcanzar una serie de hitos -relacionados con los distintos módulos del curso que aparecen detallados en el epígrafe “Tareas a Realizar”. Has de cumplir con las tareas que ahí se detallan, 
desde requisitos de implementación hasta de gestión y entrega del proyecto, para que el reto se considere resuelto.
- Consulta el epígrafe “Criterios de Evaluación” para conocer en detalle los criterios que seguirá el equipo docente para evaluar tu trabajo en cada uno de los módulos.

## Tareas a realizar

### Sistemas informáticos:
	- Crea desde línea de comandos en tu máquina un directorio donde almacenar los ficheros con las canciones. Nos referiremos a este directorio como la biblioteca de canciones.
	- Copia o mueve desde línea de comandos las canciones desde el soporte donde se encuentran a tu biblioteca.
	- Formatea desde línea de comandos los títulos de las canciones para darles el formato adecuado.
	- Instala desde línea de comandos el programa VLC.
	- Invoca desde línea de comandos el programa VLC y averigua qué parámetros admite.
	- Averigua qué errores genera una mala invocación de VLC.
	- Ejecuta el programa VLC desde línea de comandos para reproducir una determinada canción.
	- Ejecuta el programa VLC desde línea de comandos para reproducir una lista de canciones.
	- Arranca desde línea de comandos el editor que te permita crear el fichero XML con la descripción de las canciones de tu biblioteca que diseñarás en el módulo de lenguaje de marcas.
	- Arranca desde línea de comandos el editor que te permite crear un fichero Schema que valida la biblioteca XML y que diseñarás en el módulo de lenguaje de marcas.
### Bases de datos:
	- Realiza el modelo E-R de la base de datos que almacenaría las canciones.
	- Pasa el modelo E-R al modelo relacional.
	- Extrae los atributos que describen las canciones de la biblioteca.
	- Define el tipo de dato de cada atributo.
	- Establece la clave primaria y la clave foránea.
### Lenguaje de marcas
	- Crea un fichero XML que describa la información contenida en la biblioteca de canciones.
	- Escribe su Schema que describa la biblioteca de canciones con el fin de poder validarla.
	- Valida el fichero XML. Comprueba que el fichero está bien formado (utilizando el Schema).
	- Utiliza el modelo E-R y el modelo relacional que has propuesto en el módulo de bases de datos para definir los tipos de datos de los elementos del fichero XML.
	- Utiliza el modelo E-R y el modelo relacional que has propuesto en el módulo de bases de datos para definir los tipos de los elementos del fichero XML.
	- Define los espacios de nombres que sean necesarios.
### Entornos de desarrollo
	- Crea un repositorio del proyecto en GitHub.
	- Crea un fichero README.MD que describa adecuadamente el proyecto.
	- Realiza el control de versiones y trabaja de manera colaborativa con tu pareja de programación.
	- Utiliza ramas para realizar los evolutivos, testing y debugging, siguiendo el flujo de trabajo que especificaremos en las sesiones presenciales.
	- Documenta todo el proceso.
	- ¿Escribe las historias de usuario/a? = identifica y describe los requisitos funcionales de la aplicación.
	- Elige el ciclo de desarrollo que consideres más adecuado a tu manera de trabajar (y a la de tu pareja de programación) y al proyecto.
	- Utiliza clockify para llevar un seguimiento del tiempo de desarrollo empleado en cada una de las fases del ciclo de vida del proyecto. Sé riguroso porque los informes generados por este herramienta serán un producto a entregar.
### Programación
	- Divide el código en rutinas de modo que sea SRP y OCP.
		* SRP (S) o Principio de Única Responsabilidad o Single Responsibility Principle. Un componente sólo debe tener un motivo para cambiar.
		* OCP (O) o Open/Closed Principle. Las entidades de software (clases, módulos, funciones, etc.) deben estar “abiertas” a la extensión pero “cerradas” a la modificación.
	- Emplea precondiciones y postcondiciones para chequear las invariantes (las estructuras de datos) que maneja el programa y que se comunican las distintas funciones.
	- Utiliza las librerías XML que proporciona el lenguaje Python para extraer del fichero XML (la biblioteca de canciones) la información que necesitas de las canciones para construir la playlist (aleatoria) de canciones que le pasarás al programa VLC.
	- Elige la estructura de datos adecuada para representar y manipular en memoria la lista de canciones.
	- Utiliza bloques try /except para capturar las excepciones que se puedan producir durante la ejecución del programa.
	- Crea una lista aleatoria con las canciones de tu biblioteca de música. Si la lista no es aleatoria, el proyecto no se considera resuelto satisfactoriamente.
	- Invoca desde Python el programa VLC y pásale la lista de canciones importando las librerías adecuadas.
