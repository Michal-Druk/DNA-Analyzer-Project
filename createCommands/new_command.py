from createCommands.create_command import CreateCommand
from dnaData.dna_sequence import DnaSequence


class NewCommand(CreateCommand):
    """
    handle the command "new"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 1, 2)
            if len(details) == 2:
                if details[1][0] != '@':
                    print("sequence name must start with @")
                    return False
                name = self.create_new_name(details[1][1:], '')
            else:
                name = self.create_name("seq")
            sequence = details[0]
            id = self.get_data().get_next_id()
            new_dna_sequence = DnaSequence(sequence)
            self.get_data().add_sequence(name, new_dna_sequence, 'o')
            print("[{}] {}: {}".format(id, name, new_dna_sequence))
        except Exception as e:
            print("Error: ", e)

    def create_name(self, name):
        i = 2
        new_name = name + str(1)
        old_name = name
        while (new_name in self.get_data().get_dna_data_by_name()):
            new_name = old_name + str(i)
            i += 1
        return new_name
