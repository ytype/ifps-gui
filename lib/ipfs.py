import os
import platform
import subprocess

class ipfs:
    def __init__(self):
        self.message = ''
        pwd = os.path.dirname(os.path.realpath(__file__))
        pwd = pwd.replace('\\','/')
        self.path = f'{pwd}/ipfs.exe'


    def returnMessage(self):
        return self.message

    def isWindows64(self):
        if(os.name=='nt' and platform.architecture()[0]=='64bit'):
            return True
        else:
            return False

    def init(self):
        try:
            subprocess.Popen(f"{self.path} init", shell=True)
            return True
        except:
            return False

    def daemon(self):
        try:
            subprocess.Popen(f"{self.path} daemon", shell=True)
            return True
        except:
            return False

    def add(self, file):
        try:
            process = subprocess.run([self.path, 'add', file], check=True, stdout=subprocess.PIPE, universal_newlines=True)
            output = process.stdout
            return output.split()[1]
        except:
            return False


if __name__ == "__main__":
    ipfs = ipfs()
    ipfs.isWindows64()
    #ipfs.init()
    #ipfs.daemon()
    print('output:',ipfs.add('ipfs.py'))