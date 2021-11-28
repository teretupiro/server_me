from socket import *
from tkinter import *


sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind(('', 5400))
sockobj.listen(5)


while True:
         connection, address = sockobj.accept()  # ждем сообщение от клиента, устонавливаем соединение с клиентом, получаем ip адрес

         bin_data = connection.recv(1024)  # количество байтов
         str_data = bin_data.decode('utf-8')



         ip_addr = address[0]

         print("Сервер получил сообшение :", str_data, '\n\n',)


         str_answer = ip_addr +':'+ str_data

         connection.send(str_answer.encode('utf-8'))
         connection.close()


