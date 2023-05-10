import base64
from service import config


def convert(path_to_file):
    with open(path_to_file, 'rb') as pdf_file:
        encoded_pdf = base64.b64encode(pdf_file.read())

    return encoded_pdf


if __name__ == '__main__':
    print(convert(config.path_file))
