import os
import shutil
from pelican import signals
from fontawesome_markdown import FontAwesomeExtension


def add_markdown_plugin(peli):
    md_ext = peli.settings.get('MD_EXTENSIONS')
    cls = FontAwesomeExtension
    inst = cls()
    if not md_ext:
        peli.settings['MD_EXTENSIONS'] = [inst]
    elif not any([isinstance(ext, cls) for ext in md_ext]):
        md_ext.append(inst)
        peli.settings['MD_EXTENSIONS'] = md_ext


def publish_fontawesome_assets(peli):
    for ass in ['font', 'css']:
        input_dir = os.path.join(os.path.split(__file__)[0], 'static', ass)
        output_dir = os.path.join(peli.output_path, 'theme', ass)
        try:
            os.makedirs(output_dir)
        except OSError as exc:
            if exc.errno == 17:
                pass
        for name in os.listdir(input_dir):
            input_file = os.path.join(input_dir, name)
            output_file = os.path.join(output_dir, name)
            shutil.copy(input_file, output_file)

    css_file = os.path.join(
                            peli.output_path,
                            'theme',
                            'css',
                            peli.settings['CSS_FILE'])

    with open(css_file, "r+") as f:
        s = f.read()
        f.seek(0)
        f.write("@import url('font-awesome.css');\n" + s)


def register():
    signals.initialized.connect(add_markdown_plugin)
    signals.finalized.connect(publish_fontawesome_assets)
