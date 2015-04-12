Borrando paquetes en OpenBSD
############################
:author: Francisco Valladolid
:tags: openbsd, ports, paquetes, pkgtools 
:lang: es
:category: blog
:slug: borrar-paquetes-openbsd
:date: 2012-10-04 23:59

Algunas veces borrar un numero determinado de paquetes en OpenBSD puede
ser un trabajo arduo; pkg\_delete aun no puede usar comodines para poder
filtrar un patron de paquetes que no deseamos mas en nuestro sistema.

OpenBSD esta pensando para personas con un nivel distinto a
los demas y piensa que pueden escribir sus propias rutinas, para hacer
X o Y cosas con el sistema. 

Por ejemplo:

:: 

	$ pkg_delete -ax ruby-*.* 

Esto no funciona aun, sin embargo, podemos escribir un script que de manera
automatica nos permita hacer la tarea que queremos; quiza
alguien tenga otra mejor, Yo deseo quitar todos los paquetes del
lenguaje Ruby en mi sistema, no necesito mas esto, el pkg\_info revela
una lista de mas de 20 paquetes instalados.

.. code-block:: sh

     $ pkg_info | grep ruby | awk '{print $1}'

La instruccion anterior en el shell de OpenBSD, nos proporciona una
lista de todas las coincidencias con ruby, usando solo el nombre del
paquete, y con ello puedo iterar a traves de la lista.

.. code-block:: sh

    #!/bin/sh
    packages=`pkg_info | grep ruby | awk '{print $1}'`
    for i in $packages
    do
            pkg_delete  -ax $i
            echo "Borrando: $i ..." 
    done

El codigo anterior permite consultar, almacenar en una variable e
iterar a traves de la lista para borrar uno a uno los paquetes en
cuestion. No se si haya una forma mas facil de hacerlo, pero fue lo que
tuve a la mano en el momento de la urgencia.

