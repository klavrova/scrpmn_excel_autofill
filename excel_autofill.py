from openpyxl import load_workbook

import util
import config


def autofill_excel(input_file, show_brand, scb):
    sheet = load_workbook(input_file)
    wb = sheet[sheet.get_sheet_names()[0]]
    row = 2
    while wb[config.price + str(row)].value is not None:
        util.copy_description(wb, row)
        util.collect_names(wb, row, show_brand, scb)
        util.cell_to_null(wb, row, config.link)
        util.cell_to_null(wb, row, 'T')
        util.show_on_site(wb, row)
        row += 1
    sheet.save(input_file[:-5] + '(1).xlsx')


if __name__ == '__main__':
    autofill_excel(*util.parse_arguments())
