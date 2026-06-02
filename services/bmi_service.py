def calculate_bmi(weight_kg, height_cm):
    if height_cm <= 0:
        return 0
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "超重"
    else:
        return "肥胖"