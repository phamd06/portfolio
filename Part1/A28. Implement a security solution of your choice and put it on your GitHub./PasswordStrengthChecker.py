def PasswordStrengthCheck(password):
    common_passwords = ["123456", "password", "qwerty", "abc123"]
    if password.lower() in common_passwords:
        return "Weak"
    score = 0
    special_chars = set('!@#$%^&*(),.?":{}|<>_-[]/\\+=~`\';')
 
    has_upper   = any(c.isupper() for c in password)
    has_lower   = any(c.islower() for c in password)
    has_digit   = any(c.isdigit() for c in password)
    has_special = any(c in special_chars for c in password)

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
 
    if has_upper:   score += 1
    if has_lower:   score += 1
    if has_digit:   score += 1
    if has_special: score += 2
    
    if has_upper and has_lower and has_digit and has_special:
        score += 1
 
    if score >= 6:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"
    
def main():
    print("Password Strength Checker")
    print("Type 'quit' to exit.\n")
    while True:
        password = input("Enter a password: ")
 
        if password.lower() == 'quit':
            print("Goodbye!")
            break
 
        if not password:
            print("Please enter a password.\n")
            continue
 
        result = PasswordStrengthCheck(password)
 
        icons = {"Strong": "✅", "Medium": "⚠️", "Weak": "❌"}
        print(f"Strength: {icons[result]} {result}\n")
    
if __name__ == "__main__":
    main()