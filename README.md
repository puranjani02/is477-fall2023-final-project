# IS477-FALL2023-FINAL-PROJECT - Exploration of the Wine Dataset from UCI repository

## Overview 
This repository is created for the Final Assignment for the course IS477. Here we take the [wine dataset](https://archive.ics.uci.edu/dataset/109/wine) which is found on the UCI Machine Learning Repository under the [CC-BY-4.0 license](https://creativecommons.org/licenses/by/4.0/legalcode). The dataset has been created by Stefan Aeberhard and M. Forina. The dataset contains the results of a chemical analysis of wines grown in a region in Italy, derived from three different cultivars. The dataset consists of 13 constituents found in each of the three types of wines as attributes. There are 178 instances in the dataset. This dataset was first used in the paper [Aeberhard, S., Coomans, D., & Vel, O.Y. (1994). Comparative analysis of statistical pattern recognition methods in high dimensional settings. Pattern Recognit., 27, 1065-1077.](https://www.semanticscholar.org/paper/Comparative-analysis-of-statistical-pattern-methods-Aeberhard-Coomans/83dc3e4030d7b9fbdbb4bde03ce12ab70ca10528). In this project, a Logistic Regression classification model is run on the dataset, with the 'Class' variable as the target. This variable stores the type of wine and there are 3 classes of wines in this dataset. Initially a preliminary exploratory data analysis is run on the dataset. The performance of the model is judged using Accuracy Score (94.4%) and F1-Score (0.945). The confusion matrix resulting from the classification task is visualized using a heatmap. The results of the exploratory data analysis, performance of the classification model and the visualization of the confusion matrix is stored in the _Results_ folder in this repository.     

## Analysis
A classification task was performed on the dataset for prediction of classes of wine (target variable). On performing a Logistic Regression classification on the dataset, it gave an accuracy of 94.4% and a 0.945 F1-score. According to the confusion matrix, the model calculated 17, 21, 13 true positives for classes 1, 2, and 3 of wine respectively. 

## Workflow 
The Workflow of the repository was built using SnakeMake. 

![Workflow]((https://edotor.net/?engine=dot#digraph%20G%20%7B%0Arankdir%3DTB%0Afontname%3DCourier%3B%20fontsize%3D18%3B%20labelloc%3Dt%0A%0Anode%20%5Bshape%3Dbox%20style%3D%22filled%2C%20rounded%22%2C%20fillcolor%20%3D%20%22%23FFFFD1%22%5D%0A%22data%2Fwine%22%0A%22data%2Fwine.csv%22%0A%22data%2Fwine.csv%22%0A%22profiling%2Freport.html%22%0A%22data%2Fwine.csv%22%0A%22results%2Fsummary_statistics.csv%22%0A%22results%2Fwine_logistic_regression_scores.txt%22%0A%22confusion_matrix.pdf%22%0A%0Anode%20%5Bshape%3Dbox3d%20style%3D%22filled%2C%20rounded%22%2C%20fillcolor%20%3D%20%22%23D6FDD0%22%5D%0A%22prepare%22%0A%22analyze%22%0A%0Aedge%20%5Bcolor%20%3D%20black%5D%0A%22data%2Fwine.csv%22%20-%3E%20%22profile%22%0A%22data%2Fwine.csv%22%20-%3E%20%22analyze%22%0A%22prepare%22%20-%3E%20%22data%2Fwine%22%0A%22prepare%22%20-%3E%20%22data%2Fwine.csv%22%0A%22profile%22%20-%3E%20%22profiling%2Freport.html%22%0A%22analyze%22%20-%3E%20%22results%2Fsummary_statistics.csv%22%0A%22analyze%22%20-%3E%20%22results%2Fwine_logistic_regression_scores.txt%22%0A%22analyze%22%20-%3E%20%22confusion_matrix.pdf%22%0A%0A%7D%0A))

## Reproducing

## License

## References
1. Aeberhard,Stefan and Forina,M.. (1991). Wine. UCI Machine Learning Repository. [https://doi.org/10.24432/C5PC7J](https://doi.org/10.24432/C5PC7J).
2. 





