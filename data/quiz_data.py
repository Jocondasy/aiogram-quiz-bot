quiz_data = [
    # Вопрос 1
    {
        'question': 'Какое ключевое слово используется для объявления асинхронной функции в Python?',
        'options': ['async def', 'function', 'deffunc', 'await'],
        'correct_option': 0
    },
    # Вопрос 2
    {
        'question': 'Что делает `await asyncio.sleep(5)`?',
        'options': ['Загружает процессор на 5 секунд', 'Приостанавливает выполнение и передает управление на 5 секунд', 'Удаляет файл через 5 секунд', 'Завершает программу'],
        'correct_option': 1
    },
    # Вопрос 3
    {
        'question': 'Какой инструмент в `asyncio` используется для параллельного запуска нескольких задач и ожидания их всех?',
        'options': ['asyncio.run()', 'asyncio.create_task()', 'asyncio.gather()', 'asyncio.wait()'],
        'correct_option': 2
    },
    # Вопрос 4
    {
        'question': 'Для какого типа задач `asyncio` наиболее эффективен?',
        'options': ['Связанных с ожиданием (I/O-bound)', 'Связанных с вычислениями (CPU-bound)', 'Для всех задач одинаково', 'Только для работы с текстом'],
        'correct_option': 0
    },
    # Вопрос 5
    {
        'question': 'Что используется для защиты общих данных от "состояния гонки" в асинхронном коде?',
        'options': ['asyncio.Queue', 'asyncio.Event', 'asyncio.Semaphore', 'asyncio.Lock'],
        'correct_option': 3
    },
    # Вопрос 6
    {
        'question': 'Как называется специальный цикл для перебора асинхронного генератора?',
        'options': ['for await', 'while async', 'async for', 'loop'],
        'correct_option': 2
    },
    # Вопрос 7
    {
        'question': 'Какая библиотека используется для создания асинхронных Telegram-ботов и построена на asyncio?',
        'options': ['telebot', 'python-telegram-bot', 'aiogram', 'requests'],
        'correct_option': 2
    },
    # Вопрос 8
    {
        'question': 'Что вернет вызов `await some_async_function()`?',
        'options': ['Объект-корутину', 'Результат выполнения функции', 'Ничего (None)', 'Строку "await"'],
        'correct_option': 1
    },
    # Вопрос 9
    {
        'question': 'Какой декоратор в aiogram используется для обработки команды, например, `/start`?',
        'options': ['@dp.on_command', '@dp.message(Command("start"))', '@dp.handler', '@dp.start'],
        'correct_option': 1
    },
    # Вопрос 10 
    {
        'question': 'Что такое "callback_data" у Inline-кнопки в Telegram?',
        'options': ['Текст на кнопке', 'Ссылка на сайт', 'Скрытые данные, отправляемые боту при нажатии', 'Цвет кнопки'],
        'correct_option': 2
    }
]