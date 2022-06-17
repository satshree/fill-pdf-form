# Fill PDF Form
Fill PDF Forms with Python

# [Requirements](requirements.txt)

# Instructions
## To run with main.py 

- Install with script `install.sh` **(Only for first time)**

    ``` 
    >> bash install.sh
    ```

- Initialize with script `initialize.sh`

    ```
    >> bash initialize.sh
    ```

- Run `main.py`

    - Enter PDF path files.
    - All the available field names of PDF form will be listed out.
    - Only enter the required field data in `data.json` file.
    - Proceed to fill the PDF form.
    - Press `ctrl + C` to exit anytime.
    

    ```
    >> python main.py
    ------------------------------------------------------------
    Fill PDF Forms.
    ------------------------------------------------------------
    PDF File Path: path/to/pdf
    Output PDF File Path [leave empty to overwrite]: path/to/output/pdf
    ------------------------------------------------------------
    The following are the form fields found.

    field_name1
    field_name2
    ...
    ------------------------------------------------------------
    Fill up the 'data.json' file with above form fields to populate data and fill the form.
    ------------------------------------------------------------
    Press Enter to continue once you fill up 'data.json' file.
    ------------------------------------------------------------
    The following is the data,
    field1 = data1
    field2 = data2
    ...
    ------------------------------------------------------------
    Enter 'YES' to fill, 'NO' to edit data, 'STOP' to exit:
    ------------------------------------------------------------
    PDF Form Filled. Check output at path/to/output/pdf^C
    ------------------------------------------------------------
    Bye Bye.
    ------------------------------------------------------------
    ```
 
 ## Methods of `fill.Fill`

- `initialize_pdf(initialize_keys=True)`
    > Initilize the PDF file. Pass `initialize_keys` as `False` to not initialize the form field keys which this method does by default.
- `initialize_keys()`
    > Initialize the form field keys found in the PDF file.
- `populate_data(data)`
    > Populate the data with required key fields as `dict` type. Do this before filling up the form.
- `fill_pdf_form()`
    > Fill up the form with data populated by `populate_data(data)` method.

### Example
```python
from fill import Fill

# PDF FILES
pdf_file = "path/to/pdf"
output_file = "path/to/output"

# CREATE OBJECT
fill_pdf_form = Fill(pdf_file, output_file)

# INITIALIZE PDF FILE, KEYS ARE INITIALIZED BY DEFAULT
fill_pdf_form.initialize_pdf()

# LIST OUT FIELD KEYS OF PDF FORM
print(fill_pdf_form.KEYS)

# POPULATE DATA TO FILL
data = {
    "field1": "data1",
    "field2": "data2",
}
fill_pdf_form.populate_data(data)

# FILL FORM
fill_pdf_form.fill_pdf_form()

# THE OUTPUT WILL BE AT output_file
print("Output file location:", fill_pdf_form.output_file)
```
