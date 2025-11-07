import html


def decode_html_entities(text):
    if not isinstance(text, str):
        return text
    return html.unescape(text)
