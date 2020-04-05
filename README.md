# opui

## Installation

- Clone the repository `git clone git@github.com:ceyhunkerti/opui.git`
- Copy the folder under desired place
- Navigate to folder `cd /path/to/opui`
- Create a virtual environment with `virtualenv env` or `python3 -m venv env`
- Activate virtualenvironment `. env/bin/activate`
- Install requirements `pip install -r requirements.txt`
- Modify the contents if `opui.sh` at will and make it executable `chmod +x opui.sh`

## Data

- Place the data under the data folder. `xlsx` is the current format. Modify the code if you want other formats.
- File name example `AEDAS.xlsx`, `BEDAS.xlsx`, etc.
- Sheet columns: `[Plan	Start	End	Duration]`
- Sheet names example: `[02042020,01042020, 31032020 ... ]`

## Running

- Run `./opui.sh`
- To run in background run it with `nohup ./opui.sh > opui.log &`