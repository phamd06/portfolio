## Pasword Hashing
Any time you are required to enter a password for logging into a website, instead of the website directly storing your password value which would get exposed in the scenario where the database is leaked and all passwords are
revealed, the password is hashed using a specific hashing algorithm such as modern instances like bcrypt and Argon2 and that hashes password is what is actually stored. Hashing is comprised of inputting a string which is then 
converted into a fixed length string that is irreversible. SHA-256 is an old hashing algorithm that most people may assume will be used in modern hashing implementations however SHA-256 algorithms are extremely easy to bruteforce
and modern day GPU's are able to compute billions of SHA-256 hashes per second. Most importantly, most passwords that are stored are salted before they are hashed meaning an extra few random characters, creating an extra 
barrier of protection. This demonstrates a cryptographic implementation used online because passwords are an important piece of data that should never be revealed and hashing is an implementation of crytopgrahy that tries to
conceal the password.

### References
https://supertokens.com/blog/password-hashing-salting

https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
