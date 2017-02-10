#/usr/bin/evn python
import subprocess
x = subprocess.check_output("ansible 127.0.0.1 -m setup",shell=True)

