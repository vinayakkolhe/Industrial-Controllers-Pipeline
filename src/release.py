"""
Demo:
Github username: Shravan-1908
Repo name: hydra
Release ID: (latest) 
Download stats for `Shravan-1908/hydra`, release `v2.2.0`
---------------------------------------------------------
hydra-darwin-amd64: 2
hydra-linux-amd64: 47
hydra-windows-amd64.exe: 19
Total: 68
"""

import requests
import shutil
import os

class AppRelease:


    color_blue = "\033[36m"
    color_yellow = "\033[33m"
    color_green = "\033[32m"
    color_red = "\033[31m"
    color_purple = "\033[35m"
    color_end = "\033[0m"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
   

    def __init__(self) -> None:
        self.url = self._create_url("vinayakkolhe", "Industrial-Controllers-Pipeline", "latest")
        path = os.path.abspath(__file__)
        self.dest_folder = os.path.dirname(path) + "\\app"
        
        self.username = "vinayakkolhe"
        self.token = "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"


    def get_version(self) -> str:
        version = "0.0.0"
        r = requests.get(self.url,auth=(self.username,self.token))
        if r.status_code == 200:
            data = r.json()

            # get remote version text
            for asset in data["assets"]:
                asset_download_url = asset["browser_download_url"]
                asset_name = asset["name"]
                if asset_name == "vvs.txt":
                    version = self._readRemoteFile(asset_download_url)
        else:
            print(r.status_code)

        return version
        

    def download_release(self):
        """
        Downloads assets from given release url of github to the dest_folder
        """
        
        r = requests.get(self.url,auth=(self.username,self.token))
        if r.status_code == 200:
            data = r.json()
            tagname = data["tag_name"]

            message = (
                f"{self.color_blue}Download of release `{tagname}` started")
            #print(f"{message}\n{'-'*(len(message)-5)}{self.color_end}")

            total = 0

            for asset in data["assets"]:
                asset_name = asset["name"]
                asset_download_url = asset["browser_download_url"]
                self._download(asset_download_url,self.dest_folder)
                # print(f"{self.color_yellow}Dowload: {self.color_green}{asset_name}")
                total += asset["download_count"]

            #print(f"\n{self.color_purple}Total: {total}{self.color_end}")

        else:
            print(self.color_red + "Unable to find download." + self.color_end)


    def _create_url(self, username, repo, release_id="latest"):
        url = ""
        if release_id != "latest":
            url = "https://api.github.com/repos/{}/{}/releases/tags/{}".format(
                username, repo, release_id)
        else:
            url = "https://api.github.com/repos/{}/{}/releases/latest".format(
                username, repo)

        return url


    def _readRemoteFile(self,file_url):
        r = requests.get(file_url, stream=True, auth=(self.username,self.token))
        if r.ok:
            return r.text


    def _download(self, file_url,dest_folder):

        """
        Downloads file from url
        """

        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)  # create folder if it does not exist

        filename = file_url.split('/')[-1].replace(" ", "_")  # be careful with file names
        file_path = os.path.join(dest_folder, filename)

        r = requests.get(file_url, stream=True, auth=(self.username,self.token))
        if r.ok:
            # print("saving to", os.path.abspath(file_path))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        else:  # HTTP status code 4XX/5XX
            print("Download failed: status code {}\n{}".format(r.status_code, r.text))


if __name__ == "__main__":
    # username = input("Github username: ")
    # repo = input("Repo name: ")
    # release_id = input("Release ID: (latest) ")
    # if release_id.strip() == "":
    #     release_id = "latest"
    # print()
    # url = create_url(username, repo, release_id)
    # download_release(username, url)
    AppReleas = AppRelease()
    print(AppReleas.get_version())
    AppReleas.download_release()
