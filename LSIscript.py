from bs4 import BeautifulSoup
import requests
import urllib.parse
import sys
import time
import json
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from pymorphy2 import MorphAnalyzer

m = MorphAnalyzer()
query_text = "осевой вентилятор"
auth_token = "AQAAAAABN0XoAAU2LB8jCEqxKE2_umpAvbYZkTQ"
url = 'https://api-sandbox.direct.yandex.ru/live/v4/json/'
data = {'token': auth_token, 'method': 'CreateNewWordstatReport', 'param': {'Phrases': [query_text]}}
body = json.dumps(data, ensure_ascii=False)
answer = requests.post(url, body.encode('utf-8'), headers={'Content-type': 'application/json; charset=utf-8'})
response = answer.json()
id = response['data']

# формирование отчета
time.sleep(10)

# Подставляем в свойство param наш id и обращаемся к API.
url = 'https://api-sandbox.direct.yandex.ru/live/v4/json/'
data = {'token': auth_token, 'method': 'GetWordstatReport', 'param': id}
body = json.dumps(data, ensure_ascii=False)
report = requests.post(url, body.encode('utf-8'), headers={'Content-type': 'application/json; charset=utf-8'})
response = report.json()

# сформировать два датафрейма, где один отвечает за столбец в Вордстат «Что искали со словом…» (SearchedWith),
# а второй – за похожие запросы (SearchedAlso).
sa_df = pd.DataFrame(response['data'][0]['SearchedAlso'])
sw_df = pd.DataFrame(response['data'][0]['SearchedWith'])

# Под этим блоком формируется URL самой XML выдачи. Копируем его и подставляем в него наш декодированный запрос.
url_enc = urllib.parse.quote_plus(query_text)
url_get = 'https://yandex.ru/search/xml?user=Syrexx&key=03.20399592:8ad8f41bc17d89c4525f5cbb0296f1e5&query=' + url_enc + '&l10n=ru&sortby=rlv&filter=strict&groupby=attr%3Dd.mode%3Ddeep.groups-on-page%3D50.docs-in-group%3D1'

# путь к файлу, в которые запишутся все URL ТОП 50 выдачи по нашему запросу.
sys.stdout = open("C:\\Users\\Evgen\\Documents\\url_list.txt", "w", encoding="utf-8")

# Отправляем запрос и парсим XML выдачу:
response = requests.get(url_get)
soup = BeautifulSoup(response.content, "html.parser")
for url in soup.findAll('url'):
    print(url.text)

# путь к файлу, куда запишем весь текст, полученный при парсинге страниц:
sys.stdout.close()
sys.stdout = open("C:\\Users\\Evgen\\Documents\\out.txt", "w", encoding="utf-8")

# Нам лишь нужно найти наиболее часто употребляемые N-граммы в текстах ТОП 50.
urls = [z.rstrip() for z in open('C:\\Users\\Evgen\\Documents\\Texts_Analyze\\url_list.txt', encoding='utf-8')]
for url in urls:
    try:
        response = requests.get(url, timeout=None)
    except:
        continue
    soup = BeautifulSoup(response.content, "html.parser")

    for pp in soup.select("p"):
        print(pp.text)

# Приступаем к анализу полученных данных.
urls = [z.rstrip() for z in open('C:\\Users\\Evgen\\Documents\\url_list.txt', encoding='utf-8')]
for url in urls:
    try:
        response = requests.get(url, timeout=None)
    except:
        continue
    soup = BeautifulSoup(response.content, "html.parser")

    for pp in soup.select("p"):
        print(pp.text)

# Указываем файл, куда запишем результаты, загружаем данные парсинга и список стоп-слов,
#  которые мы хотим исключить из анализа N-грамм (предлоги, союзы, технические и коммерческие слова и т.д.)
sys.stdout.close()
sys.stdout = open("C:\\Users\\Evgen\\Documents\\result.txt", "w", encoding="utf-8")
texts = [z.rstrip() for z in open('C:\\Users\\Evgen\\Documents\\out.txt', encoding='utf-8')]
stop_words = [z.rstrip() for z in open('C:\\Users\\Evgen\\Documents\\stop_words.txt', encoding='utf-8')]

# приводим все слова к их исходной форме,
# настраиваем CountVectorizer на подсчет N-грамм с количеством слов от 2 до 4 и записываем результат в файл.
cvn = CountVectorizer(ngram_range=(2, 4), stop_words=stop_words)
words_nf = [' '.join([m.parse(word)[0].normal_form for word in x.split()]) for x in texts]
ngrams = cvn.fit_transform(words_nf)
vb = cvn.vocabulary_
count_values = ngrams.toarray().sum(axis=0)

for ng_count, ng_text in sorted([(count_values[i], k) for k, i in vb.items()], reverse=True):
    print(ng_text, ng_count, sep='\t')

# Все, что нужно дальше, – записать все результаты в один Excel-файл:
info_data = pd.read_csv('C:\\Users\\Evgen\\Documents\\result.txt', encoding='utf-8', sep="\t", header=None)
filename = 'C:\\Users\\Evgen\\Documents\\' + query_text + '.xlsx'
writer = pd.ExcelWriter(filename)
info_data.to_excel(writer, 'NGrams', encoding='utf-8', index=False)
sa_df.to_excel(writer, 'SearchedAlso', encoding='utf-8', index=False)
sw_df.to_excel(writer, 'SearchedWith', encoding='utf-8', index=False)
writer.save()
