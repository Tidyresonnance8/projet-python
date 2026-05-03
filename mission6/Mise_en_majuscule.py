def capitalize(filename_in, filename_out):
    with open(filename_in, 'r') as file_in:
        char = file_in.read()
        char_up = char.upper()

        with open(filename_out, 'w') as file_out:
            file_out.write(char_up)