### 0x10. HTTPS SSL
  
### Resources
[What is HTTPS?](https://www.instantssl.com/http-vs-https)  
[Why SSL?](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)  
[SSL Termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)  
[Using functions in bash](https://tldp.org/LDP/abs/html/complexfunct.html)  

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
