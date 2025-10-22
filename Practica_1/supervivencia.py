import os
from IndustryApplication_v1 import SensorReceiver
from SistemaComunicacion import SistemaComunicacion

# Crear carpeta resultados si no existe
os.makedirs("resultados", exist_ok=True)

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Recibir datos por MQTT")
    print("2. Enviar mensaje por Meshtastic")
    print("3. Recibir mensajes por Meshtastic")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
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

        elif opcion == "2":
            mensaje = input("Escribe el mensaje a enviar: ")
            comunicador = SistemaComunicacion()
            comunicador.enviar_mensaje(mensaje)

        elif opcion == "3":
            comunicador = SistemaComunicacion()
            comunicador.recibir_mensajes()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
