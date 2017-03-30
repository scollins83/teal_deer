# Nose tests for python.
import teal_deer as tldr


def test_get_configuration():
    assert len(tldr.load_config('config.json')) == 3, "Configuration not loaded correctly."


def test_get_file_list():
    configuration = tldr.load_config('config.json')
    assert len(tldr.get_file_list(configuration['files_path'])) == 106, "Getting incorrect number of files."


def test_replace_file_type_in_file_name():
    configuration = tldr.load_config('config.json')
    file_list = tldr.get_file_list(configuration['files_path'])
    print(file_list[0])
    assert tldr.replace_file_type_in_file_name(file_list[0]) == \
           '/Users/saracollins/Documents/LiteratureReviews/chatbots/0310018.txt', \
        "File type replacement not happening correctly."
