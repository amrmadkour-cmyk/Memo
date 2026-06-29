tool = {
            "type": "function",
            "function": {
                "name": "set_timer",
                "description": "Sets a timer or alarm for a specific duration in seconds. You MUST call this tool whenever the user asks to set a timer, stopwatch, or alarm for a certain amount of time. Convert minutes or hours into seconds before calling.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "duration_seconds": {
                            "type": "integer",
                            "description": "The total duration of the timer converted into seconds (e.g., 5 minutes = 300)."
                        },
                        "label": {
                            "type": "string",
                            "description": "The reason or label for the timer (e.g., 'pizza', 'studying', 'break'). Default is 'Timer'."
                        }
                    },
                    "required": ["duration_seconds"]
                }
            }
        }