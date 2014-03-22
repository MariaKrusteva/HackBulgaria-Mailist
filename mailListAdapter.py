from maillist import MailList


class MailListAdapter(MailList):
    """docstring for MailListAdapter"""
    def __init__(self, name):
        super().__init__(name)

    def show_list(self):
        result = ""
        i = 1
        for key in sorted(self.contacts):
            result += "[{}]".format(i) + key + " - " \
                + self.contacts[key] + "\n"
            i += 1
        return result

    def update(self, new_name):
        self.name = new_name

    def get_name_at_index_from_contacts(self, index):
        i = 1
        for key in sorted(self.contacts):
            if i == index:
                return key
            i += 1

    def save(self):
        result = ""
        for key in sorted(self.contacts):
            result += key + " - " + self.contacts[key] + "\n"
        file_to_save = open("user_lists/" + self.name, "w")
        file_to_save.write(result)
        file_to_save.close()

 