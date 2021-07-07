from agentspace import Agent,Space
import cv2
import socket
import sys
import re

class ServerServiceAgent(Agent):

    def __init__(self,socket,name):
        self.socket = socket
        self.name = name
        super().__init__()
        
    def putline(self,line):
        self.socket.send((line+'\r\n').encode())
        
    def init(self):
        print('connected')
        self.attach_trigger(self.name)

    def senseSelectAct(self):
        data = Space.read(self.name,[])
        if len(data) > 0:
            try:
                line = str(data)
                self.putline(line)
            except Exception as e:
                print('disconnected')
                self.stop()
    
class ServerAgent(Agent):

    def __init__(self,port,name):
        self.port = port
        self.name = name
        super().__init__()
        
    def init(self):
        print('server starting on port',self.port)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0',self.port))
        except:
            self.stop()
        while not self.stopped:
            try:
                sock.listen(1)
                print('listening')
                client, address = sock.accept()
                print('connecting')
                ServerServiceAgent(client,self.name)
            except:
                pass
        try:
            sock.close()
        except:
            print('server finished')
            pass
  
    def senseSelectAct(self):
        pass

class ClientAgent(Agent):

    def __init__(self,ip,port,name):
        self.ip = ip
        self.port = port
        self.name = name
        super().__init__()
        
    def getline(self):
        while self.buffer.find('\n')==-1:
            self.buffer += self.sock.recv(1024).decode()
        result = re.sub('[\r\n].*','',self.buffer)
        self.buffer = self.buffer[self.buffer.find('\n')+1:]
        return result
     
    def init(self):
        print('client connecting to ip',self.ip,'port',self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.ip,self.port))
        except ConnectionRefusedError:
            print('server is not running')
            self.stop()
        self.buffer = ''
        while not self.stopped:
            try:
                line = self.getline() 
                data = eval(line)
                Space.write(self.name,data)
            except Exception as e:
                print(e)
                self.stop()
  
    def senseSelectAct(self):
        pass
    