# Day 9
*   Amazon EBS (Elastic Block Storage)
*   EBS is commonly used for Wordpress and MySql Databases.
*   Today's session is about connecting google drive with aws and use python to store and access data.
*   Using multiple storages and combining them together to form a single big storage it is called distributed storage.
*   Connecting multiple storage devices connected in a same system and making a group is called Device mapping (System Process) and Package (Device Mapper).
*   For connecting on different system we use CEPH and GFS to connect them.
*   Device Mapper used two tools LVM and Straitis.
## Facts
*   Smallest LXC ever created is 1.84KB which gives result of Hello World.
*   RHEL8 introduces Podman (Platform product) and Buildah (Backend Support).
*   In RHEL7.5 or Ubuntu it is called Docker.

## LVM (Logical Volume Management)
*   It is used to connect multiple hard disks and manage volumes.
*   Step 1 Connect multiple physical disks
*   Step 2 Use LVM to create a volume group
*   Step 3 Then create Logical volumes or partitions as per the requirement.
*   ```pvcreate``` is a command used to create physical storages.
*   Since ```pvcreate``` is not a by default installed package therefore we need to install it using ```yum```.
*   To find package name of a command use the command
```
yum whatprovides */pvcreate
```
## Creating Volume Group and Partition
*   We use pvcreate to create physical storage
```
pvcreate /dev/xvdg /dev/xvdf
pvcreate /dev/xvd{g,f}
```
```
[root@ip-172-31-9-238 ~]# pvcreate /dev/xvd{f,g}
  Physical volume "/dev/xvdf" successfully created.
  Physical volume "/dev/xvdg" successfully created.
```
*   Now we are creating virtual group using the command ```vgcreate``` and give a group name with that.
```
[root@ip-172-31-9-238 ~]# vgcreate myvirdd /dev/xvd{f,g}
  Volume group "myvirdd" successfully created
```
*   To display the status of virtual group use command ```vgdisplay```
```
[root@ip-172-31-9-238 ~]# vgdisplay myvirdd
  --- Volume group ---
  VG Name               myvirdd
  System ID
  Format                lvm2
  Metadata Areas        2
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                2
  Act PV                2
  VG Size               3.99 GiB
  PE Size               4.00 MiB
  Total PE              1022
  Alloc PE / Size       0 / 0
  Free  PE / Size       1022 / 3.99 GiB
  VG UUID               iNRVcL-Wez9-xYY2-QuZN-OXuf-VGvi-IEQvc9
  ```
* Physical Extent (PE Size) is similar to sectors in Hard Disk. It is by default in 4MB Multiple. 
*   PE is also the minimum size of the virtual hard disk. We can configure that according to our requirements.
*   Now we need to create logical volume so there is a command called ```lvcreate```
```
lvcreate --name part1 --size 400M myvirdd
```
*   Now we need to mount the partition you can check the path of the partition using ```lvdisplay```
*   Now mount it ```mount /dev/mapper/myvirdd-part1 /mnt/part1```

## Configure SSHD to provide access remotely.
*    Create a user account in your AWS names ```adhoc``` and use the password ```123spacespace```.
*   Edit the line no 65 of ```/etc/ssh/sshd_config```
*   Turn it to Yes
*   Then restart the service ```systemctl restart sshd```
* Now you can connect via ```ssh username@ipaddress

## Micro Services and Docker
*   These are small custom programs which are specifically designed to run a particular code or platform.
*   Setup yum package
```
[docker]
baseurl=http://13.234.66.67/summer19/kubernetes
gpgcheck=0
```
*   Install docker using ```yum install docker```



