# Documentación: Comandos de enumeración

## Descripción
Esta documentación proporciona una introducción básica de los comandos útlices para el examen EJPTv2

### FTP File Transfer Protocol - 21
El Protocolo de Transferencia de Archivos (FTP) es un estándar de red para transferir archivos entre sistemas, operando en el puerto 21. Aunque es antiguo y carece de seguridad, permite cargar y descargar archivos en servidores remotos

```python
nmap -p21 --script ftp-anon IP
wget -m --no-passive ftp://anonymous:anonymous@IP
sudo nmap -sV -p21 -sC -A IP
nc IP 21
```

#### Diccionarios
Lista de palabras para ataques de fuerza bruta

```python
/usr/share/metasploit-framework/data/wordlists/common_users.txt
/usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
```

