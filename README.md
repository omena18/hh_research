# hh_vacancies_in_kz

Провела небольшой ресерч рынка вакансий аналитиков в кз актуальный на 01.04.2022. 
Подключилась к API hh.ru, выяснила список стран, с которыми они сотрудничают, нашла в нем Кз.
Выгрузила все объявления, содержащие в своем названии "аналитик" и привела их в читабельный вид.
Посмотрела количество объявлений по городам, самый частый требуемый стаж, на какую занятость ищут сотрудников в большинстве случаев, какие навыки работодатели указывают в своих объявлениях.
Оценила минимальную, максимальную, среднюю минимальную и среднюю максимальную предлагаемую зарплату для разного стажа.
Отобрала объявления больше подходящие для меня и посмотрела предлагаемые зарплаты.

# Навыки
Использовала библиотеки:
1. requests - для запроса данных от API
2. json - для для работы с ответом запроса в виде json
3. pandas - для работы с подготовленным мною датафреймом
4. plotly.express, seaborn, matplotlib.pyplot для визуализации разными методами
5. numpy - для математических операций


# Выводы
1. Больше всего вакансий в Алмате
2. Чаще всего ищут аналитиков со сттажем 1-3 года
3. Большинство работодателей ищут работников на полный день
4. Топ-3 навыка, которые требуются чаще всего, это умение пользоваться PowerPoint, знание английского и SQL
5. минимальная предлагаемая зарплата аналитика в Кз 80000;
   максимальная предлагаемая зарплата в Алмате аналитика 1000000;
   средняя минимальная предлагаемая зарплата аналитика в кз 270200;
   средняя максимальная предлагаемая зарплата аналитика в кз 375605.
6. Зарплата у аналитиков без опыта ненамного ниже, по сравнению с теми, у кого есть стаж 1-3 года
7. Самая большая зарплата у аналитиков со стажем более 6 лет, при этом небольшой диапазон варьирования ее величины
8. Большего всего может различаться зарплата у аналитиков со стажем 3-6 лет
9. Отобрала возможные объявления для себя, потому что меня интересуют вакансии аналитика в Алмате и у меня нет опыта(((
10. Посмотрела на какую зарплату могу претендовать:
    минимальная зарплата в Алмате аналитика без опыта 80000;
    максимальная зарплата в Алмате аналитика без опыта 500000;
    средняя минимальная зарплата в Алмате аналитика без опыта 195000;
    средняя максимальная зарплата в Алмате аналитика без опыта 254000.


