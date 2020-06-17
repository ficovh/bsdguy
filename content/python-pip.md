Title: Python tips 
author: Francisco Valladolid
tags: python, oop, pip, modules, programming, openbsd, bsd
lang: es
category: blog
slug: python-pip
date: 2020-06-17
email: ficovh@gmail.com

Recién instalé [OpenBSD-6.7](https://www.openbsd.org) en mi computadora personal, acto seguido instalé [Python](http://www.python.org)
desde la rama estable de paquetes.

Por alguna razón [Python-3.8](http://www.python.org) no incluye [pip](https://www.pypi.org/project/pip) por default, encontre una forma
rápida de instalar el modulo.

    $ python3.8 -m ensurepip --default-pip
    $ python3.8 -m pip install --upgrade pip

Estas instrucciones istalan [pip]("https://www.pypi.org/project/pip) y despues actualiza el mismo.

