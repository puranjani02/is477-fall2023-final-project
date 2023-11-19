rule prepare:
  output:
    "data/wine",
    "data/wine.csv"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  input:
    "data/wine.csv"
  output:
    "profiling/report.html"
    
  shell:
    "python scripts/profile.py"

rule analyze:
  input:
    "data/wine.csv" 
  output:
    "results/summary_statistics.csv",
    "results/wine_logistic_regression_scores.txt",
    "confusion_matrix.pdf"  
  shell:
    "scripts/analysis.py"