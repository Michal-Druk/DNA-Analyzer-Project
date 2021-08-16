from analysisCommands.analysis_command import AnalysisCommand


class CountCommand(AnalysisCommand):
    """
    handle the command "count"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            seq_to_be_found, seq_to_find_in = self.get_sequences(details)
            num_sup_sequences = 0
            for i in range(len(seq_to_find_in)):
                if seq_to_find_in[i:i + len(seq_to_be_found)] == seq_to_be_found:
                    num_sup_sequences += 1
            if num_sup_sequences != 0:
                print(num_sup_sequences)
                return num_sup_sequences
            raise Exception("no such sub-dna-string")
        except Exception as e:
            print("Error: ", e)
