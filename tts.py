import edge_tts
import asyncio
import pygame
import os

def tts(message):
    """
    الدالة دي بتحول النص لصوت باستخدام مكتبة edge-tts 
    وبتشتغل باللهجة المصرية.
    """
    # تنظيف النص من المسافات الزايدة
    clean_message = str(message).replace('\n', ' ').strip()
    
    print(f"Memo says: {clean_message}")

    # لو النص فاضي، مفيش داعي نكمل
    if not clean_message:
        return

    # اختيار الصوت: 'ar-EG-SalmaNeural' (بنت) أو 'ar-EG-ShakirNeural' (ولد)
    voice = "en-US-AriaNeural" 
    
    # اسم ملف الصوت المؤقت اللي هيتحفظ
    audio_file = "temp_response.mp3"

    # دالة داخلية غير متزامنة عشان تتعامل مع edge-tts
    async def _generate_audio():
        communicate = edge_tts.Communicate(clean_message, voice)
        await communicate.save(audio_file)

    # تشغيل توليد الصوت
    try:
        asyncio.run(_generate_audio())
    except Exception as e:
        print(f"حصلت مشكلة في الاتصال بالإنترنت أو توليد الصوت: {e}")
        return

    # --- تشغيل الصوت باستخدام pygame ---
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        # الكود هيفضل مستني لحد ما الصوت يخلص (زي engine.runAndWait)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    except Exception as e:
        print(f"مشكلة في تشغيل الصوت: {e}")
    
    finally:
        # لازم نقفل الـ mixer عشان نفك الحظر عن ملف الصوت
        pygame.mixer.quit()
        
        # مسح ملف الصوت المؤقت عشان منزحمش مساحة الجهاز
        if os.path.exists(audio_file):
            try:
                os.remove(audio_file)
            except PermissionError:
                pass # لو الملف لسه مقفول نتجاهل المسح المرة دي