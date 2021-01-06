Cadenas aleatorias en Perl
##########################

:author: Francisco Valladolid
:tags: random, string, perl, programming, tricks
:lang: es
:category: blog
:slug: random-str-perl
:date: 2021-01-04 15:10
:email: ficovh@gmail.com

La siguiente linea de codigo genera una cadena aleatoria en `perl <http://www.perl.org>`_. 

.. code-block:: perl

	print( map { ("a".."z", '0'..'9')[rand 36] } 1..4 );

Básicamente la función map itera sobre el conjunto de caracteres 'a' la 'z' y '0' al '9' generando cuatro caracteres aleatorios.
