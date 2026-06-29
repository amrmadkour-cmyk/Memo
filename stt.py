import speech_recognition as sr

def stt():
    recognizer = sr.Recognizer()
    
    # ده بيعادل MAX_SILENCE_TIME = 2.0 في كودك القديم
    # بيخلي المايك يقفل لو سكت لمدة ثانيتين متواصلين
    recognizer.pause_threshold = 2.0 
    
    INITIAL_TIMEOUT = 5.0 # أقصى وقت للانتظار قبل بدء الكلام

    # الـ with statement بتفتح المايك وبتقفله أوتوماتيك (بتغنينا عن stream.close و mic.terminate)
    with sr.Microphone() as source:
        # يفضل دايماً تنضيف الدوشة في الخلفية لثانية عشان جوجل يفهم صح
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Listening...")
        try:
            # timeout=INITIAL_TIMEOUT بتعادل الجزء بتاعك لو متكلمش خالص في الأول
            audio = recognizer.listen(source, timeout=INITIAL_TIMEOUT)
            print("Speech completed, stopping...")
            
        except sr.WaitTimeoutError:
            print("No speech detected, stopping...")
            return None

    # مرحلة تحويل الصوت لنص عن طريق جوجل
    try:
        # استخدام جوجل وتحديد اللهجة المصرية
        resultText = recognizer.recognize_google(audio, language="en-US")
        print(f"Recognized: {resultText}")
        return resultText
        
    except sr.UnknownValueError:
        # لو جوجل مقدرش يميز أي كلام في الصوت
        print("لم يتم التعرف على كلام واضح.")
        return ""
    except sr.RequestError as e:
        # لو مفيش إنترنت أو في مشكلة في الاتصال
        print(f"مشكلة في الاتصال بالإنترنت: {e}")
        return None