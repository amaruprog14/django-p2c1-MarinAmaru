Pregunta 1
Explique el recorrido de una solicitud desde /resumen-zonas/ hasta la respuesta HTML. Mencione la
URL, la View, el contexto y el Template.

Respuesta: Al apretar resumen se tira la solicitud a la view que carga todo lo necesario para mostrar desde los Json, que lo lleva en el contexto hacia el template llamado "resumen_zonas".

Pregunta 2
Indique el archivo y la parte de su código donde cuenta dispositivos y suma consumo_kwh por zona.
Explique brevemente cómo funciona.

Respuesta: En la view en la funciuon detalle_zona cuento el total de consumo_kwh usaldo el sum, donde si hay coincidencia del id del dispositivo y de la zona, suma el total que hay en esa zona solamente.

Pregunta 3
Indique la condición utilizada para definir el estado de una zona y explique qué ocurre cuando una zona
no tiene dispositivos.

Respuesta: Cuando una zona no tiene dispositivos, muestra que no hay dispositivos disponibles en esa zona actualmente. La condicion utilizada fue un if donde si el consumo total de la zona supera el limite muestra que el mensaje de que lo excedio, y si no el ese ejecuta el mensaje que esta bien.