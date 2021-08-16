from commands import Commands


class BatchCommand(Commands):
    """
    batchCommands interface
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        pass

    def create_new_name(self, name, char):
        i = 1
        new_name = name
        old_name = new_name
        while (new_name in self.get_data().get_batch_names()):
            new_name = old_name + '_' + str(i)
            i += 1
        return new_name
