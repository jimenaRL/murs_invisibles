import os
from murs_invisibles import Processer

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "en",
    "io": {
        "header": 1,
        "encoding": 'latin1',
        "fns": {
            '46 - Share of female police officers_data.csv': 'split4',
            "43 - Women’s share of government ministerial positions_data.csv": "split4",
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv": "split4",

            # "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": "split4",
            # "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": "split4",
            # "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": "split4",
            # "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": "split4",
            # "15 - Employment rate of persons aged 25-49 with a child under age 3 living in a household and with no children living in the household  by sex_data.csv": "split4",
            # "5 - Proportion of employed who are contributing family workers  by sex_data.csv": "split4",
            # "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": "split4",

            ###"7 - Percentage of firms owned by women  by size_data.csv": "split4",
            ###"24c - Gender parity index of the gross enrolment ratios in tertiary education_data.csv": "split4",
            ###"13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv": "split4",

        }
    },
    "preprocesser": {
        'fns': {
            '46 - Share of female police officers_data.csv': ['no_process'],
            "43 - Women’s share of government ministerial positions_data.csv":  ["no_process"],
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv":  ["no_process"],
            # "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv":  ["no_process"],
            # "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv":  ["no_process"],
            # "24c - Gender parity index of the gross enrolment ratios in tertiary education_data.csv":  ["no_process"],
            # "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv":  ["no_process"],
            # "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv":  ["no_process"],
            # "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv":  ["no_process"],
            # "15 - Employment rate of persons aged 25-49 with a child under age 3 living in a household and with no children living in the household  by sex_data.csv":  ["no_process"],
            # "5 - Proportion of employed who are contributing family workers  by sex_data.csv":  ["no_process"],
            # "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv":  ["no_process"],
            # "7 - Percentage of firms owned by women  by size_data.csv":  ["no_process"],
        },
        'rename': {
            'country': 'Country',
            'year': 'Year',
            'indicator': 'Indicator Name',
            'value': 'Value'
        },
    },
    "mapper": {
        'fns': {
            '46 - Share of female police officers_data.csv': 'proportion1',
            "43 - Women’s share of government ministerial positions_data.csv": "proportion100",
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv": "proportion100",
            # "7 - Percentage of firms owned by women  by size_data.csv": "proportion100",
            # "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": "",
            # "24c - Gender parity index of the gross enrolment ratios in tertiary education_data.csv": "",
            # "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": "",
            # "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": "",
            # "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": "",
            # "15 - Employment rate of persons aged 25-49 with a child under age 3 living in a household and with no children living in the household  by sex_data.csv": "",
            # "5 - Proportion of employed who are contributing family workers  by sex_data.csv": "",
            # "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": "",
            # "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv": "",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "43 - Women’s share of government ministerial positions_data.csv": 2010,
            '46 - Share of female police officers_data.csv': 2010,
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv": 2010,
            # "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": 2010,
            # "24c - Gender parity index of the gross enrolment ratios in tertiary education_data.csv": 2010,
            # "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": 2010,
            # "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": 2010,
            # "7 - Percentage of firms owned by women  by size_data.csv": 2010,
            # "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": 2010,
            # "15 - Employment rate of persons aged 25-49 with a child under age 3 living in a household and with no children living in the household  by sex_data.csv": 2010,
            # "5 - Proportion of employed who are contributing family workers  by sex_data.csv": 2010,
            # "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": 2010,
            # "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            '46 - Share of female police officers_data.csv': 'percX100',
            "43 - Women’s share of government ministerial positions_data.csv": "perc",
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv": "perc",
            # "7 - Percentage of firms owned by women  by size_data.csv": "perc",
            # "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": "",
            # "24c - Gender parity index of the gross enrolment ratios in tertiary education_data.csv": "",
            # "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": "",
            # "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": "",
            # "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": "",
            # "15 - Employment rate of persons aged 25-49 with a child under age 3 living in a household and with no children living in the household  by sex_data.csv": "",
            # "5 - Proportion of employed who are contributing family workers  by sex_data.csv": "",
            # "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": "",
            # "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv": "",
        },
    },
    "sorter": {
        'fns': {
            '46 - Share of female police officers_data.csv': 'none',
            "43 - Women’s share of government ministerial positions_data.csv": "none",
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv": "none",
            # "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": "none",
            # "24c - Gender parity index of the gross enrolment ratios in tertiary education_data.csv": "none",
            # "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": "none",
            # "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": "none",
            # "7 - Percentage of firms owned by women  by size_data.csv": "none",
            # "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": "none",
            # "15 - Employment rate of persons aged 25-49 with a child under age 3 living in a household and with no children living in the household  by sex_data.csv": "none",
            # "5 - Proportion of employed who are contributing family workers  by sex_data.csv": "none",
            # "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": "none",
            # "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv": "none",
        }
    },
}

Processer(config).process()
