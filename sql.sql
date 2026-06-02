-- 用户基本资料（单用户本地模式，可扩展多账号）
CREATE TABLE user_profile (
    id INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    birth_date TEXT,
    height_cm REAL,
    weight_kg REAL,
    target_weight_kg REAL,
    activity_level TEXT,     -- sedentary, light, moderate, active, extreme
    goal TEXT                -- lose_fat, build_muscle, maintain
);

-- 体重历史记录
CREATE TABLE weight_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    weight_kg REAL,
    bmi REAL,
    body_fat_pct REAL
);

-- 饮食记录
CREATE TABLE diet_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    meal_type TEXT,    -- breakfast, lunch, dinner, snack
    food_name TEXT,
    calories REAL,
    protein REAL,
    carbs REAL,
    fat REAL
);

-- 运动记录
CREATE TABLE workout_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    exercise_name TEXT,
    duration_min INTEGER,
    calories_burned REAL,
    completed INTEGER DEFAULT 0
);

-- 健身计划模板
CREATE TABLE plan_template (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day_of_week INTEGER,     -- 0=周一 ... 6=周日
    exercise_name TEXT,
    sets INTEGER,
    reps INTEGER,
    duration_min INTEGER,
    rest_seconds INTEGER
);

-- 成就
CREATE TABLE achievements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    badge_name TEXT,
    unlocked INTEGER DEFAULT 0,
    unlock_date TEXT
);