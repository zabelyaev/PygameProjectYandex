import sqlite3

from patterns import Singleton


class DBManager(Singleton):
    def __init__(self):
        self.db = sqlite3.connect('data/db/game.db')
        self.cur = self.db.cursor()

    def start_new_game(self) -> None:
        self.reset_game()
        self.cur.execute('INSERT INTO save (current_level) VALUES (1)')
        self.db.commit()

    def fetch_current_level(self) -> (str, bool):
        levels = self.cur.execute('SELECT * FROM save').fetchone()

        if not levels:
            self.start_new_game()

        res = self.cur.execute('''SELECT name, end_game FROM levels
                                  INNER JOIN save ON save.current_level = levels.id
                                  WHERE save.current_level = levels.id''').fetchone()
        level_name = res[0]
        end_game = int(res[1])

        if end_game == 1:
            end_game = True
        else:
            end_game = False

        return level_name, end_game

    def increase_level(self) -> bool:
        id = int(self.cur.execute('SELECT id FROM save').fetchone()[0])
        current_level = int(self.cur.execute(f'SELECT current_level FROM save WHERE id={id}').fetchone()[0])
        if current_level + 1 <= self.count_levels():
            self.cur.execute(f'''UPDATE save SET current_level={current_level + 1} WHERE id={id}''')
            self.db.commit()
            return True

        self.end_game(True)
        return False

    def increase_score(self, level_increase) -> None:
        id = int(self.cur.execute('SELECT id FROM save').fetchone()[0])
        if id:
            self.cur.execute(f'''UPDATE save SET score=score+{level_increase} WHERE id={id}''')
            self.db.commit()

    def fetch_score(self) -> int:
        id = int(self.cur.execute('SELECT id FROM save').fetchone()[0])
        score = int(self.cur.execute(f'SELECT score FROM save WHERE id={id}').fetchone()[0])

        return score

    def end_game(self, end: bool) -> None:
        if end:
            end = 1
        else:
            end = 0
        id = int(self.cur.execute('SELECT id FROM save').fetchone()[0])
        self.cur.execute(f'''UPDATE save SET end_game={end} WHERE id={id}''')
        self.db.commit()

    def count_levels(self) -> int:
        res = self.cur.execute('SELECT COUNT(id) FROM levels').fetchone()

        return int(res[0])

    def reset_game(self) -> None:
        self.cur.execute('DELETE FROM save')
        self.db.commit()
