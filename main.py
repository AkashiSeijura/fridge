from decimal import Decimal
from datetime import date, timedelta, datetime


goods: dict = {}
DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if expiration_date:
        expiration_date = datetime.strptime(expiration_date, DATE_FORMAT).date()
    elif title in items:
        items[title].append({'amount': amount, 'expiration_date': expiration_date})
    else:
        items[title] = [{'amount': amount, 'expiration_date': expiration_date}]


def add_by_note(items, note):
    list_note = note.split()
    date_in_note = len(str.split(list_note[-1],'-'))
    if date_in_note == 3:
        expiration_date = list_note[-1]
        amount = Decimal(list_note[-2])
        title = str.join(' ', list_note[0:-2])
    else:
        expiration_date = None
        amount = Decimal(list_note[-1])
        title = ' '.join(list_note[:-1])
    add(items, title, amount, expiration_date)


def find(items, needle):
    return [name for name in items if needle.lower() in name.lower()]


def amount(items, needle):
    name_keys = list(dict.keys(items))
    chet = Decimal('0')
    for name in name_keys:
        if needle.lower() in name.lower():
            for amount_item in items[name]:
                chet += amount_item['amount']
    return chet


def expire(items, in_advance_days=0):
    today = date.today()
    zero_list = []
    target_date = today + timedelta(days=in_advance_days)
    for key, item in items.items():
        total_amount = Decimal('0')
        for name in item:
            if name['expiration_date'] is None:
                continue

            elif name['expiration_date'] <= target_date:
                total_amount += name['amount']

            else:
                continue

        if total_amount > 0:
            zero_list.append((key, total_amount))

    return zero_list


add(goods, 'Пельмени Универсальные', Decimal('0.5'), '2023-07-17')
add(goods, 'Пельмени Универсальные', Decimal('2'), '2023-10-28')
add(goods, 'Вода', Decimal('0.5'))
add_by_note(goods, 'Яйца Гусиные 4')
add_by_note(goods, 'Вода 2.5')
print(find(goods, 'пельмени'))
print(amount(goods, 'пельмени'))
print(expire(goods))