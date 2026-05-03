def write(letter_template, name):
    try:
        with open(letter_template, 'r') as file:
            e = file.read().replace('#', name)
            with open(letter_template, 'w') as file:
                file.write(e)

    except (FileExistsError, FileNotFoundError, Exception):
        return None