import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        if self.user_exist(nickname):
            print(f"Users {nickname} already exist")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Create user {nickname}")

    def user_exist(self, nickname):
        for user in self.users:
            if user.nickname == nickname:
                return True
        return False

    def log_in(self, nickname, password):
        hashed_password = hash(str(password))
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"User {nickname} entered in system")
                return
        print(f"User {nickname} not found")

    def log_out(self):
        self.current_user = None
        print("You exited of the system")

    def add(self, *args):
        for vid in args:
            if self.video_exist(vid.title):
                print(f"Video '{vid.title}' already exist")
            else:
                self.videos.append(vid)
                print(f"Video '{vid.title}' has been added")

    def video_exist(self, title):
        for vid in self.videos:
            if vid.title == title:
                return True
        return False

    def get_videos(self, key_word):
        found_videos = []
        for vid in self.videos:
            if key_word.lower() in vid.title.lower():
                found_videos.append(vid.title)
        return found_videos

    def watch_video(self, vid_title):
        if self.current_user is None:
            print("Log in to watch the video")
        else:
            found = False
            for vid in self.videos:
                if vid.title == vid_title:
                    found = True
                    if vid.adult_mode and self.current_user.age < 18:
                        print("Your age is less than 18 years old, please leaved this page")
                    else:
                        while vid.time_now != vid.duration+1:
                            time.sleep(0.1)
                            print(vid.time_now, end=" ")
                            vid.time_now += 1
                        time.sleep(1)
                        vid.time_now = 0
                        print("The END")
            if not found:
                print(f"Video '{vid_title}' not found")

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

