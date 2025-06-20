import sys
import pandas as pd
from sklearn.metrics import accuracy_score
import warnings

# ignore warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def normalize_code(code):
    return code.strip().upper()

def detect_delimiter(filename):
    """ Get file delimiter based on first line. """
    with open(filename, 'r') as file:
        first_line = file.readline()
    if ';' in first_line:
        return ';'
    else:
        return ','

def read_and_prepare_data(filepath):
    """ Read csv file, renames columns and prepares data."""
    try:
        delimiter = detect_delimiter(filepath)
        data = pd.read_csv(filepath, delimiter=delimiter)
        # Sicherstellen, dass mindestens zwei Spalten vorhanden sind
        if len(data.columns) >= 2:
            data.columns = ['subject_id', 'disease'] + data.columns.tolist()[2:]
        data['disease'] = data['disease'].apply(normalize_code)
        data.dropna(subset=['subject_id'], inplace=True)
        return data
    except Exception as e:
        print(f"Error while reading file {filepath}: {e}")
        return None

def calculate_metrics(groundtruth_path, student_results_path):
    """Calculate Accuracy based on input."""
    groundtruth = read_and_prepare_data(groundtruth_path)
    student_results = read_and_prepare_data(student_results_path)

    if groundtruth is None or student_results is None:
        return

    merged_data = pd.merge(groundtruth, student_results, on='subject_id', how='left', suffixes=('_gt', '_sr'))
    merged_data = merged_data.dropna()
    print(merged_data)
    if merged_data.empty:
        print("No matching IDs between files or no data left after join.")
        return

    # Calc accuracy
    acc = accuracy_score(merged_data['disease_gt'], merged_data['disease_sr'])
    print(f"Accuracy: {acc}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py groundtruth.csv student_results.csv")
    else:
        groundtruth_path = sys.argv[1]
        student_results_path = sys.argv[2]
        calculate_metrics(groundtruth_path, student_results_path)