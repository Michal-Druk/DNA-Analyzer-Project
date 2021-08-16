from batchCommands.batch_command import BatchCommand


class BatchCreation(BatchCommand):
    """
    handle the command "batch"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 1, 1)
            name = self.create_new_name(details[0], '_')
            not_end = True
            batch = []
            while (not_end):
                command = input(">batch >>>")
                if command.rstrip().lstrip() == "end":
                    self.get_data().add_batch(name, batch)
                    not_end = False
                else:
                    batch.append(command)
        except Exception as e:
            print("Error: ", e)
