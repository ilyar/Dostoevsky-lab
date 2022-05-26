from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

messages = [
    'Как попали, хотели тона купить а купили вот это вот все:-) Теперь разобрались что мы лошары, но сидим холдим на всякий случай:-)',
    'Да, всем удачи! Пусть победят сильнейшие самые везучие)',
    'Привет. Желаю удачи.',
    'Всем Привет👋',
    'Сегодня хорошая погода',
    'Сегодня хорошая погода',
    'Я счастлив проводить с тобою время',
    'Мне нравится эта музыкальная композиция',
    'В больнице была ужасная очередь',
    'Сосед с верхнего этажа мешает спать',
    'Маленькая девочка потерялась в торговом центре',
]

results = model.predict(messages, k=2)
for message, sentiment in zip(messages, results):
    print(message, '=', sentiment)
