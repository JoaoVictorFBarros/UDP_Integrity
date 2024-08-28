import socket
import random
import time

def calculate_parity_bit(data):
    """Calcula o bit de paridade para uma string de dados binários."""
    ones_count = sum(bit == '1' for bit in data)
    return '1' if ones_count % 2 == 0 else '0'

def create_frame(data):
    """Cria um quadro com dados e bit de paridade."""
    parity_bit = calculate_parity_bit(data)
    return data + parity_bit

def send_data(data, port):
    """Simula o envio contínuo de dados para um receptor na porta especificada."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', port)
    
    try:
        while True:
            frame = create_frame(data)
            print(f"Enviando quadro: {frame}")
            
            # Introduzir um erro aleatório
            if random.random() < 0.1:  # 10% de chance de erro
                frame = list(frame)
                index = random.randint(0, len(frame) - 1)
                frame[index] = '0' if frame[index] == '1' else '1'
                frame = ''.join(frame)
                print(f"Erro introduzido: {frame}")

            sock.sendto(frame.encode(), server_address)
            time.sleep(2)  # Pausa de 2 segundos entre envios
    finally:
        sock.close()

# Teste do emissor
if __name__ == "__main__":
    data = '1010101010'  # Dados de exemplo
    port = 3112  # Porta para comunicação
    send_data(data, port)
