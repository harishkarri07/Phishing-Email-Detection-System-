# Phishing Email Detection System

A complete machine learning solution to classify emails as either 'Phishing' or 'Legitimate' using Python and scikit-learn.

## Features

- **Data Simulation**: Generates a balanced dataset of 20 emails (10 phishing, 10 legitimate)
- **Text Preprocessing**: Comprehensive text cleaning including tokenization, stopword removal, and lemmatization
- **Feature Extraction**: TF-IDF vectorization for converting text to numerical features
- **Machine Learning**: Multinomial Naive Bayes classifier for email classification
- **Evaluation**: Complete model evaluation with accuracy, classification report, and confusion matrix
- **Prediction Function**: Easy-to-use function for classifying new emails

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- nltk

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. The script will automatically download required NLTK data on first run.

## Usage

### Basic Usage

Run the main script to see the complete system in action:

```bash
python phishing_detection.py
```

### Custom Usage

```python
from phishing_detection import PhishingEmailDetector

# Initialize the detector
detector = PhishingEmailDetector()

# Prepare and train the model
df = detector.prepare_data()
X_test, y_test, y_pred = detector.train_model(df)

# Evaluate the model
detector.evaluate_model(y_test, y_pred)

# Predict a new email
result, confidence, processed = detector.predict_email("Your email text here")
print(f"Prediction: {result} (Confidence: {confidence:.2f}%)")
```

### Example Usage

Run the example script to see more test cases:

```bash
python example_usage.py
```

## How It Works

1. **Data Simulation**: Creates a balanced dataset with realistic phishing and legitimate email examples
2. **Text Preprocessing**:
   - Converts text to lowercase
   - Removes special characters and numbers
   - Tokenizes the text
   - Removes stop words
   - Lemmatizes words to their base form
3. **Feature Extraction**: Uses TF-IDF vectorization to convert processed text into numerical features
4. **Model Training**: Trains a Multinomial Naive Bayes classifier on the processed data
5. **Evaluation**: Provides comprehensive metrics including accuracy, precision, recall, and F1-score
6. **Prediction**: Classifies new emails with confidence scores

## Model Performance

The system typically achieves:
- **Accuracy**: ~75% on the test set
- **Precision**: High precision for legitimate emails
- **Recall**: Good recall for phishing detection

*Note: Performance may vary due to the small dataset size. For production use, train on a larger, more diverse dataset.*

## File Structure

- `phishing_detection.py`: Main implementation with the PhishingEmailDetector class
- `example_usage.py`: Example script showing how to use the system
- `requirements.txt`: Required Python packages
- `README.md`: This documentation file

## Key Components

### PhishingEmailDetector Class

- `simulate_data()`: Creates the training dataset
- `preprocess_text()`: Cleans and preprocesses email text
- `prepare_data()`: Loads and prepares the dataset
- `train_model()`: Trains the machine learning model
- `evaluate_model()`: Evaluates model performance
- `predict_email()`: Predicts if an email is phishing or legitimate

## Example Output

```
Phishing Email Detection System
==================================================
Loading and preparing email dataset...
Dataset created with 20 emails
Phishing emails: 10
Legitimate emails: 10

Preprocessing email text...

Training the machine learning model...

Model Evaluation Results:
==================================================
Accuracy Score: 0.7500

Classification Report:
              precision    recall  f1-score   support

  Legitimate       0.67      1.00      0.80         2
    Phishing       1.00      0.50      0.67         2

    accuracy                           0.75         4
   macro avg       0.83      0.75      0.73         4
weighted avg       0.83      0.75      0.73         4

Confusion Matrix:
                 Predicted
                 Legitimate  Phishing
Actual Legitimate     2         0
Actual Phishing       1         1
```

## Extending the System

To improve the system:

1. **Larger Dataset**: Use a real, larger dataset of emails
2. **Feature Engineering**: Add more features like email headers, sender information, etc.
3. **Advanced Models**: Try other algorithms like Random Forest, SVM, or Neural Networks
4. **Cross-Validation**: Implement k-fold cross-validation for better evaluation
5. **Hyperparameter Tuning**: Optimize model parameters

## License

This project is open source and available under the MIT License.
