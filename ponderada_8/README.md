# Ponderada 7: Criação de tradutor de voz

Este script em Python implementa um tradutor de voz que realiza a transcrição de um áudio para texto, o traduz para um idioma escolhido, sintetiza uma voz a partir dessa tradução e a reproduz. Utilizando as bibliotecas speech_recognition, googletrans e gtts, o script é capaz de converter a fala em texto, traduzir o texto para outro idioma e, em seguida, sintetizar o texto traduzido de volta para áudio. 

Os usuários podem fornecer caminhos de arquivo de áudio, selecionar os idiomas de origem e destino, e o script automatiza o processo de tradução, proporcionando uma experiência de tradução de voz simplificada. O áudio traduzido é salvo para posterior audição, e o script oferece a flexibilidade de ser personalizado para diferentes necessidades de tradução e idiomas.

## 1.  Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-nome/translator-de-voz.git
   cd translator-de-voz
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## 2.  Uso

1. Certifique-se de ter arquivos de áudio no diretório ponderada_8/falas_originais/.

2. Execute o script:

    ```bash
    python3 tradutor_voz.py
    ```

3. Siga as instruções no temrinal:

- Você será solicitado a inserir o caminho do arquivo de áudio que deseja traduzir.
- Insira o idioma original do áudio (por exemplo, pt-BR, en, es).
Insira o idioma alvo para a tradução (por exemplo, pt-BR, en, es).
- O script realizará então a conversão de voz para texto, a tradução de texto e a síntese de texto para voz. O áudio traduzido será salvo no diretório ponderada_8/falas_traduzidas/.
- Para sair do programa, digite "sair" quando solicitado a inserir o caminho do arquivo de áudio.

## Observação
- Certifique-se de fornecer códigos de idioma válidos (por exemplo, pt-BR para Português Brasileiro, en para Inglês).
- Se o script falhar ao reconhecer a fala no áudio, ele fornecerá uma mensagem de erro.