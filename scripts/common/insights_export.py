from datetime import datetime
import os

from base import session
from tables import PprCleanAll
import xlsxwriter

# Settings
base_path = os.path.abspath(__file__ + "/../../../")
ref_month = datetime.today().strftime("%Y-%m")

if __name__ == "__main__":
    data = session.execute("SELECT * FROM insights").all()
    ref_month = datetime.today().strftime("%Y-%m")
    
    # Create the workbook
    workbook = xlsxwriter.Workbook(
        f"{base_path}/data/insights/InsightsExport_202102.xlsx"
        #f"{base_path}/data/raw/downloaded_at=2021-02-01/ppr-all.csv"
    )
    
    # Add a new worksheet
    worksheet = workbook.add_worksheet()
    worksheet.set_column("B:G", 12)

    ##print(data)
    
    # Add the table with all results in the newly created worksheet
    worksheet.add_table(
        "B3:G20",
        {
            "data": data,
            "columns": [
                {"header": "County"},
                {"header": "Number of Sales 3 month"},
                {"header": "Tot sales 3 months"},
                {"header": "Max sales 3 months"},
                {"header": "Min sales 3 months"},
                {"header": "Avg sales 3 months"},
            ],
        },
    )
    workbook.close()
    
    print("Data exported:",  f"{base_path}/data/insights/InsightsExport_202102.xlsx")