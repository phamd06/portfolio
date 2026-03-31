## Website observed
https://pba.yepbooking.com.au/new-account.php


## Vulnerability identified
Weak Password Policy / Insufficient Password Strength Enforcement


## What I observed
During account creation, the website accepted a weak password that did not appear to meet strong password security standards. The password inputted was 12345678. Not only that but there is no email verification process to ensure that the email used is a correct one.


## Why this is a vulnerability
Allowing weak passwords increases the likelihood of unauthorised access because simple passwords are easier to guess, reuse, or crack. Non-verification of emails leads to high bounce rates, and a security risk because malicious actors may use fake emails to overflow the website's servers with fake unusable emails. 


## Potential impact
If attackers are able to guess or obtain weak passwords, they may gain unauthorised access to user accounts and any associated personal or account information. Website servers may be cluttered with unusable and unwanted emails due to no verification.

## Evidence 
[Weak registration requirements](Vulnerable_Wesbite.png)
