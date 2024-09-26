import os
import subprocess

import serial

def leer_desde_serial():
    # Configurar el puerto serie
    puerto_serial = serial.Serial(
        port='/dev/serial0',  # Puede ser '/dev/ttyS0' o '/dev/serial0' dependiendo de tu configuración
        baudrate=9600,        # Velocidad de transmisión
        timeout=1             # Tiempo de espera para leer datos (en segundos)
    )
    
    try:
        print("Esperando datos desde el puerto serie...")
        while True:
            # Leer datos desde el puerto serie
            if puerto_serial.in_waiting > 0:
                data = puerto_serial.readline().decode('utf-8').strip()
                if data:
                    print(f"Recibido: {data}")
                    # Puedes retornar el string recibido o procesarlo aquí
                    return data
    except KeyboardInterrupt:
        print("Interrumpido por el usuario.")
    finally:
        puerto_serial.close()

# Llamar a la función para leer desde el puerto serial
#mensaje = leer_desde_serial()
#print(f"Mensaje recibido: {mensaje}")
print("Leer mensaje desde el serial:")




def generar_voz(texto):
    """
    Genera un archivo de audio .wav a partir de una cadena de texto utilizando Piper TTS.
    
    :param texto: Cadena de texto que será convertida en audio.
    :return: None
    """
    # Definir la ruta del modelo y el archivo de salida
    model_path = "/home/joseheinz/Documents/piper/voices/aldo.onnx"
    output_file = "/home/joseheinz/Documents/piper/scripts/mensaje.wav"
    piper_executable = "/home/joseheinz/Documents/piper/piper/piper"

    # Verificar si el archivo de modelo existe
    if not os.path.isfile(model_path):
        print(f"Error: El archivo de modelo '{model_path}' no existe.")
        return

    print(f"El archivo de modelo '{model_path}' fue encontrado.")

    # Ejecutar el comando para generar el archivo de audio con el texto proporcionado
    command = f"echo '{texto}' | {piper_executable} --model {model_path} --output_file {output_file}"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Archivo de salida generado en '{output_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")
        
import pygame
import time       
        
def play_dtmf_sequence():
    # Initialize pygame mixer
    pygame.mixer.init()

    # List of DTMF tones to play in sequence
    tones = ['Dtmf-0.wav', 'Dtmf-9.wav', 'Dtmf-9.wav', 'mensaje.wav']

    # Play each tone in the list
    for tone in tones:
        pygame.mixer.music.load(tone)
        pygame.mixer.music.play()
        # Wait until the tone is finished playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)  # Sleep briefly to avoid busy-waiting

# Call the function to play the sequence


# Ejemplo de uso:
texto = input("Escuchando: ")
generar_voz(texto)

play_dtmf_sequence()
