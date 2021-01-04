Cadenas aleatorias en Perl
#################################

:author: Francisco Valladolid
:tags: random, string, perl, programming, tricks
:lang: es
:category: blog
:slug: random-str-perl
:date: 2021-01-04 15:10

El siguiente codigop genera cadenas aleatorioas en `perl <http://www.perl.or">` 


.. code-block:: perl

	print( map { ("a".."z", '0'..'9')[rand 36] } 1..4 );


