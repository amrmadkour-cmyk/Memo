tool = {
            "type": "function",
            "function": {
                "name": "todo_manager",
                "description": "Manages the user's daily To-Do list stored in a JSON file. Can add new tasks, show all tasks, delete a task, or mark a task as completed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["add", "show", "delete", "complete"],
                            "description": "The action to perform on the to-do list."
                        },
                        "task_text": {
                            "type": "string",
                            "description": "The description of the task. Required only for 'add' action."
                        },
                        "task_id": {
                            "type": "integer",
                            "description": "The unique ID of the task. Required only for 'delete' or 'complete' actions."
                        }
                    },
                    "required": ["action"]
                }
            }
        }