# plugins/open_application.py
import subprocess
import sys

def open_application(app_name):
    try:
        app_name_lower = app_name.lower().strip()
        
        # كود باور شيل ذكي يبحث في كشاف ويندوز الشامل للتطبيقات (Get-StartApps)
        # ميزة الكود ده إنه بيشغل البرامج بشكل مستقل ومبيخليش بايثون يقف مستني قفل البرنامج
        ps_command = f'''
        $search = "{app_name_lower}";
        $app = Get-StartApps | Where-Object {{ $_.Name -like "*$search*" -or $_.AppID -like "*$search*" }} | Select-Object -First 1;
        if ($app) {{
            Start-Process "shell:AppsFolder\\$($app.AppID)";
            Write-Output "SUCCESS";
        }} else {{
            try {{
                Start-Process $search -ErrorAction Stop;
                Write-Output "SUCCESS";
            }} catch {{
                Write-Output "NOT_FOUND";
            }}
        }}
        '''
        
        # تنفيذ الأمر وجلب النتيجة للتأكد الفعلي من نجاح التشغيل
        process = subprocess.run(
            ["powershell", "-Command", ps_command],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
        )
        
        output = process.stdout.strip()
        
        if "SUCCESS" in output:
            return f"Successfully opened {app_name}."
        else:
            return f"Could not find or open {app_name}. Please make sure it is installed on your system."
            
    except Exception as e:
        return f"Error opening {app_name}: {str(e)}"