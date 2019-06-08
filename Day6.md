# Day 6

In chmod we have a octal number system also there.<br>
Read  -   4
Write  -    2
execute -   1
remove  -   0

754 
4+2+1 = 7 read write execute
4+1 = 5 read execute
4 = 4 read

Sticky bit  -    1
SGID        -    2
2+1 =3 SGID and STicky bit
1 sticky
2 sgid

chmod 3777 /folder

Set File Access Control List
-m stands for modify
setfacl -m u:u4:rx /check
u stands for user
g stands for group

Get File Access Control List
getfacl /check
This is used to check the permissions

To remove facl we use
setfacl -x u:u4 /check

umask is a factor in permissions which gives permission to every new file or directory.

To remove permission from firefox from user 4
setfacl -m u:u4:--- /usr/bin/firefox

# Storage Management

There are two types of storage
*   Primary
*   Secondary

There are two types of RAM Static and Dynamic

## Secondary Storage

There are two types of partition table
*   MBR (Master Boot Record)
*   GPT (Guided Partition Table)

Partition table is a memory or a storage which remembers no of partitions size and other info.

### MBR Characterstics
* Maximum Size 2TB
* Maximum memory of partition information is 64 Bytes
* Maxximum 4 Primary partitions


### GPT Characterstics
* Maximum Size 8EB
* There is no logic behind extended partition we only have primary partitions no logical.
* Maximum by default number of partitions can be 128 we can configure that for more.


### Primary Partition
* An operating system needs primary partition for its installation.
* We can make maximum 4 primary partitions in MBR.

### Logical Partition
* There are under Extended partition.
* In an extened partition we have 60 Logical partition.

# Python Class

```py
impory sys
x= sys.argv[1:]
sum = 0
for i in x:
    sum = sum + int(i)
print(sum)
```
```
$python sum.py 1 5351 8453 465 3554 454 3
354015
```