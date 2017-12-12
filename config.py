import configparser
import os
import sys

# в uppercase
filename = 'config.ini'
file = os.path.join(os.path.dirname(sys.argv[0]), filename)  # TODO: сделать более универсальный вариант
config = configparser.RawConfigParser()
config.read(file)
# Один раз получить `Column`, потом из него уже получать всё остальное
our_article = config.get('Column', 'OurArticle')
full_name = config.get('Column', 'FullName')
quantity = config.get('Column', 'Quantity')
price = config.get('Column', 'Price')
group = config.get('Column', 'Group')
show = config.get('Column', 'Show').encode('cp1251').decode('UTF-8')
short_name = config.get('Column', 'ShortName')
short_descr = config.get('Column', 'ShortDescription')
full_descr = config.get('Column', 'FullDescription')
brand = config.get('Column', 'Brand')
weight = config.get('Column', 'Weight')
filters = config.get('Column', 'Filters')
theme = config.get('Column', 'Theme')
barcode = config.get('Column', 'Barcode')
article = config.get('Column', 'VendorArticle')
base1 = config.get('Column', 'Empty1')
base2 = config.get('Column', 'Empty2')
shop_price = config.get('Column', 'ShopPrice')
link = config.get('Column', 'Link')
empty_brands = [i[1].encode('cp1251').decode('UTF-8') for i in config.items('Brands')]
