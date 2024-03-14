# Generando Shell TTY con Python

## Descripción
Cuando ingresamos al shell del sistema (despues de una explotación, en este caso linux o aveces windows), notamos que no hay ningún mensaje presente, pero aún podemos emitir algunos comandos del sistema. Este es un caparazón típicamente conocido como non-tty shell. Estos shells tienen una funcionalidad limitada y a menudo pueden impedir el uso de comandos esenciales como su( switch user) y sudo( super user do), que probablemente necesitaremos si buscamos aumentar los privilegios. Esto sucedió porque el usuario de Apache ejecutó la carga útil en el objetivo. Nuestra sesión se establece como usuario de apache. Normalmente, los administradores no acceden al sistema como usuarios de Apache, por lo que no es necesario definir un lenguaje de intérprete de shell en las variables de entorno asociadas con Apache.

```python
python -c 'import pty; pty.spawn("/bin/sh")' 
```
