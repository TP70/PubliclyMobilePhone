# from Options import UserOptions
class UserMenus:

    @staticmethod
    def string():
        """
        Prints a dashed string
        """
        return print('---------------------------------------------------------------------------------------------')

    @staticmethod
    def n_string():
        """
        Prints a dashed string jumping a line at the beginning
        """
        return print('\n---------------------------------------------------------------------------------------------')

    @staticmethod
    def string_n():
        """
        Prints a dashed string jumping a line at the end
        """
        return print('---------------------------------------------------------------------------------------------\n')

    @classmethod
    def display_initial_menu(cls):
        """
        Displays the initial menu
        """
        UserMenus.string()
        print('PLEASE CHOOSE ONE OF THE FOLLOWING OPTIONS:')
        UserMenus.string()
        print('1) RUN THE FULL DATABASE SORTED BY "CURRENT RENT"')
        print('2) RUN THE FIRST 5 ITEMS')
        print('3) RUN A NEW LIST WITH "LEASE YEARS" = 25 YEARS')
        print('4) GET TOTAL RENT WHERE "LEASE YEARS" = 25 YEARS')
        print('5) GET TENANTS UNIQUE NAMES')
        print('6) GET ROWS BETWEEN DATES 1/06/99 AND 31/08/2007')
        print('7) EXIT')
        UserMenus.string()
        # UserOptions.get_user_option()





