from analysisCommands.analysis_command import AnalysisCommand


class FindCommand(AnalysisCommand):
    """
    handle the command "find"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            seq_to_be_found, seq_to_find_in = self.get_sequences(details)
            for i in range(len(seq_to_find_in)):
                if seq_to_find_in[i:i + len(seq_to_be_found)] == seq_to_be_found:
                    print(i + 1)
                    return i + 1
            raise Exception("no such sub-dna-string")
        except Exception as e:
            print("Error: ", e)
