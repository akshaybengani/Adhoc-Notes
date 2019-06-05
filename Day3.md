# Day 3

### Why to work on open source projects
If you have some idea which you want to build and many times you dont have much resources to do this alone then you can go with open source.

### Why people join your project?
People will join because they want to contribute in the project because by this there name will be added in that project

### GSOC (Google Summer of Code)

### To check system information
```
cat /etc/os-release
PRETTY_NAME="Kali GNU/Linux Rolling"
NAME="Kali GNU/Linux"
ID=kali
VERSION="2019.1"
VERSION_ID="2019.1"
ID_LIKE=debian
ANSI_COLOR="1;31"
HOME_URL="https://www.kali.org/"
SUPPORT_URL="https://forums.kali.org/"
BUG_REPORT_URL="https://bugs.kali.org/"
```
### Redhat system information
```
cat /etc/os-release

```
This is similar to fedora distribution

### To get value of Path
Path is the collection of folders where different commands are stored.
```
echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/mnt/c/Program Files/WindowsApps/KaliLinux.54290C8133FEE_1.1.9.0_x64__ey8k8hqnwqnmg:/mnt/c/Windows/System32:/mnt/c/Windows:/mnt/c/Windows/System32/wbem:/mnt/c/Windows/System32/WindowsPowerShell/v1.0:/mnt/c/Program Files/Java/jdk-11.0.2/bin:/mnt/c/Program Files/nodejs:/mnt/c/ProgramData/chocolatey/bin:/mnt/c/Program Files/Git/cmd:/mnt/c/Windows/System32/OpenSSH:/mnt/c/Users/DrVirus/AppData/Local/Programs/Python/Python37-32/Scripts:/mnt/c/Users/DrVirus/AppData/Local/Programs/Python/Python37-32:/mnt/c/Users/DrVirus/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/DrVirus/AppData/Roaming/npm:/mnt/c/Users/DrVirus/AppData/Local/Programs/Microsoft VS Code/bin:/mnt/d/flutter/bin:/mnt/c/Users/DrVirus/AppData/Local/Android/Sdk/tools:/mnt/c/Users/DrVirus/AppData/Local/Android/Sdk/platform-tools
```
### To check what is the path of a command
To  get the value we use a command ```which``` for getting path of a command.
```
which python

```
### Input output devices
Input devices are the devices where we can give input to the computer in any form by touch, click, key press etc

Output devices are the devices where we get the output by the system in any form to the user understandable format.

**FLAG: Important topic of RedHat exam**<br>
**```Output Redirection```** means changing the output location from the actual place to somewhere else. Now we will redirect output to.
file, email, printer, whatsapp etc..

### to save a data in a file by console
Use ```>``` sign and file name to save the data in a new or existing file.
```
date > ok.txt
```
When we use ```>``` this sign this will overrite the file.<br>
To create a file without using any other command<br>
```
>ok.txt
```
this will create a new file with empty text
### To Send Output of a program in a file
For example we have a python file of
```python
print("Hello World")
```
and we want to save its output we use
```
python a.py > hello.txt
```
### Use ```>>``` for appending text in file
This symbol ```>>``` will add a new line without deleting the previous output in the file.
```
date > a.txt
cat >> a.txt
```
now calender will be appended in the previous file without overiting it.
### If we have used wrong command and used this operator.
In this case this will overite the file with null, basically empty file again

### To save the error log or error output in file
Use ```2``` and the ```> >>``` symbol to save the error log. By using ```2``` here will save the output as well as error both.

### To check that the output bash have given output or error
Here we use exit code every program used a exit code process which remembers the exit code of the program
```
echo $?
```
Run this line after running your previous testing command and if it returns ```0``` then there is no error and if it will return a non-zero value then it is different.

### To get the exit code in a file we use ```&```
To check that the program gives an error exit code and we can save this using ```&>``` or ```&>>```. <br><br>
**Python uses sh: shell for the processing**<br>
**Storing and reading data from hard disk is the most slow process of the entire Operating system process**
### To count lines words and characters in shell language
```
wc -l hello.txt
wc -w hello.txt
wc -c hello.txt
```
### To get the line where the text is stored
**General regular expression pattern**
```
grep 'hello' file.txt
hello world
hello world this
hellovsv world this
hvkvv hello world this
```
To get the non case sensitive output we will use ```-i``` argument with grep
```
grep -i hello file.txt
hello world
hello world this
HELLO WOrld this
HeLLo world this
hellovsv world this
hvkvv hello world this
```
To get the word where hello is only specific seperate word not joined ```-w```.
```
grep -w hello file.txt
hello world
hello world this
hvkvv hello world this
```
You can use multiple arguments also like ```-i``` and ```-w``` to find a word.
```
grep -iw hello file.txt
```
To get non match lines we use ```-v``` in grep as argument.
### To execute two commands in single line we use ```|``` pipe
to count no of lines, word, characters without saving in storage.
```
cal | wc -l
```
### Press Ctrl+D to get word, line, character output from wc directly by pressing this combination
```
bash$ wc
akshuysv
jjnvk
 vdf
vdnl
$ctrl+d 
    3   5  40
```
### Pipe examples
```
cal | grep 1
cal | grep 1 | grep -i june
cal | grep 1 | grep -i june | wc -w
```
### ```head``` and ```tail``` command
To get top n no of lines we use head.<br>
To get bottom n no of lines we use tail.
```
cal | head -3
cal | tail -3
cal | head -4 | tail -1
```
### To send mail from terminal
There is a command called ```mail``` explore  
dns watch

### Version Control System
The system which maintain your souce code everyday everytime for different versions.
<br>Source Code Management is the technology which remembers the code day wise date wise everyday.
### We can assign a comment to a variable also
```python
option = '''
Hey My name is Akshay Bengani
This is Day3 
'''
print(option)
```
**To use a command in shell as a text use back quotes [``` ` ```].**
## Some python liberaries 
```Commands``` is a liberary which allows me to access system commands, note this is not available in python3.<br>
```subprocess``` is a liberary which allows me to access system commands and processes in python.<br>
```OS``` is a liberary which allows me to access OS functionality.
```python
import subprocess
dir(subprocess)
subprocess.getoutput('gedit')
```
### Google Search URL
https://www.google.com/search?q=hello This URL can be used to search a string. on goofle by python using subprocess by firefox.

### Web Browser module in Python
This liberary ```webbrowser``` will provide you functionality to access system web browsers.
```python
import webbrowser
dir(webbrowser)
data = input("Enter your search term")
webbrowser.open_new_tab('https://www.google.com/search?q='+data)
```




 








