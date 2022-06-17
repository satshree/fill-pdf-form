"""Fill PDF Forms."""


# IMPORT PACKAGE
try:
    import pdfrw
except ModuleNotFoundError:
    print("Install 'pdfrw' package.")

    import sys
    sys.exit(1)

__author__ = "Satshree Shrestha"


class Fill:
    """Fill PDF Forms."""

    ANNOT_KEY = '/Annots'
    ANNOT_FIELD_KEY = '/T'
    ANNOT_VAL_KEY = '/V'
    ANNOT_RECT_KEY = '/Rect'
    SUBTYPE_KEY = '/Subtype'
    WIDGET_SUBTYPE_KEY = '/Widget'

    KEYS = []

    data = {}

    def __init__(self, pdf_file, output_file=None):
        self.pdf_file = pdf_file

        if output_file is None:
            self.output_file = pdf_file
        else:
            self.output_file = output_file
        self.pdf = None

    def initialize_pdf(self, initialize_keys=True):
        """Initialize PDF File."""
        self.pdf = pdfrw.PdfReader(self.pdf_file)
        if initialize_keys:
            self.initilize_keys()

    def initilize_keys(self):
        """Initialize form field keys."""
        for page in self.pdf.pages:
            annotations = page[self.ANNOT_KEY]
            for annotation in annotations:
                if annotation[self.SUBTYPE_KEY] == self.WIDGET_SUBTYPE_KEY:
                    if annotation[self.ANNOT_FIELD_KEY]:
                        key = annotation[self.ANNOT_FIELD_KEY][1:-1]
                        self.KEYS.append(key)

    def populate_data(self, data):
        """Populate data before filling the PDF form."""
        if not isinstance(data, dict):
            raise Exception("'data' needs to be a dictionary.")

        self.data = data
        return self.data

    def fill_pdf_form(self):
        """Fill PDF form with populated data."""
        for page in self.pdf.pages:
            annotations = page[self.ANNOT_KEY]
            for annotation in annotations:
                if annotation[self.SUBTYPE_KEY] == self.WIDGET_SUBTYPE_KEY:
                    if annotation[self.ANNOT_FIELD_KEY]:
                        key = annotation[self.ANNOT_FIELD_KEY][1:-1]
                        if key in self.data.keys():
                            if type(self.data[key]) == bool:
                                if self.data[key] == True:
                                    annotation.update(pdfrw.PdfDict(
                                        AS=pdfrw.PdfName('Yes')))
                            else:
                                annotation.update(
                                    pdfrw.PdfDict(
                                        V='{}'.format(self.data[key]))
                                )
                                annotation.update(pdfrw.PdfDict(AP=''))

        pdfrw.PdfWriter().write(self.output_file, self.pdf)
