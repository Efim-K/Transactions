# Transactions
## Код для виджета «Операции по счетам»

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)

### Технологии:
- python 3.12
- coverage   7.5.0
- pip        24.0
- pytest     8.2.0
- pytest-cov 5.0.0


### Инструкция для развертывания проекта:

Клонирование проекта:
```
git clone https://github.com/Efim-K/Transactions
```
Запуск:

Для запуска проекта необходимо создать виртуальное окружение venv:
 
1. Запустить команду, указанную ниже из директории проекта

  *для Windows:*
```
python -m venv venv
```
  *для Linux, macOS:*
```
python3 -m venv venv
```
2. Активировать вирутулальое окружение

  *для Windows:*
```
venv\Scripts\activate
```
  *для Linux, macOS:*
```
source ./venv/bin/activate
```
3. Установить библиотеки
```
pip install -r requirements.txt
```


### Пример вывода для одной операции:
```
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
```

Автор проекта Ефим Кашапов
