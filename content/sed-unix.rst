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

Recientemente me top&eacute; con un archivo exportado que incluye un conjunto de usuarios
separados por ^M (enter msdos)  del cual ten&iacute; que ordenarlo en forma de lista.

El archivo en cuestion se ve as&iacute; 

.. image:: test1.png
   :target: https://imgur.com/NVhvxj6

Necesito sustituir los espacios en blanco por un caracter de nueva linea para
crear una lista de usuarios, usamos el comando *sed* de la siguiente forma.

::
    $ sed 's/\s/\n/g' test.txt > sed1.txt

Despu&eacute;s de eecutarl el comando, el archivo luce as&iacute;.

.. image:: sed1.png
    :target: https://imgur.com/tOXctyF

Además de eso, necesito agregar una cadena de texto al inicio:  *add name=*

::
    $ sed -i 's/^/add name\=/g' sed1.txt

.. image:: sed3.png
    :target: https://imgur.com/MguwLUC

Tambien necesito agregar al final la siguiente cadena:

::
    sed -i 's/$/ limit-uptime\=02:00:00 disabled\=no profile\=\"1mega\"/g' sed1.txt

.. image:: result.png
    :target: https://imgur.com/KhedLDe

Unix es un sistema operativo muy completo, como tal ya no existe, pero sus derivados si,
por citar algunos: *Linux, OpenBSD, FreeBSD, NetBSD, OSX*. Para el especialista en sistemas 
es una delicia trabajar con este.
