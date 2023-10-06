# Script de Aplicação de Filtros de Imagem 
Este script foi desenvolvido como parte do curso de Sistemas e Sinais, com o propósito de aplicar filtros em imagens utilizando a convolução 2D. O objetivo principal é explorar técnicas de processamento de imagem, incluindo filtros de detecção de bordas e suavização.
## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.



### 📋 Pré-requisitos

De que coisas você precisa para rodar o script e como instalá-lo?

* Python 3.x
* Bibliotecas: NumPy, scikit-image, matplotlib


### 🔧 Instalação

Você pode instalar as bibliotecas necessárias utilizando o pip:

```
pip install numpy scikit-image matplotlib

```

## ⚙️ Executando

1. Clone ou faça o download deste repositório.

2. Certifique-se de que você possui as imagens que deseja processar na mesma pasta do script ou forneça o caminho completo para as imagens como argumentos de linha de comando.

3. Execute o script com os seguintes comandos:

Para aplicar um filtro de detecção de bordas (por exemplo, filtro Sobel):

```
python filter_script.py --input Sinais/imagem.jpg --output output_bordas.jpg --filter bordas

```
Para aplicar um filtro de suavização (por exemplo, filtro Gaussiano):

```
python filter_script.py --input Sinais/imagem.jpg --output output_suavizacao.jpg --filter suavizacao

```
![Texto alternativo](https://i.ibb.co/Xk8LG6J/asd.png)

Certifique-se de substituir Sinais/imagem.jpg pelo caminho da imagem que você deseja processar e output_bordas.jpg ou output_suavizacao.jpg pelo nome desejado para o arquivo de saída.

## 🛠️ Filtros suportados
O script suporta os seguintes filtros:

* bordas: Detecção de bordas usando filtros Sobel.
* suavizacao: Suavização da imagem usando um filtro Gaussiano.

Você pode facilmente estender o script para incluir outros filtros de convolução personalizados, se necessário.

## 🖇️ Colaborando

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests) para melhorias ou correções.

## ✒️ Autores


* **Willian Rodrigues** - *Implementação* - [Contato](https://github.com/WillianRodriguesz)
* **Email** - *wdesrodrigues@inf.ufpel.edu.br*

## 📄 Licença

Este projeto está sob a licença Licença MIT. - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

---
⌨️ com ❤️ por Willian Rodrigues 😊
