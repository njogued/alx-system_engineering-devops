## 0x0A. Configuration Management

- Automated configuration management using Puppet.Configuration management handles changes systematically to ensure that a system maintains its integrity over time. 
- Repetitive tasks can be managed using configuration management tools and such tools allow management of several servers from a central controller machine.
```
Benefits include:
 - Quick provisioning of new servers
 - Quick recovery from critical events
 - Version control for the server environment
```
### Puppet
Puppet has a master-slave architecture  
The Puppet agent sends ```Facts``` to the Puppet Master and the Puppet Master sends a ```Catalogue``` that defines the configuration settings. The Puppet Slave sends back a ```Report``` to indicate that the settings have been implemented.  
Puppet Master and Puppet Slave communicate through a secured SSL.  

### Task 0. Create a file
Using Puppet, create a file in /tmp.
```
Requirements:
File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet
```

### Task 1. Install a package
Using Puppet, install flask from pip3.
```
Requirements:
Install flask
Version must be 2.1.0
```

### Task 2. Execute a command
Using Puppet, create a manifest that kills a process named killmenow.
```
Requirements:
Must use the exec Puppet resource
Must use pkill
```
