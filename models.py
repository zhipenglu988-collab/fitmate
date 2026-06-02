"""
数据模型定义
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class UserProfile:
    id: int = 1
    name: str = ""
    gender: str = ""
    birth_date: str = ""
    height_cm: float = 0.0
    weight_kg: float = 0.0
    target_weight_kg: float = 0.0
    activity_level: str = "sedentary"
    goal: str = "maintain"


@dataclass
class WeightLog:
    date: str = ""
    weight_kg: float = 0.0
    bmi: float = 0.0
    body_fat_pct: Optional[float] = None


@dataclass
class DietLog:
    date: str = ""
    meal_type: str = ""
    food_name: str = ""
    calories: float = 0.0
    protein: float = 0.0
    carbs: float = 0.0
    fat: float = 0.0


@dataclass
class WorkoutLog:
    date: str = ""
    exercise_name: str = ""
    duration_min: int = 0
    calories_burned: float = 0.0
    completed: bool = False


@dataclass
class PlanItem:
    day_of_week: int = 0
    exercise_name: str = ""
    sets: int = 0
    reps: int = 0
    duration_min: int = 0
    rest_seconds: int = 60


def profile_to_dict(profile_tuple) -> dict:
    """将 user_profile 数据库行转为 dict"""
    if not profile_tuple:
        return {}
    return {
        "name": profile_tuple[1] or "",
        "gender": profile_tuple[2] or "",
        "birth_date": profile_tuple[3] or "",
        "height_cm": profile_tuple[4] or 0,
        "weight_kg": profile_tuple[5] or 0,
        "target_weight_kg": profile_tuple[6] or 0,
        "activity_level": profile_tuple[7] or "sedentary",
        "goal": profile_tuple[8] or "maintain",
    }
