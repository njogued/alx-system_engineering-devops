### Attack is the best defense

#### Concepts
[Resouce - ARP Spoofing](https://www.imperva.com/learn/application-security/arp-spoofing/)  
[Resource - Installing and Using tcpdump](https://www.hugeserver.com/kb/install-use-tcpdump-capture-packets/)  
  
#### Network Sniffing
- Computers on the LAN are configured to ignore any other traffic on the network except for the traffic intended for it.
- Network sniffing software opens up the computer's Network Interface Card (NIC) and reads all data on the LAN.

#### ARP Spoofing  
- Some legacy systems such as ```telnet``` continue to use unencrypted communication means.
- ARP spoofing is a ```Man In The Middle``` attack ([MITM](https://www.imperva.com/learn/application-security/man-in-the-middle-attack-mitm/)) in which an attacker impersonates one of the parties in an attack. 
- ARP spoofing takes advantage of the ARP protocol used with the IPv4 standard (IPv6 uses the Neighbor Discovery Protocol(NDP)).
- The ARP protocol translates the IP address to the MAC address, and viceversa. The ARP protocol relies on an ARP cache on the host which has a mapping table to match IP addresses and MAC addresses.
- If the host does not know the MAC address corresponding to the IP address, the host sends an ARP request packet asking machines on the network for th matching MAC address.
- The ARP protocol does not verify the authorization of the machine that sends the response and also lets the host accept ARP responses even without sending out requests. Thus the ARP protocol allows for ARP spoofing.

#### Steps in ARP Spoofing
<ol type="1">
    <li>Attacker accesses the network</li>
    <li>Attacker uses a spoofing tool such as Arpspoof, Abel, Arpoison, Ettercap, Cain, or Driftnet to send forged ARP responses</li>
    <li>The forged response advertises the attackers MAC address as the correct MAC address for both the router and the attacked workstation</li>
    <li>The router and attacked workstation can only communicate through the Man in the Middle</li>
</ol>
<img src="https://www.imperva.com/learn/wp-content/uploads/sites/13/2020/03/thumbnail_he-ARP-spoofing-attacker-pretends-to-be-both-sides-of-a-network-communication-channel.jpg" alt="ARP Spoofing Attack" width="400" height="400"/>

#### Stopping and preventing an ARP attack
- To check if the ARP cache has been poisoned, run ```arp -a``` and check if there is a MAC address that corresponds to two IP addresses or use the opensource Wireshark protocol.
- To prevent an ARP Spoffing, use a VPN, a static ARP, packet filtering, ARP spoofing detection software, cryptographic network protocols such as HTTPS, SSH, and TLS, and simulate spoofing attacks to identify vulnerabilities. 

#### Using tcpdump
- run ```man tcpdump``` or read the [documentation](https://www.hugeserver.com/kb/install-use-tcpdump-capture-packets/). 
- Basic: ```tcpdump -i <interface>``` captures traffic on the interface specified, e.g. eth0 for Ethernet. Flag ```-c``` specifies number of packets to capture, ```-w``` writes to a file. Combined, ```sudo tcpdump -i eth0 -c 100 -w capture.pcap```
```
- Tip: Use a base-64 decoder like [this one](https://www.base64decode.org/) to find the password specified by the authorization code 334
```

#### 
