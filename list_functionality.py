import os

class CommandLineMailist():
    """docstring"""

    def show_list(identifier):
        files = sorted(os.listdir("user_lists/"))
        if identifier > len(files):
            print("List with unique identifier {} was not found!").format(identifier)
        else:
            result = ""
            file_name = files[identifier - 1]
            file = open("user_lists/" + file_name, "r")
            content = file.read()
            content = content.split("\n")
            i = 1
            for name_mail in content:
                result += ("[{}] {}\n".format(i, name_mail))
                i += 1
            file.close()
            return result

    def show_lists(filePath):
        """
        Returns a list of the files with names
        """
        list_of_files = sorted(os.listdir(filePath))
        result = ""
        for i in range(0, len(list_of_files)):
            result += "[{}] - {}\n".format(i+1, list_of_files[i])
        return result

    def merge_lists(list_identifier1, list_identifier2, new_list_name):
        files = sorted(os.listdir("user_lists/")) #MUST BE GLOBAL

        file1 = open("user_lists/" + files[list_identifier1-1], "r")
        content1 = file1.read()
        file1.close()

        file2 = open("user_lists/" + files[list_identifier2-1], "r")
        content2 = file2.read()
        file2.close()

        new_file = open("user_lists/" + new_list_name, "w")
        new_file.write(content1 + "\n" + content2)
        new_file.close()
