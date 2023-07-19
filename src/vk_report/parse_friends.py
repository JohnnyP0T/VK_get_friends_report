import datetime


def parse_friends_country(item_field: any) -> str:
    if item_field is not None:
        return item_field.get('title')
    else:
        return 'unknown'


def parse_friends_city(item_field: any) -> str:
    if item_field is not None:
        return item_field.get('title')
    else:
        return 'unknown'


def parse_friends_birth_date(item_field: any) -> str:
    if item_field is not None:
        format_date_point_count = item_field.count('.')
        if format_date_point_count == 2:
            return datetime.datetime.strptime(item_field, "%d.%m.%Y").date().isoformat()
        if format_date_point_count == 1:
            return datetime.datetime.strptime(item_field, "%d.%m").date().isoformat()
        else:
            return 'unknown'
    else:
        return 'unknown'


def parse_friends_sex(item_field: any) -> str:
    if item_field == 1:
        return 'female'
    elif item_field == 2:
        return 'male'
    else:
        return 'unknown'


def parse_friends(items: list) -> list:
    person_list = []
    for i in items:
        person_temp = dict()
        person_temp['first_name'] = i.get('first_name')
        person_temp['last_name'] = i.get('last_name')
        person_temp['country'] = parse_friends_country(i.get('country'))
        person_temp['city'] = parse_friends_city(i.get('city'))
        person_temp['birth_date'] = parse_friends_birth_date(i.get('bdate'))
        person_temp['sex'] = parse_friends_sex(i.get('sex'))
        person_list.append(person_temp)
    return person_list
