## Video Game Saves
Video Game save files are susceptible to being tampered with if not for the usage of cryptography. Most old video game save files can be edited using a hex editor, essentially allowing every player to cheat in the game via
changing variables such as money, level and other essential game functions. Typially in modern era games, save files are first encrypted with AES and then signed with HMAC-SHA256. AES is a type of symmetric encryption algorithm that utilises same private key for encryption and decryption, and in this context prevents users from directly altering game data without first decryption. HMAC-SHA256 is the method of signing the file using SHA-256 which will tell the game whether or not the save data has been altered with, as altering the file will result in a differnet signature being created. This is a strong real world example of crytpographic implementation used offline because it showcases how even offline game data saves need security from being altered. Representing confidentiality and integrity of the CIA triad.



### References
https://videlais.com/2021/02/28/encrypting-game-data-with-unity/
