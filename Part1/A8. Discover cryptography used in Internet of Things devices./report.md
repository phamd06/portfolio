## Fitness Watches
Fitness trackers or to be specific watches communicate with mobile phones through Bluetooth Low Energy (BLE), a variant of Bluetooth constructred for minimal energy usage. This variant of bluetooth has several methods for
pairing tracker to mobile phone, these include from weakest to strongest Just Works, Passkey Entry, Numeric Comparison and Out of Bound (OOB). The least secure pairing method and yet the most popular is Just Works, which requires no user verification and is vulnerable to man-in-the-middle attacks, where an attacker intercepts the pairing process and positions themselves between the tracker and the phone without either party knowing. This leads to an attacker nearby during the pairing process could potentially intercept and decrypt communication between the device and the smartphone, leading to multiple privacy breaches and injecting fake data into the sync, access GPS location history and reading step counts which could reveal what times you are away from home.

### References
https://technotes.kynetics.com/2018/BLE_Pairing_and_bonding/

https://academy.nordicsemi.com/courses/bluetooth-low-energy-fundamentals/lessons/lesson-5-bluetooth-le-security-fundamentals/topic/pairing-process/
