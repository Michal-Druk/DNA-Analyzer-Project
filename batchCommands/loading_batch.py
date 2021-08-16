from batchCommands.batch_command import BatchCommand


class LoadingBatch(BatchCommand):
    """
    handle the command "batchload"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 1, 3)
            if details[0][-9:] != ".dnabatch": raise Exception("file name must end with .dnabatch")
            if len(details) == 3:
                if details[2][0] != '@': raise Exception("sequence name must start with @")
                if details[1] != ":": raise Exception("you must include : before a new name")
                name = self.create_new_name(details[2][1:], '_')
            else:
                name = self.create_new_name(details[0][:-9], '_')
            batch = []
            with open(details[0], 'r') as f:
                for line in f:
                    batch.append(line[:-1])
            self.get_data().add_batch(name, batch)
        except Exception as e:
            print("Error: ", e)
