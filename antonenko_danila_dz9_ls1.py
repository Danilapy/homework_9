import time


class TrafficLight:
    __color = 'red'

    def running(self):
        print('Светофор работает')

        self.__color = 'red'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(7)

        self.__color = 'yellow'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'green'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(5)

        while True:
            self.running()


traff_light = TrafficLight()
print(traff_light.running())
