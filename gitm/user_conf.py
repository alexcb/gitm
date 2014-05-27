import json

def load_config_or_default(config_file):
    try:
        with open(config_file) as fp:
            config = parse_config(fp.read())
    except FileNotFoundError:
        config = {}
    add_expected_fields_to_config(config)
    return config

def parse_config(config_bytes):
    return json.loads(config_bytes)

def save_config(config, config_file):
    with open(config_file, 'w') as fp:
        fp.write(serialize_config(config))

def serialize_config(config):
    return json.dumps(config)

def add_expected_fields_to_config(config):
    if not isinstance(config, dict):
        raise ValueError('Config must be a dictionary, got %s' % type(config))

    for key, default in (
            ('tags',  {}),
            ('repos', []),
            ):
        try:
            if not isinstance(config[key], type(default)):
                raise ValueError('config value for key "%s" is not expected type %s (got %s)' % (
                    key, type(default), type(config[key])))
        except KeyError:
            config[key] = default
