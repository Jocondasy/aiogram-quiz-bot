import aiosqlite

DB_NAME = 'quiz_bot.db'

async def create_table():
    async with aiosqlite.connect(DB_NAME) as db:
        # Добавляем новые колонки correct_answers и wrong_answers
        # DEFAULT 0 означает, что при создании новой строки этим полям будет присвоено значение 0
        await db.execute('''
            CREATE TABLE IF NOT EXISTS quiz_state (
                user_id INTEGER PRIMARY KEY,
                question_index INTEGER,
                correct_answers INTEGER DEFAULT 0,
                wrong_answers INTEGER DEFAULT 0
            )
        ''')
        await db.commit()

async def update_quiz_index(user_id, index, correct_increment=0, wrong_increment=0):
    async with aiosqlite.connect(DB_NAME) as db:
        # Проверяем, существует ли пользователь
        cursor = await db.execute('SELECT correct_answers, wrong_answers FROM quiz_state WHERE user_id = ?', (user_id,))
        data = await cursor.fetchone()

        if data:
            # Если пользователь существует, обновляем его данные
            new_correct = data[0] + correct_increment
            new_wrong = data[1] + wrong_increment
            await db.execute(
                'UPDATE quiz_state SET question_index = ?, correct_answers = ?, wrong_answers = ? WHERE user_id = ?',
                (index, new_correct, new_wrong, user_id)
            )
        else:
            # Если пользователя нет, создаем новую запись
            await db.execute(
                'INSERT INTO quiz_state (user_id, question_index, correct_answers, wrong_answers) VALUES (?, ?, ?, ?)',
                (user_id, index, correct_increment, wrong_increment)
            )
        await db.commit()

async def get_quiz_index(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT question_index FROM quiz_state WHERE user_id = (?)', (user_id,)) as cursor:
            results = await cursor.fetchone()
            if results:
                return results[0]
            else:
                return 0

async def get_user_stats(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT correct_answers, wrong_answers FROM quiz_state WHERE user_id = (?)', (user_id,)) as cursor:
            results = await cursor.fetchone()
            if results:
                return {"correct": results[0], "wrong": results[1]}
            else:
                return {"correct": 0, "wrong": 0}