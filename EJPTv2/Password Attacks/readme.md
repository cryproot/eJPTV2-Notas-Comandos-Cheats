# Password Attacks o Ataques de Contraseña
## Descripción
MSFVENOM es una herramienta que viene integrada en metasploit framework que sirve principalmente para crear payloads, podemos ver algunos ejemplos con enconders para darle algo mas de sabor.

### WinRM (5985 HTTP y 5986 HTTPS)
```python
crackmapexec winrm IP -u user.list -p password.list
evil-winrm -i IP -u user -p password (tenemos credenciales arriba y esto es para hacer login)
