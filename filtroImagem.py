import skimage.io as io
import numpy as np
import os
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

def main():
    
    imagem = io.imread("Sinais/imagem.jpg")
    imagemCinza = rgb2gray(imagem)

    #Fitros
    filtroBordas = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    filtroSuavizacao = (1/9) * np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    # Aplicando filtro usando a função convolucao
    filtroBordasAplicado = convolucao(imagemCinza, filtroBordas)
    filtroSuavAplicado = convolucao(imagemCinza, filtroSuavizacao)

    # Calculando os valores máximos e mínimos na saída
    maxf1 = filtroBordasAplicado.max()
    minf1 = filtroBordasAplicado.min()

    maxf2 = filtroSuavAplicado.max()
    minf2 = filtroSuavAplicado.min()

    # Normalizando a imagem resultante
    resultadoFiltro1 = (filtroBordasAplicado - minf1) / (maxf1 - minf1)
    resultadoFiltro2 = (filtroSuavAplicado - minf2) / (maxf2 - minf2)
    
    showImg(imagemCinza, resultadoFiltro1, resultadoFiltro2)

# Função de convolução
def convolucao(imagem, kernel):
    altura, largura = imagem.shape
    altura_kernel, largura_kernel = kernel.shape
    margem_altura = altura_kernel // 2
    margem_largura = largura_kernel // 2

    resultado = np.zeros_like(imagem, dtype=np.float64)

    for i in range(margem_altura, altura - margem_altura):
        for j in range(margem_largura, largura - margem_largura):
            regiao_interesse = imagem[i - margem_altura:i + margem_altura + 1, j - margem_largura:j + margem_largura + 1]
            resultado_convolucao = np.sum(regiao_interesse * kernel)
            resultado[i, j] = resultado_convolucao

    return resultado

#Função para mostrar as imagens 
def showImg (imagem, resultadoFiltro1, resultadoFiltro2):
    # Criando uma figura com tamanho desejado
    plt.figure(figsize=(12, 4))

    # Exibindo a imagem resultante
    plt.subplot(1, 3, 1)
    plt.title("Imagem Original", fontsize=30)
    plt.imshow(imagem)

    plt.subplot(1, 3, 2)
    plt.title("Detector de bordas", fontsize=30)
    plt.imshow(resultadoFiltro1, cmap='gray')

    plt.subplot(1, 3, 3)
    plt.title("Suavização", fontsize=30)
    plt.imshow(resultadoFiltro2, cmap='gray')

    plt.show()

if __name__ == "__main__":
    main()