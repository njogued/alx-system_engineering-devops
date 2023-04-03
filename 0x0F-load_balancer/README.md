### 0x0F. Load balancer
  
#### Concepts
[HAProxy and Load Balancer Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)  
[HTTP Headers](https://www.techopedia.com/definition/27178/http-header)  
[Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)  
  
#### Types of Load Balancing
  
##### Layer 4 Load Balancing
- Load balancing on layer 4 (load balancing) forwards user traffic based on IP range and port. 
  
##### Layer 7 Load Balancing
- The load balancer using layer 7 forwards user content to different servers based on the content of the user's request
- For example, frontend configuration for a load balancer may be:
```
frontend http
    bind *:80
    mode http
```
  
```
Note: Despite using different servers, the servers use the same database.
```
  
#### Task 0. Double the number of webservers
- In this first task you need to configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!
- Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.
```
Requirements:
Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
The name of the custom HTTP header must be X-Served-By
The value of the custom HTTP header must be the hostname of the server Nginx is running on
Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task
Ignore SC2154 for shellcheck
```
