#!/usr/bin/env python3
"""
Simple Web Interface for Phishing Email Detection System
A lightweight web application using Flask for email classification.
"""

from flask import Flask, render_template_string, request, jsonify
import re

app = Flask(__name__)

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

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phishing Email Detection System</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .description {
            background: #e8f4f8;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            border-left: 4px solid #3498db;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #34495e;
        }
        textarea {
            width: 100%;
            height: 200px;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
            resize: vertical;
        }
        textarea:focus {
            outline: none;
            border-color: #3498db;
        }
        button {
            background: #3498db;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        button:hover {
            background: #2980b9;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
            font-weight: bold;
            text-align: center;
        }
        .phishing {
            background: #ffebee;
            color: #c62828;
            border: 2px solid #f44336;
        }
        .legitimate {
            background: #e8f5e8;
            color: #2e7d32;
            border: 2px solid #4caf50;
        }
        .examples {
            margin-top: 20px;
        }
        .example {
            background: #f8f9fa;
            padding: 10px;
            margin: 5px 0;
            border-radius: 3px;
            cursor: pointer;
            border: 1px solid #dee2e6;
        }
        .example:hover {
            background: #e9ecef;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ Phishing Email Detection System</h1>
        
        <div class="description">
            <strong>Analyze emails for potential phishing attempts</strong><br>
            This system uses machine learning to detect phishing emails. Simply paste the email content 
            in the text box below and click "Analyze Email" to get the analysis result.
        </div>
        
        <form method="POST">
            <div class="form-group">
                <label for="email_text">Paste Email Content Here:</label>
                <textarea id="email_text" name="email_text" placeholder="Enter the email content you want to analyze...">{{ email_text or '' }}</textarea>
            </div>
            <button type="submit">Analyze Email</button>
        </form>
        
        {% if result %}
        <div class="result {{ 'phishing' if result == 'PHISHING DETECTED' else 'legitimate' }}">
            {{ result }}
        </div>
        {% endif %}
        
        <div class="examples">
            <h3>Try these examples:</h3>
            <div class="example" onclick="document.getElementById('email_text').value='URGENT: Your account will be suspended! Click here to verify immediately!'">
                URGENT: Your account will be suspended! Click here to verify immediately!
            </div>
            <div class="example" onclick="document.getElementById('email_text').value='Thank you for your recent purchase. Your order has been confirmed.'">
                Thank you for your recent purchase. Your order has been confirmed.
            </div>
            <div class="example" onclick="document.getElementById('email_text').value='Congratulations! You\\'ve won $1000! Click this link to claim your prize now!'">
                Congratulations! You've won $1000! Click this link to claim your prize now!
            </div>
            <div class="example" onclick="document.getElementById('email_text').value='Your monthly statement is ready. Please review your account activity.'">
                Your monthly statement is ready. Please review your account activity.
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    email_text = ""
    
    if request.method == 'POST':
        email_text = request.form.get('email_text', '')
        if email_text:
            result = phishing_detector(email_text)
    
    return render_template_string(HTML_TEMPLATE, result=result, email_text=email_text)

@app.route('/api/detect', methods=['POST'])
def api_detect():
    """API endpoint for programmatic access"""
    data = request.get_json()
    email_text = data.get('email_text', '')
    result = phishing_detector(email_text)
    return jsonify({'result': result})

def main():
    """Main function to run the Flask application"""
    print("Starting Phishing Email Detection Web Interface...")
    print("=" * 60)
    print("The web interface will be available at: http://127.0.0.1:5000")
    print("Open your web browser and navigate to the URL above")
    print("=" * 60)
    
    # Run the Flask app
    app.run(debug=True, host='127.0.0.1', port=5000)

if __name__ == "__main__":
    main()
