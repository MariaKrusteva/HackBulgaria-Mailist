import os


def show_lists(filePath):
    """
    Returns a list of the files with names
    """
    list_of_files = os.listdir(filePath)
    result = ""
    for i in range(1, len(list_of_files)):
        result += "[{}] - {}\n".format(i, lilist_of_files[i])
    return result
