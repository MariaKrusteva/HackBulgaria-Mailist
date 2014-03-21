from maillist import MailList


class MailListAdapter(MailList):
    """docstring for MailListAdapter"""
    def __init__(self, name):
        super().__init__(name)

    def show_list(self):
        result = ""
        i = 1
        for key in sorted(self.contacts):
            result += "[{}]".format(i) + key + " - " + self.contacts[key] + "\n"
            i += 1
        return result

    def update(self, new_name):
        self.name = new_name
