


class Controller(object):

    def __init__(self,auto=True,**kwargs):
        if not auto:
            try:

                self.no_c = kwargs.get("clients")
            except KeyError:
                print("number of clients not specified")
                exit(-1)
        self.auto=auto

        self.childs = dict()



    def auto_balance(self):
        pass

    def fork_child(self):
        pass


    def kill_all(self):
        pass