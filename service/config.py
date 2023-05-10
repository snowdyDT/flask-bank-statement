import keyring

path_file = keyring.get_password('FILE', 'FILE_PATH')

re_patterns = {
    "date_pattern": r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}\s\w{3}",
    "name_pattern": r"Выписка по Контракту клиента (.+)",
    "contract_pattern": r"Номер контракта (\w+-\w+-\w+)",
    "account_pattern": r"Номер счета (\d+)",
    "card_pattern": r"Карта (\d+\.\.\d+)",
    "bank_pattern": r"Отделение Банка (.+)",
    "currency_pattern": r"Основная валюта контракта (\w+)",
}
