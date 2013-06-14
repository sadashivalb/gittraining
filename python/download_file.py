import subprocess
import requests
from requests.auth import HTTPBasicAuth
def download():
    r = requests.get('http://www.python.org/ftp/python/2.6.8/Python-2.6.8.tar.bz2', auth=HTTPBasicAuth('user', 'pass'),verify = False)
    print "Downloading python"
    with open("Python-2.6.8.tar.bz2", "wb") as code:
        code.write(r.content)
    if r.status_code == 200:
        return True
    else:
        return False
def install_python():
    print "Extracting the python"
    import pdb;pdb.set_trace()
    cwd = os.getcwd()
    subprocess.call('tar xvf Python-2.6.8.tar.bz2', shell=True)
    new_path = os.path.join(cwd, 'Python-2.6.8')
    #subprocess.call('cd Python-2.6.8', shell=True)
    subprocess.call('./configure --prefix=/home/halesh/python && make && make install', shell=True)
    print "Installing the python"
if __name__ == '__main__':
    download()
    install_python()
