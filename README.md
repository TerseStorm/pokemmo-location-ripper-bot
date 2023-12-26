# pokemmo-location-ripper
A commandline tool to quickly compile bulk location data for PokeMMO.

## Usage
For a list of all available arguments, use
 
  `$ py PLR.py --help`

For general usage, use

  `$ py PLR.py -A OPTION`
Where -A is the argument, and OPTION is the corresponding option to said argument.

Use more arguments when running to get more complex filters.

If using the pre-compiled .exe file, replace `py PLR.py` with `PLR.exe`

If using argument options consisting of 2 or more words, enclose it in quotation marks. Ex. `Viridian Forest` should be `"Viridian Forest"`.

If filtering by Route 1-18, filter by Kanto or Unova as well, to avoid mixed results.

## Examples
Getting all Hordes in Sinnoh

  `$ py PLR.py --region Sinnoh --rarity Horde`


Getting all Lure encounters in Johto

  `$ py PLR.py --region Johto --rarity Lure`


Getting all encounters in Viridian Forest

  `$ py PLR.py --location "Viridian Forest"`


Getting all Tentacruel locations with a minimum level of 40

  `$ py PLR.py --name Tentacruel --minlevel`


Getting all Surfing encounters in Undella Bay

  `$ py PLR.py --location "Undella Bay" --type Water`


## Requirements
Python 3.10+, which can be downloaded [here](https://www.python.org/downloads/).

