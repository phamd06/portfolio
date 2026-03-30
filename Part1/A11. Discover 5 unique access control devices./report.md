## CAPTCHA
CAPTCHA, which stands for Completely Automated Public Turing test to tell Computers and Humans Apart, is a type of access control mechanism designed to distinguish human users from automated bots. Early CAPTCHAs presented 
users with distorted, noisy text and asked them to type what they saw. This worked because human brains are capable of recognising patterns even through significant visual noise. This approach became ineffective and was 
replaced with image-based challenges, such as asking users to select all images containing traffic lights or bicycles. These exploited the fact that image recognition was still computationally difficult for machines, 
however as machine learning models improved ironically trained in part on the very CAPTCHA data being collected this approach was also eventually defeated. Modern Captcha's instead rely on running in the background capturing
mouse movement, browsing history, typing rhythm and time spent on pages.

## Mutli Factor Authentication
Multi-Factor Authentication (MFA) is a digital access control mechanism that requires a user to verify their identity through two or more independent factors before being granted access to a system or account. The three 
categories of factors are something you know (such as a password or PIN), something you have (such as a phone or hardware key), and something you are (such as a fingerprint or face scan) which ties directly to the 
Authentication component of Access Control. The most common implementation of MFA is the Time-based One Time Password (TOTP), used by authenticator apps such as Google Authenticator and Microsoft Authenticator. When setting 
up TOTP, the server generates a secret key which is shared with the authenticator app, typically by scanning a QR code. From that point on, both the server and the app independently use that shared secret key combined with 
the current time to compute the same 6 digit code every 30 seconds. Because both sides perform the same computation using the same inputs, the codes match without ever needing to be transmitted between them. This means 
even if an attacker is intercepting network traffic, there is no code being sent over the network to steal, and any intercepted code is useless after 30 seconds.

## Iris Scanner
An iris scanner is a biometric access control device that uses the unique patterns of a person's iris, the coloured ring surrounding the pupil; to verify their identity. The iris is considered one of the most reliable 
biometric identifiers available because its complex pattern of ridges, furrows, and crypts is unique to each individual and remains stable throughout a person's lifetime, unlike fingerprints which can be worn down or altered 
over time. When a user first registers with an iris scanner, the device captures a high resolution infrared image of the iris. Infrared light is used rather than visible light because it penetrates the iris more effectively,
revealing patterns that are not visible to the naked eye and reducing interference from lighting conditions or eye colour. The captured image is then processed using mathematical transforms, commonly wavelet transforms. 
Critically, the actual image of the iris is never stored; only this mathematical representation is kept, which protects user privacy and reduces the consequences of a data breach since the template cannot be reversed back 
into a usable image of the iris.

## Fingerprint Scanner
A fingerprint scanner is a biometric access control device that verifies a person's identity by analysing the unique ridge patterns on the surface of their finger. Fingerprints are largely unique to each human on Earth,
making them a reliable source of a unique identifier. There are two main types of fingerprint scanners, optical and capacitive. Optical scanners purely capture a 2D image of the finger and analyses the patterns on the print.
Capacitive scanners on the other hand, use tiny capacitors to read the electrical charge of the ridges in the fingerprint when pressed against the sensor. Capacitive scanner is considered a more secure way of access control
since Optical scanners are susceptible to image replication. Regardless of the scanner type, the processing of the fingerprint follows a similar approach to iris scanning. The captured fingerprint is not stored as an image 
but is instead converted into a mathematical template.

## Boom gates
Boom gates is a physical access control device consisting of a horizontal bar that blocks vehicle entry to a restricted area and can be raised or lowered to grant or deny access. The most common trigger mechanism is RFID,
where authorised vehicles are issued a card or tag that communicates wirelessly with a reader mounted near the gate. When a valid tag is detected, the gate raises automatically.  More sophisticated deployments use Licence
Plate Recognition (LPR) cameras, which capture an image of an approaching vehicle's licence plate and use optical character recognition to read the plate number, comparing it against a database of authorised vehicles in 
real time. LPR removes the need for drivers to carry any physical credential at all, as the vehicle itself becomes the identifier. Some high security boom gate installations combine multiple mechanisms to implement 
multi-factor access control at the vehicle level. For example, a facility might require both a valid RFID tag and a matching licence plate before raising the barrier, ensuring that a stolen access tag cannot be used in 
an unauthorised vehicle.


### References
https://www.cloudflare.com/learning/bots/how-captchas-work/

https://www.vic.gov.au/multi-factor-authentication

https://ucr.fbi.gov/fingerprints_biometrics/biometric-center-of-excellence/files/iris-recognition.pdf

https://www.okta.com/identity-101/fingerprint-biometrics-definition-how-secure-it-is/

https://www.tonish.com.au/post/understanding-the-mechanics-behind-boom-gates
