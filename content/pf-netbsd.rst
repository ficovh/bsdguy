Configuracion de PF en NetBSD 5.1
#################################
:author: Francisco Valladolid
:tags: scsi, netbsd, unix, bsd, linux
:lang: es
:category: blog
:slug: pf-netbsd
:date: 2011-09-10 4:27


PF (packet filter) es un filtro de paquetes proveniente de OpenBSD;
Incorporado en el sistema base desde NetBSD 4.0 y puede ser usado para
implementar firewalls. NetBSD 5.1 incorpora la version 4.2 de pf, por lo
que es importante leer la
`FAQ <ftp://ftp.openbsd.org/pub/OpenBSD/doc/history/pf-faq42.pdf>`__
correspondiente; En esta ocasion, tengo un servidor corriendo
ssh/web/dns y varios intentos de login via ssh, asi que decidi
implementar una solucion para mitigar los intentos, para ello use PF y
NetBSD 5.1; a continuacion detallo el proceso simple; Editamos
/etc/lkm.conf y anexamos:

::

    /usr/lkm/pf.o   -   -   -   -  BEFORENET

En /etc/rc.conf

::

    lkm=YES
    pf=YES
    pflogd=YES

y manualmente iniciamos el modulo lkm para pf

::

    $ sudo modload /usr/lkm/pf.o

Una vez realizado el proceso, editamos a conveniencia el archivo
/etc/pf.conf y agregamos lo necesario, en mi caso:

::

    int_if = "fxp0"
    localnet = $int_if:network

    tcp_services = "{ ssh, smtp, domain, www, pop3, auth, https }"
    udp_services = "{ domain }"

    table  <bruteforce> persist

    block quick from <bruteforce>

    pass inet proto tcp to $localnet port $tcp_services \
            keep state (max-src-conn 100, max-src-conn-rate 15/5, \
            overload <bruteforce> flush global)

Descripcion:
------------

**persist:** Mantiene la tabla en memoria, aunque no haya reglas que
refieran a ella.
 
**max-src-conn :** Indica el numero de conexiones
simultaneas provenientes de un host, puedes incrementar o disminuir este
valor segun sea el caso. 

**max-src-conn-rate:** Indica la tasa de
transferencia permitida por conexion, aqui es 15 conexiones cada 5
segundos, expresada: 15/5 

**Overload:** Toda conexion que exceda la
condicion anterior, sera agregada a la tabla bruteforce, y sera
bloqueado todo el contenido de la tabla. 
Para ver la lista de IP baneadas, usa la siguiente linea:

::

     $ sudo /sbin/pfctl -t bruteforce -T show 

Con estas adiciones podemos bloquear intentos fallidos via ssh hacia
nuestro servidor.
