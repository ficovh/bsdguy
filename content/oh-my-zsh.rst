Usando oh-my-zsh
################
:author: Francisco Valladolid
:tags: openbsd, zsh, git, oh-my-zsh, shell
:lang: es
:category: blog
:slug: oh-my-zsh
:date: 2011-11-13 1:28

He usado `zsh <http://www.zsh.org/>`__ desde hace un tiempo como mi
shell preferido en BSD. 
Hace un par de meses descubri `Oh-my-zsh <https://github.com/robbyrussell/oh-my-zsh>`__ 
y empeze a usarlo. 

Que es precisamente `Oh-my-zsh <https://github.com/robbyrussell/oh-my-zsh>`__ ?
La pagina del proyecto, lo denomina un framework para manejar tu
configuracion personal de zsh, incluye mas de 40 plugins mas 80
temas y una utileria para actualizarse periodicamente. 
Para configurar `Oh-my-zsh <https://github.com/robbyrussell/oh-my-zsh>`__ en OpenBSD 5.0
hice lo siguiente (lo mismo aplica a NetBSD, FreeBSD, excepto la
instalacion de paquetes). 

Requerimientos:
---------------

 * Git
 * zsh

.. code-block:: console

    export PKG_PATH=ftp://ftp.openbsd.org/pub/OpenBSD/5.0/packages/i386
    $ sudo pkg_add -v zsh-4.3.12 git-1.7.6p0 

Cambiamos el shell a zsh

.. code-block:: console

    $ chsh -s /usr/local/bin/zsh

Obtenemos `Oh-my-zsh <https://github.com/robbyrussell/oh-my-zsh>`__ via
github en nuestro directorio local, renombramos el directorio creado y
copiamos un .zshrc a nuestro home.

.. code-block:: console

    $ git clone git://github.com/robbyrussell/oh-my-zsh.git
    $ mv oh-my-zsh .oh-my-zsh
    $ cp .oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  

Reiniciamos nuestra sesion, o en sucaso ejecutamos zsh directamente.
Basta modificar nuestro **.zshrc** y elegir el
`Tema <https://github.com/robbyrussell/oh-my-zsh/wiki/Themes>`__ dentro
de los mas de 50 existentes y reiniciar el shell. 

zshroadmap(1) es una pagina de manual para un rapido repaso a lo mas importante de ZSH.
