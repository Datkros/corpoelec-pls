# CORPOELEC Please
Quieres saber a qué hora se va la luz? Usa este pequeño script para monitorear el twitter de CORPOELEC!

NOTA IMPORTANTE: No está funcionando en la version actual debido a que CORPOELEC Monagas ha decidido dejar de postear anuncios. Sin embargo, todavía pueden usar el código como referencia para escribir su propio script!

CORPOELEC Please es un pequeño script que monitorea el twitter de CORPOELEC usando la API de Twitter, revisa la infomación relevante en cada tweet que realiza la compañia, y si habla sobre restricciones de servicio (a.k.a cortes de electricidad), lo toma en cuenta y agarra el link de Twitlonger que siempre está presente en el tweet. (Ya que ellos usan Twitlonger para los anuncios). Hace web scraping de Twitlonger, obtiene el texto y envía una notificación a todos tus dispositivos a través de PushBullet.

**Dependencias:**

- requests
- Tweetpy
- lxml
- PushBullet para teléfonos inteligentes y/o PC.

**¿Cómo uso CORPOELEC Please?**

Para poder usar CORPOELEC Please, necesitar seguir los siguientes pasos:

Si no tienes conocimientos de Programación y/o no tienes Python:

1 - Primero descarga Python 2.7.11 desde la página oficial del proyecto: https://www.python.org/downloads/

2 - Luego instala pip desde https://pypi.python.org/pypi/pip 

3 - Instalas las dependencias de librerias asegúrate de que Python esté en tu PATH:
  * pip install requests
  * pip install tweetpy
  * pip install lxml

Una vez ya tienes todo lo necesario en cuanto al lenguaje de programación, vamos a obtener las APIs necesarias para conectarnos a Twitter y a PushBullet.

1 - Vamos a twitter.com y nos logeamos con nuestra cuenta de Twitter. Luego nos dirigimos a https://apps.twitter.com/ y creamos nuestra App. Llenamos todos los campos necesarios. Cuando ya la hemos creado nos vamos a la sección 'Keys and Access Tokens' en nuestra App. De aquí vamos a obtener lo siguiente:
  * Consumer Key (API Key)
  * Consumer Secret (API Secret)
  * Access Token
  * Access Token Secret

Tener en consideración que como explica Twitter, no deben compartirla con nadie porque le permite acceso a su cuenta de Twitter  y a las acciones que realiza tu app.

2 - Una vez ya hemos obtenido nuestras APIs de Twitter, vamos a necesitar PushBullet. Lo puedes descargar desde la página de PushBullet. Mientras se descarga la aplicación en nuestros dispositivos podemos logear en la página de PushBullet con nuestra cuenta de Gmail. Vamos a crear un Token de Accesso, lo puedes hacer dirigiendote a https://www.pushbullet.com/#settings bajo la sección llamada 'Access Tokens' seleccionas 'Create Access Token' y lo copias.

3 - Una vez ya tengamos estos 5 tokens, tenemos dos opciones:
  A) Definir los Tokens en el mismo script
  B) Hacerlo en otro archivo diferente (Yo lo he hecho así permitiendome compartirlo en GitHub sin arriesgar mis cuentas)
  
  Para hacerlo de la primera manera, sólo borran  (o la comentan) la siguiente sentencia: from keys import ckey, csecret, atoken, asecret, PBAccessToken  y crean las siguientes variables donde van a remplazar el texto entre comillas simples por su API:
 * ckey = 'TWITTER_CONSUMER_KEY'
 * csecret = 'TWITTER_CONSUMER_SECRET'
 * atoken = 'TWITTER_ACCESS_TOKEN'
 * asecret = 'TWITTER_ACCESS_TOKEN_SECRET'
 * PBAccessToken = 'PushBullet_AccessToken'
  
  Si quieres tenerlo en archivos diferentes: vas a crear un nuevo archivo llamado keys.py y definir las variables mencionadas en la primera manera. Este es preferido si piensas compartirlo a un amigo pero no quieres que tenga acceso a tu API personal. Es cuestión de sólo compartir el archivo principal.

Si les retorna 401, significa que hay un problema con su Token de Acceso.
  
  
A mejorar: 

- Parametros de búsqueda en los tweets. Actualmente es un poco débil
- Añade la posibilidad de seleccionar a cual dispositivos quieres enviarlo en lugar de usar broadcasting.
- Pensar muchas más cosas que mejorar.

