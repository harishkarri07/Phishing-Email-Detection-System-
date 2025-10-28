#!/usr/bin/env python3
"""
Command Line Interface for Phishing Email Detection System
A simple CLI version for immediate testing.
"""

import re
import sys

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
    """Main function for command line interface"""
    print("Phishing Email Detection System - Command Line Interface")
    print("=" * 60)
    print("Enter email content to analyze (or 'quit' to exit):")
    print()
    
    while True:
        try:
            # Get input from user
            email_text = input("Email: ").strip()
            
            # Check for quit command
            if email_text.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            # Skip empty input
            if not email_text:
                continue
            
            # Analyze the email
            result = phishing_detector(email_text)
            
            # Display result with color coding
            if result == "PHISHING DETECTED":
                print(f"Result: {result} (SUSPICIOUS)")
            else:
                print(f"Result: {result} (SAFE)")
            
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
