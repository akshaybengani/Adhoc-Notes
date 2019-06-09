# Day 7

MBR (Master Boot Record) In our old laptops we have by default bios loaders which means we have MBR installed. Since new releases have by default UEFi installed.

## To list the disks attached in the system
Use the command ```lsblk``` to list the attached volumes

## To list detailed view of hard drives
Use the command ```fdisk -l``` to list detailed view of drives.

```
[root@ip-172-31-43-73 ~]# fdisk -l
WARNING: fdisk GPT support is currently new, and therefore in an experimental phase. Use at your own discretion.

Disk /dev/xvda: 10.7 GB, 10737418240 bytes, 20971520 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: gpt
Disk identifier: 477BBCC7-BB8A-408B-9778-8F4E6E46B138


#         Start          End    Size  Type            Name
 1         2048         4095      1M  BIOS boot
 2         4096     20971486     10G  Microsoft basic

Disk /dev/xvdf: 2147 MB, 2147483648 bytes, 4194304 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```
## To list detailed view of a selected drive
Use ```fdisk -l /diskname```
```
[root@ip-172-31-43-73 ~]# fdisk -l /dev/xvdf

Disk /dev/xvdf: 2147 MB, 2147483648 bytes, 4194304 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

## To get inside a hard disk
Use ```fdisk /drivename```
```
[root@ip-172-31-43-73 ~]# fdisk /dev/xvdf
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table
Building a new DOS disklabel with disk identifier 0xf5cce8b6.

Command (m for help): print

Disk /dev/xvdf: 2147 MB, 2147483648 bytes, 4194304 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0xf5cce8b6

    Device Boot      Start         End      Blocks   Id  System

Command (m for help):
```
## Create ```new``` partition
The smallest thing in a hard disk is sector which is a size of 512bytes.
Now to create a new partition use the command ```new``` or ```n``` to create a new partition.

```
Command (m for help): n
Partition type:
   p   primary (0 primary, 0 extended, 4 free)
   e   extended
Select (default p):
```

## To create a primary partition in disk
By default we create a primary partition so in order to create a primary partition we have to press ```p``` in order to create a primary partition.
```
Select (default p): p
Partition number (1-4, default 1):
```
## To start the first sector we have to enter the block value by default we have to press ```enter```.
```
First sector (2048-4194303, default 2048):
Using default value 2048
```
## Now we have to give size or number of sectors
To give size we use ```+300M``` to create a 300MB partition in the drive
```
Last sector, +sectors or +size{K,M,G} (2048-4194303, default 4194303): +300M
```
## Again we have to create 2 more primary partitions total 3 primary
```
Command (m for help): n
Partition type:
   p   primary (2 primary, 0 extended, 2 free)
   e   extended
Select (default p): p
Partition number (3,4, default 3):
First sector (1026048-4194303, default 1026048):
Using default value 1026048
Last sector, +sectors or +size{K,M,G} (1026048-4194303, default 4194303): +100M
Partition 3 of type Linux and of size 100 MiB is set
```
## Now we have to create the last partition as extended partition.

```
Command (m for help): n
Partition type:
   p   primary (3 primary, 0 extended, 1 free)
   e   extended
Select (default e):
Using default response e
Selected partition 4
First sector (1230848-4194303, default 1230848):
Using default value 1230848
Last sector, +sectors or +size{K,M,G} (1230848-4194303, default 4194303):
Using default value 4194303
Partition 4 of type Extended and of size 1.4 GiB is set
```

#### Note never ever delete or format extended partition because it contains all of your logical partitions.

## Now we will create our 1st logical partition.
```
Command (m for help): n
All primary partitions are in use
Adding logical partition 5
First sector (1232896-4194303, default 1232896):
Using default value 1232896
Last sector, +sectors or +size{K,M,G} (1232896-4194303, default 4194303): +250M
Partition 5 of type Linux and of size 250 MiB is set

Command (m for help): p

Disk /dev/xvdf: 2147 MB, 2147483648 bytes, 4194304 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0xcff9d12c

    Device Boot      Start         End      Blocks   Id  System
/dev/xvdf1            2048      616447      307200   83  Linux
/dev/xvdf2          616448     1026047      204800   83  Linux
/dev/xvdf3         1026048     1230847      102400   83  Linux
/dev/xvdf4         1230848     4194303     1481728    5  Extended
/dev/xvdf5         1232896     1744895      256000   83  Linux
```
## Now to save the partition system we have to use ```wq``` to save and exit the partition system
```
Command (m for help): wq
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
[root@ip-172-31-43-73 ~]#
```
#### Now we have created partitions now we need to format the partitions in order to make it understandable to Operating system
Formatting a system means making enviorment, when we format a drive it cleans the ```Inode``` table index, this doesn't means that we have deleted the data from the hard drive.
