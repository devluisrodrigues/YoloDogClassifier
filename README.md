# Projeto para detecçao de raças de cachorros

## Descrição do Projeto
<!-- Python com Yolov11 -->
O Projeto foidesenvolvido para estudo individual, com o objetivo de classificar raças de cachorros. O projeto foi desenvolvido utilizando Python e a biblioteca Yolov11.

O dataset utilizado foi o Stanford Dogs Dataset, que contém 20.580 imagens de 120 raças de cachorros. O qual pode ser encontrado no link: https://www.kaggle.com/jessicali9530/stanford-dogs-dataset

---

## Pré-requisitos

Crie um ambiente virtual e instale as dependências do projeto:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

É importante ressaltar que o dataset foi pré-catalogado, de modo que as imagens já estão separadas por raças. Além disso, para cada imagem foi criado um arquivo de texto com as coordenadas dos objetos presentes na imagem.

Como o dataset original é imenso, para fins de estudo, foi feito um recorte de 10 raças de cachorros, totalizando 1639 imagens e outros 1639 arquivos de texto com as coordenadas dos objetos.

Esse recorte do dataset pode ser encontrado dentro da pasta "dataset". Ele foi dividido em 80% para treino e 20% para teste, e sua estrutura é a seguinte:

```
dataset
│
|   data.yaml
|
└───train
│   └───images
│   │   │   n02085620_7.jpg
│   │   │   n02085620_8.jpg
│   │   │   ...
│   └───labels
│       │   n02085620_7.txt
│       │   n02085620_8.txt
│       │   ...
│
└───val
    └───images
    │   │   n02085620_326.jpg
    │   │   n02085620_1455.jpg
    │   │   ...
    └───labels
        │   n02085620_326.txt
        │   n02085620_1455.txt
        │   ...
```

*OBS: Visto que o dataset já está com a estrutura correta, não é necessário realizar a etapa `Preparando o dataset` do notebook training.*

As raças de cachorros escolhidas para o treinamento do modelo foram:

1. Chihuahua
2. Shih-Tzu
3. Yorkshire Terrier
4. Golden Retriever
5. Border Collie
6. Rottweiler
7. Doberman
8. Boxer
9. Great Dane
10. Pug

---

### Treinando o modelo

Para treinar o modelo, basta executar o notebook `training.ipynb`. O modelo será treinado com as 10 raças de cachorros presentes no dataset.
O notebook foi dividido em 2 partes:

1. Preparando o dataset:

    Essa etapa é reponsável por receber o dataset original, tal como foi baixado do Kaggle, separar as raças de cachorros desejadas e criar a estrutura de pastas necessária para o treinamento do modelo (tal como foi descrito acima).

2. Treinando o modelo:

    Essa etapa é responsável por treinar o modelo com as imagens e labels presentes no dataset. Para isso, foi utilizado um modelo pré-treinado, que pode ser encontrado no link: https://docs.ultralytics.com/tasks/detect/

    A partir desse modelo, foi feito o fine-tuning com as imagens do dataset.

    Um modelo pré-treinado "zerado", sem fine-tuning, foi disponibilizado dentro da pasta training, para que seja possível realizar o treinamento sem a necessidade de baixar um modelo pré-treinado do site da Ultralytics.

---

### Testando o modelo

Para o teste do modelo, basta acessar a pasta `Detection` e executar o notebook `detection.ipynb`. Nesse notebook, o modelo treinado será carregado e testado com imagens de teste. 

Foram utilizadas imagens das raças de cachorros escolhidas para o treinamento do modelo, e o modelo foi testado com imagens inéditas, que não foram utilizadas no treinamento.

As imagens abaixo são exemplos da detecção de raças de cachorros feita pelo modelo:

![detection1](/Detection/imagensExemplo/Detected/YorkShire.png)

![detection2](/Detection/imagensExemplo/Detected/Shih-tzu.png)
