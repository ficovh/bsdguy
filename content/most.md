Title: Usando most para colorear man pages 
author: Francisco Valladolid
tags: Unix man linux netbsd openbsd freebsd pages doc
lang: es
category: blog
slug: most
date: 2021-03-23
email: ficovh@gmail.com

### Coloreando `man pages` en sistemas tipo Unix.


Las `man` pages son la documentacion oficinal para sistemas tipo Unix (BSD/Linux) el comando [man](http://man.netbsd.org/man.1) seguido del nombre de un programa muestra la documentacion para este, por ejemplo:

`$ man  echo`

[![man echo](https://i.imgur.com/QvEO7OXl.png)]()

*most* puede ser instalado con el gestor de paquetes de tu sistema operativo, en mi caso estoy usando [NetBSD](https://www.netbsd.org) y *pkgin* para instalar paquetes binarios.

```
 $ sudo pkgin in most
```
El siguiente paso es definir el paginador por default en el archivo de configuracion de nuestro shell, en mi caso *zsh*, por ejemplo:

```
 echo "export PAGER=most" >> ~/.zshrc
 source .zshrc
```
Ahora, la proxima vez que se invoque el comando *man echo* la pagina del manual del comando *echo* tendrà una apariencia distinta e incluira colores en la estructura.

[![man echo](https://i.imgur.com/OUO7qIKl.jpg)]()

