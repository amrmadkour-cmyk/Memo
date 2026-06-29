# import webbrowser

# def open_website(site_name: str):
#     websites = {
#         "google": "https://www.google.com",
#         "youtube": "https://www.youtube.com",
#         "facebook": "https://www.facebook.com",
#         "github": "https://www.github.com"
#     }

#     site_name = site_name.lower().strip()

#     if site_name in websites:
#         webbrowser.open(websites[site_name])
#         return f"Opening {site_name}..."
#     else:
#         return "Website not found"


# if __name__ == "__main__":
#     print(open_website("youtube"))
#################################################################################

# plugins/open_website.py
import webbrowser

def open_website(url):
    try:
        # لو المستخدم قال اسم الموقع بس (زي google.com)، الكود هيتأكد إن البروتوكول موجود عشان يفتح صح
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        webbrowser.open(url)
        return f"Successfully opened {url}"
    except Exception as e:
        return f"Error opening website: {str(e)}"