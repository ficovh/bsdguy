Solarized Vim
#####################
:author: Francisco Valladolid
:tags: openbsd, vi, netbsd, unix, bsd, linux
:lang: es
:category: blog
:slug: solarized-vim
:date: 2012-02-15 10:20


Solarized es un paleta de dieciseis colores para uso en la
terminal (xterm, gterminal, etc) y la interfaz grafica de usuario. --
tomado del `website: <http://ethanschoonover.com/solarized>`__ Vim es mi
editor favorito, corriendo bajo X podemos cambiar la configuracion de
colores en la edicion usando el proyecto Solarized. 

Requisitos:
 * Vim
 * Git 

Descargamos solarized para vim desde Github.

.. code-block:: console

    % git clone git://github.com/altercation/vim-colors-solarized.git

Esto creara un subdirectorio llamado vim-colors-solarized en nuestro
/home y nosotros crearemos los directorios necesarios para usar la nueva
configuracion de colores.

.. code-block:: console

    % mkdir ~/.vim
    % mkdir ~/.vim/colors ~/.vim/autoload
    % cp ~/vim-colors-solarized/colors/solarized.vim ~/.vim/colors
    % cp ~/vim-colors-solarized/autoload/toglebg.vim ~/.vim/autoload

Un sencillo ~/.vimrc queda de la siguiente forma.

.. code-block:: console

    syntax enable
    set background=dark
    colorscheme solarized

De esta forma tenemos una mejor combinacion de colores al momento de
editar programas, usando **gvim** tambien suele ser muy comodo.
Disfrutalo.

