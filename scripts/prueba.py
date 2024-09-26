import os
import subprocess

def generar_audio_no_problemas(direccion, kilometro, defectos, ejes, velocidad, temperatura):
    # Definir la ruta del modelo y el archivo de salida
    model_path = "/home/joseheinz/Documents/piper/voices/aldo.onnx"
    output_file = "/home/joseheinz/Documents/piper/scripts/mensaje.wav"
    piper_executable = "/home/joseheinz/Documents/piper/piper/piper"

    # Verificar si el archivo de modelo existe
    if not os.path.isfile(model_path):
        print(f"Error: El archivo de modelo '{model_path}' no existe.")
        return

    print(f"El archivo de modelo '{model_path}' fue encontrado.")

    # Verificar los permisos del archivo
    if not os.access(model_path, os.R_OK):
        print(f"Error: El archivo de modelo '{model_path}' no tiene permisos de lectura.")
        print("Intentando ajustar los permisos...")
        try:
            os.chmod(model_path, 0o644)
            print(f"Permisos ajustados para '{model_path}'.")
        except Exception as e:
            print(f"No se pudieron ajustar los permisos: {e}")
            return
    else:
        print(f"El archivo de modelo '{model_path}' tiene permisos de lectura adecuados.")

    # Ejecutar el comando para generar el archivo de audio con los valores modificados
    command = f"""echo 'DETECTOR FXE, DIRECCION {direccion}, KILOMETRO {kilometro}, NO TIENE DEFECTOS, TOTAL DEFECTOS
ENCONTRADOS, {defectos}, TOTAL DE EJES {ejes}, VELOCIDAD DEL TREN {velocidad} KILOMETROS POR HORA, TEMPERATURA {temperatura}
GRADOS, FIN DE MENSAJE.' | {piper_executable} --model {model_path} --output_file {output_file}"""
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Archivo de salida generado en '{output_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")
        


def generar_mensaje_alto_impacto(direccion,riel, kilometro, carro, eje, defectos, ejes, velocidad, temperatura):
    # Definir la ruta del modelo y el archivo de salida
    model_path = "/home/joseheinz/Documents/piper/voices/aldo.onnx"
    output_file = "/home/joseheinz/Documents/piper/scripts/mensaje.wav"
    piper_executable = "/home/joseheinz/Documents/piper/piper/piper"

    # Verificar si el archivo de modelo existe
    if not os.path.isfile(model_path):
        print(f"Error: El archivo de modelo '{model_path}' no existe.")
        return

    print(f"El archivo de modelo '{model_path}' fue encontrado.")

    # Ejecutar el comando para generar el archivo de audio con los valores modificados
    command = f"""echo ' DETECTOR FXE, DIRECCION {direccion}, KILOMETRO {kilometro}, ALTO IMPACTO RIEL
{riel}, CARRO {carro}, EJE {eje} DESDE EL FRENTE DEL TREN.
DETECTOR FXE, DIRECCION {direccion}, KILOMETRO {kilometro}, ALTO IMPACTO RIEL {riel} CARRO {carro}
EJE {eje} DESDE EL FRENTE DEL TREN. TOTAL DEFECTOS ENCONTRADOS {defectos}, TOTAL DE EJES {ejes},
VELOCIDAD DEL TREN {velocidad} KILOMETROS POR HORA, TEMPERATURA {temperatura} GRADOS, FIN DE MENSAJE.' | {piper_executable} --model {model_path} --output_file {output_file}"""
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Archivo de salida generado en '{output_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")


def generar_mensaje_carga_desbalanceada(direccion,riel, kilometro, carro, eje, defectos, ejes, velocidad, temperatura):
    # Definir la ruta del modelo y el archivo de salida
    model_path = "/home/joseheinz/Documents/piper/voices/aldo.onnx"
    output_file = "/home/joseheinz/Documents/piper/scripts/mensaje.wav"
    piper_executable = "/home/joseheinz/Documents/piper/piper/piper"

    # Verificar si el archivo de modelo existe
    if not os.path.isfile(model_path):
        print(f"Error: El archivo de modelo '{model_path}' no existe.")
        return

    print(f"El archivo de modelo '{model_path}' fue encontrado.")

    # Ejecutar el comando para generar el archivo de audio con los valores modificados
    command = f"""echo 'DETECTOR FXE, DIRECCION {direccion}, KILOMETRO {kilometro}, CARGA
DESBALANCEADA, RIEL {riel}, CARRO {carro}, EJE {eje}, DESDE EL FRENTE DEL TREN.
DETECTOR FXE, DIRECCION {direccion}, KILOMETRO {kilometro}, CARGA DESBALANCEADA, RIEL {riel},
CARRO {carro}, EJE {eje}, DESDE EL FRENTE DEL TREN. TOTAL DEFECTOS ENCONTRADOS {defectos}, TOTAL
DE EJES {ejes}, VELOCIDAD DEL TREN {velocidad} KILOMETROS POR HORA, TEMPERATURA {temperatura} GRADOS, FIN DE MENSAJE.' | {piper_executable} --model {model_path} --output_file {output_file}"""
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Archivo de salida generado en '{output_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")






# Ejemplo de uso:
generar_mensaje_carga_desbalanceada("SUR","DERECHO" ,"T 324", 43, 54, 3, 19,51,32)
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
play_dtmf_sequence()
