# ltpp

Small package for interacting with the NZTA LTPP database.

**Currently only tested on Ubuntu 18.04 running on WSL**

## Installation

First clone the [pandas_access](https://github.com/johnbullnz/pandas_access) package and install using `pip install -e .`

Then clone this repository and install using `pip install -e .`


## Configuration

Move the `.ltpp.ini` file to your home directory ("~" on Ubuntu) and update `database_path = ` to point to your local copy of the LTPP database.

## Usage

`import ltpp` - loads the database tables into seperate Pandas DataFrame objects at import.

`ltpp.tables.names()` - lists all tables.

`ltpp.tables.rutting_50m` - example of DataFrame containing the 50m rutting data.

`ltpp.tables["rutting_50m"]` - alternative method for accessing table data.
