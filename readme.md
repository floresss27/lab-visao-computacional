Lab de Visão Computacional

São aplicadas operações como:
- Detecção de contornos
- Transformações morfológicas
- Conversão entre espaços de cor

## Funções Implementadas

### `contorno(img_path)`

Aplica os seguintes passos:

1. **Leitura e conversão da imagem para RGB e tons de cinza.**
2. **Aplicação de limiarização binária inversa** com base na intensidade máxima da imagem.
3. **Operação de abertura morfológica** (remoção de ruído).
4. **Aplicação de blur** para suavizar detalhes.
5. **Detecção de bordas com Canny**, tanto na imagem original quanto na suavizada.
6. **Extração de contornos com `findContours`**.
7. **Desenho dos contornos na imagem original.**
8. **Exibição das imagens em grid com `matplotlib`.**

---

### `espacoCores(img_path)`

Realiza conversões entre espaços de cores:

1. **RGB** – Para visualização padrão com `matplotlib`.
2. **GRAYSCALE** – Tons de cinza.
3. **HSV** – Separação de matiz, saturação e valor.
4. **HLS** – Separação de matiz, luminosidade e saturação.

As imagens são mostradas lado a lado para comparação.

---

### `operadorMorfologico(img_path)`

Aplica transformações morfológicas clássicas:

1. **Conversão da imagem em RGB → blur → grayscale.**
2. **Threshold para binarização.**
3. **Criação de um kernel de 12x12 pixels.**
4. Aplicação das seguintes operações:
    - **Dilatação**
    - **Erosão**
    - **Abertura**
    - **Fechamento**
    - **Gradiente morfológico**
    - **Top Hat**
    - **Black Hat**
5. Exibição dos resultados em grid.

---
