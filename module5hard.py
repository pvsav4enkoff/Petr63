import time
class Video():
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
class UrTube():
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = 'User'

    def log_in(self, nickname, password):
        for us in self.users:
            if us.nickname == nickname and us.password == hash(password):
                self.current_user = nickname
                return nickname
        return False
    def register(self, nickname, password, age):
            # self.log_out()
            for nick in self.users:
                if nick.nickname == nickname and nick.password == hash(password) and nick.age == age:
                    self.log_in(nickname,password)
                    return
                else:
                    if nick.nickname == nickname:
                        print(f'Пользователь {nick.nickname} уже существует')
                        return
                    else:
                        new_user2 = User(nickname, password, age)
                        self.users.append(new_user2)
            new_user1=User(nickname, password, age)
            self.users.append(new_user1)
            self.current_user = nickname
            self.log_out()
    def log_out(self):
        self.current_user = None

    def add(self, *new_videos):
        for new_video in new_videos:
            if not any(video.title == new_video.title for video in self.videos):
                self.videos.append(new_video)
    def get_videos(self,findStr):
        listFind=[]
        for video in self.videos:
            if findStr.lower() in video.title.lower():
                listFind.append(video.title)
        return listFind

    # Поиск возраста зрителя
    def vozrast(self):
        v = 0
        for s in self.users:
            if s.nickname == self.current_user:
                v = s.age
        return v
    def watch_video(self,playFilm):

        if self.current_user != 'User':
            i = 1
            for video in self.videos:
                if playFilm == video.title:
                    if self.vozrast() < 18 and video.adult_mode==True:
                       print("Вам нет 18 лет, пожалуйста покиньте страницу")
                       break
                    else:
                       #  Определения времени
                       if video.time_now > 1:
                            i = video.time_now
                       else:
                            i = 1
                       # Воспроизведение
                       while i <= video.duration:
                                print(i, end=' ')
                                time.sleep(1)
                                video.time_now = i
                                i += 1
                       print("Конец видео.")
                       playFilm=None
                # else:
                #     # pass
                #     print('Видео не найдено.')
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

    # pass

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
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# for i in ur.users:
#     print(i.nickname,i.password,i.age)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')