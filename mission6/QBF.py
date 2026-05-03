def get_max(filename):
    try:
        l = []
        with open(filename,'r') as file:
            for line in file:
                line = line.strip().split()
                if not line:
                    continue
                if len(line) != 1:
                    continue
                try:
                    value = float(line[0])
                    if value >= 0:
                        l.append(value)
                except ValueError:
                    continue
        if not  l:
            return -1.0
        else:
            return max(l)
    except FileNotFoundError:
        return -1.0
    except Exception:
        return -1.0
                