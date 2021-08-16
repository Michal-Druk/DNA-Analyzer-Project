from manipulationCommands.manipulation_command import ManipulationCommand


class SliceCommand(ManipulationCommand):
    """
    handle the command "slice"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 3, 5)
            id, name = self.get_name_and_id(details[0])
            sequence = self.get_data().get_sequence_by_id(str(id))
            sequence = sequence[int(details[1]):int(details[2]) + 1]
            if len(details) == 3:
                if self.get_data().get_seq_status(id) == 'o':
                    status = 'o'
                else:
                    status = '*'
                self.get_data().add_sequence(name, sequence, status, id)
                print("[{}] {}: {}".format(id, name, sequence))
                return
            self.illegal_inputs_handler(details)
            new_name = self.create_new_name(details[4], '_s')
            if new_name != '@@':
                self.get_data().add_sequence(new_name[1:], sequence)
            else:
                new_name = self.create_new_name("short_seq", '_s')
                self.get_data().add_sequence(new_name, sequence, 'o')
            id = self.get_data().get_next_id() - 1
            print("[{}] {}: {}".format(id, new_name, sequence))
        except Exception as e:
            print("Error: ", e)

    def illegal_inputs_handler(self, details):
        if len(details) == 4:
            raise Exception("illegal num of arguments")
        if details[3] != ':':
            raise Exception("you must include : before a new name")
        if details[4][0] != '@':
            raise Exception("name must start with @")
