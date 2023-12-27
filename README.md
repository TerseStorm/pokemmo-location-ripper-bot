# pokemmo-location-ripper
A commandline tool to quickly compile bulk location data for PokeMMO.

## Usage
### Dumping PokeMMO dex files
A pre-dumped `dump.zip` is included. This has been dumped on 2023-12-27 UTC. It's recommended to always dump your own dex files.

The program works by reading the Pokedex (dex) files dumped directly from PokeMMO.

To dump these files, go to
 > Settings -> Utilities -> Dump Moddable Resources -> Pokedex Data

This dumps the needed files as a .zip file to the `dump\resources` directory in PokeMMO's install directory (usually in `C:\\Program Files\PokeMMO`).

Run `plr` once, and it will create a new folder in its directory called `dex_files` where the `dump.zip` file should be copied to.

Extract `dump.zip` to this folder.


### Updating PokeMMO dex files
Whenever the Pokedex in PokeMMO gets updated, the dex files should also be updated to reflect this.

To do this, simply follow the steps from the section `Dumping PokeMMO dex files` but select "Replace All" when extracting.

Alternatively, if problems with this arises, simply delete the contents of the `dex_files` folder, and extract the newly dumped `dump.zip` to the folder again.


### Arguments
For a list of all available arguments, run
 
  `$ py plr.py --help`

For general usage, run

  `$ py plr.py -A OPTION`
  
Where `-A` is the argument, and `OPTION` is the corresponding option to said argument.

Use more arguments when running to get more complex filters.

If using the pre-compiled .exe file, replace `py plr.py` with `plr.exe`

If using argument options consisting of 2 or more words, enclose it in quotation marks. Ex. `Viridian Forest` should be `"Viridian Forest"`.

If filtering by Route 1-18, filter by Kanto or Unova as well, to avoid mixed results.

## Examples
Getting all Hordes in Sinnoh

  `$ py plr.py --region Sinnoh --rarity Horde`


Getting all Lure encounters in Johto

  `$ py plr.py --region Johto --rarity Lure`


Getting all encounters in Viridian Forest

  `$ py plr.py --location "Viridian Forest"`


Getting all Tentacruel locations with a minimum level of 40

  `$ py plr.py --name Tentacruel --minlevel`


Getting all Surfing encounters in Undella Bay

  `$ py plr.py --location "Undella Bay" --type Water`


## Requirements
Python 3.10+, which can be downloaded [here](https://www.python.org/downloads/).

7-Zip or similar, which can be downloaded [here](https://www.7-zip.org/download.html)
