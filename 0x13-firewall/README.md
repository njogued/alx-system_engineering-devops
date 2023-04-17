### 0x13. Firewall
  
#### Resource(s)
[Resource - ufw commands on ubuntu](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)  
[Resource -Firewall port forwarding](https://www.baeldung.com/linux/ufw-port-forward)  
  
#### Configuring a Firewall on Ubuntu
- One may install UFW using the commands ```sudo apt-get update``` then ```sudo apt-get install -y ufw```. ```allow``` and ```deny``` commands permit or deny traffic. 
- To deny all outbound traffic: ```sudo ufw default deny incoming```
- To allow outbound traffic: ```sudo ufw default allow outgoing```
  
- Allow traffic to the HTTP, HTTPS, and SSH ports.
```
syntax: sudo ufw allow <PORT NUMBER>
```
	 - sudo ufw allow 22
	 - sudo ufw allow 80
	 - sudo ufw allow 443
  
- Enable ufw using the command: ```sudo ufw enable```. Alt: if you ever need to disable ufw, run the command ```sudo ufw disable```
  
- To block a specific IP address, syntax ```sudo ufw deny from <IP ADDRESS>```
  
#### Task 0. Block all incoming traffic but
- Let’s install the ufw firewall and setup a few rules on web-01.
```
Requirements:
- The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
- Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
	 22 (SSH)
	 443 (HTTPS SSL)
	 80 (HTTP)
```
- Share the ufw commands that you used in your answer file

#### Task 1. Port forwarding
- Firewalls can not only filter requests, they can also forward them.
```
Requirements:
	 -Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
```
- Your answer file should be a copy of the ufw configuration file that you modified to make this happen
