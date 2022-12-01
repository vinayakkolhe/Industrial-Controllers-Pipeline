import sys
#sys.path.insert(1,'../app')
import app.app as app
import time
from app_version import AppUpdates 
from threading import Thread
from importlib import reload
#from watchdog.observers import Observer
#from watchdog.events import LoggingEventHandler

 


class Controller:
    
    def __init__ (self):
        self.status = "Stop" 
        checkerThread = Thread(target = self.checker, args = (5,))
        checkerThread.start()
        
    def stop(self):
        self.status = "Stop"
        self.Run = False        
        self.executorThread.join()
        print("\n---Stoping executor---")

    def start(self):
        print("---Starting executor---")
        self.Run = True
        self.status = "Running"
        self.executorThread = Thread(target= self.executor, args = ())
        self.executorThread.start()

    def executor(self):
        myapp =app.pyapp()
        while self.Run is True:
            myapp.main()
        
    def checker(self, interval):
        
        app_updates = AppUpdates()
        while True:
            time.sleep(interval)
            if(app_updates.check_update()):

                app_updates.update()

                if app_updates.update_type == "H":
                    self.stop()
                    reload(app)
                    self.start()
            
            
        

        

    
    
        
if __name__ == "__main__" :
    controller = Controller()
    controller.start()