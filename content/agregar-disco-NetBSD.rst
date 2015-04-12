Agregando un disco extra en NetBSD
##################################
:author: Francisco Valladolid
:tags: scsi, netbsd, unix, bsd, linux
:lang: es
:category: blog 
:slug: agregar-disco-NetBSD
:date: 2011-06-29 1:57


Tengo en casa un servidor corriendo NetBSD 5.1 stable en un disco SCSI
36gb conectado a una controladora SYMBIOS que soporta siete
dispositivos. Tengo necesidad de compilar pkgsrc/, asi que me decidi a
montar un disco extra solo para ese proposito, a continuacion detallo el
proceso.

::

    $ dmesg | grep scsibus
    scsibus0 at esiop0: 16 targets, 8 luns per target
    scsibus0: waiting 2 seconds for devices to settle...
    sd0 at scsibus0 target 1 lun 0: <FUJITSU, MAP3367NP, 0106> disk fixed
    sd1 at scsibus0 target 2 lun 0: <IBM, DDYS-T36950N, S96H> disk fixed

`disklabel(8) <http://netbsd.gw.com/cgi-bin/man-cgi?disklabel++NetBSD-current>`__
nos permite crear la etiqueta de nuestra particion en el disco nuevo.

::

    $ disklabel -i -I sd1

::

    $ sudo newfs /dev/rsd1e
    /dev/rsd1e: 35003.6MB (71687340 sectors) block size 16384, fragment size 2048
            using 190 cylinder groups of 184.23MB, 11791 blks, 23296 inodes.
    super-block backups (for fsck_ffs -b #) at:

    $ sudo fsck -f /dev/rsd1e
    $ sudo mkdir /usr/pkgsrc
    $ vi /etc/fstab

    /dev/sd1e               /usr/pkgsrc ffs rw,log          1 2

    $ sudo mount -va
    $ df -h
    /dev/sd1e          34G        34M        32G   0% /usr/pkgsrc

La instalacion es simple y ahora tenemos un disco aunque de no gran
tamano, bien nos sirve para hacer compilacion de paquetes, sin
congestionar nuestro disco del sistema base. Algunas ocasiones
necesitamos limpiar el disco, llenar con ceros, para ello usamos:

::

    # dd if=/dev/zero of=/dev/sd1 bs=8k


