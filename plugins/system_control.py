# plugins/system_control.py
import os
import subprocess
import sys

def system_control(action):
    try:
        action = action.lower().strip()
        
        # 1. التحكم في الصوت باستخدام PowerShell ومحاكاة أزرار الميديا بالويندوز
        if action == "volume_up":
            # محاكاة الضغط على زر رفع الصوت 5 مرات متتالية (لرفع ملحوظ)
            ps_cmd = "$wsh = New-Object -ComObject WScript.Shell; for($i=0; $i -lt 5; $i++) { $wsh.SendKeys([char]175) }"
            subprocess.run(["powershell", "-Command", ps_cmd], creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0)
            return "Successfully increased the volume."
            
        elif action == "volume_down":
            # محاكاة الضغط على زر خفض الصوت 5 مرات
            ps_cmd = "$wsh = New-Object -ComObject WScript.Shell; for($i=0; $i -lt 5; $i++) { $wsh.SendKeys([char]174) }"
            subprocess.run(["powershell", "-Command", ps_cmd], creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0)
            return "Successfully lowered the volume."
            
        elif action == "mute":
            # محاكاة زر كتم الصوت (تشتغل Toggle كتم وفك كتم)
            ps_cmd = "$wsh = New-Object -ComObject WScript.Shell; $wsh.SendKeys([char]173)"
            subprocess.run(["powershell", "-Command", ps_cmd], creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0)
            return "Successfully toggled mute status."
            
        # 2. التحكم في طاقة الجهاز (النوم، الريستارت، القفل)
        elif action == "sleep":
            # أمر إدخال الويندوز في وضع الاستعداد
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            return "Putting the system to sleep now."
            
        elif action == "restart":
            # إعادة تشغيل بعد دقيقة واحدة ليعطي فرصة للمساعد لينطق
            os.system("shutdown /r /t 5")
            return "Restarting the computer in 5 seconds."
            
        elif action == "shutdown":
            # إغلاق الجهاز بعد 5 ثوانٍ
            os.system("shutdown /s /t 5")
            return "Shutting down the computer in 5 seconds."
            
        else:
            return f"Unknown system action: {action}"
            
    except Exception as e:
        return f"Error executing system action {action}: {str(e)}"