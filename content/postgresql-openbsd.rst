PostgreSQL en OpenBSD
#####################
:author: Francisco Valladolid
:tags: openbsd, postgresql, bsd, dbms
:lang: es
:category: blog
:slug: postgresql-openbsd
:date: 2012-10-04 10:20


Tengo un VPS corriendo `OpenBSD <http://www.openbsd.org>`__ 5.0 y
necesito instalar PostgreSQL. Algunas veces es necesario escribir para
no olvidar, sobre todo en cuestiones triviales. La forma mas facil es
instalar PostgreSQL en OpenBSD es via paquetes binarios, existe una
forma a traves de ports, mediante un conjuntos de makefiles para
compilar paquetes desde los fuentes; Si tienes instalado ports, la forma
de hacerlo es:

.. code-block:: console

      $ cd /usr/ports/databases/postgresql
      $ sudo make install clean

Y con binarios:

.. code-block:: console

     $ export PKG_PATH=ftp://ftp.openbsd.org/pub/OpenBSD/5.0/packages/i386
     $ sudo pkg_add -v postgresql-server-9.0.4p1.tgz

La version server, automaticamente resuelve las dependencias e instala la
version cliente, una vez instalada tendremos que iniciar el cluster
donde PostgreSQL almacenara las bases de datos y solo es posible con
usuario \_postgresql

.. code-block:: console

     $ sudo su - _postgresql
     $ /usr/local/bin/initdb -D /var/postgresql/data 

Lo anterior prepara el directorio /var/postgresql/data para poder ser
usado mas adelante y a continuacion iniciamos el demonio para poder
empezar a trabajar.

.. code-block:: console

     $ /usr/local/bin/pg_ctl -D /var/postgresql/data -l logfile start
       server starting

Vamos a crear un usuario para poder crear bases de datos;

.. code-block:: console

     $ psql postgres
     postgres=# create role db_admin login password 'algun_passw' createdb  
                valid until 'infinity';
     CREATE ROLE
     postgres=#

Adicionalmente, editamos el archivo /var/postgresql/data/pg\_hba.conf
para agregar seguridad a nivel de usuario a la base de datos, usando el
metodo md5, postgresql debe estar detenido.

::

    local   all             all                                     md5

Es necesario dejar el usuario \_postgresql y salir para probar nuestro
trabajo, de esta manera el usuario db\_admin y el password
'algun\_password' fue creado, la forma de acceder ahora es de la sig.
manera.

.. code-block:: console

      $ createdb -U db_admin book   
      $ psql -U db_admin book
      psql (9.0.4)
      Type "help" for help.

      book=>

Con esto hacemos una parte de la configuracion basica, PostgreSQL es un
sistema de base de datos avanzado, profesional y libre compite con
cualquier DBMS comercial actual. El sitio web de
`PostgreSQL <http://www.postgreSQL.org>`__ contiene mas informacion
sobre todos los detalles de este sistema. Si tu como yo estas usando
OpenBSD, espero y esto pueda ayudarte un poco en esa tarea. Mas
informacion:

`Sitio web de OpenBSD <http://www.openbsd.org>`__

`Documentacion PostgreSQL <http://www.postgresql.org/docs>`__

