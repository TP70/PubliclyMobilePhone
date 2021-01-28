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
    def get_lease_years_where_25(cls):
        """
        output: prints all data rows where the lease years
        is equal to 25
        """
        return [x for x in [line for line in ReadFile.read_csv() if line[9] == 25]]

    @classmethod
    def total_rent_where_lease_years_25(cls):
        """
        output: returns total rent as integer where
        lease years is 25
        """
        total_rent = 0
        for line in [line for line in ReadFile.read_csv() if line[9] == 25]:
            total_rent += line[-1]
        return total_rent

    @classmethod
    def get_rows_between_dates(cls):
        """
        output: answer for Q4, prints row info between date
        specified
        """
        date_list = [x for x in ReadFile.read_csv()[1:] if datetime(1999, 6, 1) < x[7] < datetime(2007, 8, 31)]
        for x in date_list:
            x[7] = x[7].strftime('%d/%m/%Y')
        return [x for x in date_list]

    @classmethod
    def get_unique_tenant_names(cls):  # good room for improvement
        """
        output: prints dictionary information for unique
        tenant names with instances as integer.
        """
        tenant_dict = {
            'Arqiva Services Ltd': 0,
            'Vodafone Ltd': 0,
            '02 (UK) Ltd': 0,
            'EE & Hutchinson 3G UK Ltd': 0,
            'Cornerstone Telecommunications Infrastructure': 0
        }
        for line in ReadFile.read_csv()[1:]:
            if 'arqiva' in line[6].lower().split():
                tenant_dict['Arqiva Services Ltd'] += 1
            elif 'vodafone' in line[6].lower().split():
                tenant_dict['Vodafone Ltd'] += 1
            elif 'o2' in line[6].lower().split():
                tenant_dict['02 (UK) Ltd'] += 1
            elif 'everything' in line[6].lower().split():
                tenant_dict['EE & Hutchinson 3G UK Ltd'] += 1
            elif 'cornerstone' in line[6].lower().split():
                tenant_dict['Cornerstone Telecommunications Infrastructure'] += 1

        for key, value in tenant_dict.items():
            print(f'Company: {key}, instances: {value}')


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
            DataManipulation.get_unique_tenant_names()
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


if __name__ == '__main__':
    print('\n\n     --------  Welcome!  --------\n\n'.upper())
    UserMenus.display_initial_menu()
    UserOptions.get_user_option()
