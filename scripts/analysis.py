import pandas as pd
import os
df=pd.read_csv('data/wine.csv')

if os.path.exists('results')==0:
    os.mkdir('results')
#Summary statistics of the columns
df.describe().to_csv('results/summary_statistics.csv')

#Classification Task using Logistic Regression from scikit-learn package of Python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score

y=df['Class']
x=df.iloc[:,1:]
train_x, test_x, train_y, test_y=tts(x, y, test_size=0.3, random_state=56, stratify=y)

lr=LogisticRegression()
lr.fit(train_x, train_y)
predicted_lr=lr.predict(test_x)
prob_lr=lr.predict_proba(test_x)

#Saving the Accuracy result
accuracy=accuracy_score(test_y, predicted_lr)*100
F1=f1_score(test_y, predicted_lr, average='weighted')
try:
  f=open('results/wine_logistic_regression_scores.txt', 'r+')
except:
  f=open('results/wine_logistic_regression_scores.txt', 'a') 
print("Accuracy Score for Logistic Regression:", round(accuracy, 3) ,'%',file=f)
print("F1-Score for Logistic Regression:", round(F1, 3) ,file=f)
f.close()

#Visualization of the confusion matrix
import seaborn as sns
plt=sns.heatmap(confusion_matrix(test_y, predicted_lr), annot=True)
plt.figure.savefig('results/confusion_matrix.pdf')
