# Xray-Predictions

## Description

**Xray-Predictions** est un projet académique de Data Science dédié à l’analyse, au traitement et à l’exploitation de données de radiographies thoraciques.

Le projet s’appuie sur le dataset **CheXpert (version small v1.1)** et couvre l’ensemble du cycle de vie de la donnée, depuis l’ingestion jusqu’à la modélisation.

L’objectif est de construire un pipeline complet permettant de transformer des données brutes (images et métadonnées) en un dataset fiable et exploitable pour des modèles de Machine Learning visant la prédiction de pathologies pulmonaires.

---

## Contexte et objectifs

Ce projet est réalisé dans le cadre de la certification **RNCP Data Scientist**.

### Objectifs :

* Concevoir une infrastructure de données (MinIO)
* Automatiser l’ingestion et le stockage des données
* Nettoyer et fiabiliser un dataset médical
* Réaliser une analyse exploratoire (EDA)
* Développer des modèles de Machine Learning
* Travailler sur des données structurées et non structurées

---

## Dataset

Le projet utilise le dataset :

**CheXpert (small v1.1)**

### Contenu :

* Environ **224 000 radiographies thoraciques**
* Données issues d’environ **65 000 patients**
* Métadonnées (âge, sexe, type de vue)
* Labels médicaux (pathologies multiples)

### Particularités :

* Données médicales réelles
* Présence de valeurs manquantes
* Dataset déséquilibré
* Labels partiellement annotés

---

## Fonctionnalités principales

* Ingestion de données via API Kaggle
* Stockage dans MinIO (object storage)
* Pipeline de traitement des données
* Nettoyage et préparation des données
* Analyse de la qualité des données
* Analyse exploratoire (EDA)
* Encodage et transformation des variables
* Implémentation de modèles de Machine Learning

---

## Machine Learning

### Données structurées (supervisé)

Les métadonnées issues du fichier CSV sont utilisées pour entraîner des modèles de classification.

Objectifs :

* Prédire la présence de pathologies
* Évaluer les performances des modèles

Modèles envisagés :

* Régression logistique
* Random Forest
* Gradient Boosting

---

### Données non structurées (images)

Les radiographies sont utilisées pour des analyses avancées :

#### Approche non supervisée :

* Clustering (K-Means, DBSCAN)
* Réduction de dimension (PCA)

#### Deep Learning :

* Implémentation de modèles CNN
* Extraction de caractéristiques visuelles
* Classification basée sur les images

---

## Technologies utilisées

### Langage :

* Python

### Librairies :

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* TensorFlow

### Outils :

* Jupyter Notebook
* MinIO
* Docker (docker-compose)
* Git / GitHub

---

## Installation

### 1. Cloner le projet


git clone https://github.com/fikhadriouene/M2i-Project-XrayPredictions.git
cd M2i-Project-XrayPredictions


### 2. Créer un environnement virtuel


python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows


### 3. Installer les dépendances


pip install -r requirements.txt


### 4. Lancer les services (MinIO, etc.)


docker-compose up -d


---

## Utilisation

### Étapes principales :

1. Télécharger le dataset CheXpert (small v1.1)
2. Lancer le pipeline d’ingestion (Bloc 1)
3. Explorer et nettoyer les données (Bloc 2)
4. Réaliser l’analyse exploratoire (EDA)
5. Développer les modèles de Machine Learning (Bloc 3 et Bloc 4)

---

## Exemples d’utilisation

* Identification de données incohérentes (âge, sexe)
* Analyse du déséquilibre des classes
* Préparation des données pour la modélisation
* Exploration de similarités entre images radiologiques

---

## Screenshots / Démo

À compléter avec :

* Graphiques issus de l’EDA
* Heatmap de corrélation
* Résultats des modèles
* Visualisations issues du clustering ou CNN

Les images peuvent être ajoutées dans le dossier `reports/figures/`.

---

## Structure du projet


X-RAY PREDICTIONS/
├── Bloc01_Infrastructure_de_donnees/
├── Bloc02_Analyse_des_Donnees/
├── Bloc03_Analyse_Predictive_des_Donnees_Structurees/
├── Bloc04_Analyse_predictive_des_donnees_non_structurees/
├── Bloc05_bloc5_industrialisation/
├── Bloc6_gestion_projet/
├── data/
├── logs/
├── models/
├── .env
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## Feuille de route

Les développements suivants sont prévus dans la continuité du projet :

* Implémentation et comparaison de modèles de classification
* Optimisation des performances (tuning, gestion du déséquilibre)
* Développement de modèles CNN pour les images
* Mise en place d’une API (FastAPI ou Flask)
* Création d’un dashboard de visualisation
* Industrialisation du pipeline

Ces étapes permettront de couvrir l’ensemble du cycle de vie d’un projet Data Science.

---

## Auteur

Farid Ikhadriouene
GitHub : https://github.com/fikhadriouene
LinkedIn : à compléter

---

## Licence

Projet open-source
Licence recommandée : MIT

---
