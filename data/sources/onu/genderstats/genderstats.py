import os
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')


config = {
    "base_path": file_dir,
    "origin_language": "en",
    "io": {
        "header": 1,
        "encoding": 'latin1',
        "fns": {
            '46 - Share of female police officers_data.csv': 'one_save',
            "43 - Women’s share of government ministerial positions_data.csv": "split2",
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv": "split4",

            "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": "split4",
            "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": "split2",
            "5 - Proportion of employed who are contributing family workers  by sex_data.csv": "split4",

            "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": "one_save",
            "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": "split2",
            "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": "split2",

            "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv": "one_save",

        }
    },
    "preprocesser": {
        'fns': {
            '46 - Share of female police officers_data.csv': ['no_process'],
            "43 - Women’s share of government ministerial positions_data.csv":  ["no_process"],
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv":  ["no_process"],
            "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": ["get_wm_onu", "diffFH"],
            "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": ["get_wm_onu", "diffFH"],
            "5 - Proportion of employed who are contributing family workers  by sex_data.csv": ["get_wm_onu", "diffFH"],
            "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": ["get_wm_onu_age", "diffFH"],
            "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": ["get_wm_onu_age", "diffFH"],
            "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": ["get_wm_onu_age", "diffFH"],
            "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv":  ["get_wm_onu_gender_wages_gap", "percRel100"],

        },
        'rename': {
            'country': 'Country',
            'year': 'Year',
            'indicator': 'Indicator Name',
            'value': 'Value'
        },
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            "43 - Women’s share of government ministerial positions_data.csv": 2010,
            '46 - Share of female police officers_data.csv': 2015,
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv": 2010,
            "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": 2010,
            "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": 2010,
            "5 - Proportion of employed who are contributing family workers  by sex_data.csv": 2010,
            "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": 2014,
            "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": 2013,
            "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": 2010,
            "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv": 2014,
        }
    },
    "mapper": {
        'fns': {
            '46 - Share of female police officers_data.csv': 'proportion1',
            "43 - Women’s share of government ministerial positions_data.csv": "proportion100",
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv": "proportion100",
            "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": "diffFH_20",
            "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": "diffFH_1",
            "5 - Proportion of employed who are contributing family workers  by sex_data.csv": "diffFH_10",
            "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": "diffFH_hours_4",
            "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": "diffFH_hours_4",
            "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": "diffFH_hours_1",
            "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv": "percRel100_30",
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            '46 - Share of female police officers_data.csv': 'percX100',
            "43 - Women’s share of government ministerial positions_data.csv": "perc",
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv": "perc",
            "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": "diff_pp",
            "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": "diff_hours",
            "5 - Proportion of employed who are contributing family workers  by sex_data.csv": "diff_pp",
            "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": "diff_hours",
            "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": "diff_hours",
            "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": "diff_hours",
            "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv": "diff_perc",
        },
    },
    "sorter": {
        'fns': {
            '46 - Share of female police officers_data.csv': 'none',
            "43 - Women’s share of government ministerial positions_data.csv": "none",
            "25 - Share of female science  technology  engineering and mathematics graduates at tertiary level_data.csv": "none",
            "11 - Proportion of adults (15 years and older) with an account at a bank or other financial institution or with a mobile-money-service provider  by sex_data.csv": "none",
            "2 - Average number of hours spent on total work combined (total work burden)  by sex_data.csv": "none",
            "5 - Proportion of employed who are contributing family workers  by sex_data.csv": "none",
            "1a - Average number of hours spent on domestic chores and care work  by sex  age and location_data.csv": "none",
            "1b - Average number of hours spent on unpaid domestic chores  by sex  age and location_data.csv": "none",
            "1c - Average number of hours spent on unpaid care work  by sex  age and location_data.csv": "none",
            "13 - Gender gap in wages  by occupation  age and persons with disabilities_data.csv": "country_date_indicator",
        }
    },
}

Processer(config).process()
