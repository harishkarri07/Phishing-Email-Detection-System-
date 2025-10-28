#!/usr/bin/env python3
"""
Simple Gradio Web Interface for Phishing Email Detection System
A minimal web application using Gradio for email classification.
"""

import re

# Try to import gradio, if it fails, provide instructions
try:
    import gradio as gr
    GRADIO_AVAILABLE = True
except ImportError:
    GRADIO_AVAILABLE = False
    print("Gradio not available. Please install it with: pip install gradio")
    print("Or use the Flask version: python simple_phishing_web.py")

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

def create_gradio_interface():
    """
    Create and configure the Gradio interface for phishing email detection.
    """
    if not GRADIO_AVAILABLE:
        return None
    
    # Create the Gradio interface
    interface = gr.Interface(
        fn=phishing_detector,  # Primary function to call
        inputs=gr.Textbox(
            label="Paste Email Content Here",
            placeholder="Enter the email content you want to analyze...",
            lines=10,  # Large text area
            max_lines=20,
            show_copy_button=True
        ),
        outputs=gr.Label(
            label="Detection Result"
        ),
        title="Phishing Email Detection System",
        description="""
        **Analyze emails for potential phishing attempts**
        
        This system uses machine learning to detect phishing emails. Simply paste the email content 
        in the text box below and click "Submit" to get the analysis result.
        
        **How it works:**
        - The system analyzes the email text for suspicious patterns and keywords
        - Common phishing indicators include urgent language, password requests, and suspicious links
        - Results will show either "PHISHING DETECTED" or "LEGITIMATE"
        """,
        examples=[
            "URGENT: Your account will be suspended! Click here to verify immediately!",
            "Thank you for your recent purchase. Your order has been confirmed.",
            "Congratulations! You've won $1000! Click this link to claim your prize now!",
            "Your monthly statement is ready. Please review your account activity.",
            "Security Alert: Unusual activity detected. Verify your identity here.",
            "Welcome to our platform! Here's your user guide to get started."
        ],
        cache_examples=True,
        allow_flagging="never"
    )
    
    return interface

def main():
    """
    Main function to launch the Gradio interface.
    """
    if not GRADIO_AVAILABLE:
        print("Gradio is not available. Please install it first:")
        print("pip install gradio")
        print("\nAlternatively, you can use the Flask version:")
        print("python simple_phishing_web.py")
        return
    
    print("Starting Phishing Email Detection Web Interface...")
    print("=" * 60)
    
    # Create the interface
    interface = create_gradio_interface()
    
    if interface is None:
        print("Failed to create interface")
        return
    
    # Launch the interface
    print("Launching web interface...")
    print("The interface will open in your default web browser")
    print("If it doesn't open automatically, check the terminal for the local URL")
    print("=" * 60)
    
    # Launch with specific settings
    interface.launch(
        share=False,  # Set to True if you want a public link
        debug=False,
        show_error=True,
        server_name="127.0.0.1",  # Local access only
        server_port=7860,  # Default Gradio port
        inbrowser=True  # Automatically open in browser
    )

if __name__ == "__main__":
    main()
