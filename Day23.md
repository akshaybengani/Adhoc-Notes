# Day 23 HTML
*   HTML is designed as an alternative for Microsoft Office, because Microsoft Office is not browsable.
*   HTML is a documentation language which is used to write documentation.
*   A HTML page is accessible world wide via internet.
*   A Webpage is 100% document
*   We can create HTML pages with .htm, .html.
*   To change a page every 7 seconds
```htm
<meta http-equiv="refresh" content="7;url=http://google.com">
```
*   When we dont need to open a new page and the working will be on the same page
*   We will use iframe
## Python Backend CGI
*   To communicate Apache with Python we have a Common Gateway Interface (CGI) for this.
*   CGI is used to provide connectivity to programming language with Apache server.

## Writing our 1st CGI File
*   It is necessary to give path of the python interpreter path
```py
#!/usr/bin/python3
```
*   We need to disable Selinux before using our webpage.
```
setenforceing 0
```
*   We can permanently disable Selinux vai ```/etc/selinux/config```
*   Now we need to import ```CGI``` for our use.
*   CGITB is used to display errors on the webpage and error log. CGITB full form Common Gateway Interface Trace Back.
```py
import cgi
import cgitb
```
*   Now we need to enable cgitb
```py
cgitb.enable()
```  
*   We need to write two lines neccessarily to use python as backend
```py
print("Content-type:text/html")
print("")
```
*   To get root access in CGI we have to make ```apache``` user as sudo user.
*   To add apache as sudo user open the file in ```/etc/sudoers.d/90-cloud-init-users``` and this line in it.
```
apache ALL=(ALL) NOPASSWD:ALL
```
*   To use cgi-bin in Debian distribution like ubuntu you have to tell the apache to give access to cgi-bin.
*   As such to enable cgi-bin use the command
```
a2enmod cgi
```
*   The default cgi-bin path in ubuntu is ```/usr/lib/cgi-bin```

## Things to explore about OS
*   Windows 2016 Server
*   Redhat
*   Ubuntu
*   Open SUSE

## Using Subprocess module
*   To run a linux or windows command in python we use subprocess.
```py
import subprocess
result = subprocess.getoutput("date")
```

## Tasks
*   Why we cannot open google.com in iframe
*   And how we can do this the same for our page
*   Use the iframe to drag and drop the iframe
*   The iframe should allow to resize the window

## RHEL Setup
*   Add these to your yum.repos.d/adhoc.repo
```
[adhoc]
baseurl=http://13.234.66.67/summer19/kubernetes
gpgcheck=0

[python]
baseurl=http://13.234.66.67/summer19/python3
gpgcheck=0

[ansible]
baseurl=http://13.234.66.67/summer19/ansible27
gpgcheck=0

[rhel]
baseurl=http://13.234.66.67/summer19/rhel75
gpgcheck=0
```
*   Install these using yum
```
yum install python3* -y
yum install docker* -y
yum install ansible -y
yum install httpd -y
```