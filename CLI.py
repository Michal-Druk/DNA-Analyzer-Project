from invoker import Invoker


class CLI:
    """
    command line interface, get command from the user and execute it, using the Invoker class
    """

    def __init__(self):
        self.__client_command = ""
        self.__invoker = Invoker()
        self.__run = True

    def set_run(self, boolean):
        self.__run = boolean

    def run(self):
        while (self.__run):
            self.__client_command = input("> cmd >>> ")
            command_details = self.__client_command.rstrip().lstrip().split(" ")
            self.__invoker.execute(command_details)
