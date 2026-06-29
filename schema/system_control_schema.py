tool = {
            "type": "function",
            "function": {
                "name": "system_control",
                "description": "Controls Windows system operations such as volume configuration (up, down, mute) and power states (sleep, restart, shutdown). You MUST call this tool whenever the user requests system or hardware changes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["volume_up", "volume_down", "mute", "sleep", "restart", "shutdown"],
                            "description": "The specific system action to execute based on user command."
                        }
                    },
                    "required": ["action"]
                }
            }
        }