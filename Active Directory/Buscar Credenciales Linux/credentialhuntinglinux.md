# Buscar Credenciales Linux
## Descripción
La búsqueda de credenciales es uno de los primeros pasos una vez que tenemos acceso al sistema. Estas frutas al alcance de la mano pueden otorgarnos privilegios elevados en cuestión de segundos o minutos

### Buscar credenciales en archivos de configuración
```python
for l in $(echo ".conf .config .cnf");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done
```
### Credenciales en archivos de configuración de forma directa
```python
for i in $(find / -name *.cnf 2>/dev/null | grep -v "doc\|lib");do echo -e "\nFile: " $i; grep "user\|password\|pass" 
```
### Buscar archivos txt
```python
find / -type f -name "*.txt"
find /home/* -type f -name "*.txt" -o ! -name "*.*"
```
### Buscar scripts
```python
for l in $(echo ".py .pyc .pl .go .jar .c .sh");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share";done
```
### Buscar claves privadas y publicas SSH
```python
grep -rnw "PRIVATE KEY" /home/* 2>/dev/null | grep ":1" (claves privadas)
grep -rnw "ssh-rsa" /home/* 2>/dev/null | grep ":1" (claves publicas)
```
Cada vez que poner guardar credenciales en el navegador, firefox lo almacena localmente de forma cifrada, hay una herramienta llamada firefox decrypt que puedo romperlo :https://github.com/unode/firefox_decrypt
### Credenciales almacenadas en firefox
```python
ls -l .mozilla/firefox/ | grep default (en uno de los directorios que veas logins.json lo pones abajo)
cat .mozilla/firefox/1bplpd86.default-release/logins.json | jq .
python3.9 firefox_decrypt.py (decifrar contraseñas de firefox)
```
