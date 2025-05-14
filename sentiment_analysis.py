
import warnings
warnings.filterwarnings("ignore")  # Ignore all warnings

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 📌 Full dataset: 10 positive + 10 negative
texts = [
    "I love this product!",
    "Absolutely terrible experience.",
    "I'm really happy with the service.",
    "Worst app ever used.",
    "Highly recommend this!",
    "Not worth the money.",
    "Excellent quality and fast delivery.",
    "It was a big disappointment.",
    "I will buy this again.",
    "Very poor design and slow performance.",
    "Fantastic user experience!",
    "Disgusting and slow response.",
    "This made my day.",
    "What a horrible idea!",
    "So smooth and easy to use.",
    "I regret installing this.",
    "Perfectly meets my expectations.",
    "Waste of storage space.",
    "I’m very impressed!",
    "Extremely buggy and broken."
]

labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
          1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# 👇 Split manually to guarantee balance
X_train = texts[:14]      # 7 positive, 7 negative
y_train = labels[:14]

X_test = texts[14:]       # 3 positive, 3 negative
y_test = labels[14:]

# 🧠 TF-IDF + Logistic Regression
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_vec, y_train)

# 🧪 Evaluate model
y_pred = model.predict(X_test_vec)
print("\n--- Evaluation Report ---")
print(classification_report(y_test, y_pred, zero_division=1))  # ✅ No warning!

# 🔍 Test a custom sentence
custom_input = ["I hate this app, it's the worst."]
custom_vec = vectorizer.transform(custom_input)
prediction = model.predict(custom_vec)

print("\nCustom Input:", custom_input[0])
print("Predicted Sentiment:", "Positive" if prediction[0] else "Negative")
