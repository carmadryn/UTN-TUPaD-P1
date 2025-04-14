 1) Contestar las siguientes preguntas utilizando las guías y documentación proporcionada (Desarrollar las respuestas) :
• ¿Qué es GitHub?
Es una plataforma que ofrece alojamiento de repositorios de control de versiones, que permite a los desarrolladores almacenar y gestionar sus proyectos de software. Es una herramienta gratuita y de código abierto que permite el trabajo en equipo en proyectos, el intercambio de código y el trabajo conjunto de forma eficiente.


• ¿Cómo crear un repositorio en GitHub?
Create Repository desde github Nos saldrán varias líneas de comandos como:
…or create a new repository on the comand line: Nos indica cada uno de los pasos que debemos de hacer para poder mandar desde nuestro repositorio local al repositorio que hemos creado en github y enlazarlos (recomendado cuando empiezas desde 0).
…or push an existing repository from the command line: Este caso hace referencia a que ya tienes un repositorio local y solamente deseas mandarlo a la plataforma. Para ello deberás de tipear los siguientes comandos en el bash:
$ git remote add origin https://github.com/tucanal/nombre-repo.git
$ git push -u origin master

• ¿Cómo crear una rama en Git?
Para crear una nueva rama, se usará el comando git branch:
$ git branch nuevaRama

• ¿Cómo cambiar a una rama en Git?
$ git checkout nuevaRam
}
• ¿Cómo fusionar ramas en Git?
$ git merge nuevaRama

• ¿Cómo crear un commit en Git?
$git add .
$ git commit –m “nombre”

• ¿Cómo enviar un commit a GitHub?

git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
git add nombre_del_archivo o git add .
Crea un commit de tus cambios:
git commit -m "Descripción de los cambios"
Para enviar los commits al repositorio en GitHub, debemos empujarlos con:
git push origin nombre_de_la_rama

• ¿Qué es un repositorio remoto?
Los repositorios remotos son versiones de tu proyecto que están hospedadas en Internet o en cualquier otra red. Puedes tener varios de ellos, y en cada uno tendrás generalmente permisos de solo lectura o de lectura y escritura. Colaborar con otras personas implica gestionar estos repositorios remotos enviando y trayendo datos de ellos cada vez que necesites compartir tu trabajo.

• ¿Cómo agregar un repositorio remoto a Git?
$ git remote add [nombre] [url]
$ git remote –v
Esto mostrará una lista de todos los remotos configurados con sus URLs:
[nombre] [url]
Para traer toda la información del repositorio remoto que aún no tienes en tu repositorio local, usa el comando git fetch seguido del nombre del remoto:
$ git fetch [nombre]

• ¿Cómo empujar cambios a un repositorio remoto?
Antes de empujar tus cambios, es una buena práctica obtener los últimos cambios del repositorio remoto para evitar conflictos:
git pull origin nombre_de_la_rama
Empuja tus cambios al repositorio remoto:
git push origin nombre_de_la_rama


• ¿Cómo tirar de cambios de un repositorio remoto?
Como mencionamos en el punto anterior, para tirar los cambios del repositorio remoto Usa el comando git pull para descargar y fusionar los cambios del repositorio remoto con tu rama local:
git pull origin nombre_de_la_rama
Por ejemplo, si estás trabajando en la rama main:
git pull origin main

• ¿Qué es un fork de repositorio?
En muchas ocasiones podemos ver en github repositorios que son de nuestro agrado y donde nosotros queremos tener una copia y hacerle algunas modificaciones, para ello github nos ofrece la implementación de fork.

• ¿Cómo crear un fork de un repositorio?
Para entender esto podes por ejemplo crear una cuenta adicional en github para que puedas desde allí hacer un Fork de alguno de los repositorios de tu cuenta original, clonarlo en alguna carpeta y en algún archivo que nosotros notamos que podría mejorarse algo, procedemos a realizar algún cambio, lo agregamos al stage y lo commiteamos (todo esto desde nuestro repositorio local remoto) y luego mandamos los cambios a el forking que hicimos con un git push origin master.

14. ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?
Para hacer el pull request nos dirigiremos a la solapa de Pull requests allí daremos click en new pull request, veremos una ventana a modo de resumen en donde se reflejarán los cambios que hemos hecho nosotros en comparación al repositorio original (el código original, mejor dicho). Daremos click en Create pull request donde veremos el asunto (colocamos algún mensaje global) y más abajo tenemos suficiente lugar para poder explayarnos en mencionar el porque ese cambio que hemos realizado nosotros, sería considerado como algo que a el repositorio original le vendrían bien agregarlo.
15. ¿Cómo aceptar una solicitud de extracción?
El autor del repositorio verá en sus pull requests el mensaje que le hemos enviado, para que lo pueda observar y si lo considera realizar el cambio pertinente (además de poder responderle al usuario que le ha propuesto ese cambio). Lo bueno de todo esto es que si el usuario original considera que esta modificación es buena y no genera conflictos con la rama maestra de su repositorio local remoto, puede clickear en Merge pull request y de esta manera sumará a su repositorio los cambios que hizo un usuario (en modo de ayuda).
16. ¿Qué es un etiqueta en Git?
Como muchos VCS, Git tiene la posibilidad de etiquetar puntos específicos del historial como importantes. Esta funcionalidad se usa típicamente para marcar versiones de lanzamiento (v1.0, por ejemplo).
17. ¿Cómo crear una etiqueta en Git?
Git utiliza dos tipos principales de etiquetas: ligeras y anotadas.
Una etiqueta ligera es muy parecida a una rama que no cambia - simplemente es un puntero a un commit específico.
Sin embargo, las etiquetas anotadas se guardan en la base de datos de Git como objetos enteros. Tienen un checksum; contienen el nombre del etiquetador, correo electrónico y fecha; tienen un mensaje asociado; y pueden ser firmadas y verificadas con GNU Privacy Guard (GPG). Normalmente se recomienda que crees etiquetas anotadas, de manera que tengas toda esta información; pero si quieres una etiqueta temporal o por alguna razón no estás interesado en esa información, entonces puedes usar las etiquetas ligeras.
18. ¿Cómo enviar una etiqueta a GitHub?
Primero, debes crear una etiqueta en tu repositorio local. Puedes crear una etiqueta anotada (que incluye información adicional como el autor y la fecha) o una etiqueta ligera (simplemente un puntero a un commit):
Ej. etiqueta ligera: git tag v1.0
Podes verificar las etiquetas que has creado localmente con:
git tag

Programación I
Una vez que has creado la etiqueta en tu repositorio local, necesitas empujarla al repositorio remoto en GitHub. Puedes hacer esto con el siguiente comando:
git push origin v1.0
(origin es el nombre del repositorio remoto (por defecto suele ser origin) y v1.0 es el nombre de la etiqueta.)
Para empujar todas las etiquetas creadas, usar:
git push origin --tags
19. ¿Qué es un historial de Git?
El historial de Git es una secuencia de todos los cambios realizados en un repositorio de Git. Cada cambio en el repositorio se guarda como un commit, y cada commit contiene información sobre el estado del proyecto en un momento específico, incluyendo:
Identificador del commit
Autor
Fecha de realización
Mensaje enviado
20. ¿Cómo ver el historial de Git?
Esto lo conseguimos con el comando de Git:
git log
Con tipear este comando en el bash de Git podremos apreciar el histórico de commits, estando situados en la carpeta de nuestro proyecto. El listado de commits estará invertido, es decir, los últimos realizados aparecen los primeros.
El comando git log --oneline es una forma compacta de visualizar el historial de commits en un repositorio Git. Muestra un resumen conciso de los commits recientes, con cada commit representado en una sola línea.
Si tu proyecto ya tiene muchos commits, quizás no quieras mostrarlos todos, ya que generalmente no querrás ver cosas tan antiguas como el origen del repositorio. Para ver un número de logs determinado introducimos ese número como opción, con el signo "-" delante (-1, -8, -12...). Por ejemplo, esto muestra los últimos tres commits: git log -3
Si queremos que el log también nos muestre los cambios en el código de cada commit podemos usar la opción -p. Esta opción genera una salida mucho más larga, por lo que seguramente nos tocará movernos en la salida con los cursores y usaremos CTRL + Z para salir. git log -2 -p
21. ¿Cómo buscar en el historial de Git?

Para buscar en el historial de commits de Git, puedes utilizar varios comandos y opciones que te permiten filtrar y localizar commits específicos.
Para buscar commits que contengan una palabra o frase específica en el mensaje de commit, usa git log con la opción –grep: git log --grep="palabra clave"
Para buscar commits que han modificado un archivo específico, usa git log seguido del nombre del archivo: git log -- nombre_del_archivo
Para buscar commits en un rango de fechas específico, usa las opciones --since y --until:
git log --since="2024-01-01" --until="2024-01-31"
Para encontrar commits hechos por un autor específico, usa --author:
git log --author="Nombre del Autor"
22. ¿Cómo borrar el historial de Git?
El comando git reset se utiliza sobre todo para deshacer las cosas, como posiblemente puedes deducir por el verbo. Se mueve alrededor del puntero HEAD y opcionalmente cambia el index o área de ensayo y también puede cambiar opcionalmente el directorio de trabajo si se utiliza - hard. Esta última opción hace posible que este comando pueda perder tu trabajo si se usa incorrectamente, por lo que asegúrese de entenderlo antes de usarlo.
Existen distintas formas de utilizarlo:
• git reset -> Quita del stage todos los archivos y carpetas del proyecto.
• git reset nombreArchivo -> Quita del stage el archivo indicado.
• git reset nombreCarpeta/ -> Quita del stage todos los archivos de esa carpeta.
• git reset nombreCarpeta/nombreArchivo -> Quita ese archivo del stage (que a la vez está dentro de una carpeta).
• git reset nombreCarpeta/*.extensión -> Quita todos los archivos que cumplan con la condición indicada previamente dentro de esa carpeta del stage.
23. ¿Qué es un repositorio privado en GitHub?
Un repositorio privado en GitHub es un tipo de repositorio en el que el contenido solo es accesible para usuarios específicos que han sido autorizados. A diferencia de los repositorios públicos, donde cualquier persona puede ver y clonar el contenido, un repositorio privado limita el acceso a los colaboradores que tú elijas. Esto es útil para proyectos que contienen información sensible o que aún están en desarrollo y no deseas que estén disponibles públicamente.