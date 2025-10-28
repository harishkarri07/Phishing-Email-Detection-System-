#!/usr/bin/env python3
"""
Test script for the phishing detection function
"""

import re

def phishing_detector(email_text):
    """
    Placeholder machine learning function for phishing email detection.
    
    Args:
        email_text (str): The email content to analyze
        
    Returns:
        str: 'PHISHING DETECTED' or 'LEGITIMATE'
    """
    if not email_text or not isinstance(email_text, str):
        return "LEGITIMATE"
    
    # Convert to lowercase for case-insensitive matching
    email_lower = email_text.lower()
    
    # Simple rule-based detection for simulation
    # Check for common phishing indicators
    phishing_keywords = ['password', 'urgent', 'click here', 'verify now', 'suspended', 
                        'expires', 'immediately', 'act now', 'limited time', 'free money',
                        'congratulations', 'winner', 'claim now', 'security alert']
    
    # Check if any phishing keywords are present
    for keyword in phishing_keywords:
        if keyword in email_lower:
            return "PHISHING DETECTED"
    
    # Additional checks for suspicious patterns
    suspicious_patterns = [
        r'urgent.*click',  # "urgent" followed by "click"
        r'password.*expir',  # "password" followed by "expir"
        r'verify.*immediately',  # "verify" followed by "immediately"
        r'account.*suspend',  # "account" followed by "suspend"
        r'click.*here.*now',  # "click here now" pattern
        r'free.*money',  # "free money" pattern
        r'winner.*congratulations',  # "winner congratulations" pattern
    ]
    
    for pattern in suspicious_patterns:
        if re.search(pattern, email_lower):
            return "PHISHING DETECTED"
    
    # If no suspicious indicators found, classify as legitimate
    return "LEGITIMATE"

def main():
    """Test the phishing detection function with various examples"""
    print("Testing Phishing Email Detection Function")
    print("=" * 50)
    
    test_emails = [
        "URGENT: Your account will be suspended! Click here to verify immediately!",
        "Thank you for your recent purchase. Your order has been confirmed.",
        "Congratulations! You've won $1000! Click this link to claim your prize now!",
        "Your monthly statement is ready. Please review your account activity.",
        "Security Alert: Unusual activity detected. Verify your identity here.",
        "Welcome to our platform! Here's your user guide to get started.",
        "Your password expires in 3 days. Click here to change it now!",
        "Meeting reminder: Project review tomorrow at 10 AM.",
        "Free money! Limited time offer. Act now!",
        "Your subscription has been renewed. Thank you for being a valued customer."
    ]
    
    for i, email in enumerate(test_emails, 1):
        result = phishing_detector(email)
        print(f"\nTest {i}:")
        print(f"Email: {email}")
        print(f"Result: {result}")
        print("-" * 30)

if __name__ == "__main__":
    main()
