def format_value(key, value):
    keys = ['breed', 'color', 'owner', 'friend']
    if key in keys and isinstance(value, str):
        return [value]
    return value


def format_key(key):
    keys = ['color', 'owner', 'friend']
    if key in keys:
        return key + 's'
    return key


def format_dog(dict):
    return {format_key(k): format_value(k, v) for k, v in dict.items()}
