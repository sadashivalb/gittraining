
def run():
    print "Hello"

if __name__ == '__main__':
    run()

"""to adduser in linux
useradd sada
passwd
vim /etc/sudoers
## Allow root to run any commands anywhere
root	ALL=(ALL) 	ALL
sada    ALL=(ALL) 	ALL
add the user in the
/etc/ssh/sshd_config
make password authentication yes
change PermitRootLogin from 'without-password' to yes
PermitRootLogin without-password
/etc/init.d/sshd restart
service iptables stop
sudo /sbin/service network restart
"""
