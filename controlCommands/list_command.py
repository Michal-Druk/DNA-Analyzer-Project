from controlCommands.control_command import ControlCommand


class ListCommand(ControlCommand):
    """
    handle the command "list"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 0, 0)
            data = self.get_data().get_dna_data_by_id()
            for id in data:
                print("{} [{}] {}: {}".format(self.get_data().get_seq_status(id), id, data[id]['name'],
                                              self.get_data().get_sequence_by_id(id)))
        except Exception as e:
            print("Error: ", e)
