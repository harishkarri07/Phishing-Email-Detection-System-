#!/usr/bin/env python3
"""
Example usage of the Phishing Email Detection System
"""

from phishing_detection import PhishingEmailDetector

def main():
    # Initialize the detector
    detector = PhishingEmailDetector()
    
    # Prepare and train the model
    df = detector.prepare_data()
    X_test, y_test, y_pred = detector.train_model(df)
    
    # Evaluate the model
    detector.evaluate_model(y_test, y_pred)
    
    print("\n" + "="*60)
    print("CUSTOM EMAIL TESTING")
    print("="*60)
    
    # Test with custom emails
    test_emails = [
        "URGENT: Your bank account has been compromised! Click here immediately to secure it!",
        "Your package delivery failed. Please update your address information now!",
        "Thank you for subscribing to our newsletter. Here are this week's updates.",
        "You've won a free vacation! Click here to claim your prize before it expires!",
        "Meeting reminder: Project review tomorrow at 10 AM in the conference room.",
        "Your password expires in 3 days. Click here to change it now or lose access!",
        "Welcome to our platform! Here's your user guide to get started.",
        "Suspicious activity detected on your account. Verify your identity here!",
        "Your monthly invoice is ready. Please review and pay by the due date.",
        "Congratulations! You've been selected for our exclusive membership program!"
    ]
    
    for i, email in enumerate(test_emails, 1):
        result, confidence, processed = detector.predict_email(email)
        print(f"\nEmail {i}:")
        print(f"Text: {email}")
        print(f"Prediction: {result} (Confidence: {confidence:.2f}%)")
        print(f"Processed: {processed}")

if __name__ == "__main__":
    main()
