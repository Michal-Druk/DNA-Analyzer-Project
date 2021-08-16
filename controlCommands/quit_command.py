import sys
from controlCommands.control_command import ControlCommand


class QuitCommand(ControlCommand):
    """
    handle the command "quit"
    """

    def __init__(self):
        super().__init__()

    def execute(self, details):
        try:
            self.validate_arguments_number(details, 0, 0)
            data = self.get_data().get_dna_data_by_id()
            num_modified_seq = 0
            num_new_seq = 0
            for id in data:
                if self.get_data().get_seq_status(id) == 'o':
                    num_new_seq += 1
                elif self.get_data().get_seq_status(id) == '*':
                    num_modified_seq += 1
            wait_to_confirm = True
            if num_modified_seq == 0 and num_new_seq == 0:
                wait_to_confirm = False
            else:
                print("There are {} modified and {} new sequences. Are you sure you want to quit?".format(
                    num_modified_seq, num_new_seq))
                print("Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
            while (wait_to_confirm):
                confirm = input(">confirm >>>")
                if confirm == 'Y' or confirm == 'y':
                    print("Thank you for using Dnalanyzer.\nGoodbye!")
                    sys.exit()
                elif confirm == 'N' or confirm == 'n':
                    print("quit was canceled")
                    wait_to_confirm = False
                else:
                    print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
        except Exception as e:
            print("Error: ", e)
