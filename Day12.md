# Day 12 
*   Edit the file
```
/etc/selinux/config
```
*   and write ```disable``` in that
*   Awk is used to print column of a file
*   sed is used to replace the keyword

# Ansible
* Ansible will connect windows using WinRM protocol.
*   To connect docker we have docker API written in GO
*   To connect network devices we will use SSH
*   To Connect Cloud we use API
*   To connect Linux we use SSH
*   I have two machines both are on AWS.
*   To install Ansible use the command
```
yum install ansible
```
*   In which machine we install ansible a file created called inventory file in ```/etc/ansible/hosts```
*   We have to define IP address of the host

## Steps for Ansible
1.  Pick two machines
2.  Install Ansible in Machine 1
3.  Assign password to ```ec2-user``` in OS2
```
passwd ec2-user
```
4.  Change in OS2 /etc/ssh/sshd_config to accept Password in OS2
```
Line 65:    PASSWORD_AUTHENTICATION = YES
```
5.  Restart the sshd service
```
systemctl restart sshd
```
6.  Add IP address in the hosts file of ansible ```/etc/ansible/hosts```
```
[a]
13.234.48.87
```
*   Run the command this will run group ```a``` of the host file
```
ansible a -u ec2-user -m ping -k
```
*   ```-u``` is for defining the username
*   ```-m``` is used for importing a python module and here we are using ```ping```
*   ```-k``` is used for defining SSH Password

## Generating your own Keys
*   Generate keys using ```ssh-keygen```
```
ssh-copy-id ec2-user@13.234.48.87
```
*   Now enter password of the machine and the public key is sent to machine2.
*   mod-ssl is used to setup website https


