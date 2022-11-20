class VVS:
    def __init__(self):
        self.filePath = "./vvs.txt"

    def get(self):
        with open(self.filePath,"r") as version:
            return version.readline()


if __name__ == "__main__" :
    vvs = VVS()
    version = vvs.get()
    print(version)