tool = {
            "type": "function",
            "function": {
                "name": "open_application",
                "description": "Opens a local desktop application or program on the user's computer (like VS Code, Chrome, Notepad, Calculator). You MUST call this tool whenever the user explicitly asks to open, launch, run, or start a program/app.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_name": {
                            "type": "string",
                            "description": "The exact name of the application to open (e.g., 'vscode', 'chrome', 'notepad', 'calculator')."
                        }
                    },
                    "required": ["app_name"]
                }
            }
        }