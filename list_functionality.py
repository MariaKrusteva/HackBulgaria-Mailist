import os


def show_lists(filePath):
    """
    Returns a list of the files with names
    """
    list_of_files = sorted(os.listdir(filePath))
    result = ""
    for i in range(0, len(list_of_files)):
        result += "[{}] - {}\n".format(i+1, list_of_files[i])
    return result
