from flask import Flask, render_template, request
import os, traceback
import subprocess
import paralleldots
from nltk.tokenize import sent_tokenize
import pickle
from textblob import TextBlob
app = Flask(__name__)


def analysis(string):
    text = string
    tokenized_text = []
    tokenized_text = sent_tokenize(text)
    replace_lf(tokenized_text)
    paralleldots.set_api_key("iccd4cMkkR8ApGn781vM3Y0f11sDidB1YUahDDTHIXU")
    result = []
    verdictEmotionHandler(tokenized_text, result)
    with open('fairyTale.data', 'wb') as f:
        pickle.dump(result, f)
    return result


def replace_lf(str_list):
    for i, s in enumerate(str_list):
        if s[0:1] == "\n":
            str_list[i] = s[1:]
        else:
            str_list[i] = s.replace("\n", " ")


def verdictEmotionHandler(textList, resultList):
    for sentence in textList:
        emoDict = paralleldots.emotion(sentence.strip())
        emotion = emoDict['emotion']
        selectedEmotion = ""
        emoList = []
        emoList = sorted(emotion, key=lambda k: emotion[k], reverse=True)
        selectedEmotion = emoList[0]

        textblobPolarity = TextBlob(sentence).sentiment.polarity
        print(emotion)
        print(textblobPolarity)
        if textblobPolarity == 0:
            resultList.append([sentence, selectedEmotion])
        elif (textblobPolarity > 0 and (selectedEmotion == 'Happy' or selectedEmotion == 'Excited')) or (
                textblobPolarity < 0 and (
                selectedEmotion == 'Sad' or selectedEmotion == 'Angry' or selectedEmotion == 'Fear')):
            resultList.append([sentence, selectedEmotion])
        elif (textblobPolarity < 0 and (selectedEmotion == 'Happy' or selectedEmotion == 'Excited')) or (
                textblobPolarity > 0 and (
                selectedEmotion == 'Sad' or selectedEmotion == 'Angry' or selectedEmotion == 'Fear')):
            resultList.append([sentence, 'Neutral'])
        else :
            resultList.append([sentence, selectedEmotion])
@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/book1', methods=['GET', 'POST'])
def book1():
    return render_template('index.html')


@app.route('/book2', methods=['GET', 'POST'])
def book2():
    return render_template('index2.html')


@app.route('/book3', methods=['GET', 'POST'])
def book3():
    return render_template('index3.html')


@app.route('/info')
def main_page():
    return render_template('main_page.html')

@app.route('/request', methods=['POST'])
def query():
    value = request.form['SensorID']
    data = ["@echo on\n", "cd C:\\Users\\dongh\\Desktop\\webdev\n",
            "call C:\\Users\\dongh\\Anaconda3\\Scripts\\activate.bat\n", "call activate webserver\n",
            "call python app.py\n", "pause\n"]
    with open("batch_file.bat",'w') as file:
        file.writelines(data)
    print(os.getcwd()+"\\batch_file.bat")
    #if os.path.isfile() == true: #파일이 존재하면
    #    print(true)
    #os.system(os.getcwd()+"\\batch_file.bat")
    #이 텍스트 이용해서
    #배치파일 생성하고 O
    #배치파일 실행 O
    #배치파일 실행시 그 텍스트로 오디오 생성

    try:
        result = analysis(value)
        return result[0][1]
    except IndexError:
        return "Neutral"
          # 여기다가 오디오 리턴해줘야함

    #오디오 생성될 때까지 기다림
    #오디오 생성시 return 수행






@app.route('/item1', methods=['POST','GET'])
def item1_page():
    return render_template('main_page.html')

@app.route('/about', methods=['POST','GET'])
def about_page():
    return render_template('main_page.html')

@app.route('/item3', methods=['POST','GET'])
def item3_page():
    return render_template('main_page.html')
if __name__ == "__main__":
    app.run(debug=True)