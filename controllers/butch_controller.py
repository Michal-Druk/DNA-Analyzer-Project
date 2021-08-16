from batchCommands.batch_running import BatchRunning
from batchCommands.listing_batch import ListingBatch
from batchCommands.loading_batch import LoadingBatch
from batchCommands.saving_batch import SavingBatch
from batchCommands.showing_batch import ShowingBatch


class ButchController:
    """
    butch commands controller (factory method pattern)
    """

    def __init__(self):
        self.__reserved_commands = {
            'run': BatchRunning,
            'batchlist': ListingBatch,
            'batchshow': ShowingBatch,
            'batchsave': SavingBatch,
            'batchload': LoadingBatch
        }

    def execute(self, cmd):
        exec_command = self.__reserved_commands[cmd[0]]()
        exec_command.execute(cmd[1:])
