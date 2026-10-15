# SpamShower

A beginner machine-learning project that classifies SMS messages as **spam** or **ham** (not spam).

**Language:** [فارسی🇮🇷](https://github.com/A-coder8/SpamShower/blob/main/README.fa.md)
> Educational project: predictions can be wrong, so this is not a perfect spam filter.

## Features
- Text feature extraction with `CountVectorizer` and `TfidfVectorizer`
- Experiments with Decision Tree, Logistic Regression, and Multinomial Naive Bayes
- Evaluation using accuracy and a confusion matrix
- Prediction for a custom SMS message

## Results

Results observed on the current test split:

| Feature extraction | Classifier | Accuracy |
|---|---|---:|
| CountVectorizer | Decision Tree | 97.13% |
| TF-IDF | Decision Tree | 97.49% |
| TF-IDF | Logistic Regression | 97.27% |
| TF-IDF | Multinomial Naive Bayes | 96.41% |

These results depend on the current train/test split and setup; they do not guarantee performance on other data. Consider precision, recall, and F1-score as well as accuracy.

### Confusion matrix example

One experiment produced this matrix, with labels ordered as `ham`, `spam`:

| Actual \\ Predicted | ham | spam |
|---|---:|---:|
| ham | 1196 | 11 |
| spam | 29 | 157 |

This corresponds to about **97.13% accuracy**. Some spam messages were missed, and some ordinary messages were incorrectly flagged as spam.

## Requirements
- Python
- pandas
- scikit-learn
- matplotlib


## Example

```text
Enter Text: Congratulations! You won a free prize!
Prediction: spam
```

The exact prediction depends on the trained model and preprocessing pipeline.

## Dataset
This project uses the **SMS Spam Collection** dataset. Include the dataset source and any required attribution in your documentation. Check its current terms before redistributing the data.

## Disclaimer
This project is for learning and experimentation, not a production-ready security or messaging filter.
