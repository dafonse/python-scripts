import cv2

# Inicializa a câmera usando o dispositivo padrão do Ubuntu 24 no Raspberry Pi
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Usa Video4Linux2 (V4L2) para compatibilidade

# Define a resolução do vídeo (opcional, ajuste conforme necessário)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not camera.isOpened():
    print("Erro: Não foi possível abrir a câmera.")
    exit()

print("Pressione 'q' para sair.")

# Loop para capturar e exibir o vídeo
while True:
    ret, frame = camera.read()

    if not ret:
        print("Erro ao capturar o frame.")
        break

    # Exibe o vídeo em uma janela
    cv2.imshow("Camera OV5647 - Raspberry Pi 5", frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha todas as janelas
camera.release()
cv2.destroyAllWindows()
