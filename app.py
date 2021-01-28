from Validation import Validations
from Menus import UserMenus
import csv
import operator
from datetime import datetime


class ReadFile:

    @classmethod
    def read_csv(cls) -> list:
        """
        :args file: csv file inputted as string path
        """
        data = list(csv.reader(open('Python Developer Test Dataset.csv')))
        for line in data[1:]:
            line[7] = datetime.strptime(line[7], "%d %b %Y")
            line[9] = int(line[9])
            line[-1] = float(line[-1])
        return data


class DataManipulation:

    @staticmethod
    def get_datafile_ascending_order() -> list:
        """
        returns data file as list that has been
        sorted by current rent in ascending order
        """
        return sorted(ReadFile.read_csv()[1:], key=operator.itemgetter(10))

    @classmethod
    def get_first_five_current_rent_rows(cls) -> list:
        """
        output: prints the first five rows of the data file that
        has been sorted by current rent in ascending order
        """
        return [line for line in (sorted(ReadFile.read_csv()[1:], key=operator.itemgetter(10)))[:5]]

    @classmethod
    def get_lease_years_where_25(cls) -> list:
        """
        output: prints all data rows where the lease years
        is equal to 25
        """
        return [x for x in [line for line in ReadFile.read_csv() if line[9] == 25]]

    @classmethod
    def total_rent_where_lease_years_25(cls) -> float:
        """
        output: returns total rent as integer where
        lease years is 25
        """
        total_rent = 0
        for line in [line for line in ReadFile.read_csv() if line[9] == 25]:
            total_rent += line[-1]
        return total_rent

    @classmethod
    def get_rows_between_dates(cls) -> list:
        """
        output: answer for Q4, prints row info between date
        specified
        """
        date_list = [x for x in ReadFile.read_csv()[1:] if datetime(1999, 6, 1) < x[7] < datetime(2007, 8, 31)]
        for x in date_list:
            x[7] = x[7].strftime('%d/%m/%Y')
        return [x for x in date_list]

    @classmethod
    def get_unique_tenant_names(cls) -> object:
        """
        output: prints dictionary information for unique
        tenant names with instances as integer.
        """
        return print(*(set([x[6] for x in [x for x in ReadFile.read_csv()[1:] if x not in x]])), sep='\n')


class UserOptions:

    @classmethod
    def user_options(cls, chose_option: str):
        """
        Directs the client according to the requested option
        """
        if chose_option == '1':
            print(*([x for x in DataManipulation.get_datafile_ascending_order()]), sep='\n')
            cls.display_initial_menu()
        elif chose_option == '2':
            print(*([x for x in DataManipulation.get_first_five_current_rent_rows()]), sep='\n')
            cls.display_initial_menu()
        elif chose_option == '3':
            print(*([x for x in DataManipulation.get_lease_years_where_25()]), sep='\n')
            cls.display_initial_menu()
        elif chose_option == '4':
            print(DataManipulation.total_rent_where_lease_years_25())
            cls.display_initial_menu()
        elif chose_option == '5':
            DataManipulation.get_unique_tenant_names()
            # print(*(set([x[6] for x in DataManipulation.get_unique_tenant_names()])), sep='\n')
            cls.display_initial_menu()
        elif chose_option == '6':
            print(*([x for x in DataManipulation.get_rows_between_dates()]), sep='\n')
            cls.display_initial_menu()
        elif chose_option == '7':
            quit()

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
        UserOptions.get_user_option()

    @classmethod
    def get_user_option(cls) -> object:
        """
        Gets the validated option from the client
        """
        return cls.user_options(
            Validations.validation_user_input('OPTION NUMBER: ', ['1', '2', '3', '4', '5', '6', '7'], True))


if __name__ == '__main__':
    print('\n\n     --------  Welcome!  --------\n\n'.upper())
    UserOptions.display_initial_menu()

