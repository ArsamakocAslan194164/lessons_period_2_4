import socket

HOST = input("Введите адрес сервера (по умолчанию localhost): ") or 'localhost' # Адрес сервера по умолчанию — localhost
PORT = input("Введите номер порта (по умолчанию 8000): ") or 8000 # Номер порта по умолчанию — 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, int(PORT)))

    while True:
        message = input('Введите сообщение: ')

        if not message:
            break

        s.sendall(message.encode())

        data = s.recv(1024)
        response = data.decode("utf-8")
        print(response)

        if message.strip() == 'exit':
            print('Закрытие соединения с сервером')
            break

    s.close()

print('Клиент выходит')