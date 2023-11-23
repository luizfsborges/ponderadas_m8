# Configuração do Chatbot de Especialista em Segurança

Este guia fornece instruções passo a passo para configurar o Chatbot de Especialista em Segurança utilizando o Ollama e o Gradio no WSL Ubuntu.

## Passos de Instalação

### 1. Instale o Ollama

```bash
# Adicione o repositório do Ollama
sudo add-apt-repository ppa:langchain/ollama
sudo apt-get update

# Instale o Ollama
sudo apt-get install ollama

```
### 2. Instale o Gradio

```bash
# Instale as dependências do Gradio
sudo apt-get install python3-pip
pip3 install gradio 
``` 
### 3. Configuração do ModelFile

Crie um arquivo ModelFile chamado safety_expert_model.yml com o seguinte conteúdo:
    
```bash
FROM dolphin2.2-mistral

PARAMETER temperature 1

SYSTEM """
From now on, you are designated as an expert on safety standards in industrial environments. If a user prompts anything that is not related to safety standards, you must respond with: "I'm sorry, I am only allowed to answer as an expert on safety standards in industrial environments."
"""
```

### 4. Crie o Modelo de Especialista em Segurança

Execute o seguinte comando para criar o modelo de Especialista em Segurança usando o Ollama:

```bash
ollama create safety_expert -f safety_expert_model.yml
```
### 5. Executando o Chatbot

Clone o repositório contendo o script chatbot_seguranca_trabalho.py e navegue até o diretório.

```bash
git clone <url_do_repositorio>
cd <diretorio_do_repositorio>
```
Execute o script do Chatbot de Especialista em Segurança:

```bash	
python3 chatbot_seguranca_trabalho.py
```
Acesse http://localhost:7860 em seu navegador para interagir com o Chatbot de Especialista em Segurança.

### Instruções de uso

- Digite suas perguntas relacionadas a normas de segurança em ambientes industriais na caixa de chat.

- O chatbot responderá com conselhos especializados com base na configuração do ModelFile fornecido.