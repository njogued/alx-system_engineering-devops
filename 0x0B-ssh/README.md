## 0x0B. SSH

### SSH Key Pair - Public and Private
SSH Keys may be generated using the command ```ssh-keygen``` which generates both the public and the private key  
  
The public key is saved with an extension ```.pub``` 
The flag ```-t``` may be used to specify the type of key to create ie. ```ssh-keygen -t rsa``` generates an rsa key  
  
The key should also be copied to the public key to the server to be used.
```ssh-copy-id username@remote_IP_host``` copies the public key to the authorized_keys file  
Alternatively paste the key without copy-id using ```cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"```  
  
Logging in to the remote server using: ```ssh username@remote_IP_host```  

### Commands
#### Moving files or folders to remote
In local machine run command ```scp <PATH TO EXAMPLEFILE> username@remote_IP_host:<DESTINATION PATH>```  

### Task 0. Use a private key
- Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.
```
Requirements:
Only use ssh single-character flags
You cannot use -l
You do not need to handle the case of a private key protected by a passphrase
```
### Task 1. Create an SSH key pair
- Write a Bash script that creates an RSA key pair.
```
Requirements:
Name of the created private key must be school
Number of bits in the created key to be created 4096
The created key must be protected by the passphrase betty
```

### Task 2. Client configuration file
- Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.
```
Requirements:
Your SSH client configuration must be configured to use the private key ~/.ssh/school
Your SSH client configuration must be configured to refuse to authenticate using a password
```
