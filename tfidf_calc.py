import pandas as pd
import numpy as np
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer


sentence = "\
吾輩は猫である。名前はまだ無い。\
どこで生れたかとんと見当がつかぬ。\
何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。\
吾輩はここで始めて人間というものを見た。\
しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。\
この書生というのは時々我々を捕つかまえて煮にて食うという話である。\
"

target = sentence.split("。")

tokenizer = Tokenizer()


def get_token(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    word = ""
    for token in tokens:
        part_of_speech = token.part_of_speech.split(",")[0]
        if part_of_speech == "名詞":
            word +=token.surface + " "
        if part_of_speech == "動詞":
            word +=token.base_form+ " "
        if part_of_speech == "形容詞":
            word +=token.base_form+ " "
        if part_of_speech == "形容動詞":
            word +=token.base_form+ " "
    return word
corpus=[]
for item in target:
    token=get_token(item)
    corpus.append(token)
print(corpus)



# TF-IDFのベクトル処理
vectorizer = TfidfVectorizer(use_idf=True)
tfidf = vectorizer.fit_transform(corpus)
 
print(tfidf.toarray())


# DataFrame型に変換して見やすく処理
import pandas as pd
display(pd.DataFrame(tfidf.toarray(), columns=vectorizer.get_feature_names(), index=corpus))