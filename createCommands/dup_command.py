from createCommands import create_command


class DupCommand(create_command.CreateCommand):
    """
   handle the command "dup"
   """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 1, 2)
            if len(details) == 2:
                if details[1][0] != '@':
                    raise Exception("sequence name must start with @")
                new_name = self.create_new_name(details[1][1:], '_')
            else:
                new_name = None
            id, name = self.get_name_and_id(details[0])
            if new_name == None: new_name = self.create_new_name(name, '_')
            sequence = self.get_data().get_sequence_by_id(str(id))
            self.get_data().add_sequence(new_name, sequence, 'o')
            id = self.get_data().get_next_id() - 1
            print("[{}] {}: {}".format(id, new_name, sequence))
        except Exception as e:
            print("Error: ", e)
