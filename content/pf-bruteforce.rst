Bloqueando intentos masivos por SSH
###################################
:author: Francisco Valladolid
:tags: openbsd, security, pf, tcp
:lang: es
:category: blog
:slug: pf-attack
:date: 2015-02-15


PF (packet filter) es el filtro de paquetes por defecto en OpenBSD desde la version 3.0, su uso mas frecuente
es en Firewall y control de ancho de banda por tipo de trafico.

Pf se puede usar para bloquear intentos fallidos por SSH u otro protocolo, ejemplo:
Si leemos el authlog en OpenBSD observamos lo siguiente:

::

  $ sudo tail -f /var/log/authlog  

  Feb 13 22:43:55 openbsd last message repeated 2 times
  Feb 13 22:43:55 openbsd sshd[2705]: Received disconnect from 83.217.254.216: 11:  [preauth]
  Feb 13 22:43:56 openbsd sshd[6102]: reverse mapping checking getaddrinfo for 83-217-254-216-eu1.opsourcecloud.net [83.217.254.216] failed 
  Feb 13 22:43:56 openbsd sshd[6102]: Failed password for root from 83.217.254.216 port 47388 ssh2
  Feb 13 22:43:56 openbsd last message repeated 2 times
  Feb 13 22:43:56 openbsd sshd[6102]: Received disconnect from 83.217.254.216: 11:  [preauth]
  Feb 13 22:43:56 openbsd sshd[22991]: reverse mapping checking getaddrinfo for 83-217-254-216-eu1.opsourcecloud.net [83.217.254.216] failed 
  Feb 13 22:43:56 openbsd sshd[22991]: Failed password for root from 83.217.254.216 port 47546 ssh2
  Feb 13 22:43:56 openbsd last message repeated 2 times
  Feb 13 22:43:56 openbsd sshd[22991]: Received disconnect from 83.217.254.216: 11:  [preauth]


En el archivo /etc/pf.conf necesitamos agregar
----------------------------------------------

::

        int_if = "fxp0"

        table  <ataque> persist

        block quick from <ataque>

        pass quick proto tcp from any to any port ssh \
                flags S/SA keep state \
                (max-src-conn 100, max-src-conn-rate 5/3, \
                overload <ataque> flush global)


Recargamos el archivo
---------------------

::

        $ sudo /sbin/pfctl -f /etc/pf.conf


Todas las IP's baneadas permanecen en la tabla <ataque> mientras no decidamos liberarlas, pf cuenta con la opcion expiretable para ese
proposito, la siguiente linea da un tiempo de vencimiento a la tabla <ataque> de 24 horas.

::

     $ sudo /sbin/pfctl -t ataque -T expire 86400

