# plugins/todo_manager.py
import os
import json

TODO_FILE = "todo.json"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)

def todo_manager(action, task_text=None, task_id=None):
    try:
        action = action.lower().strip()
        todos = load_todos()

        # 1. إضافة مهمة جديدة
        if action == "add":
            if not task_text:
                return "Please provide the task description."
            
            # توليد ID تلقائي بسيط
            new_id = 1 if not todos else max(t["id"] for t in todos) + 1
            new_task = {
                "id": new_id,
                "task": task_text.strip(),
                "status": "pending"
            }
            todos.append(new_task)
            save_todos(todos)
            return f"Successfully added task: '{task_text}' (ID: {new_id})."

        # 2. عرض المهام
        elif action == "show":
            if not todos:
                return "Your To-Do list is empty! Keep up the good work."
            
            reply = "Here is your To-Do list:\n"
            for t in todos:
                status_icon = "✅" if t["status"] == "completed" else "⏳"
                reply += f"- [{t['id']}] {status_icon} {t['task']}\n"
            return reply

        # 3. مسح مهمة
        elif action == "delete":
            if task_id is None:
                return "Please provide the task ID to delete."
            
            try:
                t_id = int(task_id)
            except ValueError:
                return "Task ID must be a valid number."

            # فلترة القائمة لحذف المهمة المطلوب مسحها
            initial_count = len(todos)
            todos = [t for t in todos if t["id"] != t_id]
            
            if len(todos) == initial_count:
                return f"Could not find a task with ID: {t_id}."
            
            save_todos(todos)
            return f"Successfully deleted task ID: {t_id}."

        # 4. اختيار إضافي: تحديث المهمة كمكتملة (مفيدة جداً)
        elif action == "complete":
            if task_id is None:
                return "Please provide the task ID to mark as completed."
            try:
                t_id = int(task_id)
            except ValueError:
                return "Task ID must be a valid number."

            for t in todos:
                if t["id"] == t_id:
                    t["status"] = "completed"
                    save_todos(todos)
                    return f"Successfully marked task '{t['task']}' as completed!"
            
            return f"Could not find a task with ID: {t_id}."

        else:
            return f"Unknown action: {action}"

    except Exception as e:
        return f"Error inside todo_manager: {str(e)}"