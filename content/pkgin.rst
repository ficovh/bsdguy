Paquetes binarios con pkgin
##################################
:author: Francisco Valladolid
:tags: netbsd, unix, bsd, pkgsrc, pkgin
:lang: es
:category: blog 
:slug: pkgin
:date: 2011-06-29 18:06


Uno de los principales incovenientes de los que muchos usuarios suelen
quejarse al probar NetBSD es su sistema de paquetes (pkgsrc), ya que
cada programa necesita ser compilado desde los fuentes y probado lo que
llega a ser tedioso y algunas veces frustrante. El tiempo de compilacion
e instalacion llegar a ser critico tratandose de meta-programas; Por
ejemplo; compilar OpenOffice 3 quiza tarde unas seis horas o mas
dependiendo del equipo, consumiendo recursos, tiempo y en ocasiones
pueden presentarse problemas de compilacion; es posible que despues de
esto detalles, dejemos el sistema y sigamos con lo que estamos
acostumbrados a usar. 

Afortunadamente ahora existe `pkgin <http://pkgin.net/>`__, una utileria al estilo "apt-get" o "yum"
para instalar paquetes binarios bajo NetBSD. 
Es una forma atractiva y facil, eliminando el mito aquel de compilar desde fuentes.

Puedes bajar el binario de `pkgin <http://pkgin.net/>`__ desde el sitio
ftp e instalarlo manualmente con
`pkg\_add(1) <http://netbsd.gw.com/cgi-bin/man-cgi?pkg_add++NetBSD-current>`__
y despues proceder con la configuracion anterior.

`pkgin <http://pkgin.net/>`__ usa un simple archivo .conf ubicado en
*/usr/pkg/etc/pkgin/repositories.conf*, este archivo acepta lineas
apuntando a servidores ftp o http con depositos de paquetes binarios de
NetBSD para una version determinada.

Por ejemplo:
*ftp://ftp.fr.netbsd.org/pub/pkgsrc/packages/NetBSD/i386/5.0/All* 

Esta linea contiene paquetes binarios para NetBSD 5.0 y la plataforma i386.
Un simple: *$ sudo pkgin update* creara una lista de paquetes y sus
dependecias en una base de datos sqlite3 listos para ser instalados.

Ejemplos:
---------

Para instalar Apache y sus dependencias:

.. code-block:: console

     $ sudo pking install apache-2.2.17

Para buscar mysql en la base de datos:

.. code-block:: console

     $ sudo pkgin se mysql 

Para ver las las opciones de `pkgin <http://pkgin.net/>`__ solo ejecuta
el programa sin argumentos. 
Tener un sistema NetBSD con los paquetes necesarios es realmente sencillo 
con esta utileria, lo mismo para meta-paquetes como gnome, xfce4, kde, 
e incluso puedes tener un servidor AMP (Apache, MySQL, Perl/PHP) 
en cuestion de minutos sin esfuerzo, con el soporte del extraordinario pkgsrc.


