from batchCommands.batch_command import BatchCommand


class SavingBatch(BatchCommand):
    """
   handle the command "batchsave"
   """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 1, 2)
            if details[0][0] != '@': raise Exception("butch name must start with @")
            name = details[0][1:]
            batch = self.get_data().get_batch(name)
            if len(details) == 2:
                file_name = details[1] + ".dnabatch"
            else:
                file_name = name + ".dnabatch"
            with open(file_name, 'w') as file:
                for element in batch:
                    file.write(str(element + "\n"))
        except Exception as e:
            print("Error: ", e)
