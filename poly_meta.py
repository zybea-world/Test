from abc import abstractmethod,ABCMeta

class Employee(object,metaclass=ABCMeta):

    def __init__(self,name):

        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def salory(self):

        pass

class Manager(Employee):

    _base = 15000
    def salory(self):
        print(f'\nManeger {self.name},your salory is {self._base}')

class Saler(Employee):
    _base = 1500
    def __init__(self,name,sale=0):
        super().__init__(name)
        self._sale = sale

    @property
    def sale(self):
        return self._sale

    @sale.setter
    def sale(self,sale):
        self._sale = sale

    def salory(self):
        all = self._base+self._sale*0.1
        print(f'\nSaler {self.name},your salory is {all}')

class Programer(Employee):

    def __init__(self,name,workhours=0):
        super().__init__(name)
        self._workhours = workhours

    @property
    def workhours(self):
        return self._workhours

    @workhours.setter
    def workhours(self,workhours):
        self._workhours = workhours

    def salory(self):
        salo = self.workhours*200
        print(f'\nProgramer{self.name},your salory is {salo}')

def main():
    for em in [Programer('Mike'),Saler('Alice'),Manager('Poly')]:
        if isinstance(em,Programer):
            em.workhours = int(input(f"Programmer {em.name} workours is :"))
        elif isinstance(em,Saler):
            em.sale  = int(input(f"Saler {em.name} total_sale is :"))
        em.salory()


if __name__=='__main__':
    main()