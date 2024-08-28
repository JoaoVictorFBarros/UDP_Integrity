# Emissor e receptor UDP com verificação de integridade

Este projeto demonstra uma solução básica para comunicação de dados entre um emissor e um receptor utilizando o protocolo UDP. A comunicação inclui a verificação de integridade dos dados transmitidos por meio de bits de paridade e simula condições de transmissão reais com a possibilidade de introdução de erros.


### Clone o repositório
```bash
git clone https://github.com/JoaoVictorFBarros/UDP_Integrity.git
```


### Instalação das Dependências

Todas as bibliotecas usadas são padrão do python.

## Execução

1. **Inicie o Receptor**: Execute o script do receptor para começar a ouvir os dados na porta especificada:
    ```
    python3 receiver.py
    ```
2. **Inicie o Emissor**: Execute o script do emissor para começar a enviar dados para o receptor.
    ```
    python3 sender.py
    ```

Certifique-se de que ambos os scripts estão configurados para usar a mesma porta para comunicação.

<div align="center">
<img src=print.png >
</div>

## Componentes

O projeto é composto por dois scripts Python:

### Emissor

- **Função**: Simula o envio de dados para um receptor.
- **Características**:
  - Adiciona um bit de paridade aos dados.
  - Introduz erros aleatórios para simular condições reais de transmissão.

### Receptor

- **Função**: Recebe dados do emissor e verifica a integridade dos quadros recebidos.
- **Características**:
  - Verifica o bit de paridade para garantir que os dados foram recebidos corretamente.
  - Detecta erros e aguarda a retransmissão dos dados, se necessário.

## Funcionamento

### Emissor

1. O emissor cria quadros de dados adicionando um bit de paridade a cada quadro.
2. Os quadros são enviados continuamente para o receptor.
3. Erros aleatórios são introduzidos com uma certa probabilidade para testar a robustez da comunicação.

### Receptor

1. O receptor escuta continuamente na porta especificada para receber os quadros de dados.
2. Verifica o bit de paridade de cada quadro recebido para assegurar que os dados não foram corrompidos.
3. Caso um erro seja detectado, o receptor exibe uma mensagem de erro e aguarda a retransmissão dos dados.

## Camada de Enlace

A camada de enlace é uma das camadas fundamentais no modelo OSI (Open Systems Interconnection) e é responsável por garantir a entrega correta dos dados entre dispositivos em uma rede local. No contexto deste projeto:

- **Verificação de Paridade**: O uso de bits de paridade no emissor e receptor é um exemplo básico de uma técnica de controle de erro da camada de enlace. A verificação de paridade ajuda a detectar erros que podem ocorrer durante a transmissão dos dados, garantindo que a informação seja recebida de forma correta.

- **Simulação de Erros**: Introduzir erros aleatórios no emissor é uma maneira de simular as condições que a camada de enlace pode enfrentar, como interferências e falhas na transmissão. Isso permite testar a capacidade do receptor de detectar e lidar com erros, uma função crítica da camada de enlace.

- **Controle de Fluxo e Retransmissão**: Embora este projeto não implemente controle de fluxo e retransmissão de forma detalhada, na prática, a camada de enlace pode incluir mecanismos para gerenciar a taxa de transmissão e assegurar que os dados sejam retransmitidos em caso de falhas detectadas, o que é uma extensão natural do conceito de verificação de paridade.
