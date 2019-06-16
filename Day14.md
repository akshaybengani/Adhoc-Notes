# Day 14
Today we will learn about ```NFS``` (Network File System)

*   We need to install this package, This package gives us a feature to use ```tab``` key to autocomplete things.
```
yum install bash-completion
```
*   After installing we need to restart bash service just type ```bash```
```
bash
```
## NFS Configuration
*   The package which provide us NFS service we use the package
```
yum install nfs-utils
```
*   Now we need to start the service and keep that enabled in next boot we use
```
systemctl start nfs-server
systemctl enable nfs-server
```
*   Now we need to create a directory in ```/``` partition which we will use to share on the network
```
mkdir /nfs
```
*   We can check the configuration file of a package using the command
```
whereis /*nfs
```
*   Using ```-qc``` with rpm gives us a list of all the configuration file.
```
[root@ip-172-31-9-238 nfs]# rpm -qc nfs-utils
/etc/gssproxy/24-nfs-server.conf
/etc/modprobe.d/lockd.conf
/etc/nfs.conf
/etc/nfsmount.conf
/etc/request-key.d/id_resolver.conf
/etc/sysconfig/nfs
/var/lib/nfs/etab
/var/lib/nfs/rmtab
/var/lib/nfs/state
/var/lib/nfs/xtab
```
*   Now we need to create a configuration file in ```/etc/exports``` so we have created a configuration file called exports
*   change folder permissions
```
chmod 757 /nfs/
```
```
/nfs *(ro)
```
*   Now run these
*   ```exportfs -r``` is used to reload the ```exports``` configuration
```
exportfs -r
showmount -e 172.31.45.242
systemctl status firewalld.target
systemctl status iptables.service
systemctl restart nfs
iptables -F
```
*   iptables works at the backend of the firewall configuration.
*   To force allow everything to iptables we use
```
iptables -F
```
*   This command will turn SELinux off.
```
setenforce 0
setenforce: SELinux is disabled
```
*   Now we need to mount the ip address
```
mkdir /mnt/mynfs
mount 172.31.45.242:/nfs /mnt/mynfs
```
*   This is used to give root access to the user who is using the NFS system.
```
/nfs *(rw,no_root_squash)
```
*   Now we need to entry in fstab
*   ```_netdev``` is used to specify that mount this device when you get networkIP, so that while in boot time this entry don't get crashed.
*   So first we will get systemIP then we will mount to the nfs drive.
```
vi /etc/fstab
172.131.45.242:/nfs /mnt/nfs/   nfs  _netdev 0 0
```
*   Check this before you restart.
```
mount -a
```
