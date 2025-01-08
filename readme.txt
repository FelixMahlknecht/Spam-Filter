# Spam Filter Project

This project involves creating a machine learning-based spam filter for email classification. The goal is to distinguish between "spam" and "ham" (non-spam) emails with high accuracy.

## Project Overview
- **Dataset**: The project uses email datasets categorized into "spam" and "ham". Additional "hard ham" emails are used for testing robustness.
- **Algorithm**: Multinomial Naive Bayes is utilized for text classification due to its effectiveness and simplicity.
- **Feature Extraction**: Emails are vectorized using TF-IDF, converting text into numerical feature vectors.

## Project Files
1. **convert_to_txt.py**: Converts files in a directory to `.txt` format.
2. **get_data.py**: Handles reading email data, assigning labels, and saving datasets as CSV files.
3. **spam-filter.py**: Prepares the dataset, trains the Naive Bayes model, and evaluates its performance.
4. **test_trained_model.py**: Tests the trained model on new datasets, displaying spam and ham classification percentages.
5. **vectorizer.pkl**: Saved TF-IDF vectorizer.
6. **naive_bayesModel.pkl**: Saved trained Naive Bayes model.

## Requirements
- Python 3.12 or later
- Dependencies:
  - pandas >= 2.2.3
  - numpy < 2
  - scikit-learn >= 1.6.0
  - joblib

Install dependencies using:
```bash
pip install -r requirements.txt
