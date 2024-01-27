import requests
import re
from bs4 import BeautifulSoup

while True:
    word = input('输入要造句的单词或词组>>')
    content = requests.get('https://dict.youdao.com/result?word=lj%3A' + word + '&lang=en').text
    soup = BeautifulSoup(content, "html.parser")
    Sentences = soup.findAll("div", attrs={"class":"sen-eng"})
    for s in Sentences:
        result = re.sub('<[^>]+>', '', str(s))
        # result = re.sub(word,'\033[0;32;40m'+ word +'\033[0m',result)
        print(result)