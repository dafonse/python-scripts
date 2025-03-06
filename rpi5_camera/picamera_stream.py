import cv2
from picamera2 import Picamera2

# Inicializa a câmera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration())

# Inicia a captura
picam2.start()

while True:
    frame = picam2.capture_array()

    # Mostra o frame em uma janela OpenCV
    cv2.imshow("Camera OV5647 - Raspberry Pi 5", frame)

    # Encerra se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Finaliza a captura e fecha janelas
picam2.stop()
cv2.destroyAllWindows()
