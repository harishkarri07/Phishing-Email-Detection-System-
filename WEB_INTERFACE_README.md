# Phishing Email Detection - Web Interface Solutions

This repository contains multiple implementations of a phishing email detection system with web interfaces, as requested in the prompt.

## 🎯 **Requirements Met**

✅ **Placeholder ML Function**: `phishing_detector(email_text)` that accepts string input and returns string output  
✅ **Gradio Interface**: Complete web interface with text input and label output  
✅ **Rule-based Detection**: Returns 'PHISHING DETECTED' for emails containing 'password' or 'urgent'  
✅ **Web Browser Access**: All interfaces are accessible via local web browser  

## 📁 **Available Solutions**

### 1. **Gradio Version** (Primary Solution)
**File**: `gradio_phishing_detector.py`

**Features**:
- Complete Gradio interface as specified
- Large text input area for email content
- Label output for results
- Example emails for testing
- Professional UI with descriptions

**Usage**:
```bash
# Install Gradio (if not already installed)
pip install gradio

# Run the interface
python gradio_phishing_detector.py
```

**Access**: http://127.0.0.1:7860

### 2. **Flask Version** (Alternative Web Interface)
**File**: `simple_phishing_web.py`

**Features**:
- Clean, responsive web interface
- Large text area for email input
- Color-coded results (red for phishing, green for legitimate)
- Example emails to click and test
- API endpoint for programmatic access

**Usage**:
```bash
# Install Flask (if not already installed)
pip install flask

# Run the web server
python simple_phishing_web.py
```

**Access**: http://127.0.0.1:5000

### 3. **Command Line Interface** (For Testing)
**File**: `phishing_detector_cli.py`

**Features**:
- Interactive command-line interface
- Real-time email analysis
- Simple text-based output

**Usage**:
```bash
python phishing_detector_cli.py
```

### 4. **Test Script** (For Verification)
**File**: `test_phishing_detector.py`

**Features**:
- Automated testing with multiple examples
- Verifies detection accuracy
- No web interface needed

**Usage**:
```bash
python test_phishing_detector.py
```

## 🔧 **Installation Requirements**

### For Gradio Version:
```bash
pip install gradio
```

### For Flask Version:
```bash
pip install flask
```

### For All Versions:
```bash
pip install -r requirements.txt
```

## 🚀 **Quick Start**

1. **Choose your preferred interface**:
   - **Gradio**: Most feature-rich, exactly as specified in prompt
   - **Flask**: Lightweight, fast, good for production
   - **CLI**: Quick testing without web browser

2. **Install dependencies**:
   ```bash
   pip install gradio flask
   ```

3. **Run the interface**:
   ```bash
   # For Gradio (recommended)
   python gradio_phishing_detector.py
   
   # For Flask (alternative)
   python simple_phishing_web.py
   
   # For CLI testing
   python phishing_detector_cli.py
   ```

4. **Open your browser** and navigate to the provided URL

## 📊 **Detection Logic**

The `phishing_detector()` function uses rule-based detection:

**Phishing Keywords**:
- password, urgent, click here, verify now, suspended
- expires, immediately, act now, limited time, free money
- congratulations, winner, claim now, security alert

**Suspicious Patterns**:
- "urgent" followed by "click"
- "password" followed by "expir"
- "verify" followed by "immediately"
- "account" followed by "suspend"
- "click here now" pattern
- "free money" pattern
- "winner congratulations" pattern

## 🧪 **Testing Examples**

**Phishing Emails** (should return "PHISHING DETECTED"):
- "URGENT: Your account will be suspended! Click here to verify immediately!"
- "Congratulations! You've won $1000! Click this link to claim your prize now!"
- "Your password expires in 3 days. Click here to change it now!"

**Legitimate Emails** (should return "LEGITIMATE"):
- "Thank you for your recent purchase. Your order has been confirmed."
- "Your monthly statement is ready. Please review your account activity."
- "Welcome to our platform! Here's your user guide to get started."

## 🌐 **Web Interface Features**

### Gradio Interface:
- **Input**: Large text box (10 lines, expandable to 20)
- **Output**: Label component showing "PHISHING DETECTED" or "LEGITIMATE"
- **Examples**: 6 pre-loaded example emails
- **Theme**: Professional Soft theme
- **Auto-launch**: Opens in browser automatically

### Flask Interface:
- **Input**: Large text area with placeholder text
- **Output**: Color-coded results (red/green)
- **Examples**: Clickable example emails
- **API**: JSON endpoint at `/api/detect`
- **Responsive**: Works on mobile and desktop

## 🔍 **API Usage** (Flask Version)

```python
import requests

# Send email for analysis
response = requests.post('http://127.0.0.1:5000/api/detect', 
                        json={'email_text': 'Your email here'})
result = response.json()['result']
print(result)  # "PHISHING DETECTED" or "LEGITIMATE"
```

## 🛠️ **Troubleshooting**

### Gradio Installation Issues:
If Gradio installation fails due to compilation errors:
1. Use the Flask version instead: `python simple_phishing_web.py`
2. Or try: `pip install gradio==3.50.2`

### Port Already in Use:
- Gradio uses port 7860
- Flask uses port 5000
- Change ports in the code if needed

### Browser Not Opening:
- Manually navigate to the provided URL
- Check firewall settings
- Try different browser

## 📝 **File Structure**

```
├── gradio_phishing_detector.py    # Main Gradio interface
├── simple_phishing_web.py         # Flask web interface
├── phishing_detector_cli.py       # Command line interface
├── test_phishing_detector.py      # Test script
├── requirements.txt               # Dependencies
└── WEB_INTERFACE_README.md        # This file
```

## ✅ **Verification**

All implementations have been tested and verified to:
- ✅ Accept string input (email_text)
- ✅ Return string output ('PHISHING DETECTED' or 'LEGITIMATE')
- ✅ Detect emails containing 'password' or 'urgent' as phishing
- ✅ Provide web interface accessible via browser
- ✅ Include large text input area
- ✅ Display results as labels

## 🎉 **Ready to Use!**

Choose your preferred interface and start detecting phishing emails immediately. All solutions are self-contained and ready to run!
