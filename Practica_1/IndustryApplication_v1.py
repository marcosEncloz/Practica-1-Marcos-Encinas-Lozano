import json
import os
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import csv

###########################################
class SensorReceiver:
    def __init__(self, broker, port, topics):
        
        self.broker = broker
        self.port = port
        self.topics = topics
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message= self.on_message
        self.data_log = []

#################################################

    # Configuración del cliente MQTT
    BROKER = "broker.emqx.io"  # Cambia esto por tu broker MQTT
    PORT = 1883  # Puerto del broker MQTT
    TOPICS = ["sensor/data/sen55", "sensor/data/gas_sensor"]  # Temas a los que se suscribirá el cliente       

###################################################

    def crear_carpeta_resultados(self):
        if not os.path.exists("resultados"):
            os.makedirs("resultados")


# Callback cuando se establece la conexión con el broker
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Conexión exitosa al broker MQTT")
            # Suscribirse a los temas
            for topic in self.topics:
                client.subscribe(topic)
                print(f"Suscrito al tema '{topic}'")
        else:
            print(f"Error de conexión, código: {rc}")

# Callback cuando se recibe un mensaje en los temas suscritos
    def on_message(self, client, userdata, msg):
        print(f"Mensaje recibido en el tema '{msg.topic}':")
        print(msg.payload.decode("utf-8"))

        try:
            # Decodificar y convertir el mensaje de JSON a diccionario
            payload = json.loads(msg.payload.decode("utf-8"))
            print(json.dumps(payload, indent=4))  # Mostrar el mensaje formateado
            self.data_log.append(payload)
        except json.JSONDecodeError as e:
            print(f"Error decodificando JSON: {e}")


    def start(self):
        self.client.connect(self.broker, self.port, 60)
        print("Esperando mensajes... Presiona Ctrl+C para salir")
        try:
            self.client.loop_forever()
        except KeyboardInterrupt:
            print("Desconectando del broker...")
            self.client.disconnect()


    def save_to_json(self, ruta="resultados/datos_sensores.json"):
        self.crear_carpeta_resultados()
        with open(ruta, "w") as f:
            json.dump(self.data_log, f)


    def save_to_csv(self, filename="resultados/datos_sensores.csv"):
        self.crear_carpeta_resultados()
        if self.data_log:
            keys = self.data_log[0].keys()
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(self.data_log)
            print(f"Datos guardados en {filename}")




    def graficar_temperatura(self, ruta="resultados/grafica_temperatura.png"):
        temperaturas = [d["AmbientTemperature"] for d in self.data_log if "AmbientTemperature" in d]
        plt.plot(temperaturas)
        plt.title("Evolución de la temperatura")
        plt.xlabel("Muestras")
        plt.ylabel("Temperatura (°C)")
        plt.grid(True)
        plt.savefig(ruta)
        plt.close()

    def graficar_humedad(self, ruta="resultados/grafica_humedad.png"):
        humedad = [d["AmbientHumidity"] for d in self.data_log if "AmbientHumidity" in d]
        plt.plot(humedad, color="blue")
        plt.title("Evolución de la humedad")
        plt.xlabel("Muestras")
        plt.ylabel("Humedad (%)")
        plt.grid(True)
        plt.savefig(ruta)
        plt.close()

    def graficar_pm25(self, ruta="resultados/grafica_pm25.png"):
        pm25 = [d["MassConcentrationPm2p5"] for d in self.data_log if "MassConcentrationPm2p5" in d]
        plt.plot(pm25, color="green")
        plt.title("Concentración de PM2.5")
        plt.xlabel("Muestras")
        plt.ylabel("µg/m³")
        plt.grid(True)
        plt.savefig(ruta)
        plt.close()

    def graficar_gas(self, gas_name, ruta=None):
        gas_values = [d[gas_name] for d in self.data_log if gas_name in d]
        plt.plot(gas_values, label=gas_name)
        plt.title(f"Evolución de {gas_name}")
        plt.xlabel("Muestras")
        plt.ylabel("Intensidad")
        plt.grid(True)
        plt.legend()
        if ruta is None:
            ruta = f"resultados/grafica_{gas_name}.png"
        plt.savefig(ruta)
        plt.close()

    def guardar_todo(self):
        self.save_to_json()
        self.save_to_csv()
        self.graficar_temperatura()
        self.graficar_humedad()
        self.graficar_pm25()
        self.graficar_gas("GM102B")


if __name__ == "__main__":
    receiver = SensorReceiver(
        broker="broker.emqx.io",
        port=1883,
        topics=["sensor/data/sen55", "sensor/data/gas_sensor"]
    )
    try:
        receiver.start()
    except KeyboardInterrupt:
        receiver.guardar_todo()
        print("Datos guardados y gráficas generadas en la carpeta 'resultados/'.")

