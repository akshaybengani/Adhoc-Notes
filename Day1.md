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

## Create new users  in linux
*   To create new user we use ```useradd``` command to add a new user
```
useradd akshay
```
*   There is a command called ```pinky``` which displays users and state.

## Files in Linux
*   You can create files in linux using ```touch``` command and delete files in linux using ```rm```
```
touch akshay.txt
touch akshay{1,2,3,4,5}.txt
touch akshay{1..50}.txt

rm akshay.txt
rm akshay{1,2,3,4,5}.txt
rm akshay{1..50}.txt
```
#### To get the current logedin username there is a command called ```whoami``` for getting name of the user logedin.
## Date and Cal
*   To check the current date in linux and calender in linux we have commands ```date``` and ```cal``` for these.
*   There are various special arguments in date command to get your specialized date format. Example
```
date +%d/%m/%y
```
*   ```cal``` or Calender command displays a calender in terminal for example
```
      June 2019
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30
```
*   To get calender of a specific year or such enter the year number in arguments and there are lots of arguments in calender
