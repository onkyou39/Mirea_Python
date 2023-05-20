def remove_none(data):
    result = []
    for sublist in data:
        temp = [item.strip() for item in sublist if item is not None]
        result.append(temp)
    return result


def parse_string(data):
    result = []
    for row in data:
        temp = []
        domain = row[0].split('@')[-1]
        temp.append(domain)
        name = row[1].split('!')
        mark = name[1]
        if mark == "Не выполнено":
            mark = "N"
        else:
            mark = "Y"
        name = name[0]
        name = name.split()[0:3:2]
        name.reverse()
        name = " ".join(name)
        date = row[2].split('-')
        date = f"{date[0]}/{date[1]}/{date[2][-2:]}"
        temp.append(mark)
        temp.append(date)
        temp.append(name)
        result.append(temp)
    return result


def main(data):
    data = remove_none(data)
    data = parse_string(data)
    return data
