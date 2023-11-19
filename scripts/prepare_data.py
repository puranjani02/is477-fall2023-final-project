import os
import requests
import zipfile
import hashlib
import pandas

#Download link for the dataset
url_wine='https://archive.ics.uci.edu/static/public/109/wine.zip'

#Creating the data folder if it does not exist
if os.path.exists('data')==0:
    os.mkdir('data')

#Creating the wine dataset and saving it in a folder 'wine' under 'data' directory and checking its integrity
responses=requests.get(url_wine)
with open('data/wine.zip', mode='wb') as f:
    f.write(responses.content)
with zipfile.ZipFile('data/wine.zip', 'r') as zip_ref:
    zip_ref.extractall('data/wine')
filename = 'data/wine.zip'
with open(filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()
    uci_wine_sha256 = '2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab'
    if uci_wine_sha256 != sha256hash:
        print("Computed hash does not match expected hash for wine.zip dataset from UCI repository")
    else:
        print("Computed hash matches expected hash for wine.zip dataset from UCI repository")
os.remove('data/wine.zip')

#Creating a csv file with column heading
df=pandas.read_csv('data/wine/wine.data')
df.columns=['Class','Alcohol', 'Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols',
											  'Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue',
                                              'OD280/OD315 of diluted wines','Proline']
df.to_csv('data/wine.csv')