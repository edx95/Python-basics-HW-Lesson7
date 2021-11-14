''' 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.'''

from abc import ABC, abstractmethod

class Suit(ABC):
    @abstractmethod
    def __init__(self, h):
        self.suit = h

    @abstractmethod
    def coats(self):
        pass

    @abstractmethod
    def suits(self):
        pass


class Coat(ABC):
    @abstractmethod
    def __init__(self, v):
        self.coat = v

    @abstractmethod
    def coats(self):
        pass

    @abstractmethod
    def suits(self):
        pass


class Clothes(Suit, Coat):
    def __init__(self, v, h):
        super().__init__(h)
        super().__init__(v)
        self.suit = h
        self.coat = v

    def coats(self):
        print(f'На пошив одного пальто размером {self.coat} требуется {(self.coat / 6.5 + 0.5):.2f} метров ткани')

    @property
    def suits(self):
        print(
            f'На пошив одного костюма на рост {self.suit} требуется {(self.suit / 2 * self.suit + 0.3):.2f} метров ткани')

    @property
    def total(self):
        print(f'Всего понадобится {(self.coat / 6.5 + 0.5) + (self.suit / 2 * self.suit + 0.3):.2f} метров ткани')


instance = Clothes(42, 1.70)

instance.coats()
instance.suits
instance.total