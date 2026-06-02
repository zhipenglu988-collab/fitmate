import sqlite3
from datetime import datetime, date

DB_PATH = "fitmate.db"


def init_db():
    """初始化数据库，创建所有表"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS user_profile (
            id INTEGER PRIMARY KEY,
            name TEXT,
            gender TEXT,
            birth_date TEXT,
            height_cm REAL,
            weight_kg REAL,
            target_weight_kg REAL,
            activity_level TEXT,
            goal TEXT
        );

        CREATE TABLE IF NOT EXISTS weight_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            weight_kg REAL,
            bmi REAL,
            body_fat_pct REAL
        );

        CREATE TABLE IF NOT EXISTS diet_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            meal_type TEXT,
            food_name TEXT,
            calories REAL,
            protein REAL,
            carbs REAL,
            fat REAL
        );

        CREATE TABLE IF NOT EXISTS workout_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            exercise_name TEXT,
            duration_min INTEGER,
            calories_burned REAL,
            completed INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS plan_template (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day_of_week INTEGER,
            exercise_name TEXT,
            sets INTEGER,
            reps INTEGER,
            duration_min INTEGER,
            rest_seconds INTEGER
        );

        CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            badge_name TEXT,
            unlocked INTEGER DEFAULT 0,
            unlock_date TEXT
        );
    """)
    conn.commit()
    conn.close()


class DBHelper:
    """数据库增删改查封装"""

    # ── 用户资料 ──
    @staticmethod
    def get_profile():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT * FROM user_profile WHERE id=1")
        row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update_profile(data):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            REPLACE INTO user_profile (id, name, gender, birth_date, height_cm,
                                       weight_kg, target_weight_kg, activity_level, goal)
            VALUES (1, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get("name", ""),
            data.get("gender", ""),
            data.get("birth_date", ""),
            data.get("height_cm", 0),
            data.get("weight_kg", 0),
            data.get("target_weight_kg", 0),
            data.get("activity_level", ""),
            data.get("goal", ""),
        ))
        conn.commit()
        conn.close()

    # ── 体重日志 ──
    @staticmethod
    def insert_weight(weight_kg, bmi, body_fat_pct=0):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO weight_log (date, weight_kg, bmi, body_fat_pct) VALUES (?, ?, ?, ?)",
            (date.today().isoformat(), weight_kg, bmi, body_fat_pct)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_weight_history(limit=20):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "SELECT date, weight_kg, bmi, body_fat_pct FROM weight_log ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        rows = cur.fetchall()
        conn.close()
        return rows

    # ── 饮食日志 ──
    @staticmethod
    def insert_diet(meal_type, food_name, calories, protein=0, carbs=0, fat=0):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO diet_log (date, meal_type, food_name, calories, protein, carbs, fat) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (date.today().isoformat(), meal_type, food_name, calories, protein, carbs, fat)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_diet_log(target_date=None):
        if target_date is None:
            target_date = date.today().isoformat()
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "SELECT meal_type, food_name, calories, protein FROM diet_log WHERE date=? ORDER BY id",
            (target_date,)
        )
        rows = cur.fetchall()
        conn.close()
        return rows

    # ── 运动日志 ──
    @staticmethod
    def insert_workout(exercise_name, duration_min, calories_burned, completed=1):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO workout_log (date, exercise_name, duration_min, calories_burned, completed) "
            "VALUES (?, ?, ?, ?, ?)",
            (date.today().isoformat(), exercise_name, duration_min, calories_burned, completed)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_workout_log():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT date, exercise_name, duration_min, calories_burned FROM workout_log ORDER BY id DESC")
        rows = cur.fetchall()
        conn.close()
        return rows

    # ── 健身计划 ──
    @staticmethod
    def clear_plan():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("DELETE FROM plan_template")
        conn.commit()
        conn.close()

    @staticmethod
    def insert_plan(day_of_week, exercise_name, sets, reps, duration_min, rest_seconds):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO plan_template (day_of_week, exercise_name, sets, reps, duration_min, rest_seconds) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (day_of_week, exercise_name, sets, reps, duration_min, rest_seconds)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_plan():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "SELECT day_of_week, exercise_name, sets, reps, duration_min, rest_seconds "
            "FROM plan_template ORDER BY day_of_week, id"
        )
        rows = cur.fetchall()
        conn.close()
        return rows

    # ── 成就徽章 ──
    @staticmethod
    def get_achievements():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT badge_name, unlocked, unlock_date FROM achievements ORDER BY id")
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def unlock_achievement(badge_name):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "UPDATE achievements SET unlocked=1, unlock_date=? WHERE badge_name=?",
            (date.today().isoformat(), badge_name)
        )
        conn.commit()
        conn.close()

    # ── 初始化成就数据（首次运行调用） ──
    @staticmethod
    def init_achievements():
        badges = ["初次记录", "坚持一周", "健身达人", "体重达标", "饮食自律"]
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        for b in badges:
            cur.execute(
                "INSERT OR IGNORE INTO achievements (badge_name, unlocked, unlock_date) VALUES (?, 0, NULL)",
                (b,)
            )
        conn.commit()
        conn.close()
