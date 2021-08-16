from commands import Commands


class AnalysisCommand(Commands):
    """
    analysisCommands interface
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        pass

    def get_sequences(self, details):
        self.validate_arguments_number(details, 2, 2)
        seq_to_find_in_id, seq_to_find_in_name = self.get_name_and_id(details[0])
        seq_to_find_in = self.get_data().get_sequence_by_id(str(seq_to_find_in_id))
        if details[1][0] in "@#":
            seq_to_be_found_id, seq_to_be_found_name = self.get_name_and_id(details[1])
            seq_to_be_found = str(self.get_data().get_sequence_by_id(str(seq_to_be_found_id)))
        else:
            seq_to_be_found = details[1]
        return seq_to_be_found, seq_to_find_in
