# Anonymisation du Fichier des Écritures Comptables (FEC)

Ce projet contient un script Python permettant d'anonymiser les fichiers des écritures comptables (FEC) conformément aux exigences réglementaires tout en préservant l'intégrité des données pour les analyses comptables et entraîner les futurs modèles d'IA.

## Fonctionnalités

- Détection automatique du délimiteur dans les fichiers CSV
- Anonymisation des colonnes `EcritureLib`, `CompteNum`, `CompteLib` et `CompAuxLib`
- Interface graphique simple pour sélectionner le fichier FEC à anonymiser
- Enregistrement du fichier anonymisé avec un nouveau nom afin d'éviter d'avoir le SIREN dans le titre

## Prérequis

- Python 3.9 et suivants
- Bibliothèques Python: pandas, tkinter, csv

## Utilisation

- Placez votre fichier FEC original dans le répertoire du projet ou à un emplacement accessible.
- Exécutez le script : `python anonymiser_fec.py`
- Une fenêtre de dialogue s'ouvrira pour vous permettre de sélectionner le fichier FEC à anonymiser.
- Le fichier anonymisé sera enregistré dans le même répertoire que le fichier original avec le suffixe `_FEC_anonyme`.

## Configuration

Le script n'utilise pas de fichier de configuration externe. Les colonnes à anonymiser sont codées en dur dans le script.

Si vous souhaitez anonymiser d'autres colonnes ou personnaliser l'anonymisation, vous pouvez modifier les fonctions suivantes dans le script :

- `anonymize_ecriturelib(df)`: Anonymise la colonne `EcritureLib`.
- `anonymize_comptenum(df)`: Tronque les valeurs de la colonne `CompteNum` et met à jour `CompAuxNum`.
- `anonymize_comptelib(df)`: Anonymise les colonnes `CompteLib` et `CompAuxLib` en fonction des valeurs de `CompteNum`.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Anonymization of Accounting Entry Files (FEC)

This project contains a Python script that anonymizes accounting entry files (FEC) in accordance with regulatory requirements while preserving data integrity for accounting analysis and training future AI models.

## Features

- Automatic detection of delimiters in CSV files
- Anonymization of `EcritureLib`, `CompteNum`, `CompteLib`, and `CompAuxLib` columns
- Simple graphical interface to select the FEC file to be anonymized
- Saving the anonymized file with a new name to avoid having the SIREN in the title

## Prerequisites

- Python 3.9 and above
- Python libraries: pandas, tkinter, csv

## Usage

- Place your original FEC file in the project directory or an accessible location.
- Run the script: python anonymiser_fec.py
- A dialog window will open to allow you to select the FEC file to be anonymized.
- The anonymized file will be saved in the same directory as the original file with the suffix _FEC_anonyme.

## Configuration
The script does not use an external configuration file. The columns to be anonymized are hardcoded in the script.

If you want to anonymize other columns or customize the anonymization, you can modify the following functions in the script:
- anonymize_ecriturelib(df): Anonymizes the EcritureLib column.
- anonymize_comptenum(df): Truncates the values of the CompteNum column and updates CompAuxNum.
- anonymize_comptelib(df): Anonymizes the CompteLib and CompAuxLib columns based on the values of CompteNum.
