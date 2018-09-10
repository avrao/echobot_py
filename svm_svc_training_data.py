# Supervised learning
# A classifier predicts the intent label given a sentence
# 'Fit' classifier by tuning it on training data
# Evaluate performance on test data
# Accuracy: the fraction of labels we predict correctly

# ATIS dataset
# Thousands of sentences with labeled intents and entities
# Collected from a real flight booking service
# Intents like:
# atis_flight
# atis_airfare

# Support vector machines
# Nearest neighbours is very simple - we can do better
# SVM / SVC: support vector machine / classifier

# Import SVC
from sklearn.svm import SVC

# Create a support vector classifier
clf = SVC(C=1)

# Fit the classifier using the training data
clf.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = clf.predict(X_test)

# Count the number of correct predictions
n_correct = 0
for i in range(len(y_test)):
    if y_pred[i] == y_test[i]:
        n_correct += 1

print("Predicted {0} correctly out of {1} test examples".format(n_correct, len(y_test)))
