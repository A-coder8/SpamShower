from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read csv file
file = pd.read_csv(
    "SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)
file.fillna(None)
# set x and y
X = file["message"]
Y = file["label"]

# train and test split
train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size=0.25, random_state=42)

# set a correct data
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_x)
X_test = vectorizer.transform(test_x)

# create model
model_tree = DecisionTreeClassifier()
model_tree.fit(X_train, train_y)
yhat = model_tree.predict(X_test)

print("accuracy_score:", accuracy_score(test_y, yhat))

cm = confusion_matrix(
    test_y,
    yhat,
    labels=["ham", "spam"]
)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["ham", "spam"]
)

display.plot()
plt.show()

text = input("Enter Text:")
new_x_text = vectorizer.transform([text])
prediction_new = model_tree.predict(new_x_text)

print("model Answer:", prediction_new)
