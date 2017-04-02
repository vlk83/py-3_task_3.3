# Домашнее задание к лекции 3.3 «Работа с библиотекой requests, http-запросы»

import requests
import glob
import os.path


# функция перевод + параметры. yandex translate API
def translate_it(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    parameters = {
        'key': key,
        'lang': 'ru',
        'text': text
    }
    response = requests.get(url, params=parameters).json()
    return response


# создаем директорию для хранения переводов
if not os.path.exists('translations_into_russian'):
    os.mkdir('translations_into_russian')

# создаем список для исходных файлов с текстами
list_of_source_texts = glob.glob('source_texts/*.txt')

# открываем каждый файл, читаем текст, перевод сохраняем в отдельный файл
for source_text in list_of_source_texts:
    with open(source_text, 'r', encoding='utf8') as f:
        text_for_translation = f.read()

    translated_ = translate_it(text_for_translation)
    translated_text = ''.join(translated_['text'])
    translated_lang = translated_['lang']

    name_of_translated_file = source_text.replace('source_texts\\', '') \
    .replace('.txt', '_translated_[{}].txt'.format(translated_lang))

    with open(os.path.join('translations_into_russian', name_of_translated_file), 'w', encoding='utf8') as f:
        f.write(translated_text)
