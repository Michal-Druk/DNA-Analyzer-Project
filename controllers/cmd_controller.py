from analysisCommands.count_command import CountCommand
from analysisCommands.find_command import FindCommand
from analysisCommands.findall_command import FindallCommand
from analysisCommands.len_command import LenCommand
from batchCommands.batch_creation import BatchCreation
from controlCommands.list_command import ListCommand
from controlCommands.quit_command import QuitCommand
from createCommands.dup_command import DupCommand
from createCommands.load_command import LoadCommand
from createCommands.new_command import NewCommand
from managementCommands.del_command import DelCommand
from managementCommands.rename_command import RenameCommand
from managementCommands.save_command import SaveCommand
from manipulationCommands.replace_command import ReplaceCommand
from manipulationCommands.slice_command import SliceCommand


class CmdController:
    """
   cmd commands controller (factory method pattern)
   """

    def __init__(self):
        self.__reserved_commands = {
            'new': NewCommand,
            'load': LoadCommand,
            'dup': DupCommand,
            'slice': SliceCommand,
            'replace': ReplaceCommand,
            'rename': RenameCommand,
            'del': DelCommand,
            'save': SaveCommand,
            'find': FindCommand,
            'findall': FindallCommand,
            'len': LenCommand,
            'count': CountCommand,
            'list': ListCommand,
            'quit': QuitCommand,
            'batch': BatchCreation,
        }

    def execute(self, cmd):
        exec_command = self.__reserved_commands[cmd[0]]()
        exec_command.execute(cmd[1:])
