from datetime import date, timedelta
from typing import Set
import csv


# Get all holydays from the official federal list from:
# https://www.data.gv.at/katalog/en/dataset/3deb9da7-8394-4797-9f32-5ca95281ba5b
# Note: yes this might look as not as sustainable as downloading from an API,
# but since the csv includes dates for the next 10 years I think we will be
# good. Also the webscraping will break much faster than this.
def holidays() -> Set[date]:
    with open("holiday.csv") as f:
        reader = csv.DictReader(f)

        holidays = {
            day
            for row in reader
            if row["TYP"] == "HF"
            and date.today()
            < (day := date.fromisoformat(row["DATUM"]))
            < (date.today() + timedelta(days=365))
        }

        return holidays
