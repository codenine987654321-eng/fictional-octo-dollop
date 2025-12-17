# Project: Fictional Octo Dollop
# Lead Developer: Mohammed Fahad (محمد فهد)

import random

def start_engine():
    developer_name = "محمد فهد"
    
    print("="*40)
    print(f"نظام الشخصيات الخيالية - تطوير: {developer_name}")
    print("="*40)
    
    roles = ["محارب سيبراني", "مستكشف بيانات", "مهندس أحلام", "حارس الكود"]
    skills = ["البرمجة بلغة النجوم", "تفكيك التشفير", "بناء العوالم"]

    print(f"مرحباً بك في مستودع {developer_name} الجديد.")
    print(f"الشخصية المقترحة لك اليوم هي: {random.choice(roles)}")
    print(f"المهارة المختارة: {random.choice(skills)}")
    print("="*40)

if __name__ == "__main__":
    start_engine()

