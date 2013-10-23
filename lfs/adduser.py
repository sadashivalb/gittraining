
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
To change the partition to some other
vim /etc/fstab
change to /mount to /apps
mount -a
iptables/ip6tables used to block the port to outside the world.
chkconfg - used to check the service status,start,stop and restart
Firewall-prgm to block and open required one
network -- transfer of data
tcp - communicate two machines with huge data
udp - less data for communication

