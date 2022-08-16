import datetime


def parse_friends(items:list) -> list:
    person_list = []
    for i in items:
        person_temp = dict()
        person_temp['first_name'] = i.get('first_name')
        person_temp['last_name'] = i.get('last_name')
        if i.get('country') is not None:
            person_temp['country'] = i.get('country').get('title')
        else:
            person_temp['country'] = 'unknown'
        if i.get('city') is not None:
            person_temp['city'] = i.get('city').get('title')
        else:
            person_temp['city'] = 'unknown'
        if i.get('bdate') is not None:
            format_date_point_count = i.get('bdate').count('.')
            if format_date_point_count == 2:
                person_temp['birth_date'] = datetime.datetime.strptime(i.get('bdate'), "%d.%m.%Y").isoformat()
            if format_date_point_count == 1:
                person_temp['birth_date'] = datetime.datetime.strptime(i.get('bdate'), "%d.%m").isoformat()
        else:
            person_temp['birth_date'] = 'unknown'
        if i.get('sex') == 1:
            person_temp['sex'] = 'female'
        elif i.get('sex') == 2:
            person_temp['sex'] = 'male'
        else:
            person_temp['sex'] = 'unknown'

        person_list.append(person_temp)
    return person_list

