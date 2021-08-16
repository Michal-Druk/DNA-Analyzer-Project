from manipulationCommands.manipulation_command import ManipulationCommand


class ReplaceCommand(ManipulationCommand):
    """
    handle the command "replace"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            if len(details) < 3: raise Exception("too few arguments")
            id, name = self.get_name_and_id(details[0])
            sequence = self.get_data().get_sequence_by_id(str(id))
            self.illegal_inputs_handler(details)
            if details[-1][0] == '@':
                param_len = len(details) - 2
            else:
                param_len = len(details)
            for i in range(1, param_len, 2):
                sequence[int(details[i])] = details[i + 1]
            if details[-1][0] == '@':
                new_name = self.create_new_name(details[-1], '_r')
                if new_name != '@@':
                    self.get_data().add_sequence(new_name[1:], sequence, 'o')
                else:
                    new_name = self.create_new_name("repl_seq", '_r')
                    self.get_data().add_sequence(new_name, sequence, 'o')
                    id = self.get_data().get_next_id() - 1
            else:
                if self.get_data().get_seq_status(id) == 'o':
                    status = 'o'
                else:
                    status = '*'
                self.get_data().add_sequence(name, sequence, status, id)
                new_name = name
            print("[{}] {}: {}".format(id, new_name, sequence))
        except Exception as e:
            print("Error:", e)

    def illegal_inputs_handler(self, details):
        if len(details[1:]) % 2 != 0:
            raise Exception("illegal num of arguments")
        if details[-1][0] == '@' and details[-2] != ':':
            raise Exception("you must include : before a new name")
