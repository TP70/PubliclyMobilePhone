class Validations:


    @classmethod
    def validation_user_input(cls, message, possible_inputs, case_sensitive):
        """
        Checks the information given according to the established validation criteria
        """
        user_input = input(message).lower()

        if case_sensitive:
            while user_input not in possible_inputs:
                print('Please enter a valid option')
                user_input = input(message).lower()
        else:
            while user_input not in [choice for choice in possible_inputs]:
                print('Please enter a valid option')
                user_input = input(message)
        return user_input