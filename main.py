import speech_recognition as sr
import pyttsx3 
import datetime
import wikipedia
import pywhatkit
audio = sr.Recognizer()
maquina = pyttsx3.init()
def executa_comando():
 try:
  with sr.Microphone() as source:
    print('Fale...')
    voz = audio.listen(source)
    comand = audio.recognize_google(voz, language='pt-BR')
    comand = comand.lower()
    if 'agnes' in comand:
        comand = comand.replace('agnes', '')
        maquina.say(comand)
        maquina.runAndWait()
 except:
    print("Microfone com erro")
 return comand 

def comando_voz_user():
    comand = executa_comando()
    if 'horas' in comand:
        hora = datetime.datetime.now().strftime('%H:%M:%S')
        maquina.say(f'São {hora}')
        maquina.runAndWait()
    elif 'data' in comand:
        data = datetime.datetime.now().strftime('%d/%m/%Y')
        maquina.say(f'Hoje é {data}')
        maquina.runAndWait()
    elif 'tudo bem' in comand:
        maquina.say('Estou bem, obrigado!')
        maquina.runAndWait()
    elif 'bom dia' in comand:
        data = datetime.datetime.now().strftime('%d/%m/%Y')
        hora = datetime.datetime.now().strftime('%H:%M:%S')
        maquina.say(f'Bom dia Hoje é {data},' + 'são' + hora)
        maquina.runAndWait()
    elif 'como você está' in comand:
        maquina.say('Estou bem, obrigado!')
        maquina.runAndWait()
    elif 'procure por' in comand:
        procurar = comand.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'pesquise por' in comand:
        procurar = comand.replace('pesquise por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comand:
        musica = comand.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando' + musica)
        maquina.runAndWait()
    elif 'piada' in comand:
        maquina.say('O que o pato disse para o outro pato? Quack, quack!')
        maquina.runAndWait()
    elif 'quem é você' in comand:
        maquina.say('Eu sou a Agnes, uma assistente virtual.')
        maquina.runAndWait()
    elif 'quem é agnes' in comand:
        maquina.say('Foi me dado esse nome devido ao meu criador, ele ama uma Agnes.')
        maquina.runAndWait()
    elif 'quem é seu criador' in comand:
        maquina.say('Meu criador é o Pedro Silva')
        maquina.runAndWait()
    elif 'tchau' in comand:
        maquina.say('Até mais!')
        maquina.runAndWait()
        exit()
 
comando_voz_user()