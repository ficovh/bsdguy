Title: getopt in C
author: Francisco Valladolid
tags: C function programming arguments posix 
lang: es
category: blog
slug: getops
date: 2021-03-12
email: ficovh@gmail.com

### Funcion getopt en C - Linux/BSD y variantes unicamente.

### Definición.

 **getopt()** es una función escrita en lenguaje C para analizar argumentos en la linea de comandos.

### Sintaxis.
```
  getopt(int argc, char *const argv[], const char *optstring)

  Donde optstring es una lista de caracteres, 
  cada uno representando una opción.
```

### Valores de retorno.

La funcion *getopt()* regresa diferentes valores.

* Si la opcion toma un valor en la linea de comandos, el valor es un puntero
a la variable externa **optarg**

* '-1' Si no hay mas argumentos.
* '?' Valor no reconocido y almacenado en la variable optopt
* if una opcion requiere un valor (-f archivo.txt) y no existe tal, entonces **getopt()** regresa un '?'

* Si colocamos ':' como primer caracter en la lista de argumentos **optstring** *getopt()* regresa
':' en lugar de '?' cuando no hay ningun valor.

Normalmente *getopt()* es llamada dentro de un ciclo condicional, el ciclo termina cuando la función regresa -1

*switch()* es usada entonces con el valor regresado por la funcion *getopt()* y evalua las opciones dadas.

un segundo ciclo es usado para procesar los argumentos extra que no pudieron ser procesados en el primer ciclo.

A continuación, el siguiente ejemplo escrito en C ilustra la función correctamente.

### Ejemplo:

```
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	int opt;
	while((opt=getopt(argc, argv, ":if:lxr")) != -1)
	{
		switch(opt)
		{
			case 'i':
			case 'l':
			case 'r':
				printf("opcion: %c\n", opt);
				break;
			case 'f':
				printf("nombre del archivo: %s\n", optarg);
				break;
			case ':':
				printf("Se necesita un valor\n");
				break;
			case '?':
				printf("Opcion Desconocida: %c\n", optopt);
				break;
		}
	}
	for(; optind < argc; optind++){
		printf("argumentos extra: %s\n", argv[optind]);
	}

	return 0;
}

```
