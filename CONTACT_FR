
```markdown
# EXECUTIVE SUMMARY
Loan Default / Risk Scoring — Résumé Exécutif

Objectif du projet
Construire une pipeline ML reproductible pour prédire les défauts de prêt à partir de données tabulaires réelles : nettoyage, feature engineering, gestion de la multicolinéarité (VIF), gestion du déséquilibre (SMOTETomek), et explicabilité.

Approche
- Nettoyage des données et création de features robustes.  
- Encodage par fréquence pour les variables à forte cardinalité, transformations numériques ciblées.  
- Suppression itérative des variables multicolinéaires via VIF.  
- Entraînement et évaluation (RandomForest baseline, XGBoost principal) en CV, avec SMOTETomek appliqué **à l'intérieur** des folds pour éviter le fuite de données.  
- Ajustement du seuil de décision pour maximiser le F1 et génération des courbes PR/ROC et calibration.

Résultats clés (exemple)
- XGBoost (CV + threshold tuning) : ROC-AUC ≈ 0.74, F1 ≈ 0.36  
Interprétation : Le modèle discrimine utilement mais nécessite une calibration métier (precision@k, coût des faux positifs/négatifs) avant production.

Étapes suivantes
1. Formaliser la politique d'étiquetage (définition métier du défaut).  
2. Finaliser la reproductibilité : config, date de snapshot déterministe, scripts d'exécution.  
3. Ajouter calibration, precision@k et tuning d'hyperparamètres (Optuna).  
4. Préparer une démo courte et une diapositive d'1 page pour les entretiens.

Contact
Juba Amari — amari.juba2006@gmail.com — github.com/Juba-Amr
