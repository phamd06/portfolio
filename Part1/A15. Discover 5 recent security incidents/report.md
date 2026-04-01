## Jaguar Land Rover 2025
On August 31, 2025, Jaguar Land Rover detected a network intrusion serious enough to warrant an immediate shutdown of their global IT infrastructure. Production lines across plants in the UK, Slovakia, Brazil, and India were halted entirely, with staff sent home. The attack was claimed by Scattered Lapsus$ Hunters, an alliance of Scattered Spider, Lapsus$, and ShinyHunters, who published screenshots of JLR's internal systems on Telegram as proof of access.

This attack highlights several critical cybersecurity failures:
1. Social Engineering and Credential Theft — The attack originated from a vishing campaign where attackers impersonated internal IT personnel to extract employee credentials. This highlights the danger of targeting the human layer of security and the need for strict verification procedures for credential resets.
2. Lateral Movement and Privilege Escalation — Once inside, attackers exploited vulnerabilities in JLR's SAP NetWeaver system to escalate privileges and move across the network, concealing traffic through TOR. This demonstrates the importance of network segmentation and minimal privilege policies.
3. Third-Party Risk — JLR had outsourced IT services to Tata Consultancy Services, the same provider used by Marks & Spencer and Co-op, both targeted by the same group. Concentrating outsourced IT services across multiple high-profile targets created a shared vulnerability.


## Marks and Spencer 2025
In April 2025, Marks & Spencer was struck by a ransomware attack attributed to Scattered Spider. The breach began as early as February 2025 and went undetected for months before ransomware was deployed on April 24. The attack forced M&S to suspend all online orders, disable contactless payments, and revert warehouse operations to manual processes, wiping over £500 million from its stock market value.

This attack highlights several critical cybersecurity failures:
1. Social Engineering Against Third-Party IT — Attackers impersonated M&S employees and called the IT helpdesk operated by Tata Consultancy Services, convincing agents to reset passwords. With valid credentials, they accessed M&S's Active Directory and extracted password hashes for every domain user. This illustrates why helpdesks must implement strict verification protocols before performing any credential reset.
2. Prolonged Undetected Access — Attackers maintained access for approximately two months before deploying ransomware, conducting reconnaissance and exfiltrating customer data the entire time. This points to inadequate real-time monitoring and insufficient anomaly detection for outbound data transfers.
3. Double Extortion Ransomware — The attackers deployed DragonForce ransomware while simultaneously exfiltrating customer data, threatening to publish it unless a ransom was paid. Double extortion means organisations cannot fully recover by restoring backups alone — the threat of data exposure remains regardless.


## Powerschool Data Breach 2024
In December 2024, PowerSchool — a student information system provider supporting over 60 million students across 90 countries — was breached by a 19-year-old college student, Matthew Lane. Using a single compromised employee credential, Lane accessed PowerSchool's customer support portal and exfiltrated sensitive data from millions of student and teacher records. PowerSchool was unaware of the breach until Lane sent an extortion demand of $2.85 million in Bitcoin. The ransom was paid, yet Lane later re-extorted individual school districts in May 2025 using the same stolen data.

This attack highlights several critical cybersecurity failures:
1. Absence of Multi-Factor Authentication — The portal providing access to thousands of schools globally did not support MFA at the time of the breach. A single compromised credential was all that was required, a fundamental security failure at this scale.
2. Prolonged Undetected Access — Forensic investigation revealed Lane had first accessed PowerSchool's network in August 2024, over four months before detection. The same credentials were used across both access attempts with no alerts triggered, pointing to a serious failure in access monitoring.
3. The Danger of Paying Ransoms — PowerSchool's decision to pay was widely criticised as setting a dangerous precedent. The subsequent re-extortion proved payment provides no security guarantee and may incentivise further attacks. Children's personal data is particularly valuable as it can be used for identity fraud for years before being detected.


## References
https://www.securityweek.com/cyberattack-on-jlr-prompts-1-5-billion-uk-government-intervention/
https://en.wikipedia.org/wiki/Jaguar_Land_Rover_cyberattack
https://www.blackfog.com/marks-and-spencer-ransomware-attack/
https://thehackernews.com/2025/07/four-arrested-in-440m-cyber-attack-on.html
