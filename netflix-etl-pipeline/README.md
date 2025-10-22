# 🧩 Netflix ETL Pipeline
  
Créer un mini pipeline **ETL** pour nettoyer et structurer le dataset public *Netflix Titles* (Kaggle).  
Ce projet démontre un flux de traitement de données clair et modulaire, inspiré des pratiques de Data Engineering réelles.

---


1. **Extract** – lecture du fichier CSV .  
2. **Transform** – nettoyage, typage, suppression des doublons, parsing de colonnes complexes.  
3. **Load** – sauvegarde du dataset propre dans un nouveau fichier CSV.


# execution

1. installe les dépendances :
```bash
pip install -r requirements.txt

Lancer le pipeline : python main.py

le fichier nettoyé est généré ici : output/cleaned_netflix.csv
