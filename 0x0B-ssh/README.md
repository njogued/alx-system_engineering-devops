## 0x0B. SSH

### SSH Key Pair - Public and Private
SSH Keys may be generated using the command ```ssh-keygen``` which generates both the public and the private key  
  
The public key is saved with an extension ```.pub``` 
The flag ```-t``` may be used to specify the type of key to create ie. ```ssh-keygen -t rsa``` generates an rsa key  
  
The key should also be copied to the public key to the server to be used.
```ssh-copy-id username@remote_IP_host``` copies the public key to the authorized_keys file  
Alternatively paste the key without copy-id using ```cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"```  
  
Logging in to the remote server using: ```ssh username@remote_IP_host```
