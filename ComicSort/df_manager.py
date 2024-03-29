import pandas as pd
from natsort import natsort_keygen
import datetime as dt


class DF_Manager():
    """ Input df filtered by series and publisher"""

    def __init__(self, df_in):
        self.df = df_in
        self.target_folders = []
        self.two_1_list = []
        self.title = self.df['Series'].unique()[0]


    def return_target_folders(self):
        """Returns 2 lists.  target_folders, two_1_list"""

        # Searches for issue 1's to create new folders
        cond_one = (self.df['Number'] == 1)
        df_ones = self.df[cond_one].copy()
        if not df_ones.empty:
            df_ones.sort_values(by=['Year', 'Month', 'Day'], ascending=[True, True, True], inplace=True,
                                key=natsort_keygen())

        # Two issue 1's in one year check
        self.two_1_list = []
        df_ones_count = df_ones.groupby(['Year']).size()
        for y in df_ones_count.index:
            if df_ones_count[y] > 1:
                if len(df_ones[df_ones['Year'] == y]['Month'].unique().tolist()) > 1:
                    self.two_1_list.append(y)

        # Basic issue 1 check
        if not df_ones.empty:
            for row in df_ones.itertuples():
                if row.Year not in (entry[0] for entry in self.target_folders):
                    if "Countdown" in self.title:
                        # The Countdown Series Exception
                        df_countdown = self.df.nsmallest(1, 'Year')
                        self.target_folders.append(
                            [df_countdown.Year.min(), df_countdown.Month.min(), df_countdown.Day.min()])
                    else:
                        self.target_folders.append([row.Year, row.Month, row.Day])
                elif row.Year in (entry for entry in self.two_1_list):
                    self.target_folders.append([row.Year, row.Month, row.Day])

        elif df_ones.empty:
            # No issue 1's found, creates only ONE folder
            df_no_ones = self.df.nsmallest(1, 'Year')
            self.target_folders.append([df_no_ones.Year.min(), df_no_ones.Month.min(), df_no_ones.Day.min()])

        # At least one folder created, but there was a previous series with no issue 1
        if self.target_folders:
            min_year = int(self.df['Year'].min())
            target_min_year = min(self.target_folders, key=lambda x: x[0])[0]
            if target_min_year != min_year:
                df_no_ones = self.df.nsmallest(1, 'Year')
                self.target_folders.append([df_no_ones.Year.min(), df_no_ones.Month.min(), df_no_ones.Day.min()])

        # # Duplicate check, to check for non-first folder series missing issue 1's
        # cond_two = (self.df['Number'] == 2)
        # df_twos = self.df[cond_two].copy()
        # if df_twos.shape[0] > 1:
        #     # if more than one issue 2 found
        #     if df_twos.Year.unique().size > 1 or df_twos.Month.unique().size > 1 or df_twos.Day.unique().size > 1:
        #         # if they have different dates Y-M-D
        #         for row in df_twos.itertuples():
        #             if (row.Year not in (entry[0] for entry in self.target_folders)
        #                     and row.Year - 1 not in (entry[0] for entry in self.target_folders)):
        #                 self.target_folders.append([row.Year, row.Month, row.Day])
        # cond_three = (self.df['Number'] == 3)
        # df_threes = self.df[cond_three].copy()
        # if df_threes.shape[0] > 1:
        #     # if more than one issue 2 found
        #     if df_threes.Year.unique().size > 1 or df_threes.Month.unique().size > 1 or df_threes.Day.unique().size > 1:
        #         # if they have different dates Y-M-D
        #         for row in df_threes.itertuples():
        #             if (row.Year not in (entry[0] for entry in self.target_folders)
        #                     and row.Year - 1 not in (entry[0] for entry in self.target_folders)):
        #                 self.target_folders.append([row.Year, row.Month, row.Day])
        self.target_folders.sort()

        return self.target_folders, self.two_1_list












    # UNUSED - Complete this code when needed
    # Creates a list of years for each folder matching series name
    # for (path, dirs, files) in os.walk(target_path, topdown=True):
    #     # Parse folder names
    #     folder = path.replace(target_path, '')
    #
    #     # Ignores root folder
    #     if len(folder) > 0:
    #         folder_name = folder[:-7]
    #         folder_year = folder[-5:-1]
    #
    #         # Unused - For scanning folders with existing files
    #         if folder_name == safe_title:
    #             target_tree.append((path,files))
    #
    #         # Records Folder year for sorting,
    #         if folder_year not in target_folders and folder_name == safe_title:
    #             target_folders.append(int(folder_year))





