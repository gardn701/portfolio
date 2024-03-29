import xml.etree.ElementTree as ET
import rarfile
import zipfile
import pandas as pd

class File_Manager():

    def __init__(self):
        self.FILE_LIST = []
        self.ITEM_COUNT = 0
        self.ERROR_COUNT = 0
        self.ERROR_LOG = []

        self.xml_file = ""
        self.xml_found = False
        self.empty_entry = {}
        self.df_errors = pd.DataFrame()

        self.volume_number = 0
        self.month = None
        self.day = None




    def add_info(self, xml, file_path):
        """
        xml = zipfile/rarfile opened xml object
        file_path = str of file path

        REQUIRED: Series, Number, Year, Publisher
        OPTIONAL: Volume,
        """
        xml_tree = ET.parse(xml)
        xml_root = xml_tree.getroot()

        # Some series will have volume numbers, others will not
        try:
            self.volume_number = int(xml_root.find("Volume").text)
        except:
            self.volume_number = 0

        try:
            self.month = int(xml_root.find("Month").text)
        except:
            self.month = None

        try:
            self.day = int(xml_root.find("Day").text)
        except:
            self.day = None

        file_dict = {
            "Publisher": xml_root.find("Publisher").text,
            "Series": xml_root.find("Series").text,
            "Volume": self.volume_number,
            "Number": xml_root.find("Number").text,
            "Year": xml_root.find("Year").text,
            "Month": self.month,
            "Day": self.day,
            "FilePath": file_path}
        self.FILE_LIST.append(file_dict)

    def print_info(self, n=0):
        if n == 0:
            for line in self.FILE_LIST:
                print(line)
        else:
            for i in range(0, n):
                print(self.FILE_LIST[i])

    def volume(self, i=0):
        # Check for unrealistic volume #.  Return True if Volume # > 50.  False < 50.
        if self.FILE_LIST[i]['Volume'] > 50:
            return True
        else:
            return False
        
    def print_errors(self):
        """prints errors from importing to console log"""

        self.df_errors = pd.DataFrame(self.ERROR_LOG)
        self.df_errors.to_csv("error_log.csv")

        # prints errors found during xml scan #
        print("Number of import errors:   ", self.ERROR_COUNT)

        if self.ERROR_COUNT > 0:
            print("=========================================")
            print("Error Log")
            print("=========================================")

            for e_line in self.ERROR_LOG:
                print(e_line[1], " - ", e_line[0])

    def return_errors(self):
        """returns errors from importing as a string for GUI display"""

        self.df_errors = pd.DataFrame(self.ERROR_LOG)
        self.df_errors.to_csv("error_log.csv")

        # prints errors found during xml scan #
        error_text = f"Number of import errors:   {self.ERROR_COUNT}"

        if self.ERROR_COUNT > 0:
            error_text += "\n========================================="
            error_text += "\nError Log"
            error_text += "\n========================================="

            for e_line in self.ERROR_LOG:
                error_text += f"\n{e_line[1]} - {e_line[0]}"

        return error_text
        
    def add_error(self, file, msg):
        self.ERROR_COUNT += 1
        self.ERROR_LOG.append((file, msg))
    
    def parse_cbr(self, full_path, file):
        with rarfile.RarFile(full_path) as rf:
            for f in rf.infolist():
                if f.filename.endswith(".xml"):
                    xml_file = f.filename
                    self.xml_found = True

            if self.xml_found is False:
                self.add_error(file, "No XML")
                self.FILE_LIST.append(self.empty_entry)
            elif self.xml_found:
                with rf.open(xml_file) as xml:
                    self.add_info(xml, full_path)

                    if self.volume(self.ITEM_COUNT):
                        self.add_error(file, "Incorrect Volume Number (50+)")
    
    def parse_cbz(self, full_path, file):
        with zipfile.ZipFile(full_path) as zf:
            for f in zf.infolist():
                if f.filename.endswith(".xml"):
                    xml_file = f.filename
                    self.xml_found = True

            if self.xml_found is False:
                self.add_error(file, "No XML")
                self.FILE_LIST.append(self.empty_entry)
            elif self.xml_found:
                with zf.open(xml_file) as xml:
                    self.add_info(xml, full_path)

                    if self.volume(self.ITEM_COUNT):
                        self.add_error(file, "Incorrect Volume Number (50+)")
        
    def parse_file(self, full_path, file):
        self.xml_file = ""
        self.xml_found = False
        self.empty_entry = {
            "Publisher": "Error",
            "Series": file,
            "Volume": 0,
            "Number": 0,
            "Year": 0,
            "Month": 0,
            "Day": 0,
            "FilePath": full_path}
        # print(self.ITEM_COUNT, " - ", len(self.FILE_LIST), " - ", file)
        try:
            if file.lower().endswith(".cbr"):
                self.parse_cbr(full_path, file)
            elif file.lower().endswith(".cbz"):
                self.parse_cbz(full_path, file)
        except AttributeError:
            self.add_error(file, "Missing Metadata Field!")
            self.FILE_LIST.append(self.empty_entry)
        except rarfile.BadRarFile:
            self.add_error(file, "Bad RAR File")
            self.FILE_LIST.append(self.empty_entry)
        except zipfile.BadZipFile:
            self.add_error(file, "Bad ZIP File")
            self.FILE_LIST.append(self.empty_entry)
        except rarfile.NotRarFile:
            # elif str(e) == "Not a RAR file":
            try:
                self.parse_cbz(full_path, file)
            except AttributeError:
                self.add_error(file, "Missing Metadata Field!")
                self.FILE_LIST.append(self.empty_entry)
            except IndexError:
                self.add_error(file, "List Error?")
                self.FILE_LIST.append(self.empty_entry)
                # print(self.ITEM_COUNT)
                # print(self.FILE_LIST[self.ITEM_COUNT])
            except Exception as e:
                print(e, file)
                self.FILE_LIST.append(self.empty_entry)

   
        self.ITEM_COUNT += 1
        
        
        
        