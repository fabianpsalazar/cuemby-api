# cuemby-api

Leer!

Funcion canBeSplitted adjunta en la misma carpeta de cuemby-api, alojada como canBesplitted.py.

API fifa alojada en carpeta cuemby-api desarrollado con Django, con las solicitudes get y post respectivas acerca de los jugadores y equipos.
Pages, TotalPages, Items, TotalItems, para este modelo solicite explicacion dado que TotalPages, Items y TotalItems en la API
de Fifa son variables constantes y no entendia como actuaban o tenian relevancia dentro de la base de datos, asi que opte por 
guardar y desarrollar metodos get y post para los jugadaores,nacionalidades, equipos, posiciones que eran las variables relevantes 
dentro de las solicitudes. Adicionalmente se realizo Token Authentication. Adjunto Imagenes de testeo para get y post de la API con POSTMAN.
Dado que se uso postgresql localmente, adjunte dentro de las views un metodo para guardar los datos pedidos de la API de fifa en la base de 
datos de preferencia de manera automatica al hacer las migraciones, este metodo solo se ejecutar para la primera migracion, luego es conveniente
comentarlo o desadjuntarlo, o crear un switch para cada vez que se detecta una base de datos vacia(Cualquiera de estas dependiendo de la conveniencia).
De antemano gracias por la atencion prestada!

Adjunto API EN funcionamiento con postman
![unautho](https://user-images.githubusercontent.com/23225354/128450598-a9542b4c-279d-4198-8186-3a6e6ced5d9c.png)
![token](https://user-images.githubusercontent.com/23225354/128450625-157e56ca-bf2f-456c-8ae9-0264e0817ffc.png)
![acces](https://user-images.githubusercontent.com/23225354/128450670-513a6c7f-af84-467f-834f-9c8434d23327.png)
![post](https://user-images.githubusercontent.com/23225354/128450677-972078d4-69af-4035-a6d3-94a735bb9884.png)
![post2](https://user-images.githubusercontent.com/23225354/128450683-939534af-5322-4ba6-9c68-3e1f1a37e496.png)
![get](https://user-images.githubusercontent.com/23225354/128450692-f27cabc7-3e05-4d6f-b62e-c3cf15198481.png)



