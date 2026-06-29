# plugins/set_timer.py
import time
import threading
import winsound

def timer_worker(seconds, label):
    """دالة تعمل في الخلفية لانتظار الوقت ثم إطلاق التنبيه"""
    time.sleep(seconds)
    
    # تشغيل صوت التنبيه (تردد 1000 هرتز لمدة 600 مللي ثانية) وتكراره 5 مرات
    for _ in range(5):
        winsound.Beep(1000, 600)
        time.sleep(0.1)
        
    print(f"\n[TIMER ALERT] '{label}' time is up!")

def set_timer(duration_seconds, label="Timer"):
    try:
        seconds = int(duration_seconds)
        if seconds <= 0:
            return "Please provide a duration greater than zero."
            
        # تشغيل المؤقت في Thread منفصل تماماً عشان الكود الأساسي للمساعد ميقفش
        timer_thread = threading.Thread(target=timer_worker, args=(seconds, label), daemon=True)
        timer_thread.start()
        
        # تحويل الثواني لدقائق وثواني لشكل لطيف في الرد
        mins, secs = divmod(seconds, 60)
        time_str = f"{mins} minutes and {secs} seconds" if mins > 0 else f"{secs} seconds"
        
        return f"Successfully set a timer for {time_str} for '{label}'."
    except Exception as e:
        return f"Error setting timer: {str(e)}"