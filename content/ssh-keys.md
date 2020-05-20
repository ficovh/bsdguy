Title: Generando llaves SSH
author: Francisco Valladolid
tags: openbsd, zsh, git, shell, ssh, keys, rsa, ed_25519
lang: es
category: blog
slug: ssh-keys
date: 2020-05-17

## Generando llaves SSH


Use el comando [ssh-heygen(1)](https://man.openbsd.org/ssh-keygen.1) para crear un par de llaves e introduzca una contraseña de seguridad.


    $  ssh-keygen -o -t ed25519 -a 100 -f ~/.ssh/id_ed25519 
    Generating public/private ed25519 key pair.
    Enter file in which to save the key (/Users/userX/.ssh/id_ed25519):
    Generating public/private ed25519 key pair.
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in ~/.ssh/id_ed25519.
    Your public key has been saved in ~/.ssh/id_ed25519.pub.
    The key fingerprint is:
    SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx comment
    The key's randomart image is:
    +--[ED25519 256]--+
    |       .o=@*=    |
    |        oX = .=  |
    |        * o +    |
    |       = o =     |
    |        S o +    |
    |       * + o     |
    |      = X.o.=    |
    |       O =+o     |
    |      . E++++    |
    +----[SHA256]-----+
    $

    -o Graba la llave privada usando el nuevo formato de OpenSSH  
    -t indica el tipo de llave, en este caso ed25519.
    -a 100  especifica el numero de "rounds" KDF (Key derivation function)
	-f especifica el nombre del archivo
		
### Puedes copiar la nueva llave al clipboard para subirla a Github/Gitlab.

	en OSX
	$ pbcopy < ~/.ssh/id_ed25519.pub
 
	en OpenBSD
	$ xclip -selection clipboard ~/.ssh/id_ed25519.pub

Listo, ahora ya tenemos nuestras llaves SSH usando el algoritmo ed25519 para mayor seguridad.
