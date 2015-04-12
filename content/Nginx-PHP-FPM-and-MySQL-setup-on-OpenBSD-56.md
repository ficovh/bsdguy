Title:Nginx - PHP-FPM - MySQL OpenBSD 5.6
author: Francisco Valladolid
tags: nginx, openbsd, php
lang: en
category: blog
slug: nginx-openbsd56
Date: 2015-04-04

**El siguiente articulo esta en Ingles y fue escrito por mi para www.vultr.com.**

OpenBSD is most used in firewall implementations,however, many people around the world are using OpenBSD as web server, mainly programmers and sysadmins.
We assume a knowledge of OpenBSD, nginx and Unix in general.

nginx [engine x] is an HTTP and reverse proxy server, as well as a mail proxy server, written by Igor Sysoev. For a long time, it has been running on many heavily loaded Russian sites . (_from the website_).

PHP-FPM (FastCGI Process Manager) is an alternative PHP FastCGI implementation with some additional features useful for sites of any size, especially busier sites. (_from the site_)

### Requeriments:

* OpenBSD 5.6 installed in your vultr.com VPS
* set the PKG_PATH = ftp://ftp.openbsd.org/pub/OpenBSD/5.6/packages/\`arch -s\`
* super user access


## Install nginx

    $ sudo pkg_add -v nginx
    Ambiguous: choose package for nginx
    a     0: <None>
          1: nginx-1.4.7p0
          2: nginx-1.4.7p0-lua
          3: nginx-1.4.7p0-naxsi
          4: nginx-1.4.7p0-passenger
          5: nginx-1.5.7p3
          6: nginx-1.5.7p3-lua
          7: nginx-1.5.7p3-naxsi
          8: nginx-1.5.7p3-passenger
      Your choice:

For the purposes of this document, we install the "5" option.

## Install PHP-FPM

   $ sudo pkg_add -v php-fpm-5.5.14.tgz

The _/etc/rc.conf.local_ must be containt the next line

  nginx_flags=""

And the _/etc/rc.conf_ for start automatically in each reboot.

    # rc.d(8) packages scripts
    # started in the specified order and stopped in reverse order
    pkg_scripts=nginx

** Editing _/etc/nginx/nginx.conf_ and _/etc/php-fpm.conf_ **

Basic requeriments for /etc/nginx/nginx.conf in the _server_ section.

	location ~ \.php$ {
                try_files $uri =404;
                fastcgi_split_path_info ^(.+\.php)(/.+)$;
                fastcgi_pass   127.0.0.1:9000;
                fastcgi_index index.php;
                fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
                include fastcgi_params;
        }

**Edit /etc/php-fpm.conf**

	; Unix user/group of processes
	; Note: The user is mandatory. If the group is not set, the default user's 
	; group will be used.
	user = www
	group = www


	; The address on which to accept FastCGI requests.
	; Valid syntaxes are:
  	; 'ip.add.re.ss:port'    - to listen on a TCP socket to a specific address on
  	;                            a specific port;
  	;   'port'                 - to listen on a TCP socket to all addresses on a
  	;                            specific port;
  	;   '/path/to/unix/socket' - to listen on a unix socket.
  	; Note: This value is mandatory.

  	listen = 127.0.0.1:9000

## Installing MySQL

	$ sudo pkg_add -v mysql-server-5.1.73p0v0.tgz

	Update candidates: quirks-2.9 -> quirks-2.9 (ok)
	quirks-2.9 signed on 2014-07-31T22:37:55Z
	mysql-server-5.1.73p0v0:p5-Net-Daemon-0.48: ok
	mysql-server-5.1.73p0v0:p5-PlRPC-0.2018p1: ok
	mysql-server-5.1.73p0v0:p5-Clone-0.36p0: ok
	mysql-server-5.1.73p0v0:p5-Params-Util-1.07p0: ok
	mysql-server-5.1.73p0v0:p5-SQL-Statement-1.405: ok
	mysql-server-5.1.73p0v0:p5-FreezeThaw-0.5001: ok
	mysql-server-5.1.73p0v0:p5-MLDBM-2.05: ok
	mysql-server-5.1.73p0v0:p5-DBI-1.631p0: ok
	mysql-server-5.1.73p0v0:mysql-client-5.1.73v0: ok
	mysql-server-5.1.73p0v0:p5-DBD-mysql-4.027: ok
	mysql-server-5.1.73p0v0: ok
	The following new rcscripts were installed: /etc/rc.d/mysqld
	See rc.d(8) for details.
	Look in /usr/local/share/doc/pkg-readmes for extra documentation.
	Extracted 39040357 from 39044890

### Initial setup

Later to install MySQL you need setup this.
	
Create the initial database:
	
	$ sudo /usr/local/bin/mysql_install_db

You can run the ``/usr/local/bin/mysql_secure_installation`` script for optimize your mysql installation or 
set the root password directly with the next command.

	$ sudo /usr/local/bin/mysqladmin -u root password 'password'

And execute mysql as root for administrations tasks only, you can create databases and users.

	$ mysql -u root -p
	Enter password: 
	Welcome to the MySQL monitor.  Commands end with ; or \g.
	Your MySQL connection id is 47
	Server version: 5.1.73-log OpenBSD port: mysql-server-5.1.73p0v0

	Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

	Oracle is a registered trademark of Oracle Corporation and/or its
	affiliates. Other names may be trademarks of their respective
	owners.

	Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

	mysql>

### MySQL support for PHP

	$ sudo pkg_add -v php-pdo_mysql-5.5.14.tgz


## Starting daemons

    $ sudo /etc/rc.d/nginx start
    $ sudo /etc/rc.d/php-fpm start
    $ sudo /etc/rc.d/mysqld start

You can write a basic ``info.php`` file into documentroot, in my case, /var/www/htdocs/example.com


    <?php
        phpinfo();
    ?>

if all is ok, then you can view the PHP information web page.

## Logs

Basic log files are found in ``/var/log/nginx`` subdirectory for audit purposes.

Enjoy.
