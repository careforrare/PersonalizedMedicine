import sys
import pandas as pd
from sklearn.metrics import f1_score, recall_score
import warnings

# Warnungen fuer FutureWarnings unterdruecken
warnings.filterwarnings("ignore", category=FutureWarning)

def detect_delimiter(filename):
    """ Versucht, den Delimiter einer Datei zu erkennen, indem die erste Zeile gelesen wird. """
    with open(filename, 'r') as file:
        first_line = file.readline()
    if ';' in first_line:
        return ';'
    else:
        return ','

def read_and_prepare_data(filepath):
    """Liest die CSV-Datei ein, benennt die Spalten um und bereitet die Daten vor."""
    try:
        delimiter = detect_delimiter(filepath)
        data = pd.read_csv(filepath, delimiter=delimiter)
        # Umbenennen der ersten beiden Spalten in 'subject_id' und 'disease'
        if len(data.columns) >= 2:
            data.columns = ['subject_id', 'disease'] + data.columns.tolist()[2:]
        data.dropna(subset=['subject_id'], inplace=True)
        return data
    except Exception as e:
        print(f"Fehler beim Lesen der Datei {filepath}: {e}")
        return None

def calculate_metrics(groundtruth_path, student_results_path):
    """Berechnet Metriken basierend auf den Eingabedaten."""
    groundtruth = read_and_prepare_data(groundtruth_path)
    student_results = read_and_prepare_data(student_results_path)

    if groundtruth is None or student_results is None:
        return

    merged_data = pd.merge(groundtruth, student_results, on='subject_id', how='left', suffixes=('_gt', '_sr'))
    merged_data = merged_data.dropna()
    if merged_data.empty:
        print("Keine übereinstimmenden IDs zwischen den Dateien gefunden.")
        return
    print(merged_data)
    f1 = f1_score(merged_data['disease_gt'], merged_data['disease_sr'], average='macro')
    recall = recall_score(merged_data['disease_gt'], merged_data['disease_sr'], average='micro')
    
    print(f"F1 Score: {f1}")
    #print(f"Sensitivity (Recall): {recall}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Benutzung: python script.py groundtruth.csv student_results.csv")
    else:
        groundtruth_path = sys.argv[1]
        student_results_path = sys.argv[2]
        calculate_metrics(groundtruth_path, student_results_path)
