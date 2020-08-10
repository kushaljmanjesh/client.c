import xml.sax
import sys
import socket
import time
from timerExt import RepeatedTimer
# Python program to  create a simple GUI Using Tkinter


# import everything from tkinter module
from Tkinter import *

expression = ""

client_socket = socket.socket()

 
    def clear(self):
        global expression
        expression = ""
        self.equation.set("")
        
    def connect(self):
        port = int(self.PORT.get())
        host = socket.gethostbyname('localhost')
        client_socket.connect((host, port))  # connect to the server

    def disconnect(self):
        print('socket closed')
        client_socket.close()  # close the connection


    def fire():
        key_value = self.KEY_VALUE.get()
        total_count = int(self.NUM.get())
        delay_sec = int(self.DELAY.get())
       
        rt = RepeatedTimer(delay_sec, total_count,self.press, key_value)
    
     def press(self, num):
        # point out the global expression variable
        global expression
        global key_state
        global key_buffer
        
        if key_state:
            key_buffer.stop()
            expression = expression + str(num)
            # update the expression by using set method
            self.equation.set(expression)
            # start timer
            key_buffer = RepeatedTimer(response_time, 1, self.push_buffer())
            key_state = 1
       else:
           
            expression = expression + str(num)            
            self.equation.set(expression)           
            key_buffer = RepeatedTimer(response_time, 1, self.push_buffer())
            key_state = 1


 def __init__(self,parent):
        self.parent = parent

        # get value of "Port_Number" element
        self.port = StringVar()
        self.port.set(getElementValue(self.xmlDocument, "Port_Number"))

        # create attribute for "Remote" element
        self.xmlheading = getElement(self.xmlDocument, "Remote")

        # create attribute for "Service" element
        self.xmlSoftRemote = getElement(self.xmlheading, "GUI")

        # get value of "DELAY" element
        self.DELAY = StringVar()
        self.DELAY.set(getElementValue(self.xmlSoftRemote, "DELAY"))

        # get value of "KEY_VALUE" element
        self.KEY_VALUE = StringVar()
        self.KEY_VALUE.set(getElementValue(self.xmlSoftRemote, "KEY_VALUE"))

        # get value of "NUM" element
        self.NUM = StringVar()
        self.NUM.set(getElementValue(self.xmlSoftRemote, "NUM"))

        # get value of "KEY1" element
        self.KEY1 = getElementValue(self.xmlSoftRemote, "KEY1")

        # get value of "KEY2" element
        self.KEY2 = getElementValue(self.xmlService, "KEY2")

        # get value of "KEY3" element
        self.KEY3 = getElementValue(self.xmlSoftRemote, "KEY3")

        # get value of "KEY4" element
        self.KEY4 = getElementValue(self.xmlSoftRemote, "KEY4")

        # get value of "KEY5" element
        self.KEY5 = getElementValue(self.xmlSoftRemote, "KEY5")

        # get value of "KEY6" element
        self.KEY6 = getElementValue(self.xmlSoftRemote, "KEY6")

        # get value of "KEY7" element
        self.KEY7 = getElementValue(self.xmlSoftRemote, "KEY7")

        # get value of "KEY8" element
        self.KEY8 = getElementValue(self.xmlSoftRemote, "KEY8")

        # get value of "KEY9" element
        self.KEY9 = getElementValue(self.xmlSoftRemote, "KEY9")

        # get value of "KEY0" element
        self.KEY0 = getElementValue(self.xmlSoftRemote, "KEY0")

        # get value of "VOLUP" element
        self.VOLUP = getElementValue(self.xmlSoftRemote, "VOLUP")

        # get value of "VOLDOWN" element
        self.VOLDOWN =getElementValue(self.xmlSoftRemote, "VOLDOWN")

        # get value of "CHNLUP" element
        self.CHNLUP = getElementValue(self.xmlSoftRemote, "CHNLUP")

        # get value of "CHNLDOWN" element
        self.CHNLDOWN = getElementValue(self.xmlSoftRemote, "CHNLDOWN")

        # get value of "MENU" element
        self.MENU = getElementValue(self.xmlSoftRemote, "MENU")

        # get value of "RETURN" element
        self.RETURN = getElementValue(self.xmlSoftRemote, "RETURN")

        # get value of "INFO" element
        self.INFO = getElementValue(self.xmlSoftRemote, "INFO")

        # get value of "NAV_RIGHT" element
        self.NAV_RIGHT = getElementValue(self.xmlSoftRemote, "NAV_RIGHT")

        # get value of "NEV_LEFT" element
        self.NEV_LEFT = getElementValue(self.xmlSoftRemote, "NEV_LEFT")

        # get value of "NAV_UP" element
        self.NAV_UP = getElementValue(self.xmlSoftRemote, "NAV_UP")

        # get value of "NAV_DOWN" element
        self.NAV_DOWN = getElementValue(self.xmlSoftRemote, "NAV_DOWN")

        # get value of "FAST_FORWARD" element
        self.FAST_FORWARD = getElementValue(self.xmlSoftRemote, "FAST_FORWARD")

        # get value of "REWIND" element
        self.REWIND = getElementValue(self.xmlSoftRemote, "REWIND")

        # get value of "PLAY_PAUSE" element
        self.PLAY_PAUSE = getElementValue(self.xmlSoftRemote, "PLAY_PAUSE")

        # get value of "POWER" element
        self.POWER = getElementValue(self.xmlSoftRemote, "POWER")

        # get value of "FAV" element
        self.FAV = getElementValue(self.xmlSoftRemote, "FAV")

        
        # get value of "FAV" element
        self.NETFLIX = getElementValue(self.xmlSoftRemote, "NETFLIX")

        
        # get value of "FAV" element
        self.AMAZON = getElementValue(self.xmlSoftRemote, "AMAZON")

        # initialize UI
        self.initUI()
        
        
         def initUI(self):

        # set the title of GUI window
        self.parent.title("Softremote")

        # pack frame
        self.pack(fill=BOTH, expand=1)

        # configure grid columns
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)
        self.columnconfigure(5, pad=3)
        self.columnconfigure(6, pad=3)
        self.columnconfigure(7, pad=3)
        self.columnconfigure(8, pad=3)
        self.columnconfigure(9, pad=3)
        self.columnconfigure(10, pad=3)
        self.columnconfigure(11, pad=3)

        # configure grid rows
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        self.rowconfigure(8, pad=3)
        self.rowconfigure(9, pad=3)
        self.rowconfigure(10, pad=3)
        self.rowconfigure(11, pad=3)
        self.rowconfigure(12, pad=3)
        self.rowconfigure(13, pad=3)
        self.rowconfigure(14, pad=3)
        self.rowconfigure(15, pad=3)
        self.rowconfigure(16, pad=3)
        self.rowconfigure(17, pad=3)
        self.rowconfigure(18, pad=3)
        self.rowconfigure(19, pad=3)
        self.rowconfigure(20, pad=3)
        self.rowconfigure(21, pad=3)

        # set the background colour of GUI window
        self.configure(background="white")

        # StringVar() is the variable class
        # we create an instance of this class
        self.equation = StringVar()

        # create the text entry box for
        # showing the expression .
        expression_field = Entry(self, textvariable=self.equation)

        # grid method is used for placing
        # the widgets at respective positions
        # in table like structure .
        expression_field.pack(side=LEFT)
        expression_field.grid(columnspan=5, ipadx=100)

        self.equation.set('enter your choice')

        # create a Buttons and place at a particular
        # location inside the root window .
        # when user press the button, the command or
        # function affiliated to that button is executed .
        CONNECT = Button(self, text=' connect ', fg='black', bg='green',
                         command=lambda: self.connect(), height=1, width=7)
        CONNECT.grid(row=6, column=3, sticky=E)

        L1 = Label(self, text='IP address')
        L1.grid(row=4, column=3, ipadx=10, sticky=W)
        IP_address = Entry(self, bd=5, textvariable=self.IP_address)
        IP_address.grid(row=4, column=4)

        L2 = Label(self, text='Port number')
        L2.grid(row=5, column=3, ipadx=10, sticky=W)
        Port_Number = Entry(self, bd=5, textvariable=self.Port_Number)
        Port_Number.grid(row=5, column=4)

        DISCONNECT = Button(self, text=' disconnect ', fg='black', bg='green',
                            command=lambda: self.disconnect(), height=1, width=7)
        DISCONNECT.grid(row=6, column=4, sticky=E)

        SETTINGS = Label(self, text=' Settings ', fg='white', bg='black')
        SETTINGS.grid(row=7, column=3, ipadx=10)

        L3 = Label(self, text='Delay')
        L3.grid(row=8, column=3, ipadx=10, sticky=E+W)
        DELAY = Entry(self, bd=5, textvariable=self.DELAY)
        DELAY.grid(row=8, column=4)

        L4 = Label(self, text='Key')
        L4.grid(row=9, column=3, ipadx=10, sticky=E+W)
        KEY_VALUE = Entry(self, bd=5, textvariable=self.KEY_VALUE)
        KEY_VALUE.grid(row=9, column=4)

        L5 = Label(self, text='Number of Times')
        L5.grid(row=10, column=3, ipadx=10, sticky=E+W)
        NUM = Entry(self, bd=5, textvariable=self.NUM)
        NUM.grid(row=10, column=4)

        FIRE = Button(self, text=' Fire ', fg='black', bg='green',
                      command=lambda: self.fire(), height=2, width=7)

        FIRE.grid(row=11, column=3, sticky=E)

        KEY1 = Button(self, text=' 1 ', fg='black', bg='red',
                      command=lambda: self.press(self.KEY1), height=1, width=7)
        KEY1.grid(row=4, column=0, sticky=E)

        KEY2 = Button(self, text=' 2 ', fg='black', bg='red',
                      command=lambda: self.press(self.KEY2), height=1, width=7)
        KEY2.grid(row=4, column=1, sticky=E)

        KEY3 = Button(self, text=' 3 ', fg='black', bg='red',
                      command=lambda: self.press(self.KEY3), height=1, width=7)
        KEY3.grid(row=4, column=2, sticky=E)

        KEY4 = Button(self, text=' 4 ', fg='black', bg='red',
                      command=lambda: self.press(self.KEY4), height=1, width=7)
        KEY4.grid(row=5, column=0, sticky=E)

        KEY5 = Button(self, text=' 5 ', fg='black', bg='red',
                      command=lambda: self.press(self.KEY5), height=1, width=7)
        KEY5.grid(row=5, column=1, sticky=E)

        KEY6 = Button(self, text=' 6 ', fg='black', bg='red',
                      command=lambda: self.press(self.KEY6), height=1, width=7)
        KEY6.grid(row=5, column=2, sticky=E)

        KEY7 = Button(self, text=' 7 ', fg='black', bg='red',
                      command=lambda: self.press(self.KEY7), height=1, width=7)
        KEY7.grid(row=6, column=0, sticky=E)

        KEY8 = Button(self, text=' 8 ', fg='black', bg='red',
                      command=lambda: self.press(self.KEY8), height=1, width=7)
        KEY8.grid(row=6, column=1, sticky=E)

        KEY9 = Button(self, text=' 9 ', fg='black', bg='red',
                      command=lambda: self.press(self.KEY9), height=1, width=7)
        KEY9.grid(row=6, column=2, sticky=E)

        KEY0 = Button(self, text=' 0 ', fg='black', bg='red',
                      command=lambda: self.press(self.KEY0), height=1, width=7)
        KEY0.grid(row=7, column=1, sticky=E)

        VOLUP = Button(self, text=' VOLUP ', fg='black', bg='red',
                       command=lambda: self.press(self.VOLUP), height=1, width=7)
        VOLUP.grid(row=8, column=0, sticky=E)

        VOLDOWN = Button(self, text=' VOLDOWN ', fg='black', bg='red',
                         command=lambda: self.press(self.VOLDOWN), height=1, width=7)
        VOLDOWN.grid(row=9, column=0, sticky=E)

        VOLMUTE = Button(self, text=' VOLMUTE ', fg='black', bg='red',
                         command=lambda: self.press(self.VOLMUTE), height=1, width=7)
        VOLMUTE.grid(row=3, column=2, sticky=E)

        CHNLUP = Button(self, text=' CHNLUP ', fg='black', bg='red',
                        command=lambda: self.press(self.CHNLUP), height=1, width=7)
        CHNLUP.grid(row=8, column=2, sticky=E)

        CHNLDOWN = Button(self, text=' CHNLDOWN ', fg='black', bg='red',
                          command=lambda: self.press(self.CHNLDOWN), height=1, width=7)
        CHNLDOWN.grid(row=9, column=2, sticky=E)

        MENU = Button(self, text=' MENU ', fg='black', bg='red',
                      command=lambda: self.press(self.MENU), height=1, width=7)
        MENU.grid(row=11, column=0, sticky=E)

        RETURN = Button(self, text=' RETURN ', fg='black', bg='red',
                        command=lambda: self.press(self.RETURN), height=1, width=7)
        RETURN.grid(row=9, column=1, sticky=E)

        INFO = Button(self, text=' INFO ', fg='black', bg='red',
                      command=lambda: self.press(self.INFO), height=1, width=7)
        INFO.grid(row=11, column=2, sticky=E)

        OK = Button(self, text=' OK ', fg='black', bg='red',
                    command=lambda: self.onOK(), height=1, width=7)
        OK.grid(row=8, column=1, sticky=E)

        NAV_RIGHT = Button(self, text=' NAVRIGHT ', fg='black', bg='red',
                           command=lambda: self.press(self.NAV_RIGHT), height=1, width=7)
        NAV_RIGHT.grid(row=14, column=2, sticky=E)

        NAV_LEFT = Button(self, text=' NAVLEFT ', fg='black', bg='red',
                          command=lambda: self.press(self.NAV_LEFT), height=1, width=7)
        NAV_LEFT.grid(row=14, column=0, sticky=E)

        NAV_UP = Button(self, text=' NAVUP ', fg='black', bg='red',
                        command=lambda: self.press(self.NAV_UP), height=1, width=7)
        NAV_UP.grid(row=13, column=1, sticky=E)

        NAV_DOWN = Button(self, text=' NAVDOWN ', fg='black', bg='red',
                          command=lambda: self.press(self.NAV_DOWN), height=1, width=7)
        NAV_DOWN.grid(row=15, column=1, sticky=E)

        FAST_FORWARD = Button(self, text=' FAST_FORWARD ', fg='black', bg='red',
                              command=lambda: self.press(self.FAST_FORWARD), height=1, width=7)
        FAST_FORWARD.grid(row=16, column=0, sticky=E)

        REWIND = Button(self, text=' REWIND ', fg='black', bg='red',
                        command=lambda: self.press(self.REWIND), height=1, width=7)
        REWIND.grid(row=16, column=2, sticky=E)

        PLAY_PAUSE = Button(self, text=' PLAY/PAUSE ', fg='black', bg='red',
                            command=lambda: self.press(self.PLAY_PAUSE), height=1, width=7)
        PLAY_PAUSE.grid(row=17, column=0, sticky=E)

        POWER = Button(self, text=' POWER ', fg='black', bg='red',
                       command=lambda: self.press(self.POWER), height=1, width=7)
        POWER.grid(row=2, column=2, sticky=E)

        FAV = Button(self, text=' FAV ', fg='black', bg='red',
                     command=lambda: self.press(self.FAV), height=1, width=7)
        FAV.grid(row=17, column=2, sticky=E)

        clear = Button(self, text='Clear', fg='black', bg='red',
                       command=lambda: self.clear(), height=1, width=7)
        clear.grid(row=18, column=2, sticky=E)

        NETFLIX = Button(self, text=' NETFLIX ', fg='black', bg='red',
                     command=lambda: self.press(self.NETFLIX), height=1, width=7)
        NETFLIX.grid(row=19, column=2, sticky=E)

        AMAZON = Button(self, text='AMAZON', fg='black', bg='red',
                       command=lambda: self.press(self.AMAZON), height=1, width=7)
        AMAZON.grid(row=19, column=1, sticky=E)
       
      
      if ( __name__ == "__main__"):
         main()
   
