import os


def show_lists(filePath):
    """
    Returns a list of the files with names
    """
    list_of_files = sorted(os.listdir(filePath))
    result = ""
    for i in range(0, len(list_of_files)):
        result += "[{}] - {}\n".format(i + 1, list_of_files[i])
    return result


def create(filePath, list_name):
    open(filePath + list_name, "w")


def __checkIfFileExist(filePath, list_name):
    list_of_files = os.listdir(filePath)
    return list_name in list_of_files


def add(filePath, list_name):
    if not __checkIfFileExist(filePath, list_name):
        print("List given does not exists")
        return False
    #adding the prompt functionality
    name = input("name>")
    email = input("mail>")
    file = open(filePath + list_name, "a")
    file.write(name + " - " + email + '\n')
    file.close()

def search_emails(filePath, email):
    result = ""
    list_of_files = os.listdir(filePath)
    for item in list_of_files:
        if
    if result == "":
        result = "<{}> was not found in the current mailing\
              lists.\n".format(email))
        return result
    else:
        return result
