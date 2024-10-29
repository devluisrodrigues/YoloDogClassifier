from ultralytics import YOLO
import torch
# Load model
model = YOLO('yolo11n.pt')

# testa se o CUDA está disponível
if __name__ == '__main__':

    results = model.train(
        data='C:/Users/luis/Documents/pessoal/yoloProject/dataset/data.yaml',      # Caminho para o arquivo data.yaml que criamos
        epochs=50,             # Número de épocas de treino (ajuste conforme necessário)
        imgsz=640,             # Tamanho da imagem de entrada
        batch=16,              # Tamanho do batch (ajuste conforme memória disponível)
        workers=4            # Número de workers para carregamento dos dados
    )

    # Salva o modelo treinado
    model.save('yolo11n.pt')
    