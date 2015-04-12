Servidor web OpenBSD httpd nativo
#################################

:author: Francisco Valladolid
:tags: openbsd, web, httpd
:lang: es
:category: blog
:slug: httpd-openbsd
:date: 2014-11-13 11:10

Recien se libero la version 5.6 de `OpenBSD <http://www.openbsd.org>`__ y dentro de las novedades se encuetra un servidor web ligero que sustituye a Apache 1.3.

`httpd(8) <http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man8/httpd.8?query=httpd>`__ 
como se le conoce, es un servidor httpd con soporte FastCGI y SSL.

La configuracion para httpd es simple, escribi un breve httpd.conf para configurar dos dominios
para mi sito web.

.. code-block:: sh

	ext_ip="10.0.0.1" 	# Nuestra IP
	server "default" { 
		listen on $ext_ip port 80 
	}
	
	types { 
		text/css			css ;
		text/html			htm html ; 
		text/txt			txt ;
		image/gif			gif ;
		image/jpeg			jpg jpeg  ;
		image/png			png ;
		application/javascript		js ;
		application/xml			xml ;
	}

	server "bsdguy.net" { 
		listen on $ext_ip port 80 
		root "/htdocs/bsdguy.net" 
	} 
 
	server "bsdguy.org" { 
		listen on $ext_ip port 80 
		root "/htdocs/bsdguy.net" 
	}

Es necesario agregar en rc.conf.local y en pkg_scripts=httpd para iniciar el servidor automaticamente.

.. code-block:: console 

	 $ sudo vi /etc/rc.conf.local
	 httpd_flags=""
         
         $ sudo vi /etc/rc.conf
	 pkg_scripts=httpd

Para iniciar el demonio:

.. code-block:: console

	$ sudo /etc/rc.d/httpd start

`httpd(8) <http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man8/httpd.8?query=httpd>`__ es simple pero tiene FastCGI y SSL que lo hace atractivo, enhorabuena.

