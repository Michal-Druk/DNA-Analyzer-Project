from controllers.butch_controller import ButchController
from controllers.cmd_controller import CmdController


class Invoker:
    """
    class that designed to execute commands, calling the controllers
    """

    def __init__(self):
        self.__cmd_commands = ['new', 'load', 'dup', 'slice', 'replace', 'rename', 'del', 'save', 'find', 'findall',
                               'len', 'count', 'list', 'quit', 'batch']
        self.__butch_commands = ['run', 'batchlist', 'batchshow', 'batchsave', 'batchload']
        self.__butch_controller = ButchController()
        self.__cmd_controller = CmdController()

    def execute(self, cmd):
        if cmd[0] in self.__cmd_commands:
            self.__cmd_controller.execute(cmd)
        elif cmd[0] in self.__butch_commands:
            self.__butch_controller.execute(cmd)
        else:
            raise Exception("no such command")
