import socket , threading , time
from tkinter import *
import http.client
# key = 8194
#
#
# shutdown = False
# join     = False


# def receving (name , sock):
# 	while not shutdown:
# 		try:
# 			while True:
# 				data,addr = sock.recvfrom(1024)
# 				print(data.decode("utf-8"))
#
# 				decript = "";k = False
# 				for i in data.decode("utf-8"):
# 					if i == ":":
#
# 						k = True
# 					elif k == False or i == " ":
# 						decript += chr(ord(i))
# 				print(decript)
#
# 				#end
# 				time.sleep(0.2)
# 		except :
# 			raise
# host = "127.0.0.7"
# port = 9090
#
# server = (host, port)
#
# s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
# s.bind((host,port))
# # s.setblocking(0)
#
# name = input("You name : ")
# a = str(name)
# # rT = threading.Thread( target = receving , args = ("RecvThread",s))
# # rT.start()
#
#
# while shutdown == False:
# 	if join == False:
# 		s.sendto(bytes("["+ name +"] => join chat ", encoding = 'utf-8'), server )
# 		join = True
# 	else:
# 		try:
# 			message = input("Введи смс")
#
#
# 			cript = ""
# 			for i in message:
# 				cript += chr(ord(i))
# 			message = cript
# 			#end
#
# 			if message != '':
# 				s.sendto(bytes('[' + name + '] : : ' + message).encode('utf-8').server)
#
# 			time.sleep(0.2)
# 		except:#ctrl+c
# 			s.sendto(bytes('['+ name +'] <== out chat', encoding = 'utf-8'),server)
# 			shutdown = True
# # rT.join()
# # s.close()
# host = "127.0.0.7"
# port = 9090
# server = (host, port)
# s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
# s.bind((host,port))
#
#
#
# name = input('enter name => ')
# s.sendto(bytes("["+ name +"] => join chat ", encoding = 'utf-8'), server )
# data,addr = s.recvfrom(1024)
# print(data)
# while True:
#     messange = input('enter messange => ')
#     s.sendto(bytes("["+ name +"] => " + messange + "", encoding = 'utf-8'), server )
#
#     data,addr = s.recvfrom(1024)
#     print(data)
#
# s.close()
conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
r = conn.getresponse().read().decode('utf-8')
# print(conn.getresponse().read())
host = "192.168.1.14"
#dsl = 1.14
#my  = 43.22
# host = socket.gethostbyname(socket.gethostname())
port = 9090
server = (host,9090)
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)



def loadMessng(*args , **kwargs):
    while True:
        s.connect(server)
        data,addres = s.recvfrom(1024)
        udata = data.decode("utf-8")
        fon_mess.insert(1.1,'\n'+udata +'')
def sendMessng(*args , **kwargs):
    s.connect(server)
    s.sendto(bytes(textMess.get(), encoding = 'utf-8'), server )
    # s.close()
def sendName(*args , **kwargs):
    texN = textName.get()
    s.connect(server)
    s.sendto(bytes(texN, encoding = 'utf-8'), server )

root = Tk()
root.geometry("800x500")
root.title('peep v.0.1')
#FON
images = PhotoImage(file = "Pictures_with_a_green_background_5_17070846.png")
fon_window_mess = Label(root , image = images)
fon_window_mess.place(x = '-1' , y = '-1')

#LABEL

fon_mess = Text(root , bg = '#fff')

ssss = Scrollbar(fon_mess )
ssss.pack( side = RIGHT, fill = Y )

fon_mess.place(x = '50'  ,y = '100' , width = '500' , height = '300' )
ssss.config( command = fon_mess.yview )

textName = StringVar()
name = Entry(root ,width = 20 , textvariable = textName )
name.place(x = 410 , y = 50 , width = 140 , height = 40)
label_name = Label(root , text = "Введите имя :")
label_name.place(x = 310 , y = 60 )
name.bind("<Return>" ,sendName )


textMess = StringVar()
enter_mes = Entry(width = 70 , textvariable = textMess)
enter_mes.place(x = 50 , y = 410 , width = 300 , height = 40)


send_widget_mess = Button(root , text = "Отправить")
send_widget_mess.place(x = 390 , y = 410 , width = 100 , height = 40)

send_widget_mess.bind("<Button-1>" ,sendMessng )
enter_mes.bind("<Return>" ,sendMessng )



t = threading.Thread(target=loadMessng)
t.start()
root.mainloop()
s.close()
