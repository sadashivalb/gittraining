import os
import sys
import subprocess
import shutil
from datetime import date
import argparse
import requests
from requests.auth import HTTPBasicAuth

def verify_subsys_pkgserver(version,name):
    url = 'url'
    r = requests.get(url, auth=HTTPBasicAuth('un', 'pwd'), verify=False)
    print r.status_code
    if r.status_code == 200:
        print "hello"
        sys.exit(1)
    else:
        print "not found"
if __name__ == '__main__':
    version = version
    name = name
    verify_subsys_pkgserver(version,name)
