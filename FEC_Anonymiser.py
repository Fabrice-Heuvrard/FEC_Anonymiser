import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import csv
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def detect_delimiter(file_path):
    """
    Détecte le délimiteur utilisé dans le fichier CSV.
    """
    possible_delimiters = [',', ';', '\t', '|', ' ']
    
    with open(file_path, 'r') as file:
        sample = file.read(2048)  # Augmenter la taille de l'échantillon
        
    sniffer = csv.Sniffer()
    
    for delimiter in possible_delimiters:
        try:
            dialect = sniffer.sniff(sample, delimiters=delimiter)
            return dialect.delimiter
        except csv.Error:
            continue
    
    raise ValueError("Impossible de déterminer le délimiteur")


def anonymize_ecriturelib(df):
    """
    Anonymise la colonne 'EcritureLib' en remplaçant chaque caractère par une étoile.
    """
    df['EcritureLib'] = df['EcritureLib'].apply(lambda x: '*' * len(x) if isinstance(x, str) else x)

def anonymize_comptenum(df):
    """
    Tronque les valeurs de la colonne 'CompteNum' et 'CompAuxNum' si elles commencent par certains préfixes.
    """
    df['CompteNum'] = df['CompteNum'].apply(lambda x: x[:3] + '000' if x.startswith(('401', '411', '421', '455')) else x)
    df['CompAuxNum'] = df['CompteNum']

def anonymize_comptelib(df):
    """
    Anonymise les colonnes 'CompteLib' et 'CompAuxLib' en fonction des valeurs de 'CompteNum'.
    """
    df['CompteLib'] = df.apply(lambda row: '*' * len(row['CompteLib']) if isinstance(row['CompteLib'], str) and row['CompteNum'].startswith(('401', '411', '421', '455')) else row['CompteLib'], axis=1)
    df['CompAuxLib'] = df.apply(lambda row: '*' * len(row['CompAuxLib']) if isinstance(row['CompAuxLib'], str) and row['CompteNum'].startswith(('401', '411', '421', '455')) else row['CompAuxLib'], axis=1)

def anonymize_file(file_path):
    """
    Anonymise les colonnes spécifiques d'un fichier CSV et enregistre le résultat dans un nouveau fichier.
    """
    try:
        delimiter = detect_delimiter(file_path)
        logging.info(f"Délimiteur détecté: {delimiter}")
        
        df = pd.read_csv(file_path, delimiter=delimiter, dtype=str)
        
        required_columns = ['EcritureLib', 'CompteNum', 'CompteLib', 'CompAuxLib']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("Les colonnes nécessaires ne sont pas présentes dans le fichier.")
        
        anonymize_ecriturelib(df)
        anonymize_comptenum(df)
        anonymize_comptelib(df)
        
        file_path = Path(file_path)
        new_file_name = file_path.stem[9:] + '_FEC_anonyme' + file_path.suffix
        new_file_path = file_path.with_name(new_file_name)

        df.to_csv(new_file_path, index=False, sep=delimiter, quoting=csv.QUOTE_NONNUMERIC)
        logging.info(f"Fichier anonymisé enregistré sous : {new_file_path}")
        messagebox.showinfo("Succès", f"Fichier anonymisé enregistré sous : {new_file_path}")
    
    except Exception as e:
        logging.error(f"Erreur lors de l'anonymisation du fichier FEC : {e}")
        messagebox.showerror("Erreur", f"Erreur lors de l'anonymisation du fichier FEC : {e}")

def main():
    """
    Fonction principale pour lancer le processus d'anonymisation via une interface graphique.
    """
    root = tk.Tk()
    root.withdraw()
    
    while True:
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            anonymize_file(file_path)
            break
        else:
            retry = messagebox.askretrycancel("Aucun fichier sélectionné", "Aucun fichier FEC sélectionné. Voulez-vous réessayer ?")
            if not retry:
                break

if __name__ == "__main__":
    main()
