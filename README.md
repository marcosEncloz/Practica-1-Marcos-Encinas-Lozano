# Practica-1-Marcos-Encinas-Lozano

_____________
+ Objetivos del sistema:
_____________

Enviar y recibir mensajes entre nodos Meshtastic.

Recibir datos de sensores (temperatura, humedad, gases) vía MQTT.

Almacenar mensajes, posiciones GPS y datos en formato JSON y CSV.

Visualizar gráficas de evolución ambiental.

Automatizar la organización de resultados para entrega profesional.

_____________
+ Estructura del proyecto:
_____________

Código

├── supervivencia.py ------------> # Menú principal del sistema

├── SistemaComunicacion.py ------------> # Comunicación Meshtastic (envío y recepción)

├── IndustryApplication_v1.py ------------> # Recepción de datos de sensores vía MQTT

├── interfazterminal.py ------------> # Interfaz CLI para modo y acción

_____________
+ Ejecución:
_____________

Desde terminal, ejecutar:
supervivencia.py y aparecerá el siguiente menú en el cual se puede seleccionar laaccion que quiere llevar a cabo:

--- MENÚ PRINCIPAL ---
1. Recibir datos por MQTT
2. Enviar mensaje por Meshtastic
3. Recibir mensajes por Meshtastic
4. Salir

_____________
+ Ejemplos de uso:
_____________

Opción 1: Recibe datos de sensores y guarda en resultados/datos_sensores.json y .csv.

Opción 2: Envía un mensaje a todos los nodos Meshtastic conectados.

Opción 3: Escucha mensajes entrantes en el canal Meshtastic.

Opción 4: Finaliza el programa.

_____________
+ Resultados generados:
_____________

datos_sensores.json: historial de datos ambientales.

datos_sensores.csv: versión tabular para análisis.

grafica_temperatura.png, grafica_humedad.png, etc.: visualización de evolución ambiental.

Mensajes y posiciones GPS recibidas se almacenan en JSON.

_____________
+ Diseño y documentación:
_____________

Consulta el informe PDF adjunto para:

Diagrama UML de clases.

Flujo de mensajes entre dispositivos.

Capturas de terminal en ejecución.

Evidencia de archivos generados.


------------------------------
Marcos Encinas Lozano

Universidad de Burgos

Programacion orientada a objetos

22/10/2025
