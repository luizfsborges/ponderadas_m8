# Ponderada 3 - Criação de um chatbot simples

## 1. Enunciado

Desenvolva um nó de ROS que seja um chatbot capaz de entender comandos escritos em linguagem natural para interagir com um robô de serviço fictício. O chatbot deve fornecer ao usuário a possibilidade de enviar comandos de posição para o robô de forma simples e intuitiva.

## 2. Dependências

- Pyhton 3.8.5 ou superior
- ROS 3
- rclpy
- std_msgs

## 3. Instruções de execução

Para executar o chatbot desenvolvido nessa atividade, siga os seguintes passos:

## 3.1. Navege até o diretório do chatbot

Para navegar até o diretório do chatbot, execute o seguinte comando no terminal:

```bash
cd ponderada_3/simple_chat
```

### 3.3. Realize a compilação dos scripts

Para compilar os scripts, execute o seguinte comando no terminal:

```bash
colcon build
```
### Realzie o source do ambiente em relação ao arquivo de setup

Para realizar o source do ambiente, execute o seguinte comando no terminal:

```bash
source install/local_setup.bash 
```

### 3.3. Execute o nó ROS que contém o chatbot

Para executar o nó ROS que contém o chatbot, execute o seguinte comando no terminal:

```bash
ros3 run simple_chatbot NavChat
```







