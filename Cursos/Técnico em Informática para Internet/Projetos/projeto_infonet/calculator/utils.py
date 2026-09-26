import ast
import operator
import math

# Mapeamento de operadores do AST para funções Python
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

# Funções científicas suportadas
FUNCTIONS = {
    'sqrt': math.sqrt,
    'sin': lambda x: math.sin(math.radians(x)),  # Graus para radianos para melhor usabilidade
    'cos': lambda x: math.cos(math.radians(x)),
    'tan': lambda x: math.tan(math.radians(x)),
    'log': math.log,
    'log10': math.log10,
    'exp': math.exp,
}

def safe_eval(expr_str):
    """
    Avalia com segurança uma expressão matemática simples usando AST (Abstract Syntax Tree).
    Lança ValueError, ZeroDivisionError ou TypeError em caso de falha.
    """
    if not expr_str:
        raise ValueError("Expressão vazia.")

    # Normalizar símbolos comuns
    expr_str = expr_str.replace("×", "*").replace("÷", "/").replace("^", "**")
    
    # Remover espaços em branco
    expr_str = expr_str.replace(" ", "")
    
    # Filtro de caracteres permitidos (apenas alfanuméricos e caracteres matemáticos básicos)
    allowed_chars = set("0123456789+-*/%.()_abcdefghijklmnopqrstuvwxyz")
    if not all(c in allowed_chars for c in expr_str.lower()):
        raise ValueError("Caracteres não permitidos na expressão.")
        
    try:
        node = ast.parse(expr_str, mode='eval')
    except SyntaxError:
        raise ValueError("Expressão mal formatada.")

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise TypeError("Apenas números são permitidos.")
        elif isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            
            if op_type in OPERATORS:
                # Tratamento de erros aritméticos comuns
                if op_type == ast.Div and right == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                if op_type == ast.Mod and right == 0:
                    raise ZeroDivisionError("Resto de divisão por zero não é permitido.")
                if op_type == ast.Pow:
                    if abs(left) > 1000 and right > 100:
                        raise ValueError("Resultado muito grande (overflow).")
                    if right > 1000:
                        raise ValueError("Expoente muito grande.")
                
                result = OPERATORS[op_type](left, right)
                # Impedir números complexos indesejados caso left seja negativo e right seja float
                if isinstance(result, complex):
                    raise ValueError("Resultados complexos não são suportados.")
                return result
            raise TypeError("Operador não suportado.")
        elif isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in OPERATORS:
                return OPERATORS[op_type](operand)
            raise TypeError("Operador unário não suportado.")
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id.lower()
                if func_name in FUNCTIONS:
                    if len(node.args) != 1:
                        raise ValueError(f"A função '{func_name}' espera exatamente 1 argumento.")
                    arg_val = _eval(node.args[0])
                    
                    # Tratamentos de domínio matemático
                    if func_name == 'sqrt' and arg_val < 0:
                        raise ValueError("Raiz quadrada de número negativo não suportada.")
                    if (func_name in ['log', 'log10']) and arg_val <= 0:
                        raise ValueError("Logaritmo exige valor maior que zero.")
                        
                    return FUNCTIONS[func_name](arg_val)
            raise TypeError("Função não suportada.")
        elif isinstance(node, ast.Name):
            # Suportar constantes conhecidas
            name_lower = node.id.lower()
            if name_lower == 'pi':
                return math.pi
            elif name_lower == 'e':
                return math.e
            raise NameError(f"Nome '{node.id}' não definido.")
        else:
            raise TypeError("Expressão inválida.")

    val = _eval(node)
    
    # Formatação para evitar imprecisões de ponto flutuante binário (ex: 0.1 + 0.2)
    if isinstance(val, float):
        if val.is_integer():
            return int(val)
        # Limitar a 10 casas decimais para arredondamento
        val = round(val, 10)
        # Se após arredondamento virar inteiro
        if val.is_integer():
            return int(val)
    return val
