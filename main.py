# CHECK PYTHON VERSION
import sys
if sys.version[0] != "3":
    print("Use Python 3 with 'python3'.")
    sys.exit(1)

import json
from .fill import Fill

__author__ = "Satshree Shrestha"
SEPARATOR = "-" * 60

if __name__ == "__main__":
    # BANNER
    print(SEPARATOR)
    print("Fill PDF Forms.")
    print(SEPARATOR)

    # FILE PATHS
    pdf_file = input("PDF File Path: ")
    output_pdf_file = input(
        "Output PDF File Path [leave empty to overwrite]: ")

    # INITIALIZE
    fill_pdf_form = Fill(pdf_file, output_pdf_file)
    fill_pdf_form.initialize_pdf()

    # PRINT OUT FORM FIELD KEYS
    print(SEPARATOR)
    print("The following are the form fields found.\n")
    for keys in fill_pdf_form.KEYS:
        print(keys)
    print(SEPARATOR)
    print("Fill up the 'data.json' file with above form fields to populate data and fill the form.")

    try:
        while True:
            # POPULATE DATA AND FILL PDF FORM
            print(SEPARATOR)
            input("Press Enter to continue once you fill up 'data.json' file.")

            # READ DATA
            try:
                data_json = open("data.json", "r")
                data = json.loads(data_json.read().rstrip())
                data_json.close()
            except FileNotFoundError:
                print("Cannot find 'data.json' file.")

            print(SEPARATOR)
            print("The following is the data,")
            for key, value in data.items():
                print(f"{key} = {value}")
            print(SEPARATOR)

            yesno = input(
                "Enter 'YES' to fill, 'NO' to edit data, 'STOP' to exit: ")
            if yesno.lower() == "yes":
                # FILL PDF FORM
                fill_pdf_form.populate_data(data)
                fill_pdf_form.fill_pdf_form()
                print(SEPARATOR)
                print(
                    f"PDF Form Filled. Check output at {fill_pdf_form.output_file}")
            elif yesno.lower() == "no":
                continue
            elif yesno.lower() == "stop":
                print(SEPARATOR)
                print("Bye Bye.")
                print(SEPARATOR)
                break
            else:
                print(SEPARATOR)
                print("Skipped.")
    except KeyboardInterrupt:
        print(SEPARATOR)
        print("Bye Bye.")
        print(SEPARATOR)
    except Exception as e:
        print(SEPARATOR)
        print("Error caught,")
        print(str(e))
        print(SEPARATOR)
