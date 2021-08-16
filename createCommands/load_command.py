from createCommands.create_command import CreateCommand
from dnaData.dna_sequence import DnaSequence


class LoadCommand(CreateCommand):
    """
   handle the command "load"
   """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 1, 2)
            if len(details) == 2:
                if details[1][0] != '@': raise Exception("sequence name must start with @")
                name = self.create_new_name(details[1][1:], '')
            else:
                if details[0][-7:] != ".rawdna": raise Exception("file name must end with .rawdna")
                name = self.create_new_name(details[0][:-7], '')
            with open(details[0], 'r') as f:
                for line in f:
                    sequence = line
            id = self.get_data().get_next_id()
            new_dna_sequence = DnaSequence(sequence)
            self.get_data().add_sequence(name, new_dna_sequence, '-')
            if len(new_dna_sequence) >= 40:
                new_dna_sequence = new_dna_sequence[:32] + '...' + new_dna_sequence[-3:len(new_dna_sequence)]
            print("[{}] {}: {}".format(id, name, new_dna_sequence))
        except Exception as e:
            print("Error: ", e)
