from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        print(self.__color[0])
        sleep(7)
        print(self.__color[1])
        sleep(2)
        print(self.__color[2])
        sleep(10)


list = ['RED', 'YELLOW', 'GREEN']
t_l = TrafficLight(list)
while True:
    t_l.running()