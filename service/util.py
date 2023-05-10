import PyPDF2
import io


def read_pdf(statement) -> str:
    """
    Прочитать PDF файл
    :param statement: Тело запроса в виде PDF файла
    :return: Текст PDF файла
    """

    # преобразовать байтовую строку в объект PyPDF2.PdfFileReader

    with PyPDF2.PdfFileReader(io.BytesIO(statement)) as pdf_reader:
        # получить количество страниц в документе
        num_pages = pdf_reader.getNumPages()

        # считывать текст со всех страниц документа
        text = ''
        for i in range(num_pages):
            page = pdf_reader.getPage(i)
            text += page.extractText()

    return text
