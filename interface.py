from mailListAdapter import MailListAdapter


class ManagerMailList:
    """docstring for Interface    def __init__(self, arg)"""

    def __init__(self):
        self.path_to_lists = ""
        self.maillists = []
        self.load()
        command = {"update": self.update}

    def create(self, list_name):
        list_handler = MailListAdapter(list_name)
        self.maillists.append((list_name, list_handler))

    def search_email(self, list_id):
        pass

    def show_lists(self):
        pass

    def merge_lists(self):
        pass

