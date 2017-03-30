import glob
import argparse
import json


def get_file_list(path, file_type='pdf'):
    """
    Gets a list of files of the directory of pdfs.
    :param path: Directory path
    :param file_type: Type of file to be imported.
    :return: List of files.
    """
    path += ('*.' + file_type)
    return glob.glob(path)


def parse_args():
    """
    Returns arguments passed at the command line as a dict
    """
    parser = argparse.ArgumentParser(description='Generates a machine Learning Dataset.')
    parser.add_argument('-c', help="Config File Location", required=True,
                        dest='config')
    args = vars(parser.parse_args())
    return args


def load_config(config_name):
    """
    loads a json config file and returns a config dictionary
    """
    with open(config_name) as config_file:
        config = json.load(config_file)
        return config


def replace_file_type_in_file_name(file_path, input_type='pdf', output_type='txt'):
    """
    Replace one file type with another in the specified file name.
    :param file_path: Starting file path.
    :return: File name with replacement type.
    """
    return file_path.replace('.' + input_type, '.' + output_type)