## WPA 3
WPA2 (Wifi Protected Access 2) was the dominant standard for securing Wi-Fi networks for many years, however it contained a fundamental cryptographic weakness in the way devices authenticated with a router. When a device connects to a WPA2 network, it performs a 4-way handshake with the router to verify the password and establish an encryption key for the session. This handshake is transmitted over the air, meaning anyone nearby with a wireless adapter can passively capture it without the network or its users ever knowing. The handshake does not contain the password in plaintext however since the key is directly created from the password, if an attacker figures out the algorithm behind the creation of the key, it is  absolutely plausible that they bruteforce to find the password. WPA 3 fixes this problem with WPA 2 by utilising SAE which is based on the Diffie-Helman key exchange, instead of creating a key from the Wifi password. If a hacker were to try to brute force their way into finding the password such as with WPA 2, it would theoretically be near impossible as not only would they need to be listening in and brute forcing during a real time handshake but also each handshake is unique.


### References
https://www.techtarget.com/searchsecurity/definition/Diffie-Hellman-key-exchange

https://www.malwarebytes.com/cybersecurity/basics/what-is-wpa3

