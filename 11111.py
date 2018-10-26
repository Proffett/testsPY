import re, time, urllib2

url = "http://lenta.ru/"
content = urllib2.urlopen(url).read()
imgUrls = re.findall('img .*?src="(.*?)"', сontent)

start = time.time()
for img in imgUrls:
    if img.endswith(".jpg"):
        """реализация метода по загрузке изображения из url"""

print time.time()-start