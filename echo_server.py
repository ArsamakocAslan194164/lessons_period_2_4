import logging
import socket

logging.basicConfig(filename='log_file.txt', level=logging.INFO)

HOST = input("Введите адрес сервера (по умолчанию localhost): ") or 'localhost'
PORT = input("Введите номер порта (по умолчанию 8000): ") or 8000

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()

            logging.info(f'Сервер слушает {HOST}:{PORT}')
            print(f'Сервер слушает {HOST}:{PORT}')

            while True:
                conn, addr = s.accept()
                with conn:
                    logging.info(f'Соединено с {addr}')

                    while True:
                        data = conn.recv(1024)

                        if not data:
                            logging.info(f'Соединение {addr} закрыто клиентом')
                            break

                        text = data.decode("utf-8")
                        logging.info(f'Полученное сообщение от {addr}: {text}')

                        if text.strip() == 'exit':
                            logging.info(f'Клиент {addr} запросил закрытие соединения')
                            break

                        response = f"Сервер отправил сообщение: {text}"
                        logging.info(response)
                        conn.send(response.encode())

                    conn.close()

                logging.info(f'Соединение {addr} закрыто')
    except OSError:
        PORT += 1
