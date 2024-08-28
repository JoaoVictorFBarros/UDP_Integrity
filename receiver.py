import socket

def calculate_parity_bit(data):
    """Calcula o bit de paridade para uma string de dados binários."""
    ones_count = sum(bit == '1' for bit in data)
    return '1' if ones_count % 2 == 0 else '0'

def check_parity(data):
    """Verifica o bit de paridade para uma string de dados binários."""
    received_data = data[:-1]
    received_parity = data[-1]
    calculated_parity = calculate_parity_bit(received_data)
    return received_parity == calculated_parity

def receive_data(port):
    """Recebe dados de um emissor na porta especificada e verifica a integridade."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', port))
    try:
        while True:
            print("Aguardando dados...")
            data, _ = sock.recvfrom(1024)
            frame = data.decode()
            if check_parity(frame):
                print(f"Quadro recebido corretamente: {frame}")
            else:
                print(f"Erro detectado no quadro: {frame}")
                print("Aguardando retransmissão...")
    finally:
        sock.close()

# Teste do receptor
if __name__ == "__main__":
    port = 3112  # Porta para comunicação
    receive_data(port)
