from app import DataManipulation
from Validation import Validations


class UserOptions:

    @classmethod
    def user_options(cls, chose_option):
        """
        Directs the client according to the requested option
        """
        if chose_option == '1':
            print(*([x for x in DataManipulation.get_datafile_ascending_order()]), sep='\n')
        elif chose_option == '2':
            print(*([x for x in DataManipulation.get_first_five_current_rent_rows()]), sep='\n')
        elif chose_option == '3':
            print(*([x for x in DataManipulation.get_lease_years_where_25()]), sep='\n')
        elif chose_option == '4':
            print(DataManipulation.total_rent_where_lease_years_25())
        elif chose_option == '5':
            print(DataManipulation.get_unique_tenant_names())
        elif chose_option == '6':
            print(*([x for x in DataManipulation.get_rows_between_dates()]), sep='\n')
        elif chose_option == '7':
            quit()

    @classmethod
    def get_user_option(cls):
        """
        Gets the validated option from the client
        """
        return cls.user_options(
            Validations.validation_user_input('OPTION NUMBER: ', ['1', '2', '3', '4', '5', '6', '7'], True))

