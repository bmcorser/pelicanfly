from pelican import signals

def pelicanfly(pelican_instance):
    from ipdb import set_trace;set_trace()

def gen_init(generator_instance):
    from ipdb import set_trace;set_trace()

def register():
    signals.initialized.send(pelicanfly)
    signals.generator_init.send(gen_init)
