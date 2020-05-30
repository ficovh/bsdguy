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

El sistema operativo Unix tiene un superconjunto de comandos que permiten
realizar todo tipo de tareas de procesamiento de archivos de texto.

El superconjunto incluye: *sed, awk, cat, echo, grep, ed, vi* entre otros.

Recientemente me topé con un archivo exportado que incluye un conjunto de usuarios
separados por "espacios", necesito ordenarlo en forma de lista y agregarle
algunos parametros antes y despues para exportarlo a un router Mikrotik.

El archivo en cuestion se ve así. 

.. image:: https://live.staticflickr.com/65535/49952861558_144c0d53f2_b.jpg



Necesito sustituir los espacios en blanco por un caracter de nueva linea para
crear una lista de usuarios, usamos el comando *sed* de la siguiente forma.

.. code-block:: console

    $ sed 's/\s/\n/g' test.txt > sed1.txt


Después de ejcutar el comando, el archivo luce así.


.. image:: tOXctyF.png
    :target: https://i.imgur.com/tOXctyF.png


Además de eso, necesito agregar una cadena de texto al inicio:  *add name=*


.. code-block:: console

    $ sed -i 's/^/add name\=/g' sed1.txt


.. image:: MguwLUC.png
    :target: https://i.imgur.com/MguwLUC.png


Tambien necesito agregar al final la siguiente cadena:


.. code-block:: console

    $ sed -i 's/$/ limit-uptime\=02:00:00 disabled\=no profile\=\"1mega\"/g' sed1.txt


.. image:: KhedLDe.png
    :target: https://i.imgur.com/KhedLDe.png


Unix es un sistema operativo muy completo, como tal ya no existe, pero sus derivados si,
por citar algunos: *Linux, OpenBSD, FreeBSD, NetBSD, OSX*. 
