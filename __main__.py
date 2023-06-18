from flask import Flask, render_template, request
import random

app = Flask(__name__)

slownik = [
    "Szczęście", "Uśmiech", "Miłość", "Przygoda", "Przyjaźń", "Radość", "Humor", "Śmiech", "Dobre", "Samopoczucie",
    "Entuzjazm", "Ekscytacja", "Zabawa", "Impreza", "Optymizm", "Energia", "Kreatywność", "Ekstaza", "Wolność",
    "Poważanie", "Spełnienie", "Sztuka", "Muzyka", "Tańce", "Celebracja", "Uczta", "Festiwal", "Wesołość", "Rozrywka",
    "Entertainment", "Ekwilibrystyka", "Sztuczki", "Dowcip", "Komediant", "Komedia", "Teatr", "Farsa", "Bajka", "Święto",
    "Rytuał", "Karnawał", "Bal", "Roztańczenie", "Imprezowość", "Rozkosz", "Świętowanie", "Euforia", "Uciecha",
    "Rozweselanie", "Pleasure", "Uciechowisko", "Zaklęcie", "Rozświetlenie", "Kolor", "Dźwięk", "Harmonia", "Rozmarzenie",
    "Fascynacja", "Zabawa", "Zawadiackość", "Hulanka", "Piknik", "Słodkości", "Balanga", "Odlotowość", "Beztroska",
    "Szaleństwo", "Biesiada", "Podniecenie", "Emocje", "Festiwalowy", "Towarzystwo", "Przytulność", "Uciekanie",
    "Porażka", "Wzburzenie", "Intryga", "Niezwykłość", "Przeżycie", "Szaradziarstwo", "Magia", "Brawura", "Mistrzostwo",
    "Rywalizacja", "Zapał", "Wariactwo", "Podniebienie", "Szaszłyk", "Słodko", "Ostra", "Szałas", "Draka", "Hulajnoga",
    "Skrzydło", "Taniec", "Wystrzał", "Szalony", "Wariacja", "Rozbawienie", "Pozbawienie", "Przyciąganie", "Chichot",
    "Rozkoszowanie", "Wesołość", "Kołysanie", "Uciecha", "Nawrócenie", "Skrzypce", "Przekręt", "Pojedynek", "Szturchnięcie",
    "Wprowadzenie", "Taniec", "Kołowrotek", "Wybawienie", "Pocieszka", "Kuszenie", "Festiwal", "Roztańczony",
    "Natchnienie", "Zabawianie", "Hulajnoga", "Podchody", "Znudzenie", "Szaradziarz", "Słodki", "Kokietka", "Spędzanie",
    "Wesołość", "Bujanie", "Dźwięk", "Odprężenie", "Okrągłość", "Wyrazistość", "Cudowność", "Cyrk", "Zabawni", "Dzikus",
    "Mieszanka", "Wariactwo", "Szaleństwo", "Zamieszanie", "Wodewil", "Klawiatura", "Impresjonista", "Kiermasz", "Kaskader",
    "Błazen", "Targi", "Harce", "Zadziorność", "Huczność", "Napad", "Harcownik", "Turlanie", "Skok", "Nakręcanie",
    "Kolorowość", "Piosenka", "Wesołość", "Podskok", "Harmonijność", "Uśmiech", "Zawadiactwo", "Gorzkość", "Przebój",
    "Wybuchowość", "Udanie", "Cieszenie", "Żarty", "Jarmark", "Błogość", "Gra", "Bryka", "Przeskakiwanie", "Uciechowość",
    "Podnoszenie", "Mistrz", "Pomysłowość", "Fascynowanie", "Zauroczenie", "Chichoczący", "Szerokość", "Odpoczynek",
    "Zaskoczenie", "Dobro", "Przyjemność", "Rozbawienie", "Komediancki", "Roztargnienie", "Swawola", "Odprężenie",
    "Relaks", "Oddech", "Podskakiwanie", "Pociecha", "Rozmarzenie", "Wesołość", "Wyczyny", "Kaprys", "Przebłysk",
    "Szerszenie", "Eskapada", "Roztkliwienie", "Szarada", "Szaleństwo", "Balanga", "Niespodzianka", "Balonik",
    "Urozmaicenie", "Rozświetlenie", "Wspaniałość", "Radośnie", "Brawurowość", "Hulaj", "Skaczę", "Ponętność", "Stawanie",
    "Imprezowanie", "Pustka", "Ulotność", "Działanie", "Wyskok", "Klownada", "Słodka", "Świetny", "Entuzjastyczny",
    "Roztańczony", "Rozśmieszanie", "Odrobina", "Harmonijność", "Uniesienie", "Gwar", "Błazenada", "Wytworność",
    "Szelest", "Roztargnienie", "Szczęśliwość", "Radosne", "Biesiadowanie", "Uśmiech", "Zaczarowanie", "Ożywienie",
    "Niesforność", "Szarada", "Rozładowanie", "Rozkochanie", "Zawieszanie", "Wesołość", "Pikantność", "Wesoły",
    "Rozkoszowanie", "Roztargnienie", "Szalony", "Uciecha", "Swoboda", "Impreza", "Zachwyt", "Krzyk", "Wzruszenie",
    "Radosna", "Tropienie", "Harmonia", "Oczarowanie", "Zaskoczenie", "Bajeczność", "Szaleństwo", "Biesiadnik",
    "Rozbawienie", "Rozczarowanie", "Szczęście", "Wyczynowość", "Szybkość", "Zachwyt", "Wesołość", "Podpalanie",
    "Namiętność", "Głupawka", "Utrzymanie", "Szczęśliwiec"]
def losuj_slowo():
    return random.choice(slownik)
slowo = losuj_slowo()
ukryte_slowo = "_" * len(slowo)
licznik_bledow = 0
wykorzystane_litery = []

def rysuj_szubienice(bledy):
    szubienica = [
        "________",
        "|      |",
        "|      O",
        "|     /|\\",
        "|     / \\",
        "|",
        "|___"
    ]

    return szubienica[:bledy]

@app.route('/')
def index():
    return render_template('index.html', slowo=ukryte_slowo, bledy=licznik_bledow, wykorzystane=wykorzystane_litery)

@app.route('/', methods=['POST'])
def zgaduj():
    global slowo, ukryte_slowo, licznik_bledow, wykorzystane_litery
    litera = request.form['litera']
    wykorzystane_litery.append(litera)

    if litera in slowo:
        for i in range(len(slowo)):
            if slowo[i] == litera:
                ukryte_slowo = ukryte_slowo[:i] + litera + ukryte_slowo[i+1:]
    else:
        licznik_bledow += 1

    if licznik_bledow >= 7 or ukryte_slowo == slowo:
        return render_template('koniec.html', slowo=slowo, ukryte_slowo=ukryte_slowo, bledy=licznik_bledow)

    return render_template('index.html', slowo=ukryte_slowo, bledy=licznik_bledow, wykorzystane=wykorzystane_litery, szubienica=rysuj_szubienice(licznik_bledow))

if __name__ == '__main__':
    app.run(debug=True)
