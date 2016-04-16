# CORPOELEC Please
Quieres saber a qué hora se va la luz? Usa este pequeño script para monitorear el twitter de CORPOELEC!

CORPOELEC Please es un pequeño script que monitorea el twitter de CORPOELEC usando la API de Twitter, revisa la infomación relevante en cada tweet que realiza la compañia, y si habla sobre restricciones de servicio (a.k.a cortes de electricidad), lo toma en cuenta y agarra el link de Twitlonger que siempre está presente en el tweet. (Ya que ellos usan Twitlonger para los anuncios). Hace web scraping de Twitlonger, obtiene el texto y envía una notificación a todos tus dispositivos a través de PushBullet.

**Dependencias:**

- requests
- Tweetpy
- lxml
- PushBullet para teléfonos inteligentes y/o PC.

A mejorar: 

- Parametros de búsqueda en los tweets. Actualmente es un poco débil
- Añade la posibilidad de seleccionar a cual dispositivos quieres enviarlo en lugar de usar broadcasting.
- Pensar muchas más cosas que mejorar.

