import re

# Adapted from intltool:
desktop_re = re.compile(r'^(?:#\s*(.+)\n)?^(.*)=(.*)', re.MULTILINE)


def extract_desktop_entries(content):
    # INTERNAL - Extracts (comment, keyword, message) 3-tuples.
    for match in desktop_re.finditer(content):
        yield match.groups()


def extract_desktop(fileobj, keywords, comment_tags, options):
    content = fileobj.read().decode('UTF-8')
    for comment, keyword, message in extract_desktop_entries(content):
        if keyword in keywords or keyword.startswith('_'):
            # TODO: lineno is not supported
            yield (0, None, message, [comment or ''])
