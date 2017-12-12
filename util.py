from copy import deepcopy as copy
import argparse
from contextlib import suppress

import config as c


def parse_arguments():
    parser = argparse.ArgumentParser(description='Программа для автоматической обработки файлов на выгрузку')
    parser.add_argument('path', metavar='P', type=str, help='Путь к таблице Excel в формате .xlsx')
    parser.add_argument('--without-brands', action='store_false', dest='no_brands',
                        help='не вставлять бренды в название для сайта')
    parser.add_argument('--edit-scb-articles', action='store_true', dest='edit_scb',
                        help="обработать артикул ScrapBerry's")
    args = parser.parse_args()
    return args.path, args.no_brands, args.edit_scb


def show_on_site(workbook, cell):
    workbook[c.show + str(cell)].value = 'Да'


def copy_description(workbook, cell):
    with suppress(TypeError):
        if '_' not in workbook[c.short_descr + str(cell)].value:
            workbook[c.full_descr + str(cell)].value = copy(workbook[c.short_descr + str(cell)].value)


def format_cell(s):
    if s is None:
        s = ''
    return str(s).lstrip(' ').rstrip(' ')


def format_name(s):
    return s.replace(' ()', '')\
            .replace('(, ', '(')\
            .replace(', )', ')')\
            .replace('  ', ' ')\
            .replace(' (Сима)', '')\
            .replace('Fluffy Duffy 2', 'Fluffy Duffy')


def collect_names(workbook, cell, show_brand=True, scb=False):
    if workbook[c.full_name + str(cell)].value is not None:
        name_full = workbook[c.full_name + str(cell)].value
        article = format_cell(workbook[c.article + str(cell)].value)
        brand = format_cell(workbook[c.brand + str(cell)].value)
        if brand in c.empty_brands:
            brand = ''
        if brand in ['Сима', 'Вязанка', 'Сафина']:
            workbook[c.brand + str(cell)].value = c.empty_brands[0]
        if show_brand is not True:
            name_short = copy(name_full)
        else:
            name_short = '{n} ({b})'.format(n=name_full,
                                            b=brand)
        if scb is False:
            name_full = '{n} ({b}, {a})'.format(n=name_full,
                                                b=brand,
                                                a=article)
        else:
            name_full = '{n} ({a})'.format(n=name_full,
                                           a=article.replace('SCB', 'SCB, '))

        workbook[c.full_name + str(cell)].value = format_name(name_full)
        workbook[c.short_name + str(cell)].value = format_name(name_short)
    else:
        workbook[c.full_name + str(cell)].value = None
        for row in workbook[c.group + str(cell): c.base2 + str(cell)]:
            for row_cell in row:
                row_cell.value = None


def cell_to_null(workbook, cell, line):
    workbook[line + str(cell)].value = None
