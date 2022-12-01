from release import AppRelease
from distutils.version import StrictVersion
import os

class AppUpdates:

    def __init__(self) -> None:
        path = os.path.abspath(__file__)
        self.toPath = os.path.dirname(path)
        self.vvsPath = self.toPath + "\\app\\vvs.txt"
        self.update_type = "C"

    def check_update(self):

        local_version = "0.0.0"
        remote_version = "0.0.0"
        
        # get remote version data
        remote_txt = AppRelease().get_version()
        remote_version_data = self._reformat_version(remote_txt)
        self.update_type = remote_version_data[1]

        # get local version data 
        if(os.path.exists(self.vvsPath)) :
            with open(self.vvsPath,"r") as f:
                local_text = f.read() 
                local_version_data = self._reformat_version(local_text)

        try: 
            StrictVersion.parse(StrictVersion,local_version_data[0])
            local_version = local_version_data[0]
        except ValueError:
            pass

        try: 
            StrictVersion.parse(StrictVersion,remote_version_data[0])
            remote_version = remote_version_data[0]
        except ValueError:
            pass
        
        if StrictVersion(remote_version) > StrictVersion(local_version):
            return True
        else:
            # print("No Updates")
            return False

    def update(self):
        AppRelease().download_release()

    def _reformat_version(self,version_txt):
        if version_txt is None:
            return["0.0.0","C"]

        version_txt = version_txt.replace("\n","")
        version_txt = version_txt.replace("\r","")
        versionData = version_txt.split('/')

        if(len(versionData) == 2):
            version = versionData[0]
            load_method = versionData[1]
            if(load_method != "H"):
                load_method = "C"
            
        else:
            version = versionData[0]
            load_method = "C"

        return [version,load_method]    


if __name__ == "__main__":
    print(AppUpdates().check_update())