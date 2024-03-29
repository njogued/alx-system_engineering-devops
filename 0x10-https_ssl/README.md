### 0x10. HTTPS SSL
  
### Resources
[What is HTTPS?](https://www.instantssl.com/http-vs-https)  
[Why SSL?](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)  
[SSL Termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)  
[Using functions in bash](https://tldp.org/LDP/abs/html/complexfunct.html)  
  
[Installing Certbot](https://www.digitalocean.com/community/tutorials/how-to-use-certbot-standalone-mode-to-retrieve-let-s-encrypt-ssl-certificates-on-ubuntu-20-04) - Installing certbot  
[Configuring HAProxy with SSL Certification](https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04) - Use step #2  

#### HTTP vs HTTPS
- HTTPS uses either SSL (Secure Sockets Layer) or TLS (Transport Layer Security) to encrypt communications. 
- Both TLS and SSL use an asymmetric Public Key Infrastructure (PKI) whereby the ublic key and private key are used to encrypt comunications.
- The private key is strictly protected and should be securely kept on the webserver and only accessed by the owner.
  
#### SSL Certificate
- When a HTTPS connection to a webpage is requested, the website sends the SSL certificate to the browser. The certificate contains the public key to secure the session.
- The browser and website then initiate the SSL handshake. The SSL handshake involves generation of shared secrets to establish a secure connection.
- Since client information is encrypted, i.e., in the unlikely event of an interception in conneciton, the attacker would not be able to decrypt the data.
- The SSL certificate contains character strings that are keys used in decryption
- However SSL is disadvantageous due to increased cost to set up the infrastructure and decreased performance.
  
#### SSL Termination
- ChatGPT: SSL termination is the process of decrypting encrypted traffic at the termination point, using either a load balancer or a reverse proxy server.
- Once decrypted, the traffic is analyzed ofr security threats, monitored for compliance purposes and optimized for performance. The traffic is then sent to the destination server.

#### Task 0. World wide web
- Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.
```
Requirements:
Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)
Add the subdomain lb-01 to your domain, point it to your lb-01 IP
Add the subdomain web-01 to your domain, point it to your web-01 IP
Add the subdomain web-02 to your domain, point it to your web-02 IP
Your Bash script must accept 2 arguments:
     domain:
     type: string
     what: domain name to audit
     mandatory: yes
subdomain:
     type: string
     what: specific subdomain to audit
     mandatory: no
Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
When only the parameter domain is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
When passing domain and subdomain parameters, display information for the specified subdomain
Ignore shellcheck case SC2086
Must use:
     awk
     at least one Bash function
You do not need to handle edge cases such as:
     Empty parameters
     Nonexistent domain names
     Nonexistent subdomains
```

#### Task 1. HAproxy SSL termination
- [Debugging resource - Failed to Start HAProxy Load Balancer](https://discourse.haproxy.org/t/failed-to-start-haproxy-load-balancer/5224/2)  
- “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.
- Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..
```
Requirements:
HAproxy must be listening on port TCP 443
HAproxy must be accepting SSL traffic
HAproxy must serve encrypted traffic that will return the / of your web server
When querying the root of your domain name, the page returned must contain Holberton School
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
```
- The file 1-haproxy_ssl_termination must be your HAproxy configuration file
- Make sure to install HAproxy 1.5 or higher, SSL termination is not available before v1.5.  

#### Task 2. No loophole in your website traffic
- [Resource - Redirecting HTTP to HTTPS](https://www.haproxy.com/blog/redirect-http-to-https-with-haproxy/)
- A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.
```
Requirements:
This should be transparent to the user
HAproxy should return a 301
HAproxy should redirect HTTP traffic to HTTPS
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 100-redirect_http_to_https must be your HAproxy configuration file
```
