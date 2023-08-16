class Employee:
    list = []

    def __init__(self, nome, numero, salario):
        self.nome = nome
        self.numero = numero
        self.salario = salario

    @classmethod
    def sem_argumentos(cls):
        return cls(None, None, None)

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario = salario

    @classmethod
    def insert(cls):
        nome = input('Enter employee name: ')
        numero = input('Enter employee number: ')
        salario = float(input('Enter employee salary: '))
        cls.list.append(Employee(nome, numero, salario))
        print('Employee added!')

    @classmethod
    def display(cls):
        for emp in cls.list:
            print(emp)

    @classmethod
    def search(cls):
        numero = input('Enter employee number to search: ')
        for emp in cls.list:
            if emp.numero == numero:
                print(emp.nome, emp.numero, emp.salario)

    @classmethod
    def delete(cls):
        numero = input('Enter employee number to delete: ')
        for emp in cls.list:
            if emp.numero == numero:
                cls.list.remove(emp)
                print('Employee deleted!')

    @classmethod
    def apply_raise(cls):
        numero = input('Enter employee number to apply raise (10%): ')
        for emp in cls.list:
            if emp.numero == numero:
                emp.salario *= 1.1

    @classmethod
    def update_salary(cls):
        numero = input('Enter employee number to update salary: ')
        new_salary = float(input('Enter the new salary: '))
        for emp in cls.list:
            if emp.numero == numero:
                emp.salario = new_salary
                print('Salary updated!')

    def __str__(self):
        return f"Nome: {self.nome}, Número: {self.numero}, Salário: {self.salario:.2f}"

    # observação:
    # cls -> todas as instancias da classe
    # emp -> uma unica instancia da classe