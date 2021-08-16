from managementCommands.management_command import ManagementCommand


class RenameCommand(ManagementCommand):
    """
    handle the command "rename"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 2, 2)
            id, name = self.get_name_and_id(details[0])
            sequence = self.get_data().get_sequence_by_id(str(id))
            if (details[1][0] != '@'):
                raise Exception("sequence name must start with @")
            new_name = details[1][1:]
            status = self.get_data().get_seq_status(id)
            self.get_data().delete_sequence(id, name)
            self.get_data().add_sequence(new_name, sequence, status, id)
        except Exception as e:
            print("Error: ", e)
