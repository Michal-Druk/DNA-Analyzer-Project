from analysisCommands.analysis_command import AnalysisCommand


class LenCommand(AnalysisCommand):
    """
    handle the command "len"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 1, 1)
            id, name = self.get_name_and_id(details[0])
            seq = self.get_data().get_sequence_by_id(str(id))
            print(len(seq))
            return len(seq)
        except Exception as e:
            print("Error: ", e)
