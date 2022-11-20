import os
import shutil

class Update:
    def __init__(self):

        path = os.path.abspath(__file__)

        self.toPath = os.path.dirname(path) + "\\"
        self.fromPath = "C:\\Users\\z004fmdv\\Desktop\\New folder\\"
    
    def check(self):
        pass

    def get(self):
        files = os.listdir(self.fromPath)

        for file_name in files:
            if os.path.exists(self.toPath+file_name):
                os.remove(self.toPath+file_name)
            shutil.copy(self.fromPath+file_name, self.toPath+file_name)
        
        # shutil.copytree(self.fromPath,self.toPath)



if __name__ == "__main__":
    update = Update()
    update.get()