from dnaData.dna_sequnece_data import DnaSequenceData


class Commands():
    """
    an Interface of all the commands classes, contain common methods
    """

    def __init__(self):
        self.__data = DnaSequenceData()

    def execute(self, details):
        pass

    def get_data(self):
        return self.__data

    def validate_arguments_number(self, details, i, j):
        if len(details) > j:
            raise Exception("too many arguments")
        if len(details) < i:
            raise Exception("too few arguments")

    def get_name_and_id(self, name_or_id):
        if name_or_id[0] == '#':
            id = name_or_id[1:]
            name = self.get_data().get_dna_name(id)
        elif name_or_id[0] == '@':
            name = name_or_id[1:]
            id = self.get_data().get_dna_id(name)
        else:
            raise Exception("sequence must start with @ or #")
        return id, name

    def create_new_name(self, name, char):
        i = 1
        new_name = name
        old_name = new_name
        while (new_name in self.get_data().get_dna_data_by_name()):
            new_name = old_name + char + str(i)
            i += 1
        return new_name
