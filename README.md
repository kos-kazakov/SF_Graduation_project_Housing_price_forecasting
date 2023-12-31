# Skillfactory. Курс "Специализация Data Science
# [Дипломный проект. Учебный кейс «Модель прогнозирования стоимости жилья для агентства недвижимости»](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting)

## Оглавление
* [1. Описание проекта](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/README.md#Описание-проекта)
* [2. Решаемые задачи](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/README.md#Решаемые-задачи)
* [3. Этапы проекта](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/README.md#Этапы-проекта)
* [4. Метрики качества](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/README.md#Метрики-качества)
* [5. Описание данных](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/README.md#Описание-данных)
* [6. Результаты](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/README.md#Результаты)
* [7. Итоговая оценка](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/README.md#Итоговая-оценка)

## Описание проекта
 Агентство недвижимости столкнулось с проблемой — риелторы тратят слишком много времени на сортировку объявлений и поиск выгодных предложений. Поэтому скорость их реакции и качество анализа не дотягивают до уровня конкурентов. Это сказывается на финансовых показателях агентства. Задача - разработать модель машинного обучения, которая поможет обрабатывать объявления и увеличит число сделок и прибыль агентства.

## Решаемые задачи
- Провести разведывательный анализ и очистку исходных данных. Необходимо отыскать закономерности, расшифровать сокращения, найти синонимы в данных, обработать пропуски и удалить выбросы.
- Выделить наиболее значимые факторы, влияющие на стоимость недвижимости.
- Построить модель для прогнозирования стоимости недвижимости.
- Разработать небольшой веб-сервис, на вход которому поступают данные о некоторой выставленной на продажу недвижимости, а сервис прогнозирует его стоимость.

## Этапы проекта
- [Исследование структуры, обработка и очистка данных](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/1_Data_cleaning_Housing_price_forecasting.ipynb)
- [Baseline-решение и разведывательный анализ данных](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/2_EDA_Housing_price_forecasting.ipynb)
- [Применение алгоритмов Machine Learning, оценка качества моделей и подготовка к продакшену](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/3_Modeling_Housing_price_forecasting.ipynb)

## Метрики качества
- MAE - средняя абсолютная ошибка. Показывает насколько в среднем число в предсказании разошлось с реальным числом.
- MAPE - средняя абсолютная ошибка в процентах.
- RMSE - стандартное отклонение предсказаний от истинных ответов.
- R2 - коэффициент детерминации. Помогает понять, какую долю разнообразия смогла уловить модель в данных.
   
## Описание данных

- data.csv - датасет с данными об объектах недвижимости

Описание признков:
- 'status' — статус продажи
- 'private pool' и 'PrivatePool' — наличие собственного бассейна
- 'propertyType' — тип объекта недвижимости
- 'street' — адрес объекта
- 'baths' — количество ванных комнат
- 'homeFacts' — сведения о строительстве объекта (содержит несколько типов сведений, влияющих на оценку объекта)
- 'fireplace' — наличие камина
- 'city' — город
- 'schools' — сведения о школах в районе
- 'sqft' — площадь в футах
- 'zipcode' — почтовый индекс
- 'beds' — количество спален
- 'state' — штат
- 'stories' — количество этажей
- 'mls-id' и 'MlsId' — идентификатор MLS (Multiple Listing Service, система мультилистинга)
- **'target'** — цена объекта недвижимости (целевой признак, который необходимо спрогнозировать)

## Результаты
- В процессе предобработки произведено исследование структуры данных, выявлены и устранены дубликаты и пропущенные значения.
- Подготовлено baseline-решение на основе обработанных данных. Произведено моделирование с помощью алгоритмов линейной регрессии и градиентного бустинга.
- Произведен разведывательный анализ данных (очистка от выбросов, преобразование и создание новых признаков, анализ взаимного влияния и важности признаков).
- Решена задача регрессии с использованием алгоритмов: линейная регрессия Linear Regression, полиномиальная регрессия Polynomial Regression, дерево решений Decision Tree, случайный лес Random Forest, градиентный бустинг Gradient Boosting.
- Для продакшена по результатам сравнения метрик качества выбрана модель градиентного бустинга.
- Проведен деплой модели на сервер и контейнеризация. Файлы модели, сервера, клиента и Dockerfile размещены в папке web.

## Итоговая оценка
Оценка ментора: 25 из 25 баллов.

[Отзыв ментора](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/tree/main/doc/k.kazakov.work@gmail.com_mentor_review.pdf)
_________________________

##  [К оглавлению](https://github.com/kos-kazakov/SF_Graduation_project_Housing_price_forecasting/blob/main/README.md#Оглавление)

