# GUI Imports
import sys
from PyQt6.QtCore import Qt
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QMainWindow,
    QTextEdit
)
from functools import partial

# Global
import os
import pandas as pd
import numpy as np
from tqdm.auto import tqdm
import shutil
from natsort import natsort_keygen
import datetime as dt
from IPython.display import clear_output
import time

# Custom
from file_manager import File_Manager
from df_manager import DF_Manager


class WindowSort(QMainWindow):
    def __init__(self):
        super(WindowSort, self).__init__()
        uic.loadUi("ui\\testing.ui", self)
        self.setWindowTitle("ComicSort")

        # Global Variables
        self.PUBLISHER_LIST = ['Abstract Studio',
                               'Archaia',
                               'Archie Comics',
                               'Aspen MLT',
                               'Avatar Press',
                               'Boom! Studios',
                               'Dark Horse Comics',
                               'DC Comics',
                               'Dynamite Entertainment',
                               'IDW Publishing',
                               'Image',
                               'Marvel',
                               'Top Cow',
                               'Vertigo',
                               'Wildstorm',
                               'Zenescope Entertainment']
        self.PL_LOWER = [p.lower().replace("!", "") for p in self.PUBLISHER_LIST]
        self.folder_tree = []
        self.file_manager = File_Manager()
        self.df = pd.DataFrame()
        self.df_import = pd.DataFrame()
        self.df_global = pd.DataFrame()

        # GUI entry variables
        self.HOME_PATH = "D:\-=_Comics_=-\__New Stuff"
        self.le_FolderPath.setText(self.HOME_PATH)

        # Assign slots
        self.btn_Scan.clicked.connect(self.create_tree)
        self.btn_Scan.clicked.connect(self.read_files)

        self.btn_DataCheck.clicked.connect(self.data_check)

        self.btn_CreateMove.clicked.connect(self.create_move_list)

        self.btn_MoveFiles.clicked.connect(self.move_files)

    # def print_smtg(self):
    # self.te_Log.setPlainText("Hello World")
    # self.te_Log.append(self.folder_text)

    def create_tree(self):
        """Creates a list of all subfolders that contain files"""
        self.HOME_PATH = self.le_FolderPath.text()

        for (path, dirs, files) in os.walk(self.HOME_PATH, topdown=True):
            if 'Thumbs.db' in files:
                files.remove('Thumbs.db')
                os.remove(f"{path}\\Thumbs.db")
            if 'covers.db' in files:
                files.remove('covers.db')
                os.remove(f"{path}\\covers.db")
            if len(files) > 0:
                self.folder_tree.append((path, files))

    def read_files(self):
        """
        Open comic file  and retrieve metadata
        File Check to make sure they are readable and no errors
        """

        total_folders = len(self.folder_tree)
        self.lbl_TotalFolders_enum.setText(str(total_folders))
        current_folder = 0
        time_start = time.time()

        for folder in self.folder_tree:
            directory = folder[0]
            files = folder[1]
            total_files = len(files)
            self.lbl_TotalFiles_enum.setText(str(total_files))
            current_file = 1

            for file in files:
                time_now = str(dt.timedelta(seconds=(time.time() - time_start)))

                self.pb_Scan.setValue(int((current_file / total_files) * 100))
                self.lbl_Status.setText(f"{time_now} - {file}")

                full_path = f"{directory}\{file}"
                # print(full_path)
                if file.lower().endswith(".cbr") or file.lower().endswith(".cbz"):
                    self.file_manager.parse_file(full_path, file)
                else:
                    print("Not CBR/CBZ - ", full_path)

                current_file += 1
            current_folder += 1
        self.te_Log.append(self.file_manager.return_errors())

        # Convert list of dictionaries to pandas dataframe for processing
        if self.file_manager.ERROR_COUNT == 0:
            self.df = pd.DataFrame(self.file_manager.FILE_LIST)
            self.df.to_csv('file_list.csv')
            self.te_Log.append("========================")
            self.te_Log.append("Ready for data check.")
        else:
            self.te_Log.append("========================")
            self.te_Log.append("Fix problem files and re-import.")

    def data_check(self):
        """Corrects and checks imported data for correct entries"""

        df = self.df

        self.te_Log.setPlainText("")

        df.Series = df.Series.str.strip()
        # Checking Volume numbers
        df.Volume.fillna(value=0, inplace=True)
        # Fixing issue number caveats
        df['Number'].replace('½', .5, inplace=True)
        df['Number'].replace('1½', .5, inplace=True)
        df['Number'].replace('∞', 999, inplace=True)
        df['Number'].replace('Omega', 1, inplace=True)
        # Fixes issue numbers like "10AU" or "25.BEY"
        df['Number'] = df['Number'].astype(str)
        for i in range(len(df['Number'])):
            n_string = df.iloc[i]['Number']

            l_int, l_str = "", ""
            for l in n_string:
                if not l.isalpha():
                    l_int += l
                elif l.isalpha():
                    l_str += l
            if len(l_str) > 0:
                if l_int[-1] == ".":
                    l_int += "1"
                else:
                    l_int += ".1"
            df.at[i, 'Number'] = l_int

        self.te_Log.append("==================Debug Check===================")
        try:
            df['Volume'] = df['Volume'].astype(int)
            self.te_Log.append("Passed - Volumes to int")
            self.chk_Volumes.setChecked(True)
        except Exception as e:
            self.te_Log.append("Failed - Volumes to int")
            self.te_Log.append(f"Volume Error - {e}")
            self.chk_Volumes.setChecked(False)

        try:
            df['Number'] = df['Number'].astype(float)
            self.te_Log.append("Passed - Numbers to float")
            self.chk_Numbers.setChecked(True)
        except Exception as e:
            self.te_Log.append("Failed - Numbers to float")
            self.te_Log.append(f'Number Error - {e}')
            self.chk_Numbers.setChecked(False)

        try:
            df['Year'] = df['Year'].astype(int)
            self.te_Log.append("Passed - Years to int")
            self.chk_Years.setChecked(True)
        except Exception as e:
            self.te_Log.append("Failed - Years to int")
            self.te_Log.append(f'Year Error - {e}')
            self.chk_Years.setChecked(False)

        try:
            df['Month'] = df['Month'].astype(int)
            self.te_Log.append("Passed - Months to int")
            self.chk_Months.setChecked(True)
        except Exception as e:
            self.te_Log.append("Failed - Months to int")
            self.te_Log.append(f'Month Error - {e}')
            self.chk_Months.setChecked(False)

        try:
            # df['Day'].replace(np.NaN, 1, inplace=True)
            df['Day'] = df['Day'].astype(int)
            self.te_Log.append("Passed - Days to int")
            self.chk_Days.setChecked(True)
        except Exception as e:
            self.te_Log.append("Failed - Days to int")
            self.te_Log.append(f'Day Error - {e}')
            self.chk_Days.setChecked(False)
            debug_day = df[df['Day'].isna()]
            if not debug_day.empty:
                self.te_Log.append("========Days with NaN values===========")
                for row in debug_day.itertuples():
                    self.te_Log.append(f"{row.Index} {row.Series} {row.Number} - {row.FilePath}")

        # Fixes capitalization errors in publisher names
        publishers = df.Publisher.unique().tolist()
        for p in publishers:
            p = p.lower().replace("!", "")
            if p in self.PL_LOWER:
                # find index
                p_index = self.PL_LOWER.index(p)
                # replace all occurances in df with index in publisher list
                df = df.replace(str(p), str(self.PUBLISHER_LIST[p_index]))
        # Fix Publisher Names
        df['Publisher'].replace("/", '&', regex=True, inplace=True)
        df['Publisher'].replace("BOOM! Studios", 'Boom! Studios', regex=True, inplace=True)
        # DC Imprints
        df['Publisher'].replace('I.W. Publishing', 'DC Comics', inplace=True)
        # Marvel Imprints
        df['Publisher'].replace('Marvel Digital Comics Unlimited', 'Marvel', inplace=True)
        df['Publisher'].replace('Marvel Knights', 'Marvel', inplace=True)
        df['Publisher'].replace('Max', 'Marvel', inplace=True)
        df['Publisher'].replace('Max Comics', 'Marvel', inplace=True)
        df['Publisher'].replace('Timely', 'Marvel', inplace=True)
        df['Publisher'].replace('Marvel Soleil', 'Marvel', inplace=True)
        df['Publisher'].replace('Marvel UK', 'Marvel', inplace=True)
        df['Publisher'].replace('Epic', 'Marvel', inplace=True)
        df['Publisher'].replace('Scholastic Book Services', 'Marvel', inplace=True)
        # Image Imprints
        df['Publisher'].replace('Shadowline', 'Image', inplace=True)
        df['Publisher'].replace('Skybound', 'Image', inplace=True)
        publishers = df.Publisher.unique().tolist()
        pub_big = []
        pub_misc = []
        for p in publishers:
            if p in self.PUBLISHER_LIST:
                pub_big.append(p)
            else:
                pub_misc.append(p)
        self.te_Log.append('=======Publisher List=========')
        self.te_Log.append(f"Big: {[*pub_big]}")
        self.te_Log.append(f"Misc: {[*pub_misc]}")

        self.te_Log.append('========Volume List========')
        self.te_Log.append(str(df['Volume'].unique().tolist()))

        debug_volume = df[df['Volume'] > 10]
        if not debug_volume.empty:
            self.te_Log.append("=========Files with problem Volumes=========")
            for row in debug_volume.itertuples():
                self.te_Log.append(row.FilePath)

        self.df = df

        if (self.chk_Volumes.isChecked()
                and self.chk_Numbers.isChecked()
                and self.chk_Years.isChecked()
                and self.chk_Months.isChecked()
                and self.chk_Days.isChecked()):
            self.df_import = self.df
            # Import permanent db and merge with imported for processing
            self.df_global = pd.read_csv('comic_list.csv', index_col=0,
                                         dtype={'Publisher': str,
                                                'Series': str,
                                                'Volume': int,
                                                'Number': float,
                                                'Year': int,
                                                'Month': int,
                                                'Day': int,
                                                'FilePath': str,
                                                'NewPath': str})
            self.df_global = pd.concat([self.df_import, self.df_global], ignore_index=True)
            self.df_global.sort_values(
                by=['Publisher', 'Series', 'Volume', 'Number', 'Year', 'Month', 'Day'],
                ascending=[True, True, True, True, True, True, True],
                inplace=True,
                key=natsort_keygen()
            )
            self.df_global.reset_index(drop=True, inplace=True)

            self.te_Log.append("========================")
            self.te_Log.append("Dataframes created, proceed to move list.")

    def create_move_list(self):
        """creates new file paths for moving inside df_global"""
        self.te_Log.setPlainText("")
        # Dictionary is for sorting and debugging
        root_dict = {}
        total_publishers = self.df_import.Publisher.unique().tolist()
        for p in total_publishers:
            root_dict[p] = {}

        title_dict = {}

        titles = self.df_import.Series.unique()

        # For testing
        # titles = ['Deadpool & The Mercs For Money']

        for title in titles:
            # For creating folder names.  Removing special characters
            safe_title = title.replace(":", " -")
            safe_title = safe_title.replace('/', '-')
            safe_title = safe_title.replace('?', '')
            safe_title = safe_title.replace('"', '')
            safe_title = safe_title.replace('*', '')

            title_dict[safe_title] = {}

            # Filter by series
            cond_series = (self.df_global['Series'] == title)
            df_by_series = self.df_global[cond_series]

            # Creates list of unique publishers
            number_publishers = df_by_series.Publisher.unique().tolist()
            # catch for series with same name, multiple publishers.
            for p in number_publishers:
                if p not in root_dict:
                    root_dict[p] = {}

            for publisher in number_publishers:

                # referencing inside df
                folder_dict = {}
                # Filter by publisher
                cond_publisher = (self.df_global['Publisher'] == publisher)
                df_by_publisher = self.df_global[cond_publisher & cond_series].copy()
                df_by_publisher.sort_values(by=['Year', 'Month', 'Day'], ascending=[True, True, True], inplace=True,
                                            key=natsort_keygen())

                # Sorting for smaller publishers
                if publisher not in self.PUBLISHER_LIST:
                    publisher_path = f"Misc\\{publisher}"
                else:
                    publisher_path = publisher

                # Check Publisher path for pre-existing folders
                target_path = f"D:\\-=_Comics_=-\\{publisher_path}\\"

                DF = DF_Manager(df_by_publisher)
                target_folders, two_1_list = DF.return_target_folders()
                # print(target_folders)

                # Create new folders and create dictionary reference for Year
                for y in target_folders:
                    if y[0] in (entry for entry in two_1_list):
                        folder_index = f"{y[0]}-{y[1]}"
                    else:
                        folder_index = y[0]
                    folder_dict[folder_index] = []

                # Number of Volumes Check
                volumes = df_by_publisher['Volume'].unique()

                for volume in volumes:
                    # Filter by volume
                    cond_volume = (self.df_global['Volume'] == volume)
                    df_by_volume = self.df_global[cond_volume & cond_publisher & cond_series].copy()
                    df_by_volume.sort_values(by=['Year', 'Number'], ascending=[True, True], inplace=True,
                                             key=natsort_keygen())

                    years = df_by_volume['Year'].unique()

                    for year in years:
                        cond_year = (self.df_global['Year'] == year)
                        df_by_year = self.df_global[cond_year & cond_volume & cond_publisher & cond_series].copy()

                        # Problem Checker
                        for row in df_by_year.itertuples():
                            try:
                                issue_date = dt.datetime(row.Year, row.Month, row.Day)
                            except ValueError:
                                self.te_Log.append(f"ValueError - {title} {row.Number} - {row.Year}-{row.Month}-{row.Day}")
                                break

                            issue_year = row.Year
                            issue_month = row.Month
                            issue_day = row.Day
                            issue_num = row.Number
                            save_year = 0
                            mod_0 = .85
                            pre_issues = (issue_num == 0 or issue_num == 1.5 or issue_num == .5 or issue_num == .1 or issue_num == -1)

                            # Sort issues by Year-Month-Day
                            for i in range(len(target_folders)):
                                # Check for two issue 1 in same year
                                if target_folders[i][0] in (entry for entry in two_1_list):
                                    tf_index = f"{target_folders[i][0]}-{target_folders[i][1]}"
                                    try:
                                        tf_index_next = f"{target_folders[i + 1][0]}-{target_folders[i + 1][1]}"
                                    except IndexError:
                                        tf_index_next = "0-0"
                                else:
                                    tf_index = target_folders[i][0]
                                    try:
                                        tf_index_next = target_folders[i + 1][0]
                                    except IndexError:
                                        tf_index_next = 0

                                prev_date = dt.datetime(target_folders[i][0], target_folders[i][1],
                                                        target_folders[i][2])
                                if i == len(target_folders) - 1:
                                    if pre_issues and (prev_date - issue_date).days < 365 * mod_0:
                                        save_year = tf_index
                                    elif issue_date >= prev_date:
                                        save_year = tf_index
                                else:
                                    # Standard sort
                                    next_date = dt.datetime(target_folders[i + 1][0], target_folders[i + 1][1],
                                                            target_folders[i + 1][2])

                                    if pre_issues and (next_date - issue_date).days < 365 * mod_0:
                                        # bumps up save year to the next entry if it's released less than 10 months before issue 1
                                        save_year = tf_index_next
                                    elif pre_issues and (prev_date - issue_date).days < 365 * mod_0:
                                        # bumps up save year to the next entry if it's released less than 10 months before issue 1
                                        save_year = tf_index
                                    elif prev_date <= issue_date < next_date:
                                        save_year = tf_index

                            # Add to dictionary
                            try:
                                folder_dict[save_year].append(issue_num)
                            except KeyError:
                                self.te_Log.append(f"Key Error - {row.Index} {title} {issue_num} - SaveYear {save_year} : IssueYear {issue_year} - {next_date} - {issue_date}")
                                break

                            # Saves the new correct path to df
                            move_path = f"D:\\-=_Comics_=-\\{publisher_path}\\{safe_title} ({save_year})\\"
                            self.df_global.at[row.Index, 'NewPath'] = move_path

                title_dict[safe_title].update(folder_dict)
                root_dict[publisher].update(title_dict)

        self.chk_MoveClear.setChecked(True)
        self.te_Log.append("====================")
        self.te_Log.append("Move list created successfully!  Next button will move files!")

    def move_files(self):
        """Moves comic files based off move list and deletes any empty folders in HOME_PATH"""
        self.te_Log.setPlainText("")

        count_preexist = 0
        count_moved = 0
        dup_list = []
        dup_files = []

        df_move = self.df_global[self.df_global.Series.isin(self.df_import['Series'].unique().tolist())]

        for row in tqdm(df_move.itertuples()):
            move_folder = row.NewPath
            _, file_name = os.path.split(row.FilePath)
            check_file = move_folder + file_name

            if row.FilePath != check_file:
                if not os.path.exists(move_folder):
                    os.makedirs(move_folder)

                if os.path.exists(check_file):
                    # print(f"Pre-Exists: {move_folder}{file_name} ")
                    dup_list.append(row.index)
                    dup_files.append(row.FilePath)
                    count_preexist += 1
                else:
                    try:
                        shutil.move(row.FilePath, check_file)
                        count_moved += 1
                        self.df_global.at[row.Index, 'FilePath'] = check_file
                    except:
                        print(f'Error: {file_name} - {move_folder}')

        # Not working, caused an error
        # self.df_global = self.df_global.drop(dup_list, axis='index')
        self.df_global.to_csv('comic_list.csv')

        for f in dup_files:
            os.remove(f)

        self.te_Log.append(f"Total:  {df_move.size} -  Unmoved: {count_preexist}   -   Moved: {count_moved}   -  Duplicates: {len(dup_files)}")
        self.te_Log.append("=====================================")

        # Delete old empty folders
        end_tree = []
        count_deleted = 0
        # Creates a list of all subfolders that are empty
        for (path, dirs, files) in os.walk(self.HOME_PATH, topdown=True):
            if len(files) == 0 and len(dirs) == 0:
                end_tree.append((path, len(dirs)))

        end_tree = sorted(end_tree, key=lambda x: x[1])

        for folder in end_tree:
            try:
                os.rmdir(folder[0])
                count_deleted += 1
            except:
                self.te_Log.append(f"{folder[0]} could not be deleted.")
        self.te_Log.append(f"Deleted Folders: {count_deleted}")

        self.te_Log.append("================================")
        self.te_Log.append("All done!")


