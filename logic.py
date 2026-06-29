# import re
# from ollama import chat, ChatResponse
# from plugins.getDateAndTime import get_current_date, get_current_time
# from plugins.safe_calculator import safe_calculator
# def logic(messages):
#    """
#    Process messages and handle tool calls
#    Returns appropriate response from the LLM.
#    """
#    available_functions = {
#        'get_current_date': get_current_date,
#        'get_current_time': get_current_time,
#        'safe_calculator' : safe_calculator
#    }
#    # Define tool schema more explicitly
#    tools = [{
#        "type": "function",
#        "function": {
#                "name": "get_current_date",
#            "description": "Get today's date",
#                "parameters": {
#                    "type": "object",
#                    "properties": {},
#                    "required": []
#                }
#        }
#    }, {
#        "type": "function",
#        "function": {
#                "name": "get_current_time",
#            "description": "Get the current time of the day",
#                "parameters": {
#                    "type": "object",
#                    "properties": {},
#                    "required": []
#                }
#        }
#    }, {
#     "type": "function",
#     "function": {
#         "name": "safe_calculator",
#         "description": "Safely evaluate mathematical expressions",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "expression": {
#                     "type": "string",
#                     "description": "Math expression like 5 + 3 * 2"
#                 }
#             },
#             "required": ["expression"]
#         }
#     }
# }]
#    # Get initial response
#    response = chat(model='qwen3:1.7b', messages=messages, tools=tools)
#    # Clean the response content
#    if 'content' in response.message and response.message['content']:
#        response.message['content'] = re.sub(
#            r'<think>.*?</think>', '', response.message['content'], flags=re.DOTALL).strip()
#    # If no tool calls, return the response directly
#    if not response.message.tool_calls:
#        print('No tool calls detected')
#        return response.message
#    # Handle tool calls if present
#    tool_outputs = []
#    for tool in response.message.tool_calls:
#        if function_to_call := available_functions.get(tool.function.name):
#            output = function_to_call(**tool.function.arguments)
#            if output:
#                tool_outputs.append({
#                    'role': 'tool',
#                    'content': output,
#                    'name': tool.function.name
#                })
#    if tool_outputs:
#        # Add the assistant's tool call message
#        messages.append({
#            'role': 'assistant',
#            'content': response.message.content or '',
#            'tool_calls': response.message.tool_calls
#        })
#        # Add the tool outputs
#        messages.extend(tool_outputs)
#        final_response = chat('qwen3:1.7b', messages=messages, tools=tools)
#        # Clean the final response content
#        if 'content' in final_response.message and final_response.message['content']:
#            final_response.message['content'] = re.sub(
#                r'<think>.*?</think>', '', final_response.message['content'], flags=re.DOTALL).strip()
#        return final_response.message
#    return response.message


###########################################################################################################################################################################

import re
from ollama import chat, ChatResponse
from plugins.getDateAndTime import get_current_date, get_current_time
from plugins.safe_calculator import safe_calculator
from plugins.open_website import open_website
from plugins.open_application import open_application
from plugins.system_control import system_control
from plugins.take_screenshot import take_screenshot
from plugins.set_timer import set_timer
from plugins.todo_manager import todo_manager
from plugins.random_quote_or_joke import random_quote_or_joke
def logic(messages):
   """
   Process messages and handle tool calls
   Returns appropriate response from the LLM.
   """
   available_functions = {
       'get_current_date': get_current_date,
       'get_current_time': get_current_time,
       'safe_calculator': safe_calculator,
       'open_website': open_website,
       'open_application': open_application,
       'system_control': system_control,
       'take_screenshot': take_screenshot,
       'set_timer': set_timer,
       'todo_manager': todo_manager,
       'random_quote_or_joke': random_quote_or_joke
       
   }
   # Define tool schema more explicitly
   tools = [{
       "type": "function",
       "function": {
               "name": "get_current_date",
           "description": "Get today's date",
               "parameters": {
                   "type": "object",
                   "properties": {},
                   "required": []
               }
       }
   }, {
       "type": "function",
       "function": {
               "name": "get_current_time",
           "description": "Get the current time of the day",
               "parameters": {
                   "type": "object",
                   "properties": {},
                   "required": []
               }
       }
   }, {
            "type": "function",
            "function": {
                "name": "safe_calculator",
                "description": "Safely evaluates any mathematical expression and returns the exact result. You MUST call this tool for ANY math question or calculation request, such as 'what is 5 + 3', 'calculate 12 * 8', or 'what's the square root of 81'. Never compute or guess the answer yourself from your own knowledge — always call this tool to get the exact, correct result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "Math expression like 5 + 3 * 2"
                        }
                    },
                    "required": ["expression"]
                }
            }
        } , {
            "type": "function",
            "function": {
                "name": "open_website",
                "description": "Opens a specific website or URL in the user's default web browser. You MUST call this tool whenever the user asks to open, browse, go to, or visit a website (e.g., 'open Google', 'go to youtube.com', 'open facebook'). If the user provides just the name of a popular site, automatically convert it to a valid domain (e.g., 'youtube' becomes 'youtube.com').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "The domain or full URL of the website to open (e.g., 'google.com', 'facebook.com', 'github.com')."
                        }
                    },
                    "required": ["url"]
                }
            }
        } , {
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
        } , {
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
        } , {
            "type": "function",
            "function": {
                "name": "take_screenshot",
                "description": "Takes a live screenshot of the user's current desktop screen and saves it as an image file. You MUST call this tool whenever the user explicitly asks to take a screenshot, capture the screen, or snap the desktop screen.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        } , {
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
        } , {
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
        } , {
            "type": "function",
            "function": {
                "name": "random_quote_or_joke",
                "description": "Returns a random joke, an inspirational quote, or the user's specific favorite quote. Call this tool when the user asks for a joke, motivation, or their favorite quote.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "enum": ["joke", "quote", "favorite"],  # <--- إضافة favorite هنا
                            "description": "Choose 'joke' for funny content, 'quote' for inspiration, or 'favorite' if the user explicitly asks for their favorite quote."
                        }
                    },
                    "required": ["category"]
                }
            }
        }
    ]
   # Get initial response
   response = chat(model='qwen3:1.7b', messages=messages, tools=tools)
   # Clean the response content
   if 'content' in response.message and response.message['content']:
       response.message['content'] = re.sub(
           r'<think>.*?</think>', '', response.message['content'], flags=re.DOTALL).strip()
   # If no tool calls, return the response directly
   if not response.message.tool_calls:
       print('No tool calls detected')
       return response.message
   # Handle tool calls if present
   tool_outputs = []
   for tool in response.message.tool_calls:
       if function_to_call := available_functions.get(tool.function.name):
           output = function_to_call(**tool.function.arguments)
           if output:
               tool_outputs.append({
                   'role': 'tool',
                   'content': output,
                   'name': tool.function.name
               })
   if tool_outputs:
       # Add the assistant's tool call message
       messages.append({
           'role': 'assistant',
           'content': response.message.content or '',
           'tool_calls': response.message.tool_calls
       })
       # Add the tool outputs
       messages.extend(tool_outputs)
       final_response = chat('qwen3:1.7b', messages=messages, tools=tools)
       # Clean the final response content
# Clean the final response content
       if 'content' in final_response.message and final_response.message['content']:
            final_response.message['content'] = re.sub(
                r'<think>.*?</think>', '', final_response.message['content'], flags=re.DOTALL).strip()
            final_response.message['content'] = final_response.message['content'].replace('$', '')
            final_response.message['content'] = final_response.message['content'].replace('\\times', 'x')
            final_response.message['content'] = final_response.message['content'].replace('\\div', '/')
            final_response.message['content'] = re.sub(
                r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', final_response.message['content'])
       return final_response.message
   return response.message