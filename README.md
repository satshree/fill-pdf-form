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
    >> bash ./initialize.sh
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
    PDF Form Filled. Check output at ignore/output.pdf^C
    ------------------------------------------------------------
    Bye Bye.
    ------------------------------------------------------------
    ```
 