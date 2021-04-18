import pandas as pd


def load_complete_dataset(path_to_complete_dataset: str):
    data = pd.read_csv(path_to_complete_dataset)
    return data


def get_training_length(data: pd.DataFrame):
    total_length = len(data)
    training_proportion = 0.8
    training_length = round(total_length * training_proportion)
    return training_length


def get_testing_length(data: pd.DataFrame):
    total_length = len(data)
    training_length = get_training_length(data)
    testing_length = total_length - training_length
    return testing_length


def get_training_dataset(data: pd.DataFrame):
    training_length = get_training_length(data)
    train = data.head(training_length)
    return train


def get_testing_dataset(data: pd.DataFrame):
    testing_length = get_testing_length(data)
    test = data.iloc[-testing_length:, data.columns != "target"]
    return test
