from managementCommands.management_command import ManagementCommand


class SaveCommand(ManagementCommand):
    """
    handle the command "save"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 1, 3)
            id, name = self.get_name_and_id(details[0])
            sequence = super().get_data().get_sequence_by_id(str(id))
            if len(details) == 2:
                file_name = details[1] + ".rawdna"
            else:
                file_name = name + ".rawdna"
            with open(file_name, 'w') as file:
                file.write(str(sequence))
            self.get_data().set_seq_status(id, '-')
        except Exception as e:
            print("Error: ", e)
