def table(filename_in, filename_out, width):
    try:
        barre_top = "+" + "-"*(width+2) + "+\n"
        barre_bottom = "+" + "-"*(width+2) + "+"

        with open(filename_in, 'r') as file_in:
            with open(filename_out, 'w') as file_out:
                file_out.write(barre_top)    # Je crée ma barre du haut
                for line in file_in:
                    if not line:
                        continue
                    lines = line.rstrip("\n")
                    formatted = "{:<{}.{}}".format(lines,width,width)
                    output_line = "| {} |\n".format(formatted)
                    file_out.write(output_line)

                file_out.write(barre_bottom)

    except IOError as e:
        print(f"Il y a eu une erreur qui est survenue: {e}")

