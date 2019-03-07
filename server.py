import socket, time
#
# # host = "192.168.43.22"
# # host = socket.gethostbyname(socket.gethostname())
# host = "localhost"
# port = 9090
#
# #список клиентов
# clients = []
#
# #говорим что будем использовать протокол тсп айпи
# s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
#
# #передаем кортеж с портом и хостом
# s.bind((host,port))
# # s.listen(10)
# #отвечает за старт сервера
# quit = False
# print("[Server Started ]")
#
#
# while quit == False:
# 	try:
# 		#data = это сообщение addr = адрес  а регфром это размер принимаемых файлов
# 		data , addr = s.recvfrom(1024)
# 		#проверяем на наличие этого адреса в массиве если нету до добавляем
# 		if addr not in clients:
# 			clients.append(addr)
# 		#прописываем время когда юзер зашол или смс отправил
# 		itsatime = time.strftime("%Y - %m - %d - %H:%M:%S" , time.localtime())
#
# 		#выводим инфу
#
# 		print("["+ addr[0] +"]=["+ str(addr[1]) +"]=["+ itsatime +"]/",end = "")
# 		print(data.decode("utf-8"))
# 		for client in clients:
# 			if addr != client:
# 				s.sendto(data,client)
# 	except:
# 		print("\n [Server Stopped]")
# 		quit = True
# s.close()
#
#

host = "192.168.1.14"
#dsl = 1.14
#my  = 43.22
port = 9090

#список клиентов
clients = []
#список сообщений
messanges = []

#говорим что будем использовать протокол тсп айпи
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#передаем кортеж с портом и хостом
s.bind((host,port))

# stloop = True
print('ss')
# name,addres = s.recvfrom(1024)
# if name not in clients:
#     clients.append(name)
try:
    while True:
        # con , addr = s.accept()
        data,addres = s.recvfrom(1024)
        udata = data.decode("utf-8")
        print(udata,addres)
        # print(addres[0])

        # clients.append(addres)
        # if addres not in clients:
		#     clients.append(addres)
        if addres not in clients:
            clients.append(addres)
        messUs = bytes("____["+ addres[0] +"]____===> "+udata+" " , encoding="utf-8")
        print(clients)
        for ad in clients:
            s.sendto(messUs , ad)

except:
    pass
