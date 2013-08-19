from pelican import signals
from fontawesome_markdown import FontAwesomeExtension


def pelicanfly(peli):
    md_ext = peli.settings.get('MD_EXTENSIONS')
    if md_ext:
        if 'fontawesome_markdown' not in md_ext:
            md_ext.append(FontAwesomeExtension())
    else:
        peli.settings['MD_EXTENSIONS'] = [FontAwesomeExtension()]
    peli.settings['THEME_STATIC_PATHS'].append('/Users/bmcorser/work/pelicanfly/pelicanfly/static/')

def register():
    signals.initialized.connect(pelicanfly)
