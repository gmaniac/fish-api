import re

EMAIL_REGEX = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def is_email(email):
    if re.search(EMAIL_REGEX, email):
        return True
    else:
        return False


def convert_camel_case_to_snake_case(camel_case):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_case)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def convert_snake_case_to_camel_case(snake_case):
    return ''.join(word.title() for word in snake_case.split('_'))


def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}

