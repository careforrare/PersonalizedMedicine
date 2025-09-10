import pandas as pd
import yaml
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_config(file_path):
    with open(file_path, "r") as config_file:
        config = yaml.safe_load(config_file)
    return config

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