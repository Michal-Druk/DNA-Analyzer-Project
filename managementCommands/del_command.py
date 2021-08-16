from managementCommands.management_command import ManagementCommand


class DelCommand(ManagementCommand):
    """
    handle the command "del"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 0, 2)
            id, name = self.get_name_and_id(details[0])
            sequence = self.get_data().get_sequence_by_id(str(id))
            if len(sequence) > 40: sequence = sequence[:32] + '...' + sequence[-3:len(sequence)]
            print("Do you really want to delete {} : {}?".format(name, sequence))
            print("Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
            wait_to_confirm = True
            while (wait_to_confirm):
                confirm = input(">confirm >>>")
                if confirm == 'Y' or confirm == 'y':
                    super().get_data().delete_sequence(id, name)
                    print("Deleted [{}] {}: {}".format(id, name, sequence))
                    wait_to_confirm = False
                elif confirm == 'N' or confirm == 'n':
                    print("Deletion was canceled")
                    wait_to_confirm = False
                else:
                    print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
        except Exception as e:
            print("Error: ", e)
