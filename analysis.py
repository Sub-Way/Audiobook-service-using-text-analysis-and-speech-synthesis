import paralleldots
from nltk.tokenize import sent_tokenize
import pickle

class analysis(object):
    def replace_lf(str_list):
        for i, s in enumerate(str_list):
            if s[0:1] == "\n":
                str_list[i] = s[1:]
            else:
                str_list[i] = s.replace("\n", " ")


    def verdictEmotionHandler(textList, resultList):
        for sentence in textList:
            emoDict = paralleldots.emotion(sentence)
            emotion = emoDict['emotion']
            mostList = ['', 0]
            for emo, score in emotion.items():
                if mostList[1] <= score:
                    mostList = [emo, score]
            resultList.append([sentence, mostList[0]])


if __name__ == "__main__":
    text =
    tokenized_text = []
    tokenized_text = sent_tokenize(text)
    replace_lf(tokenized_text)
    paralleldots.set_api_key("iccd4cMkkR8ApGn781vM3Y0f11sDidB1YUahDDTHIXU")
    result = []
    verdictEmotionHandler(tokenized_text, result)
    with open('fairyTale.data', 'wb') as f:
        pickle.dump(result, f)
    print(result)