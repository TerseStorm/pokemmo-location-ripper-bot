import os
import sys
import json
import string


class Converter:
    def __init__(self, arguments):
        self.pokeArgs = arguments
        self.global_counter = 0
        self.filter_name = None
        self.filter_region = None
        self.filter_rarity = None
        self.filter_min_level = None
        self.filter_max_level = None
        self.filter_type = None
        self.filter_location = None
        self.log_filename = None
        self.logging = False
        
        self.directory = os.getcwd() + '/dex_files'
        self.avail_args_short = ["-h",
                                 "-o",
                                 "-n",
                                 "-re",
                                 "-ra",
                                 "-mi",
                                 "-ma",
                                 "-t",
                                 "-l",
                                 "-lf"]
        self.avail_args_long = ["--help",
                                "--output",
                                "--name",
                                "--region",
                                "--rarity",
                                "--minlevel",
                                "--maxlevel",
                                "--type",
                                "--location",
                                "--logfile"]

    def validateArgs(self):
        if (self.pokeArgs[0] not in self.avail_args_short and self.pokeArgs[0] not in self.avail_args_long) or (self.pokeArgs[2] not in self.avail_args_short and self.pokeArgs[2] not in self.avail_args_long) or (self.pokeArgs[4] not in self.avail_args_short and self.pokeArgs[4] not in self.avail_args_long):
            return f"Make sure the 'command' argument is one of these: {self.avail_args_short} or {self.avail_args_long}"
        else:
            return "valid"

    def filesInDir(self):
        filesInDir = os.listdir(self.directory)

        # If dir exists but has no files, tell user where to put files
        if len(filesInDir) == 0:
            # print(errorMsg)
            sys.exit()

    def GetHeaderString(self, header_keys) -> str:
        header_string = "name,"

        for key in header_keys:
            header_string += f"{key}"

            # If 'key' isn't the last header element, append ','
            if key != header_keys[len(header_keys) - 1]:
                header_string += ","
            else:
                header_string += "\n"  # Append new line for next entry

        return header_string

    def ParseLocationData(self, file,
                          counter: int,
                          filter_region: str = None,
                          filter_rarity: str = None,
                          filter_min_level: int = None,
                          filter_max_level: int = None,
                          filter_type: str = None,
                          filter_location: str = None,
                          filter_name: str = None):
        '''
        Parses dumped PokeMMO dex location data from JSON files to an output file.
        '''
        # Load json file
        with open(file, 'r') as pokemon_json_file:
            json_data = json.load(pokemon_json_file)

        # Set data from JSON file
        name_data = json_data['name']  # Get name
        location_data = json_data['locations']  # Get locations

        # If no locations exists, return
        if len(location_data) == 0:
            return

        # Setup header and location data strings
        header_string = None
        location_data_string = ""

        # Get header names (keys) as list
        header_keys = list(location_data[0].keys())

        # If this is the first entry, write header before writing data
        if counter == 0:
            # Get the header string
            header_string = self.GetHeaderString(header_keys)
            location_data_string += header_string

        # For each location entry
        for i in range(len(location_data)):
            # Get location names (values) as list
            location_data_list = list(location_data[i].values())
            # Filter indexes
            indexOfType = header_keys.index('type')
            indexOfRegion = header_keys.index('region_name')
            indexOfLocation = header_keys.index('location')
            indexOfMinLevel = header_keys.index('min_level')
            indexOfMaxLevel = header_keys.index('max_level')
            indexOfRarity = header_keys.index('rarity')

            # Filters -> Yandere dev simulator
            if ((filter_name != None) and
                    name_data != filter_name):
                continue

            if ((filter_type != None) and
                    (location_data_list[indexOfType] != filter_type)):
                continue

            if ((filter_region != None) and
                    (location_data_list[indexOfRegion] != filter_region)):
                continue

            if ((filter_location != None) and
                    (location_data_list[indexOfLocation] != filter_location) and
                    (location_data_list[indexOfLocation] != filter_location.upper()) and
                    (location_data_list[indexOfLocation] != string.capwords(filter_location))):
                continue

            if ((filter_min_level != None) and
                    (location_data_list[indexOfMinLevel] != filter_min_level)):
                continue

            if ((filter_max_level != None) and
                    (location_data_list[indexOfMaxLevel] != filter_max_level)):
                continue

            if ((filter_rarity != None) and
                    (location_data_list[indexOfRarity] != filter_rarity)):
                continue

            # For each value in the location entry
            for value in location_data_list:
                # If value is the first element, append name to the string
                if value == location_data_list[0]:
                    location_data_string += f"{name_data},"

                location_data_string += f"{value}"

                # If value isn't the last element, append a seperator
                # else, append a new line
                if value != location_data_list[len(location_data_list) - 1]:
                    location_data_string += ","
                else:
                    location_data_string += "\n"

        # Print header and given location data
        # print(header_string)
        # print(location_data_string)

        return True, location_data_string

    # Get the value of a commandline argument given the prefix
    def GetValueOfArg(self, arg, arg_list):
        return arg_list[list.index(arg_list, arg) + 1]

    def setFilters(self):
        # Set filters for debugging
        out_filename = None



        # Set the filters from given arguments
        if "-h" in self.pokeArgs or "--help" in self.pokeArgs:
            self.PrintHelpMenu()
        if "-n" in self.pokeArgs or "--name" in self.pokeArgs:
            try:
                self.filter_name = self.GetValueOfArg("-n", self.pokeArgs)
            except:
                filter_name = self.GetValueOfArg("--name", self.pokeArgs)
        if "-re" in self.pokeArgs or "--region" in self.pokeArgs:
            try:
                self.filter_region = self.GetValueOfArg("-re", self.pokeArgs)
            except:
                self.filter_region = self.GetValueOfArg("--region", self.pokeArgs)
        if "-ra" in self.pokeArgs or "--rarity" in self.pokeArgs:
            try:
                self.filter_rarity = self.GetValueOfArg("-ra", self.pokeArgs)
            except:
                self.filter_rarity = self.GetValueOfArg("--rarity", self.pokeArgs)
        if "-mi" in self.pokeArgs or "--minlevel" in self.pokeArgs:
            try:
                self.filter_min_level = self.GetValueOfArg("-mi", self.pokeArgs)
            except:
                self.filter_min_level = self.GetValueOfArg("--minlevel", self.pokeArgs)
        if "-ma" in self.pokeArgs or "--maxlevel" in self.pokeArgs:
            try:
                self.filter_max_level = self.GetValueOfArg("-ma", self.pokeArgs)
            except:
                self.filter_max_level = self.GetValueOfArg("--maxlevel", self.pokeArgs)
        if "-t" in self.pokeArgs or "--type" in self.pokeArgs:
            try:
                self.filter_type = self.GetValueOfArg("-t", self.pokeArgs)
            except:
                self.filter_type = self.GetValueOfArg("--type", self.pokeArgs)
        if "-l" in self.pokeArgs or "--location" in self.pokeArgs:
            try:
                self.filter_location = self.GetValueOfArg("-l", self.pokeArgs)
            except:
                self.filter_location = self.GetValueOfArg("--location", self.pokeArgs)
        if "-lf" in self.pokeArgs or "--logfile" in self.pokeArgs:
            self.logging = True
            try:
                self.log_filename = self.GetValueOfArg("-lf", self.pokeArgs)
            except:
                self.log_filename = self.GetValueOfArg("--logfile", self.pokeArgs)
            if ".txt" not in out_filename:
                self.log_filename += ".log"  # Append .log if it doesn't exist
        else:  # Set log filename if it's not set via argument
            self.log_filename = "output.log"

        filters_list = [out_filename,
                        self.filter_region,
                        self.filter_rarity,
                        self.filter_min_level,
                        self.filter_max_level,
                        self.filter_type,
                        self.filter_location]

    def ParseAllLocationData(self):
        finalLocData = ""
        argsValidated = self.validateArgs()
        if argsValidated != 'valid':
            return argsValidated
        # For each JSON file in directory, call ParseLocationData and increment counter
        for filename in os.listdir(self.directory):
            file = os.path.join(self.directory, filename)
            if self.logging:
                log_file.write(f"Currently parsing: {file}\n")
            if os.path.isfile(file):
                # print(f"Currently converting: {filename}")
                loc_data = self.ParseLocationData(file,
                                       self.global_counter,
                                       filter_name=self.filter_name,
                                       filter_region=self.filter_region,
                                       filter_rarity=self.filter_rarity,
                                       filter_min_level=self.filter_min_level,
                                       filter_max_level=self.filter_max_level,
                                       filter_type=self.filter_type,
                                       filter_location=self.filter_location)
                if loc_data is not None and len(loc_data) > 1:
                    if len(loc_data[1]) > 0:
                        finalLocData += loc_data[1]
            self.global_counter += 1
        return finalLocData

    def helpSelector(self):
        helpSwitch = {"-h" : self.PrintHelpMenu,
                                 "-n" : self.nameHelp,
                                 "-re": self.regionHelp,
                                 "-ra": self.rarityHelp,
                                 "-mi": self.levelHelp,
                                 "-ma": self.levelHelp,
                                 "-t" : self.typeHelp,
                                 "-l" : self.locationHelp,
                                 "--help": self.PrintHelpMenu,
                                "--name": self.nameHelp,
                                "--region": self.regionHelp,
                                "--rarity": self.rarityHelp,
                                "--minlevel": self.levelHelp,
                                "--maxlevel": self.levelHelp,
                                "--type": self.typeHelp,
                                "--location": self.locationHelp}
        if "-h" in self.pokeArgs[0] or "-h" in self.pokeArgs[2] or "-h" in self.pokeArgs[4]:
            return self.PrintHelpMenu()
        else:
            if helpSwitch.get(self.pokeArgs[0]) is not None:
                return helpSwitch[self.pokeArgs[0]]()
            if helpSwitch.get(self.pokeArgs[2]) is not None:
                return helpSwitch[self.pokeArgs[2]]()
            if helpSwitch.get(self.pokeArgs[4]) is not None:
                return helpSwitch[self.pokeArgs[4]]()


    def nameHelp(self):
        return "make sure that the parameter is a valid Pokemon name."

    def regionHelp(self):
        return "make sure that the parameter is a valid region name."

    def levelHelp(self):
        return "make sure that the parameter is either a valid maximum or minimum level (1-100)"

    def typeHelp(self):
        return "make sure that the parameter is a valid encounter type in PokeMMO."

    def locationHelp(self):
        return "make sure that the parameter is a valid accessible location in PokeMMO."

    def rarityHelp(self):
        return "make sure that the parameter is a valid PokeMMO rarity."

    def PrintHelpMenu(self):
        return  f"Make sure the 'command' argument is one of these: {self.avail_args_short} or {self.avail_args_long} \nand that the 'parameter' argument is a valid corresponding value. for more info, enter in the command you want info on and the parameter 'help'."
