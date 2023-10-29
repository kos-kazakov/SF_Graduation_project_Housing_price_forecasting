import requests

if __name__ == '__main__':
    # Отправляем запрос на сервер с набором данных
    r = requests.post('http://localhost:5000/predict',
        json=[5, 5000, 4, 6, 1, 1, 2022, 1, 1, 1, 9.5, 1.8, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 9, 154])
    
    print('Статус сервера:', r.status_code)
    
    # Получаем предсказание стоимости недвижимости
    if r.status_code == 200:
        print('Ответ сервера - предсказание:', r.json()['prediction'])
    else:
        print('Ответ сервера:', r.text)