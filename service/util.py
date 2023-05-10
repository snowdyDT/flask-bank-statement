import pdfplumber
import io
import re
import config


def read_pdf(statement) -> str:
    """
    Прочитать PDF файл
    :param statement: Тело запроса в виде PDF файла
    :return: Текст PDF файла
    """

    # преобразовать байтовую строку в объект PyPDF2.PdfFileReader

    with pdfplumber.open(io.BytesIO(statement)) as content:
        # считывать текст со всех страниц документа
        text = ''
        for page in content.pages:
            text = text + "\n" + page.extract_text()

    return text


def get_data_client(text: str) -> dict:
    """
    Получить нужные данные клиента с текста
    :param text: Текст
    :return: Словарь результатов
    """

    re_patterns = config.re_patterns

    date = re.findall(re_patterns['date_pattern'], text)[0]
    name = re.findall(re_patterns['name_pattern'], text)[0]
    contract = re.findall(re_patterns['contract_pattern'], text)[0]
    account = re.findall(re_patterns['account_pattern'], text)[0]
    card = re.findall(re_patterns['card_pattern'], text)[0]
    bank = re.findall(re_patterns['bank_pattern'], text)[0]
    currency = re.findall(re_patterns['currency_pattern'], text)[0]

    result = {
        'date': date,
        'name': name,
        'contract': contract,
        'account': account,
        'card': card,
        'bank': bank,
        'currency': currency,
    }

    return result


def split_text_transaction(text: str) -> list:
    """
    Разделить текст (таблица транзакции) через каждую 3 '\n'
    :param text: Текст (таблица транзакции)
    :return: Список содержащий информацию про каждую транзакцию
    """
    lines = text.split('\n')

    transaction_list = []

    for i in range(0, len(lines), 3):
        substr = '\n'.join(lines[i:i + 3])
        transaction_list.append(substr)

    return transaction_list

