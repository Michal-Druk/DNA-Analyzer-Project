from analysisCommands.analysis_command import AnalysisCommand


class FindallCommand(AnalysisCommand):
    """
    handle the command "findall"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            seq_to_be_found, seq_to_find_in = self.get_sequences(details)
            all_sup_sequences_indexes = []
            for i in range(len(seq_to_find_in)):
                if seq_to_find_in[i:i + len(seq_to_be_found)] == seq_to_be_found:
                    all_sup_sequences_indexes.append(i + 1)
            if all_sup_sequences_indexes != []:
                print(all_sup_sequences_indexes)
                return all_sup_sequences_indexes
            raise Exception("no such sub-dna-string")
        except Exception as e:
            print("Error: ", e)
