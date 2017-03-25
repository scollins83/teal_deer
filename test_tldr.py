# Nose tests for python.
import teal_deer as tldr

def test_get_file_list():
    assert len(tldr.get_file_list(TD_PDF_FILEPATH)) == 106, "Getting incorrect number of files."
