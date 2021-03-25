sed basico 
##########
:author: Francisco Valladolid
:tags: netbsd, unix, bsd, sed, regexp
:lang: es
:category: blog 
:slug: sed-basico
:date: 2020-05-27 7:30
:email: ficovh@gmail.com

¿Que es Sed?
------------
*sed (Stream Editor)* es un editor de flujos, te permite editar, reemplazar lineas en un archivo de texto
usando expresiones regulares.

El sistema operativo Unix tiene un superconjunto de comandos que permiten
realizar todo tipo de tareas de procesamiento de archivos de texto.

El superconjunto incluye: *sed, awk, cat, echo, grep, ed, vi* entre otros.

Recientemente me topé con un archivo exportado que incluye un conjunto de usuarios
separados por "espacios", necesito ordenarlo en forma de lista y agregarle
algunos parametros antes y despues para exportarlo a un router Mikrotik.

El archivo en cuestion se ve así. 

.. image:: https://i.imgur.com/NVhvxj6m.png
   :target: https://i.imgur.com/NVhvxj6.png
   :alt: sed

Necesito sustituir los espacios en blanco por un caracter de nueva linea para
crear una lista de usuarios, usamos el comando *sed* de la siguiente forma.

.. code-block:: console

    $ sed 's/\s/\n/g' test.txt > sed1.txt


Después de ejcutar el comando, el archivo luce así.


.. image:: https://i.imgur.com/tOXctyFm.png
   :target: https://i.imgur.com/tOXctyF.png
   :alt: sed


Además de eso, necesito agregar una cadena de texto al inicio:  *add name=*


.. code-block:: console

    $ sed -i 's/^/add name\=/g' sed1.txt


.. image:: https://i.imgur.com/MguwLUCm.png
   :target: https://i.imgur.com/MguwLUC.png
   :alt: sed


Tambien necesito agregar al final la siguiente cadena:


.. code-block:: console

    $ sed -i 's/$/ limit-uptime\=02:00:00 disabled\=no profile\=\"1mega\"/g' sed1.txt


.. image:: https://i.imgur.com/KhedLDem.png
   :target: https://i.imgur.com/KhedLDe.png
   :alt: sed


Unix es un sistema operativo muy completo, como tal ya no existe, pero sus derivados si,
por citar algunos: *Linux, OpenBSD, FreeBSD, NetBSD, OSX*. 
