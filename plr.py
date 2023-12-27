import os
import sys
import json
import string


def GetHeaderString(header_keys) -> str:
    header_string = "name,"

    for key in header_keys:
        header_string += f"{key}"

        # If 'key' isn't the last header element, append ','
        if key != header_keys[len(header_keys)-1]:
            header_string += ","
        else:
            header_string += "\n" # Append new line for next entry
    
    return header_string


def ParseLocationData(file,
                      counter:int,
                      output_filename:str,
                      filter_region:str = None,
                      filter_rarity:str = None,
                      filter_min_level:int = None,
                      filter_max_level:int = None,
                      filter_type:str = None,
                      filter_location:str = None,
                      filter_name:str = None):
    '''
    Parses dumped PokeMMO dex location data from JSON files to an output file.
    '''
    # Load json file
    with open(file, 'r') as pokemon_json_file:
        json_data = json.load(pokemon_json_file)


    # Set data from JSON file
    name_data = json_data['name'] # Get name
    location_data = json_data['locations'] # Get locations


    # If no locations exists, return
    if len(location_data) == 0:
        return

 
    # Check if output file exists and create it if it doesn't
    if (os.path.isfile(output_filename) and (counter != 0)):
        output_file = open(output_filename, 'a')
    else:
        output_file = open(output_filename, 'w')


    # Setup header and location data strings
    header_string = None
    location_data_string = ""

    # Get header names (keys) as list
    header_keys = list(location_data[0].keys())


    # If this is the first entry, write header before writing data
    if counter == 0:
        # Get the header string
        header_string = GetHeaderString(header_keys)
        output_file.write(header_string) # Write header to file


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
            if value != location_data_list[len(location_data_list)-1]:
                location_data_string += ","
            else:
                location_data_string += "\n"
    
    # Print header and given location data
    #print(header_string)
    #print(location_data_string)

    output_file.write(location_data_string) # Write to output file
    
    output_file.close()



# Available short and long arguments
avail_args_short = ["-h",
                    "-o",
                    "-n",
                    "-re",
                    "-ra",
                    "-mi",
                    "-ma",
                    "-t",
                    "-l",
                    "-lf"]
avail_args_long = ["--help",
                   "--output",
                   "--name",
                   "--region",
                   "--rarity",
                   "--minlevel",
                   "--maxlevel",
                   "--type",
                   "--location",
                   "--logfile"]

print(f"For help and a list of all available arguments, use:\n$ py {sys.argv[0]} --help")

# Get the value of a commandline argument given the prefix
def GetValueOfArg(arg, arg_list):
    return arg_list[list.index(arg_list, arg) + 1]


# Print the help menu
def PrintHelpMenu(short_args:list, long_args:list):
    print(f"Usage:\n" + 
        f"$ py {sys.argv[0]} -A OPTION")
    print("")
    print("Where:\n" +
        "-A = Argument\n" +
        "OPTION = Option")
    print("")

    short_str = "Short"
    long_str = "Long"
    print(f"{short_str:<6} {long_str}")
    for i in range(len(short_args)):
        print(f"{short_args[i]:<6} {long_args[i]:<12}")

    sys.exit() # Quit program after listing the help


# Set filters for debugging
out_filename = None
filter_name = None
filter_region = None
filter_rarity = None
filter_min_level = None
filter_max_level = None
filter_type = None
filter_location = None
log_filename = None
logging = False

# Set the filters from given arguments
if "-h" in sys.argv or "--help" in sys.argv:
    PrintHelpMenu(avail_args_short, avail_args_long)
if "-o" in sys.argv or "--output" in sys.argv:
    try: # Get value depending on if short or long argument was used
        out_filename = GetValueOfArg("-o", sys.argv)
    except:
        out_filename = GetValueOfArg("--output", sys.argv)
    if ".txt" not in out_filename:
        out_filename += ".txt" # Append .txt if it doesn't exist
else: # Set output filename if it's not set via argument
    out_filename = "output.txt"
if "-n" in sys.argv or "--name" in sys.argv:
    try:
        filter_name = GetValueOfArg("-n", sys.argv)
    except:
        filter_name = GetValueOfArg("--name", sys.argv)
if "-re" in sys.argv or "--region" in sys.argv:
    try:
        filter_region = GetValueOfArg("-re", sys.argv)
    except:
        filter_region = GetValueOfArg("--region", sys.argv)
if "-ra" in sys.argv or "--rarity" in sys.argv:
    try:
        filter_rarity = GetValueOfArg("-ra", sys.argv)
    except:
        filter_rarity = GetValueOfArg("--rarity", sys.argv)
if "-mi" in sys.argv or "--minlevel" in sys.argv:
    try:
        filter_min_level = GetValueOfArg("-mi", sys.argv)
    except:
        filter_min_level = GetValueOfArg("--minlevel", sys.argv)
if "-ma" in sys.argv or "--maxlevel" in sys.argv:
    try:
        filter_max_level = GetValueOfArg("-ma", sys.argv)
    except:
        filter_max_level = GetValueOfArg("--maxlevel", sys.argv)
if "-t" in sys.argv or "--type" in sys.argv:
    try:
        filter_type = GetValueOfArg("-t", sys.argv)
    except:
        filter_type = GetValueOfArg("--type", sys.argv)
if "-l" in sys.argv or "--location" in sys.argv:
    try:
        filter_location = GetValueOfArg("-l", sys.argv)
    except:
        filter_location = GetValueOfArg("--location", sys.argv)
if "-lf" in sys.argv or "--logfile" in sys.argv:
    logging = True
    try:
        log_filename = GetValueOfArg("-lf", sys.argv)
    except:
        log_filename = GetValueOfArg("--logfile", sys.argv)
    if ".txt" not in out_filename:
        log_filename += ".log" # Append .log if it doesn't exist
else: # Set log filename if it's not set via argument
    log_filename = "output.log"


filters_list = [out_filename,
                filter_region,
                filter_rarity,
                filter_min_level,
                filter_max_level,
                filter_type,
                filter_location]

if len(sys.argv) < 2:
    PrintHelpMenu(avail_args_short, avail_args_long)

# Print filters for debugging
""" print(out_filename)
print(filter_region)
print(filter_rarity)
print(filter_min_level)
print(filter_max_level)
print(filter_type)
print(filter_location) """



""" # Region names
Kanto = "Kanto"
Johto = "Johto"
Hoenn = "Hoenn"
Sinnoh = "Sinnoh"
Unova = "Unova"

very_common = "Very Common"
common = "Common"
uncommon = "Uncommon"
rare = "Rare"
very_rare = "Very Rare"
lure = "Lure"
horde = "Horde"
special = "Special"
pheno = special # Common pseudonym """

dex_files_dir_name = "dex_files"

errorMsg = f"""Please put the dumped PokeMMO JSON PokeDex files into the newly created
'{dex_files_dir_name}' folder and run the script again."""

if logging:
    log_file = open(log_filename, 'w')

if logging:
    log_file.write("Running with the following arguments:\n")
    for i in range(1, 8):
        log_file.write(f"{avail_args_long[i]} : {filters_list[i-1]}\n")

    


# If directory doesn't exist, create it and tell user where to put files
if not os.path.isdir(dex_files_dir_name):
    if logging:
        log_file.write(f"{dex_files_dir_name} doesn't exist. Creating...\n")
    directory = os.path.join(os.getcwd() + '/', dex_files_dir_name)
    os.mkdir(directory)
    print(errorMsg)
    sys.exit()


directory = os.getcwd() + '/dex_files/info'


# Used by the ParseLocationData function
global_counter = 0

filesInDir = os.listdir(directory)

# If dir exists but has no files, tell user where to put files
if len(filesInDir) == 0:
    print(errorMsg)
    sys.exit()




# For each JSON file in directory, call ParseLocationData and increment counter
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    if logging:
        log_file.write(f"Currently parsing: {file}\n")
    if os.path.isfile(file):
        #print(f"Currently converting: {filename}")
        ParseLocationData(file,
                          global_counter,
                          output_filename=out_filename,
                          filter_name=filter_name,
                          filter_region=filter_region,
                          filter_rarity=filter_rarity,
                          filter_min_level=filter_min_level,
                          filter_max_level=filter_max_level,
                          filter_type=filter_type,
                          filter_location=filter_location)
    global_counter += 1



# Snippet to test parsing small samples
""" filename = "13.json"
f = os.path.join(directory, filename)
if os.path.isfile(f):
    print(f"Currently converting: {filename}")
    ParseLocationData(f, 1, filter_region=True, filter_region_name=Sinnoh) """
