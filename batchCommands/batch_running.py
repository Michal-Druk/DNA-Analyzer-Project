from batchCommands.batch_command import BatchCommand
from controllers.cmd_controller import CmdController


class BatchRunning(BatchCommand):
    """
     handle the command "run"
     """

    def __init__(self):
        super().__init__()
        self.__run_command = CmdController()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 1, 1)
            if details[0][0] != '@': raise Exception("butch name must start with @")
            name = details[0][1:]
            batch = self.get_data().get_batch(name)
            for command in batch:
                self.__run_command.execute(command.rstrip().lstrip().split(" "))
        except Exception as e:
            print("Error: ", e)
