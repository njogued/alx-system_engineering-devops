### 0x0E. Web stack debugging #1

#### Commands to remember when debugging
- ```sudo netstat -lndp``` displays the process for each listening port. Based on the output one may then decide if the process is listening on the correct port.  
- ```/var/log``` with ```tail -f``` checks the logs.  
- ```curl``` checks if one can connect to the HTTP port from the location.  

[Resource - First 5 Commands When I Connect on a Linux Server](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/)  
<ol>
<li>w - Displays info such as the server uptime, the users on the server and the load average</li>
<li>history - Displays the previous commands run by the user</li>
<li>top - Displays all running processes and infor such as CPU, memory utilization and Time.</li>
<li>df - with flag h, df displays the disk space</li>
<li>netstat - with flags lp, netstat displays the port and IP that the server is listening on.</li>
</ol>
  
#### Machine-level debugging
- Does the server have free disk space? - df
- Is the server able to keep up with CPU load? - w, top, ps
- Does the server have available memory? free
- Are the server disk(s) able to keep up with read/write IO? - htop
  
#### Network debugging
- Does the server have the expected network interfaces and IPs up and running? ifconfig
- Does the server listen on the sockets that it is supposed to? netstat (netstat -lpd or netstat -lpn)
- Can you connect from the location you want to connect from, to the socket you want to connect to? telnet to the IP + PORT (telnet 8.8.8.8 80)
- Does the server have the correct firewall rules? iptables, ufw:
     - iptables -L
     - sudo ufw status

#### Process Issue
- Is the software started? init, init.d:
     - service NAME_OF_THE_SERVICE status
     - /etc/init.d/NAME_OF_THE_SERVICE status
- Is the software process running? pgrep, ps:
     - pgrep -lf NAME_OF_THE_PROCESS
     - ps auxf
- Is there anything interesting in the logs? look for log files in /var/log/ and tail -f is your friend

#### Task 0. Nginx likes port 80
- Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.
```
Requirements:
Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
Write a Bash script that configures a server to the above requirements
```

#### Task 1. Make it sweet and short
- Using what you did for task #0, make your fix short and sweet.
```
Requirements:
Your Bash script must be 5 lines long or less
There must be a new line at the end of the file
You must respect usual Bash script requirements
You cannot use ;
You cannot use &&
You cannot use wget
You cannot execute your previous answer file (Do not include the name of the previous script in this one)
service (init) must say that nginx is not running ← for real
```
