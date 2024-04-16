import pandas as pd
import yaml
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

INPUT_DIR = '/mnt/input'
OUTPUT_DIR = '/mnt/output'

def read_config(file_path=f"{INPUT_DIR}/config.yml"):
    try:
        with open(file_path, "r") as config_file:
            config = yaml.safe_load(config_file)
        return config
                
    except FileNotFoundError:
        logger.info(f"Config file '{file_path}' not found.")


def write_output(content, file_path=f"{OUTPUT_DIR}/results.txt"):
    
    with open(file_path, "w") as text_file:
        text_file.write(content)


def convert_to_np(data):
    if isinstance(data, (pd.Series, pd.DataFrame)):
        return data.to_numpy()
    else:
        raise ValueError("Input data is not a Pandas Series or DataFrame.")


## Example Function how to read input files
# def read_files(train: str, test_input: str, sep: str, label_col: str):
#     train = pd.read_csv(f'{INPUT_DIR}/{train}', sep=sep)
#     test = pd.read_csv(f'{INPUT_DIR}/{test_input}', sep=sep)
#     X_train = train.drop(label_col, axis=1)
#     X_test = test.drop(label_col, axis=1)
#     y_train = train.loc[:, label_col]
#     y_test = test.loc[:, label_col]

#     X = convert_to_np(X_train)
#     y = convert_to_np(y_train)
#     X_test = convert_to_np(X_test)
#     y_test = convert_to_np(y_test)

#     return X, y, X_test, y_test