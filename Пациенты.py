# Patient: Фамилия, Имя, Отчество, Адрес, Номер медицинской карты, Диагноз.
# Создать массив объектов. Вывести:
# а) список пациентов, имеющих данный диагноз;
# б) список пациентов, номер медицинской карты которых находится в заданном интервале.
class Patient:
    def __init__(self, id, surname, name, patronymic, address, number, diagnosis=None):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.number = number
        self.diagnosis = diagnosis

    def __str__(self):
        return f'Спикок пациентов имеющих диагноз: {self.surname} {self.name} {self.patronymic}'


a = Patient(1, 'Ivanov', 'Ivan', 'Ivanovich','fffffff', 123456)
b = Patient(2, 'Ivanova', 'Olga', 'Ivanovich','ffffff', 223456, "ORV")
v = Patient(3, 'Ivanova', 'Olga', 'Ivanovich','ffff',323456, "ORV")
list1 = [a, b, v]

for patient in list1:
    if patient.diagnosis == 'ORV':

        print(patient)