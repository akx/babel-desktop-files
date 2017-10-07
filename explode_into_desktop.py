import argparse
import glob
from io import StringIO

import os
from babel.messages.pofile import read_po

from babel_desktop import extract_desktop_entries

ap = argparse.ArgumentParser()
ap.add_argument('-i', dest='input', required=True)
ap.add_argument('-d', dest='po_dir', required=True)
ap.add_argument('-k', dest='keywords', default=[], action='append')
ap.add_argument('-o', dest='output', required=True)
args = ap.parse_args()

with open(args.input, 'r') as infp:
    template = infp.read()
    original_messages = {
        keyword: message
        for (comment, keyword, message)
        in extract_desktop_entries(template)
    }

new_file = StringIO()
new_file.write(template)
new_file.write('\n')

for po_path in glob.glob(os.path.join(args.po_dir, '*.po')):
    try:
        with open(po_path, 'r') as infp:
            catalog = read_po(infp)
    except Exception as e:
        print(po_path, e)
        continue
    for keyword in args.keywords:
        original_message = original_messages.get(keyword)
        if original_message:
            translated = catalog.get(original_message)
            if translated and translated.string != original_message:
                new_file.write('{keyword}[{locale}]={translated}\n'.format(
                    keyword=keyword,
                    locale=catalog.locale,
                    translated=translated.string,
                ))

with open(args.output, 'w') as outf:
    outf.write(new_file.getvalue())
