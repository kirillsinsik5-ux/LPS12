import re

# ========= ФУНКЦИИ ВАЛИДАЦИИ =========

def validate_email(email):
    """Проверяет корректность email адреса."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, "☑ Email корректный"
    return False, "✗ Неправильный email! Пример: name@mail.ru"

def validate_phone(phone):
    """Проверяет корректность номера телефона."""
    phone = phone.strip()
    patterns = [
        r'^\+7-\d{3}-\d{3}-\d{2}-\d{2}$',  # +7-999-123-45-67
        r'^\+7 \d{3} \d{3} \d{2} \d{2}$',  # +7 999 123 45 67
        r'^\+7\d{10}$',                     # +79991234567
        r'^8-\d{3}-\d{3}-\d{4}$',          # 8-999-123-4567
        r'^8 \d{3} \d{3} \d{4}$',          # 8 999 123 4567
        r'^8\d{10}$'                        # 89991234567
    ]
    for pattern in patterns:
        if re.match(pattern, phone):
            clean = re.sub(r'\D', '', phone)
            if clean.startswith('8'):
                clean = '+' + clean[1:]
            elif clean.startswith('7'):
                clean = '+' + clean
            return True, "☑ Телефон корректный", clean
    return False, "✗ Неправильный телефон! Пример: +7-999-123-45-67", None

def validate_inn(inn):
    """Проверяет корректность ИНН (10 или 12 цифр)."""
    inn = inn.strip()
    if not inn.isdigit():
        return False, "✗ ИНН должен содержать только цифры!"
    if len(inn) == 10:
        return True, "☑ ИНН организации корректен (10 цифр)"
    elif len(inn) == 12:
        return True, "☑ ИНН физического лица корректен (12 цифр)"
    return False, "✗ ИНН должен содержать 10 или 12 цифр!"

def validate_passport(passport):
    """Проверяет формат паспорта: 45 03 123456 (2 цифры пробел 2 цифры пробел 6 цифр)"""
    pattern = r'^\d{2} \d{2} \d{6}$'
    if re.match(pattern, passport.strip()):
        return True, "☑ Паспорт корректен"
    return False, "✗ Неправильный формат паспорта! Пример: 45 03 123456"

# ========= ФУНКЦИИ ПОИСКА =========

def find_emails(text):
    """Находит все email-адреса в тексте."""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def find_phones(text):
    """Находит все номера телефонов в тексте."""
    patterns = [
        r'\+7[- ]?\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}',  # +7-999-123-45-67
        r'8[- ]?\d{3}[- ]?\d{3}[- ]?\d{4}'              # 8-999-123-4567
    ]
    phones = []
    for pattern in patterns:
        phones.extend(re.findall(pattern, text))
    return phones

def find_dates(text):
    """Находит все даты в формате ДД.ММ.ГГГГ или ДД/ММ/ГГГГ."""
    pattern = r'\d{2}[./]\d{2}[./]\d{4}'
    return re.findall(pattern, text)

def find_prices(text):
    """Находит все цены в тексте."""
    pattern = r'\d+(?:[.,]\d+)?\s?(?:руб|Р|\$|€|₽|rub|RUB)'
    return re.findall(pattern, text, re.IGNORECASE)

def find_urls(text):
    """Находит все ссылки в тексте."""
    pattern = r'https?://[a-zA-Z0-9./?=_\-]+|www\.[a-zA-Z0-9./?=_\-]+'
    return re.findall(pattern, text)

def find_ip_addresses(text):
    """Находит все IP-адреса (4 числа от 0 до 255, разделённые точками)."""
    pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.findall(pattern, text)

def find_hashtags(text):
    """Находит все хэштеги (#слово)."""
    pattern = r'#[a-zA-Zа-яА-Я0-9_]+'
    return re.findall(pattern, text, re.IGNORECASE)

# ========= ОСНОВНАЯ ПРОГРАММА =========

def main():
    print("=" * 50)
    print("ПРОГРАММА ВАЛИДАЦИИ И ПОИСКА ДАННЫХ")
    print("=" * 50)

    while True:
        print("\nМеню:")
        print("1. Проверить email")
        print("2. Проверить телефон")
        print("3. Проверить ИНН")
        print("4. Проверить паспорт")
        print("5. Поиск данных в тексте")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        if choice == "0":
            print("До свидания!")
            break

        elif choice == "1":
            email = input("Введите email: ")
            valid, msg = validate_email(email)
            print(msg)

        elif choice == "2":
            phone = input("Введите телефон: ")
            valid, msg, clean = validate_phone(phone)
            print(msg)
            if valid:
                print(f"Очищенный номер: {clean}")

        elif choice == "3":
            inn = input("Введите ИНН: ")
            valid, msg = validate_inn(inn)
            print(msg)

        elif choice == "4":
            passport = input("Введите паспорт (формат: 45 03 123456): ")
            valid, msg = validate_passport(passport)
            print(msg)

        elif choice == "5":
            print("\nВведите текст (несколько строк, Enter дважды для завершения):")
            lines = []
            empty_count = 0
            while True:
                line = input()
                if line == "":
                    empty_count += 1
                    if empty_count == 2:
                        break
                else:
                    empty_count = 0
                lines.append(line)

            text = "\n".join(lines)

            print("\n" + "=" * 50)
            print("РЕЗУЛЬТАТЫ ПОИСКА:")
            print("=" * 50)

            emails = find_emails(text)
            if emails:
                print(f"\n📧 Email: {emails}")

            phones = find_phones(text)
            if phones:
                print(f"📞 Телефоны: {phones}")

            dates = find_dates(text)
            if dates:
                print(f"📅 Даты: {dates}")

            prices = find_prices(text)
            if prices:
                print(f"💰 Цены: {prices}")

            urls = find_urls(text)
            if urls:
                print(f"🔗 Ссылки: {urls}")

            ips = find_ip_addresses(text)
            if ips:
                print(f"🌐 IP-адреса: {ips}")

            hashtags = find_hashtags(text)
            if hashtags:
                print(f"🏷️ Хэштеги: {hashtags}")

            if not (emails or phones or dates or prices or urls or ips or hashtags):
                print("Ничего не найдено")

        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()