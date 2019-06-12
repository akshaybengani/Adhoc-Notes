# Day 1
*   Kernel is a software component which communicates between the hardware and application software.
*   User Enters 2+3 in calculator application
*   An Interpreter converts the application language to machine code and send to Kernel
*   Then Kernel executes the code by application software to actual IC's and CPU to get output and input from them.
*   Operating System is made up Application Softwares, Interpreters, and most importantly kernel.

## Different Operating System have different Installation files.
*   In Windows we use ```.exe``` or ```.msi``` because its kernel understand these formats only.
*   In linux we have mainly two types of packages ```.deb``` and ```.rpm```, both are from two major distributions Debian and Fedora.
*   In MAC we use ```.dmg```.
*   Windows Kernel name is ```Windows NT```.
*   Redhat, Ubuntu or any linx OS kernel is ```Linux```.
*   Mac os uses ```darwin``` kernel.

## Folders in Linux
*   You can create folders in linux using ```mkdir``` and delete folders using ```rmdir```
```
mkdir adhoc
mkdir adhoc{1,2,3,4,5,6}
mkdir adhoc{1..50}

rmdir adhoc
rmdir adhoc{1,2,3,4,5,6}
rmdir adhoc{1..50}

for((i=1;i<50;i++))
do
mkdir adhoc$i
done
```
## Basic differences between windows and linux
| Windows     | Linux   |
| ----------- | --------|
|   Admin     |   Root  |
|   Notepad   | gedit   |
|   cmd       | Terminal|
|   IE        | Firefox |
|   exe       | .deb/.rpm|
|   c         | /       |
| c:\Users\Adhoc\Desktop | /home/Adhoc|

## Create 