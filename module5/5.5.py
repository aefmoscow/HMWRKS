from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    #     вернем полученные данные в метод login
    def getinfo(self):
        return self.nickname, self.password

    # добавим строкового отображения для верной работы метода register
    def __str__(self):
        return self.nickname

    #     теперь проверим есть ли такие пользователи
    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    # в связи с не отображением титлов из задания, вставим костыль, либо распаковать объекты данных в print *ur
    def __repr__(self):
        return self.title

    # def __contains__(self, item):


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if (login, hash(password)) == user.getinfo():
                self.current_user = user
                return user

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        for film in videos:
            if film.title not in self.videos:
                self.videos.append(film)

    def get_videos(self, search):
        title = []
        for film in self.videos:
            if search.lower() in str(film).lower():
                title.append(film)
        return title

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for film in self.videos:
            if title == film.title:
                if film.adult_mode and self.current_user.age >= 18:
                    while film.time_now < film.duration:
                        film.time_now += 1
                        print(film.time_now, end=' ')
                        sleep(0.2)
                    print('Конец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
