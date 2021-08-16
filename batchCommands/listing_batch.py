from batchCommands.batch_command import BatchCommand


class ListingBatch(BatchCommand):
    """
    handle the command "batchlist"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 0, 0)
            batches = list(self.get_data().get_batch_names())
            print(batches)
        except Exception as e:
            print("Error: ", e)
