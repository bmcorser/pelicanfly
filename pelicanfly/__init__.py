from pelican import signals

def pelicanfly(pelican_instance):
    pass

def gen_init(generator_instance):
    pass

def register():
    signals.initialized.connect(pelicanfly)
    signals.generator_init.connect(gen_init)
