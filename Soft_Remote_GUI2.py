import socket
import tkinter
import time
# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""
# Function to update expressiom

client_socket=socket.socket()
at=time.time()
print(at)#time start

# Function to clear the contents
# of text entry box
def clear():
   global expression
   expression = ""
   equation.set("")

# in the text entry box
def press(num):
  bt=time.time()
  
  if((bt-at)%2!=0):
  
    # point out the global expression variable
   global expression

    # concatenation of string
   expression = expression + str(num)
    
    # update the expression by using set method
   equation.set(expression)

   client_socket.send(expression.encode())
    # Look for the response
   data = client_socket.recv(16).decode()
   print ('received:' + data)
  #  print('Enter the message or type Bye for closing the socket')
   message = input(" -> ")   # take input
   
  if((bt-at)>2) :
   expression=""
   equation.set("")
def timedelay():
  
 key=keycode.get()
 second=seconds.get()
 frequency=number.get()
 
 #key=input("Which key are you expecting to be pressed?(KEY number)")
 k=int(key)
 #duration=input("Enter the duration (maximum duration is 900 seconds)")
 second=int(second)
 #frequency=input("enter the gap between presses in seconds")
 f=int(frequency)
 
 beginning=0
 
 while(beginning<=second):
   press(k)
   time.sleep(f) 
   beginning+=f
 
 print("total time taken for the whole operation is",finishtime-starttime)
    
def connect():
  portnumber=portnumber1.get()
  portnumber=int(portnumber)
  host = socket.gethostname()  # as both code is running on same pc
    # socket server port number
  client_socket = socket.socket()  # instantiate
  client_socket.connect((host, portnumber))  # connect to the server

def terminate():
  print("connection terminated")
  client_socket.close()

  

# Driver code 
if __name__ == "__main__":
# create a GUI window 
 gui = Tk() 
  
# set the background colour of GUI window 
 gui.configure(background="orange") 
  
# set the title of GUI window 
 gui.title("Remote GUI") 
  
# set the configuration of GUI window 
 gui.geometry("1920x1080")
 
# StringVar() is the variable class
 equation = StringVar()

# create the text entry box for
# showing the expression .
 expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
 expression_field.grid(columnspan=5, ipadx=50)

 equation.set('pressed key will appear here')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
 connect1= Button(gui, text=' connect ', fg='black', bg='green',
                     command=lambda: connect(), height=1, width=7)
 connect1.grid(row=13, column=3)

 TERMINATE = Button(gui, text=' terminate ', fg='red', bg='white',
                     command=lambda: terminate(), height=1, width=9)
 TERMINATE.grid(row=13, column=4)
 
 Settings = Label(gui, text=' Settings ')
 Settings.grid(row=8, column=3, ipadx=50)

 Label1 = Label(gui, text="Enter the duration")
 Label1.grid(row=9, column=3, ipadx=0)
 seconds= Entry(gui, bd=5)
 seconds.grid(row=9, column=4, ipadx=50)

 Label2 = Label(gui, text="Enter the key code to be pressed")
 Label2.grid(row=10, column=3, ipadx=40)
 keycode= Entry(gui, bd=5)
 keycode.grid(row=10, column=4, ipadx=50)

 Label3 = Label(gui, text="Enter frequency of firing")
 Label3.grid(row=11, column=3, ipadx=54)
 number= Entry(gui, bd=5)
 number.grid(row=11, column=4, ipadx=50)

 Label4 = Label(gui, text="Enter portnumber to be connected to server")
 Label4.grid(row=12, column=3, ipadx=30)
 portnumber1= Entry(gui, bd=5)
 portnumber1.grid(row=12, column=4, ipadx=50)

 FIRE = Button(gui, text=' Fire ', fg='black', bg='red',
                      command=lambda: timedelay(), height=2, width=7)

 FIRE.grid(row=14, column=3 )
 
  


   
 button1 = Button(gui, text='1', fg='black', bg='grey', 
                     command=lambda: press(2), height=1, width=10) 
 button1.grid(row=1, column=0) 
  
 button2 = Button(gui, text='2', fg='black', bg='grey', 
                     command=lambda: press(3), height=1, width=10) 
 button2.grid(row=1, column=1) 
  
 button3 = Button(gui, text='3', fg='black', bg='grey', 
                     command=lambda: press(4), height=1, width=10) 
 button3.grid(row=1, column=2) 
  
 button4 = Button(gui, text='4', fg='black', bg='grey', 
                     command=lambda: press(5), height=1, width=10) 
 button4.grid(row=2, column=0) 
  
 button5 = Button(gui, text='5', fg='black', bg='grey', 
                     command=lambda: press(6), height=1, width=10) 
 button5.grid(row=2, column=1) 
  
 button6 = Button(gui, text='6', fg='black', bg='grey', 
                     command=lambda: press(7), height=1, width=10) 
 button6.grid(row=2, column=2) 
  
 button7 = Button(gui, text='7', fg='black', bg='grey', 
                     command=lambda: press(8), height=1, width=10) 
 button7.grid(row=3, column=0) 
  
 button8 = Button(gui, text='8', fg='black', bg='grey', 
                     command=lambda: press(9), height=1, width=10) 
 button8.grid(row=3, column=1) 
  
 button9 = Button(gui, text='9', fg='black', bg='grey', 
                     command=lambda: press(10), height=1, width=10) 
 button9.grid(row=3, column=2) 
  
 button0 = Button(gui, text='0', fg='black', bg='grey', 
                     command=lambda: press(11), height=1, width=10) 
 button0.grid(row=4, column=1) 


  
 volup = Button(gui, text='VOLUP', fg='black', bg='grey', 
                  command=lambda: press("13"), height=2, width=7) 
 volup.grid(row=5, column=0) 
  
 voldwn = Button(gui, text='VOLDOWN', fg='black', bg='grey', 
                   command=lambda: press("12"), height=2, width=9) 
 voldwn.grid(row=7, column=0) 
  
 mute = Button(gui, text='MUTE', fg='black', bg='grey', 
                      command=lambda: press("50"), height=2, width=5) 
 mute.grid(row=6, column=1) 
  
 chnlup = Button(gui, text='CHNLUP', fg='black', bg='grey', 
                    command=lambda: press("104"), height=2, width=7) 
 chnlup.grid(row=5, column=2) 
  
 chnldwn = Button(gui, text='CHNLDOWN', fg='black', bg='grey', 
                   command=lambda: press("109"), height=2, width=9) 
 chnldwn.grid(row=7, column=2) 
  
 menu = Button(gui, text='MENU', fg='black', bg='grey', 
                   command=lambda:press("102"), height=2, width=6) 
 menu.grid(row=8, column=1) 
  
 retrn = Button(gui, text='RETURN', fg='black', bg='grey', 
                    command=lambda: press('1'), height=1, width=6) 
 retrn.grid(row=9, column=0)

 info= Button(gui, text='INFO', fg='black', bg='grey', 
                    command=lambda: press('115'), height=1, width=6) 
 info.grid(row=9, column=2)


 ok= Button(gui, text='OK', fg='black', bg='grey', 
                    command=lambda: press('28'), height=1, width=4) 
 ok.grid(row=11, column=1)
    
 nav_up= Button(gui, text='NAV_UP', fg='black', bg='grey', 
                    command=lambda: press('103'), height=1, width=9) 
 nav_up.grid(row=10, column=1)

 navdown= Button(gui, text='NAV_DOWN', fg='black', bg='grey', 
                    command=lambda: press('108'), height=1, width=9) 
 navdown.grid(row=12, column=1)

 navright= Button(gui, text='NAV_RIGHT', fg='black', bg='grey', 
                    command=lambda: press('106'), height=2, width=9) 
 navright.grid(row=11, column=2)

 navleft= Button(gui, text='NAV_LEFT', fg='black', bg='grey', 
                    command=lambda: press('105'), height=2, width=9) 
 navleft.grid(row=11, column=0)

 fastfwd= Button(gui, text='FAST_FORWARD', fg='black', bg='green', 
                    command=lambda: press('208'), height=3, width=7) 
 fastfwd.grid(row=13, column=2)

 rewind= Button(gui, text='REWIND', fg='black', bg='green', 
                    command=lambda: press('168'), height=3, width=7) 
 rewind.grid(row=13, column=0)

 playpause= Button(gui, text='PLAY/PAUSE', fg='black', bg='green',
                    command=lambda: press('57'), height=2, width=15) 
 playpause.grid(row=13, column=1)

 power= Button(gui, text='POWER', fg='black', bg='red', 
                    command=lambda: press('142'), height=1, width=7,border=1) 
 power.grid(row=0, column=2)
    
 fav= Button(gui, text='FAV', fg='black', bg='cyan',
                    command=lambda: press('49'), height=1,width=5) 
 fav.grid(row=5, column=1)

 clear = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=7)
 clear.grid(row=18, column='2')



 # start the GUI
 gui.mainloop()


   

    

'''
#def client_program():
 #   host = socket.gethostname()  # as both code is running on same pc
  #  port = 27015  # socket server port number

   # client_socket = socket.socket()  # instantiate
    #client_socket.connect((host, port))  # connect to the server
    # Send data
    client_socket.send(expression.encode())
    # Look for the response
    data = client_socket.recv(16).decode()
    print ('received:' + data)
    print('Enter the message or type Bye for closing the socket')
    message = input(" -> ")   # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data1 = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data1)  # show in terminal
        print('Enter the message or type Bye for closing the socket')
        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

    '''
    
