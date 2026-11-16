class Musician:
    def __init__(self, name='', age=0, gonorar=0):
        self.name = name
        self.age = age
        self.gonorar = gonorar

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gonorar(self):
        return self.gonorar

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gonorar(self, gonorar):
        self.gonorar = gonorar

    def __str__(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Гонорар: {self.gonorar}"
    def show_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Гонорар: {self.gonorar}")

    def __repr__(self):
        return f"Musician({self.name}, {self.age}, {self.gonorar})"

    def __del__(self):
        print(f"Деструктор Musician: об'єкт '{self.name}' видалено.")


class MusicFestival:
    def __init__(self, name='', max_bid=0, vikonavtsi=None):
        self.name = name
        self.max_bid = max_bid
        self.vikonavtsi = []
        if vikonavtsi is None:
            vikonavtsi = []
        for musician in vikonavtsi:
            self.add_musician(musician)

    def __del__(self):
        print(f"Деструктор MusicFestival: фестиваль '{self.name}' видалено.")

    def get_name(self):
        return self.name

    def get_max_bid(self):
        return self.max_bid

    def get_vikonavtsi(self):
        return self.vikonavtsi

    def set_name(self, name):
        self.name = name

    def set_max_bid(self, max_bid):
        self.max_bid = max_bid

    def set_vikonavtsi(self, vikonavtsi):
        self.vikonavtsi = []
        for musician in vikonavtsi:
            self.add_musician(musician)

    def __str__(self):
        return f"Назва: {self.name}, Максимальний бюджет: {self.max_bid}, Виконавці: {self.vikonavtsi}"

    def get_total_cost(self):
            return sum(musician.get_gonorar() for musician in self.vikonavtsi)

    def add_musician(self, musician):
        if musician in self.vikonavtsi:
            print(f"Виконавець {musician.get_name()} вже є у списку фестивалю.")
            return False
        if self.get_total_cost() + musician.get_gonorar() <= self.max_bid:
            self.vikonavtsi.append(musician)
            print(f"Виконавець {musician.get_name()} успішно доданий до фестивалю.")
            return True
        print(f"Не вдалося додати {musician.get_name()}. Перевищено бюджет фестивалю.")
        return False

    def remove_musician(self, musician):
        if musician in self.vikonavtsi:
            self.vikonavtsi.remove(musician)
            print(f"Виконавець {musician.get_name()} успішно видалений з фестивалю.")
            return True
        print(f"Виконавець {musician.get_name()} не знайдений у списку фестивалю.")
        return False

    def show_festival_info(self):
        print(f"Музичний фестиваль: '{self.name}'")
        print(f"Максимальний бюджет: ${self.max_bid:.2f}")
        print(f"Поточний витрачений бюджет: ${self.get_total_cost():.2f}")
        print(f"Залишок бюджету: ${self.max_bid - self.get_total_cost():.2f}")
        print("Список запрошених виконавців:")
        if not self.vikonavtsi:
            print("  (Список порожній)")
        else:
            for i, m in enumerate(self.vikonavtsi, start=1):
                print(f"  {i}. ", end="")
                m.show_info()


def main():
    musician1 = Musician('Morgen', 31, 5000)
    musician2 = Musician('Amargalieva', 28, 1500)
    musician3 = Musician('Fest', 40, 2000)

    festival = MusicFestival('FLEYZEN Music Festival', 7000, [musician1, musician2, musician3])
    festival.show_festival_info()

    festival.add_musician(musician3)
    festival.remove_musician(musician1)
    festival.add_musician(musician3)
    festival.show_festival_info()

    for i in festival.get_vikonavtsi():
        print(i.get_name())

main()