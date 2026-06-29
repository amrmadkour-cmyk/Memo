# plugins/take_screenshot.py
import os
from datetime import datetime
from PIL import ImageGrab

def take_screenshot():
    try:
        # إنشاء مجلد لحفظ لقطات الشاشة إذا لم يكن موجوداً
        output_dir = "screenshots"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # توليد اسم ملف فريد باستخدام التاريخ والوقت الحالي
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{output_dir}/screenshot_{timestamp}.png"
        
        # التقاط الشاشة وحفظ الصورة
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        
        return f"Successfully took a screenshot and saved it to {filename}."
    except Exception as e:
        return f"Error taking screenshot: {str(e)}"