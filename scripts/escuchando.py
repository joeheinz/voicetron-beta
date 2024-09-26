import os
import subprocess
import pygame
import time
import serial  # Assuming you are reading from a serial device

def generar_voz(texto):
    """
    Genera un archivo de audio .wav a partir de una cadena de texto utilizando Piper TTS.
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

def play_audio_sequence(audio_files):
    """
    Reproduce una secuencia de archivos de audio.
    """
    pygame.mixer.init()

    for audio_file in audio_files:
        print(f"Reproduciendo: {audio_file}")
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)  # Sleep to avoid busy-waiting

def play_dtmf_and_generated_voice():
    """
    Reproduce DTMF, mensaje generado y lo repite tras 5 segundos.
    """
    dtmf_tones = ['Dtmf-0.wav', 'Dtmf-9.wav', 'Dtmf-9.wav']
    mensaje_generado = 'mensaje.wav'

    play_audio_sequence(dtmf_tones + [mensaje_generado])
    time.sleep(5)
    play_audio_sequence([mensaje_generado])

def escuchar_serial_y_procesar():
    """
    Escucha indefinidamente en el puerto serial y procesa el mensaje cuando llega un string.
    """
    # Configurar el puerto serial (ajusta el puerto y baudrate a tu configuración)
    puerto_serial = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)

    while True:
        print("Esperando un mensaje por el puerto serial...")
        
        # Leer el string del puerto serial
        if puerto_serial.in_waiting > 0:
            mensaje = puerto_serial.readline().decode('utf-8').strip()
            print(f"Mensaje recibido: {mensaje}")
            
            if mensaje:
                # Generar el archivo de voz con el mensaje recibido
                generar_voz(mensaje)
                
                # Reproducir DTMF y mensaje generado
                play_dtmf_and_generated_voice()

                # Regresar a escuchar nuevos mensajes
                print("Esperando nuevos mensajes...")
        time.sleep(0.1)

# Ejecución principal
if __name__ == "__main__":
    try:
        escuchar_serial_y_procesar()
    except KeyboardInterrupt:
        print("Programa terminado por el usuario.")
