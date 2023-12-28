# pokemmo-location-ripper-bot
A Discord bot to quickly compile bulk location data for PokeMMO.

Despite forking this code, my code is no prettier than the original creator LOL


## Usage
### Dumping PokeMMO dex files
A pre-dumped `dump.zip` is included. This has been dumped on 2023-12-27 UTC. It's recommended to always dump your own dex files.

The program works by reading the Pokedex (dex) files dumped directly from PokeMMO.

To dump these files, go to
 > Settings -> Utilities -> Dump Moddable Resources -> Pokedex Data

This dumps the needed files as a .zip file to the `dump\resources` directory in PokeMMO's install directory (usually in `C:\\Program Files\PokeMMO`).

Create a folder called `dex_files`.

Extract `dump.zip` to this folder.


### Updating PokeMMO dex files
Whenever the Pokedex in PokeMMO gets updated, the dex files should also be updated to reflect this.

To do this, simply follow the steps from the section `Dumping PokeMMO dex files` but select "Replace All" when extracting.

Alternatively, if problems with this arises, simply delete the contents of the `dex_files` folder, and extract the newly dumped `dump.zip` to the folder again.


### Arguments
For a list of all available arguments, run
 
  `/location_finder --help` or `/location_finder -h`

For general usage, run

  `/location_finder -A OPTION`
  
Where `-A` is the argument, and `OPTION` is the corresponding option to said argument.

For argument-specific help, use

  `/location_finder -A help`

Where `-A` is the argument.

Use more arguments when running to get more complex filters.

If filtering by Route 1-18, filter by Kanto or Unova as well, to avoid mixed results.

## Examples
Getting all Hordes in Sinnoh

  `/location_finder --region Sinnoh --rarity Horde`


Getting all Lure encounters in Johto

  `/location_finder --region Johto --rarity Lure`


Getting all encounters in Viridian Forest

  `/location_finder --location Viridian Forest`


Getting all Tentacruel locations with a minimum level of 40

  `/location_finder --name Tentacruel --minlevel`


Getting all Surfing encounters in Undella Bay

  `/location_finder --location Undella Bay --type Water`


## Requirements
Python 3.10+, which can be downloaded [here](https://www.python.org/downloads/).

7-Zip or similar, which can be downloaded [here](https://www.7-zip.org/download.html)


## Reporting problems
Run the program with the argument `-logfile log` and send this file along with the command used to run the program, to me on Discord: `lyn1505`.



