from gtts import gTTS
from playsound import playsound

while palavra != 'sair':
  palavra=input("Digite a palavra que deseja que o audio reproduza:")

  s=gTTS(palavra, lang="pt")
  s.save('sample.mp3')
    playsound('sample.mp3')

