# Bloc 1 — Construction et alimentation d'une infrastructure de gestion de données

## Objectif
Mettre en place une architecture de données robuste permettant de collecter, stocker, organiser et rendre exploitables les données du projet.

## Ce qu’il faut faire

### 1. Collecte des données
- Identifier une source de données (ex : dataset d’images thoraciques)
- Télécharger et stocker les données
- Gérer les métadonnées associées (CSV, labels)

### 2. Mise en place du stockage
- Stocker les images dans un système adapté (ex : MinIO)
- Séparer les données :
  - RAW (données brutes)
  - PROCESSED (données transformées)
- Structurer les données :
  - train / val / test
  - sain / malade

### 3. Conception de l’architecture
- Définir une architecture claire :
  - stockage objet (MinIO)
  - base de données (PostgreSQL) pour les métadonnées
- Assurer la traçabilité des données

### 4. Mise en place d’un pipeline d’ingestion
- Script de téléchargement des données
- Extraction des archives
- Nettoyage des données
- Transformation et stockage dans PROCESSED

### 5. ETL (Extract Transform Load)
- Extraire les données sources
- Nettoyer les métadonnées
- Charger dans PostgreSQL

## Livrables attendus
- Arborescence de données claire
- Scripts d’ingestion
- Schéma d’architecture
- Table de métadonnées

## Technologies recommandées
- Python
- Pandas
- MinIO
- PostgreSQL
- pathlib / os