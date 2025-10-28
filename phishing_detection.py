#!/usr/bin/env python3
"""
Phishing Email Detection System
A complete machine learning solution to classify emails as phishing or legitimate.
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import warnings
warnings.filterwarnings('ignore')

# Download required NLTK data
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

class PhishingEmailDetector:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        self.model = MultinomialNB()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
    def simulate_data(self):
        """Simulate a balanced dataset of 20 emails (10 phishing, 10 legitimate)"""
        emails_data = [
            # Phishing emails (Label: 1)
            ("URGENT: Your account will be suspended! Click here to verify immediately!", 1),
            ("Congratulations! You've won $1000! Click this link to claim your prize now!", 1),
            ("Security Alert: Unusual activity detected. Verify your identity here.", 1),
            ("Your payment has failed. Update your credit card information now!", 1),
            ("Free iPhone! Limited time offer. Click here to get yours today!", 1),
            ("Your bank account needs verification. Enter your details immediately.", 1),
            ("You have 24 hours to claim your tax refund. Click here now!", 1),
            ("Suspicious login attempt. Secure your account by clicking this link.", 1),
            ("Your subscription expires today. Renew now to avoid service interruption!", 1),
            ("You've been selected for a special offer. Don't miss out - act now!", 1),
            
            # Legitimate emails (Label: 0)
            ("Thank you for your recent purchase. Your order has been confirmed.", 0),
            ("Monthly newsletter: Check out our latest products and updates.", 0),
            ("Your appointment has been scheduled for tomorrow at 2 PM.", 0),
            ("Password reset confirmation: Your password has been successfully changed.", 0),
            ("Welcome to our service! Here's how to get started with your account.", 0),
            ("Your monthly statement is ready. Please review your account activity.", 0),
            ("Meeting reminder: Team standup tomorrow at 9 AM in conference room A.", 0),
            ("Your subscription has been renewed. Thank you for being a valued customer.", 0),
            ("New feature announcement: Check out the latest updates to our platform.", 0),
            ("Your order has been shipped. Track your package using the provided link.", 0)
        ]
        
        return emails_data
    
    def preprocess_text(self, text):
        """
        Clean and preprocess email text:
        1. Convert to lowercase
        2. Remove special characters and numbers
        3. Tokenize
        4. Remove stop words
        5. Lemmatize
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and numbers, keep only letters and spaces
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Tokenize
        words = text.split()
        
        # Remove stop words and lemmatize
        processed_words = []
        for word in words:
            if word not in self.stop_words and len(word) > 2:
                lemmatized_word = self.lemmatizer.lemmatize(word)
                processed_words.append(lemmatized_word)
        
        return ' '.join(processed_words)
    
    def prepare_data(self):
        """Load and prepare the dataset"""
        print("Loading and preparing email dataset...")
        
        # Simulate data
        emails_data = self.simulate_data()
        
        # Create DataFrame
        df = pd.DataFrame(emails_data, columns=['Email', 'Label'])
        
        print(f"Dataset created with {len(df)} emails")
        print(f"Phishing emails: {sum(df['Label'])}")
        print(f"Legitimate emails: {len(df) - sum(df['Label'])}")
        
        # Preprocess emails
        print("\nPreprocessing email text...")
        df['Processed_Email'] = df['Email'].apply(self.preprocess_text)
        
        return df
    
    def train_model(self, df):
        """Train the machine learning model"""
        print("\nTraining the machine learning model...")
        
        # Prepare features and labels
        X = df['Processed_Email']
        y = df['Label']
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Vectorize the text data
        X_train_tfidf = self.vectorizer.fit_transform(X_train)
        X_test_tfidf = self.vectorizer.transform(X_test)
        
        # Train the model
        self.model.fit(X_train_tfidf, y_train)
        
        # Make predictions
        y_pred = self.model.predict(X_test_tfidf)
        
        return X_test, y_test, y_pred
    
    def evaluate_model(self, y_test, y_pred):
        """Evaluate the model performance"""
        print("\nModel Evaluation Results:")
        print("=" * 50)
        
        # Accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy Score: {accuracy:.4f}")
        
        # Classification Report
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, 
                                  target_names=['Legitimate', 'Phishing']))
        
        # Confusion Matrix
        print("Confusion Matrix:")
        cm = confusion_matrix(y_test, y_pred)
        print(f"                 Predicted")
        print(f"                 Legitimate  Phishing")
        print(f"Actual Legitimate    {cm[0,0]:2d}        {cm[0,1]:2d}")
        print(f"Actual Phishing      {cm[1,0]:2d}        {cm[1,1]:2d}")
    
    def predict_email(self, email_text):
        """
        Predict if an email is phishing or legitimate
        """
        # Preprocess the email
        processed_text = self.preprocess_text(email_text)
        
        # Vectorize using the trained vectorizer
        email_vector = self.vectorizer.transform([processed_text])
        
        # Make prediction
        prediction = self.model.predict(email_vector)[0]
        probability = self.model.predict_proba(email_vector)[0]
        
        # Convert prediction to readable format
        result = "Phishing" if prediction == 1 else "Legitimate"
        confidence = max(probability) * 100
        
        return result, confidence, processed_text
    
    def demonstrate_predictions(self):
        """Demonstrate the prediction function with example emails"""
        print("\nTesting the prediction function:")
        print("=" * 50)
        
        # Test phishing email
        phishing_email = "URGENT! Your account will be closed in 24 hours. Click here to verify your identity immediately to avoid account suspension!"
        result, confidence, processed = self.predict_email(phishing_email)
        print(f"\nTest Email 1 (Phishing):")
        print(f"Original: {phishing_email}")
        print(f"Processed: {processed}")
        print(f"Prediction: {result} (Confidence: {confidence:.2f}%)")
        
        # Test legitimate email
        legitimate_email = "Thank you for your recent purchase. Your order #12345 has been shipped and will arrive within 3-5 business days. You can track your package using the tracking number provided."
        result, confidence, processed = self.predict_email(legitimate_email)
        print(f"\nTest Email 2 (Legitimate):")
        print(f"Original: {legitimate_email}")
        print(f"Processed: {processed}")
        print(f"Prediction: {result} (Confidence: {confidence:.2f}%)")

def main():
    """Main function to run the phishing email detection system"""
    print("Phishing Email Detection System")
    print("=" * 50)
    
    # Initialize the detector
    detector = PhishingEmailDetector()
    
    # Prepare data
    df = detector.prepare_data()
    
    # Train model
    X_test, y_test, y_pred = detector.train_model(df)
    
    # Evaluate model
    detector.evaluate_model(y_test, y_pred)
    
    # Demonstrate predictions
    detector.demonstrate_predictions()
    
    print("\nPhishing Email Detection System is ready!")
    print("\nYou can now use detector.predict_email('your email text') to classify new emails.")

if __name__ == "__main__":
    main()
