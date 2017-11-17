# This python file uses the following encoding: utf-8
import collections
import sys

# Creates an immutible (unchanging) data structure
# It's great for concurrent programing supprted in Python 3
Message = collections.namedtuple('Message', [
    'language',
    'message',
])

messages = (
    Message(language='bulgarian',   message='Здравей, Мрежа!'),
    Message(language='croatian',    message='Pozdrav, mreža!'),
    Message(language='czech',       message='Dobrý den, síť!'),
    Message(language='danish',      message='Hej, netværk!'),
    Message(language='english',     message='Hello, Network!'),
    Message(language='estonian',    message='Tere, võrk!'),
    Message(language='finnish',     message='Hei, verkko!'),
    Message(language='german',      message='Hallo, Netzwerk!'),
    Message(language='greek',       message='Γεια σας, Δίκτυο!'),
    Message(language='hungarian',   message='Helló, hálózat!'),
    Message(language='irish',       message='Dia duit, Líonra!'),
    Message(language='italian',     message='Ciao, rete!'),
    Message(language='latvian',     message='Sveiki, tīkls!'),
    Message(language='lithuanian',  message='Sveiki, Tinklas!'),
    Message(language='maltese',     message='Bongu, Netwerk!'),
    Message(language='polish',      message='Cześć, sieci!'),
    Message(language='portuguese',  message='Olá, rede!'),
    Message(language='romanian',    message='Bună, Rețea!'),
    Message(language='slovak',      message='Dobrý deň, sieť!'),
    Message(language='slovenian',   message='Pozdravljeni, mreženje!'),
    Message(language='spanish',     message='Hola, ¡Red!'),
    Message(language='swedish',     message='Hej, Nätverk!'),
)


# Check if language exist in messages, returns True or False
def language_exist(language):
    return any(x.language == language for x in messages)


def language():
    language = ' '.join(sys.argv[1:])
    if not language_exist(language):
        language = 'english'  # Default language
    return language


#  Filter messages after selected language
def filter_language(language):
    return [x for x in messages if x.language == language]


def print_message(language):
    message = ' '.join(
        [str(x.message) for x in messages if x.language == language])
    print(message)


def main():
    print_message(language())


if __name__ == '__main__':
    main()
