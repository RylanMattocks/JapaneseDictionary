from django.shortcuts import render
from PyDictionary import PyDictionary
from deep_translator import GoogleTranslator
import pykakasi

# Create your views here.
def home(request):
    return render(request, "home.html")

def search(request):
    words = request.GET.get('words')
    dictionary = PyDictionary()
    meanings = dictionary.meaning(words)
    fmeaning = (list(meanings.values())[0][0])
    japanese = GoogleTranslator(source='auto', target='ja').translate(words)
    kks = pykakasi.kakasi()
    result = kks.convert(japanese)
    kana = "{}".format(result[0]['kana'])
    hiragana = "{}".format(result[0]['hira'])
    romaji = "{}".format(result[0]['hepburn'])

    context = {
        'word' : words.capitalize(),
        'meaning' : fmeaning.capitalize(),
        'japanese' : japanese,
        'kana' : kana,
        'hiragana' : hiragana,
        'romaji' : romaji
    }
    return render(request, "search.html", context)