fileSystWords = 'systemwords.txt'
fileLongmanWords = 'longman.txt'

fileFirstSpeak = 'SpeakFirst.txt'
fileSecondSpeak = 'SpeakSecond.txt'
fileThirdSpeak = 'SpeakThird.txt'

fileFirstWrite = 'WriteFirst.txt'
fileSecondWrite = 'WriteSecond.txt'
fileThirdWrite = 'WriteThird.txt'

speakFreaquency1 = 's1'
speakFreaquency2 = 's2'
speakFreaquency3 = 's3'

writeFrequency1 = 'w1'
writeFrequency2 = 'w2'
writeFrequency3 = 'w3'

listFrequency = [speakFreaquency1,speakFreaquency2,speakFreaquency3,writeFrequency1,writeFrequency2,writeFrequency3]

FILE_START = 'п»ї'

#главный метод
def main():
    try:       
        systemWords = getSystemWords(fileSystWords)
        listSpeaker1 = list()
        listSpeaker2 = list()
        listSpeaker3 = list()
        listWrite1 = list()
        listWrite2 = list()
        listWrite3 = list()
        with open(fileLongmanWords, 'r') as reader:           
            for longmanWord in reader:
                longmanWord = getNormalLine(longmanWord,systemWords)                           
                listSpeaker1 = getCategoryLongman(listSpeaker1,longmanWord,speakFreaquency1)
                listSpeaker2 = getCategoryLongman(listSpeaker2,longmanWord,speakFreaquency2)
                listSpeaker3 = getCategoryLongman(listSpeaker3,longmanWord,speakFreaquency3)
                listWrite1 = getCategoryLongman(listWrite1,longmanWord,writeFrequency1)
                listWrite2 = getCategoryLongman(listWrite2,longmanWord,writeFrequency2)
                listWrite3 = getCategoryLongman(listWrite3,longmanWord,writeFrequency3)
            saveWordsToFile(listSpeaker1, fileFirstSpeak)
            saveWordsToFile(listSpeaker2, fileSecondSpeak)
            saveWordsToFile(listSpeaker3, fileThirdSpeak)
            saveWordsToFile(listWrite1, fileFirstWrite)
            saveWordsToFile(listWrite2, fileSecondWrite)
            saveWordsToFile(listWrite3, fileThirdWrite)
    except Exception as e:
        print(e)

#разбиение слов по категориям лонгман
def getCategoryLongman(list,longman,category):
    category = category.lower()
    longman = longman.lower()
    if category in longman:
       longman = replaceSystemWord(longman, listFrequency)
       list.append(longman)
    return list
 
#получение слов которые необходимо исключить из строки
def getSystemWords(file):
    syst = list()
    with open(fileSystWords, 'r') as reader:      
        for w in reader.readlines():           
            w = replaceSpecialSymb(str(w))                                         
            syst.append(w)
    return syst
             

#запись слов в файл и сохранение
def saveWordsToFile(listWords, fileName):
    try:
        with open(fileName,'w+',encoding='utf8') as writer:
            for word in listWords:
                writer.write(word+'\n')
    except Exception as e:
        print(e)

#замена системных слов
def replaceSystemWord(line, systemWords):     
    for sysword in systemWords: 
        if sysword in line:
            if line.startswith(sysword)!=True:
                line = line.replace(sysword,' ')                  
    return line.strip()

#приведение строки к нормальному виду
def getNormalLine(line, systemWords):
    line = line.replace(',',' ')
    line = replaceSpecialSymb(line)
    return replaceSystemWord(line, systemWords)   

#замена запятой и символа переноса строки
def replaceSpecialSymb(line):
    if line.startswith(FILE_START):
        line = line.replace(FILE_START,'')
    return line.replace('\n','')
 
    
#старт скрипта    
main()




