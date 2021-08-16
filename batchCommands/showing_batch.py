from batchCommands.batch_command import BatchCommand


class ShowingBatch(BatchCommand):
    """
   handle the command "batchshow"
   """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 1, 1)
            if details[0][0] != '@': raise Exception("butch name must start with @")
            name = details[0][1:]
            batch = self.get_data().get_batch(name)
            for command in batch:
                print(command)
        except Exception as e:
            print("Error: ", e)
