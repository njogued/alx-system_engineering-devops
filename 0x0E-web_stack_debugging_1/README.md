### 0x0E. Web stack debugging #1

#### Commands to remember when debugging
- ```sudo netstat -lndp``` displays the process for each listening port. Based on the output one may then decide if the process is listening on the correct port.  
- ```/var/log``` with ```tail -f``` checks the logs.  
- ```curl``` checks if one can connect to the HTTP port from the location.  

[Resouce - First 5 Commands When I Connect on a Linux Server](https://www.linux.com/training-tutorials/first-5-commands-when-i-connect-linux-server/)  
<ol>
<li><strong>w<\strong> - Displays info such as the server uptime, the users on the server and the load average</li>
<li><strong>history<\strong> - Displays the previous commands run by the user</li>
<li><strong>top<\strong> - Displays all running processes and infor such as CPU, memory utilization and Time.</li>
<li><strong>df<\strong> - with flag h, df displays the disk space</li>
<li><strong>netstat<\strong> - with flags lp, netstat displays the port and IP that the server is listening on.</li>
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
