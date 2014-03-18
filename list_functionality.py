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
