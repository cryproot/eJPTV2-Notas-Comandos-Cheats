# Documentación: Comandos de enumeración

## Descripción
Esta documentación proporciona una introducción básica de los comandos útlices para el examen EJPTv2

### FTP File Transfer Protocol - 21
El Protocolo de Transferencia de Archivos (FTP) es un estándar de red para transferir archivos entre sistemas, operando en el puerto 21. Aunque es antiguo y carece de seguridad, permite cargar y descargar archivos en servidores remotos

```bash
nmap -p21 --script ftp-anon IP
wget -m --no-passive ftp://anonymous:anonymous@IP
sudo nmap -sV -p21 -sC -A IP
nc IP 21
```

#### Declaración de listas
Para declarar una lista en Python, se utilizan corchetes `[]` y se separan los elementos con comas. Ejemplo:

```python
mi_lista = [1, 2, 3, 4, 5]
