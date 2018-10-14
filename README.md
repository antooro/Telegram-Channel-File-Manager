# Telegram Channel File Manager [![Python 3.6](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)


## Explicación del concepto
A partir de un sistema de archivos como este...



![alt text](https://i.imgur.com/3mN2j3u.png)



Obtén un canal ordenado en telegram con botones.



![alt text](https://i.imgur.com/9ZF4DdE.png)



Añadido sistema de archivos recientes, ideal para distinguir las novedades


![alt text](https://i.imgur.com/Gyq8Iiw.png)


## Como configurarlo 
Modifica los datos necesarios en ```config.py```

- API-KEY del bot, obtenida en @botfather

- @ del canal de telegram (EJEMPLO t.me/uno) @uno

- Ruta de la carpeta que queremos ordenar y meter en el canal

### Instalación
```
pip install -r "requirements.txt"
```



USO

```
python enviar.py
```

envia los archivos y el menu final

```
python eliminar.py
```

elimina los archivos enviados anteriormente, se usa para cuando quieres actualizar

## TODO

- Sistema para poder añadir una capa de profundidad mas en los directorios
- Compatibilidad con UTF-8 en py2.7

