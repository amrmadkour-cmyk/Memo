# import ast
# import operator

# operators = {
#     ast.Add: operator.add,
#     ast.Sub: operator.sub,
#     ast.Mult: operator.mul,
#     ast.Div: operator.truediv,
#     ast.Pow: operator.pow
# }

# def evaluate(node):
#     # Numbers
#     if isinstance(node, ast.Constant):
#         return node.value

#     # Binary operations (+ - * / **)
#     elif isinstance(node, ast.BinOp):
#         left = evaluate(node.left)
#         right = evaluate(node.right)
#         op_type = type(node.op)

#         if op_type in operators:
#             return operators[op_type](left, right)
#         else:
#             raise Exception("Operation not allowed")

#     # Unary operations (like -5)
#     elif isinstance(node, ast.UnaryOp):
#         if isinstance(node.op, ast.USub):
#             return -evaluate(node.operand)
#         else:
#             raise Exception("Unary operation not allowed")

#     else:
#         raise Exception("Invalid expression")


# def safe_calculator(expression):
#     try:
#         tree = ast.parse(expression, mode='eval')
#         return evaluate(tree.body)
#     except Exception as e:
#         return f"Error: {str(e)}"


#####################################################################################################

# plugins/safe_calculator.py
import ast
import operator

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow
}

def evaluate(node):
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
        op_type = type(node.op)
        if op_type in operators:
            return operators[op_type](left, right)
        else:
            raise Exception("Operation not allowed")
    elif isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.USub):
            return -evaluate(node.operand)
        else:
            raise Exception("Unary operation not allowed")
    else:
        raise Exception("Invalid expression")

def safe_calculator(expression):
    try:
        tree = ast.parse(expression, mode='eval')
        return str(evaluate(tree.body))
    except Exception as e:
        return f"Error: {str(e)}"