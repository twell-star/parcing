#
# Решение задачи Парсинг логов
#

# для решения задачи используем функцию из курса, потому что "лучшее - это враг хорошего"
def get_value_from_list(object_list, separator, key):
    """Функция находит значение ключа key из списка object_list
    по разделителю separator
    :param object_list: список строк
    :param separator: разделитель
    :param key: искомый ключ"""

    # Объявляем переменную для хранения найденного значения
    value = None
    for element in object_list:
        # Итерируемся по каждому элементу из переданного списка object_list.
        # Каждый элемент разделяем на части, используя разделитель separator. 
        # В итоге получим, что первый элемент - это ключ, второй элемент - это значение.
        words = element.split(separator)
        if words[0] == key:
            # Если первый элемент равен искому ключу key, то обновляем значение value и выходим из цикла
            value = words[1]
            break  # оператор break можно было бы смело удалить, но мы не станем нарушать авторские права разработчика функции
                   # без него цикл сделает лишние пустые итерации (если элемент с искомым ключом будет не на последней позиции)
                   # на корректность работы функции это не повлияет, т.к. искомый ключ содержится в элементе в единственном экземпляре
                   # важно понимать, что при обработке огромных массивов данных отсутствие break может негативно повлиять на быстродействие
    
    # Возвращаем найденное значение
    return value


# Это наш "слон". Мы будем его есть по частям.
log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""

# создаем список для хранения разделенных записей
log_list = []

# нарезаем слона построчно
records = log.split('\n')

# обходим полученный список records
for log_record in records:
    
    # Определяем структуру записи, которую будем помещать в список log_list
    record_dict = {
        'name': '',
        'gender': '',
        'item': '',
        'item_cost': 0,
    }

    # Разделяем запись журнала log_record по точке с запятой - получаем список строк elements
    elements = log_record.split(';')

    # В списке elements ищем элемент по ключу и получаем значение этого элемента
    user_name = get_value_from_list(elements, ':', 'name')
    user_gender = get_value_from_list(elements, ':', 'gender')
    item_title = get_value_from_list(elements, ':', 'item')
    item_cost = get_value_from_list(elements, ':', 'item_cost')

    # Обновляем значения ключей в словаре record_dict
    record_dict['name'] = user_name
    record_dict['gender'] = user_gender
    record_dict['item'] = item_title
    record_dict['item_cost'] = item_cost

    # Добавляем полученный словарь record_dict в список log_list
    log_list.append(record_dict)

# теперь имеем список заказов log_list, из которого мы можем извлекать любые данные
# в нашем случае это список товаров, цена которых меньше 13000
#
# далее переходим к уникальному коду, решающему нашу задачу
# определяем переменную установленного ограничения цены
price_limit = 13000

# определим вспомогательный список товаров items
items = []

# обходим каждый словарь из списка log_list и проверяем соответствие цены товара установленному лимиту
# если цена меньше лимита и если название товара не содержится в списке items, то выводим название товара и его цену
# дополнительно выведем отклонение цены товара от установленного лимита
# поскольку цена бывает с копейками, то лучше флоатить, отклонение округлено с помощью функции round до двух знаков после запятой
for record_dict in log_list:
    if (float(record_dict['item_cost']) < price_limit) and (record_dict['item'] not in items):
        print(f"Товар '{record_dict['item']}', цена которого составляет {record_dict['item_cost']} рублей, удовлетворяет условию.", end=' ')
        print(f"Его цена меньше установленного ограничения на {round(price_limit - float(record_dict['item_cost']), 2)} рублей.")
        items.append(record_dict['item'])

# дополнительно вывовим список items, чтобы визуально убедиться в корректности алгоритма
print('\r')
print(items)
