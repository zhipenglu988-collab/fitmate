def generate_plan(goal, activity_level):
    # 基础动作库 (名称, 组数, 次数/时长)
    exercises_lib = {
        "lose_fat": [
            ("跑步", 1, 30),
            ("跳绳", 1, 15),
            ("HIIT", 1, 20),
            ("仰卧起坐", 3, 20),
            ("深蹲", 4, 15)
        ],
        "build_muscle": [
            ("卧推", 4, 10),
            ("引体向上", 3, 8),
            ("深蹲", 5, 10),
            ("硬拉", 4, 8),
            ("肩推", 4, 10)
        ],
        "maintain": [
            ("快走", 1, 30),
            ("瑜伽", 1, 20),
            ("俯卧撑", 3, 15),
            ("平板支撑", 3, 60)
        ]
    }
    # 根据活动水平微调
    factor = 1.0
    if activity_level == "sedentary":
        factor = 0.7
    elif activity_level == "active":
        factor = 1.3
    elif activity_level == "extreme":
        factor = 1.6

    exercises = exercises_lib.get(goal, exercises_lib["maintain"])
    plan = []

    for day in range(7):  # 0=周一, ..., 6=周日
        if day in [5, 6]:  # 周末休息或轻量
            ex_today = exercises[-2:]
        else:
            ex_today = exercises[:3]

        adjusted = []
        for name, sets, reps in ex_today:
            if name in ["跑步", "跳绳", "HIIT", "快走", "瑜伽"]:
                # 有氧运动调整时长
                new_duration = max(10, int(reps * factor))
                adjusted.append((name, 1, new_duration, 0))
            else:
                # 力量训练调整组数或次数
                new_sets = max(1, int(sets * factor))
                new_reps = max(5, int(reps * factor))
                adjusted.append((name, new_sets, new_reps, 60))  # rest 60s
        plan.append((day, adjusted))
    return plan