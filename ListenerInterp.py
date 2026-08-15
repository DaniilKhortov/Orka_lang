import sys
from antlr4 import *
from OrkaParser import OrkaParser
from OrkaListener import OrkaListener

class ListenerInterp(OrkaListener):
    def __init__(self):
        self.variables = {}  # Зберігає значення змінних
        self.variable_types = {}
    # Робота з програмою
    def exitProgram(self, ctx: OrkaParser.ProgramContext):
        print("Програма виконана успішно.")

    # Обробка секції var (оголошення змінних)
    def exitDeclarlist(self, ctx: OrkaParser.DeclarlistContext):
        for i in range(len(ctx.identlist())):
            # Отримуємо список ідентифікаторів
            ident_list = ctx.identlist(i).getText().split(',')
            # Отримуємо відповідний тип змінної
            var_type = ctx.type_(i).getText()
            #print(f"Оголошено тип {var_type} для змінних: {ident_list}")
            for ident in ident_list:
                ident = ident.strip()
                self.variables[ident] = 0  # Початкове значення
                self.variable_types[ident] = var_type  # Зберігаємо тип змінної
        #print(f"Змінні оголошені: {self.variables}")
        #print(f"Типи змінних: {self.variable_types}")

    # Присвоєння значень
    def exitAssign(self, ctx: OrkaParser.AssignContext):
        var_name = ctx.Ident().getText()  # Отримуємо текст ідентифікатора
       # print(f"Присвоєння значення змінній {var_name}")

        if var_name not in self.variables:
            raise ValueError(f"Змінна {var_name} не оголошена.")

        # Отримуємо тип змінної
        var_type = self.variable_types[var_name]

        # Обчислюємо значення виразу
        if ctx.arithmexpr():
            value = self.evaluate_arithmexpr(ctx.arithmexpr())
        elif ctx.boolconst():
            value = ctx.boolconst().getText() == 'true'
        #print(var_type)
        # Перевірка відповідності типу
        if var_type == 'integer' and not isinstance(value, int):
            raise TypeError(f"Змінній {var_name} (тип integer) не можна присвоїти значення типу real.")
        elif var_type == 'real' and not isinstance(value, (int, float)):
            raise TypeError(f"Змінній {var_name} (тип real) не можна присвоїти значення типу {type(value).__name__}.")

        # Присвоєння значення змінній
        
        self.variables[var_name] = value
        #print(f"{var_name} := {value}")

    def evaluate_arithmexpr(self, ctx: OrkaParser.ArithmexprContext):
       # Початкове значення обчислення
       result = self.evaluate_term(ctx.term(0))

       # Проходимо всі оператори і терми
       for i in range(1, ctx.getChildCount(), 2):
           operator = ctx.getChild(i).getText()
           right = self.evaluate_term(ctx.term((i + 1) // 2))
           if operator == '+':
               result += right
           elif operator == '-':
               result -= right
           else:
               raise ValueError(f"Невідомий оператор: {operator}")

       return result

    def evaluate_term(self, ctx: OrkaParser.TermContext):
       # Початкове значення обчислення
       result = self.evaluate_factor(ctx.factor(0))

       # Проходимо всі оператори і фактори
       for i in range(1, ctx.getChildCount(), 2):
           operator = ctx.getChild(i).getText()
           right = self.evaluate_factor(ctx.factor((i + 1) // 2))
           if operator == '*':
               result *= right
           elif operator == '/':
               # Перевірка типів для цілочисельного ділення
               if isinstance(result, int) and isinstance(right, int):
                   result //= right  # Цілочисельне ділення
               else:
                   result /= right  # Звичайне ділення
           else:
               raise ValueError(f"Невідомий оператор: {operator}")

       return result

     # Додано обробку степенів у факторі
    def evaluate_factor(self, ctx: OrkaParser.FactorContext):
          # Додатковий випадок: знак перед фактором (+5, -2.5)
         if ctx.getChildCount() == 2 and ctx.getChild(0).getText() in ('+', '-'):
             sign = ctx.getChild(0).getText()  # Отримуємо знак (+ або -)
             factor_value = self.evaluate_factor(ctx.getChild(1))  # Обчислюємо фактор після знака
             value = factor_value if sign == '+' else -factor_value

         # Якщо фактор — це степінь (base ^ factor)
         elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '^':
             base = self.evaluate_factor(ctx.getChild(0))  # Обчислюємо базу
             exponent = self.evaluate_factor(ctx.getChild(2))  # Обчислюємо показник
             if isinstance(base, int) and isinstance(exponent, int):
                 value = base ** exponent  # Цілий результат для `integer`
             else:
                 value = float(base) ** float(exponent)  # Дійсний результат для `real`

         # Якщо фактор — це вираз у дужках (наприклад, (x + y))
         elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
             value = self.evaluate_arithmexpr(ctx.getChild(1))  # Вираз у дужках

         # Якщо фактор — це base (ідентифікатор або число)
         elif ctx.getChildCount() == 1:
            base = ctx.getChild(0).getText()
            if self.is_integer(base):  # Перевірка: чи це ціле число
                value = int(base)
            elif self.is_real_number(base):  # Перевірка: чи це дійсне число
                value = float(base)
            elif base in self.variables:  # Якщо це змінна
                value = self.variables[base]
            else:
                raise ValueError(f"Невідома змінна або значення: {base}")

         else:
            raise ValueError(f"Невідомий формат фактора: {ctx.getText()}")

         return value


    def is_integer(self, text):
        """Перевіряє, чи є текст цілим числом."""
        try:
            int(text)
            return True
        except ValueError:
            return False

    def is_real_number(self, text):
        """Перевіряє, чи є текст дійсним числом."""
        try:
            float(text)
            return True
        except ValueError:
            return False

    # Читання даних
    def exitInput(self, ctx: OrkaParser.InputContext):
        # Отримуємо список ідентифікаторів
        ident_list = ctx.identlist().getText().split(',')

        for ident in ident_list:
            ident = ident.strip()  # Очищення ідентифікатора
            if ident not in self.variable_types:
                raise ValueError(f"Змінна {ident} не оголошена.")

            var_type = self.variable_types[ident]  # Отримуємо тип змінної

            # Вводимо значення залежно від типу змінної
            if var_type == 'integer':
                while True:
                    try:
                        value = int(input(f"Введіть ціле значення для {ident}: "))
                        break
                    except ValueError:
                        print("Помилка: потрібно ввести ціле число.")

            elif var_type == 'real':
                while True:
                    try:
                        value = float(input(f"Введіть дійсне значення для {ident}: "))
                        break
                    except ValueError:
                        print("Помилка: потрібно ввести дійсне число.")

            elif var_type == 'boolean':
                while True:
                    user_input = input(f"Введіть значення (true/false) для {ident}: ").strip().lower()
                    if user_input in {'true', 'false'}:
                        value = (user_input == 'true')  # Перетворення на булеве значення
                        break
                    else:
                        print("Помилка: потрібно ввести 'true' або 'false'.")

            else:
                raise TypeError(f"Невідомий тип змінної {ident}: {var_type}")

            # Зберігаємо значення в словник змінних
            self.variables[ident] = value

        #print(f"Зчитано: {self.variables}")
    # Вивід даних
    def exitOutput(self, ctx: OrkaParser.OutputContext):
        if ctx.identlist():
            for ident in ctx.identlist().getText().split(','):
                print(f"{ident.strip()} = {self.variables[ident.strip()]}")
        elif ctx.const():
            print(ctx.const().getText())

    # Умовні оператори
    def enterIfstatement(self, ctx: OrkaParser.IfstatementContext):
        # print("Початок обробки оператора if")

        # Перевіряємо умову
        condition = self.evaluate_boolexpr(ctx.boolexpr())
        # print(f"Умова if: {condition}")

        if condition:
            # print("Виконання then-блоку")
            
            self.execute_doblock(ctx.doblock(0))  # Виконуємо then-блок

        elif ctx.doblock(1):  # Якщо є else-блок
            # print("Виконання else-блоку")
            self.execute_doblock(ctx.doblock(1))  # Виконуємо else-блок

    # Умовні оператори
    #def exitIfstatement(self, ctx: OrkaParser.IfstatementContext):
       
    def execute_doblock(self, ctx: OrkaParser.DoblockContext):
        for command in ctx.actionsequence().command():
            # Визначаємо тип команди
            print(command.getText())
            if command.assign():
                self.exitAssign(command.assign())
            elif command.output():
                self.exitOutput(command.output())
            elif command.input_():
                self.exitInput(command.input_())
            elif command.ifstatement():
                self.enterIfstatement(command.ifstatement())
                
            elif command.whilestatement():
                self.enterWhilestatement(command.whilestatement())
            else:
                print(f"Невідома команда: {command.getText()}")
            #print(f"Поточний стан змінних після do-block: {self.variables}")    
    # Цикли while
        # Викликається на початку роботи з циклом while
    def enterWhilestatement(self, ctx: OrkaParser.WhilestatementContext):
        #print("Початок обробки циклу while")
        
        # Початкова умова
        condition = self.evaluate_boolexpr(ctx.boolexpr())
        #print(f"Початкова умова: {condition}")
    
        # Якщо умова хибна, тіло циклу не виконується
        if not condition:
            #print("Цикл не виконується, умова хибна.")
            self.skip_while = True
        else:
            self.skip_while = False
    
    # Викликається після завершення роботи з циклом while
    #3##################
    #3##################
    #3################## коментар для коректної роботи while
    def exitWhilestatement(self, ctx: OrkaParser.WhilestatementContext): #3##################
  #^  
  #|   
        if hasattr(self, "skip_while") and self.skip_while:
            print("Пропуск виконання циклу.")
            return
        
        # Виконання циклу
        while self.evaluate_boolexpr(ctx.boolexpr()):
            #print(f"Умова циклу: {self.evaluate_boolexpr(ctx.boolexpr())}")
    
            # Виконання тіла циклу
            self.execute_doblock(ctx.doblock())
            
            # Після виконання блоку оновлюється умова
            #print(f"Оновлена умова: {self.evaluate_boolexpr(ctx.boolexpr())}")
        #print("Цикл завершено.")
    

    # Логічні вирази
    def evaluate_boolexpr(self, ctx: OrkaParser.BoolexprContext):
        
        if ctx.boolconst():
            
            return ctx.boolconst().getText() == 'true'
        elif ctx.logicalexpr():
            
            return self.evaluate_logicalexpr(ctx.logicalexpr())
        else:
            raise ValueError(f"Невідомий логічний вираз: {ctx.getText()}")

    def evaluate_logicalexpr(self, ctx: OrkaParser.LogicalexprContext):
        # Початкове значення
        result = self.evaluate_logicalterm(ctx.logicalterm(0))
    
        # Обробляємо всі терми з оператором 'or'
        for i in range(1, ctx.getChildCount(), 2):
            right = self.evaluate_logicalterm(ctx.logicalterm((i + 1) // 2))
            result = result or right
    
        return result
    
    def evaluate_logicalterm(self, ctx: OrkaParser.LogicaltermContext):
        # Початкове значення
        result = self.evaluate_logicalmultiplier(ctx.logicalmultiplier(0))
    
        # Обробляємо всі множники з оператором 'and'
        for i in range(1, ctx.getChildCount(), 2):
            right = self.evaluate_logicalmultiplier(ctx.logicalmultiplier((i + 1) // 2))
            result = result and right
    
        return result


    def evaluate_logicalmultiplier(self, ctx: OrkaParser.LogicalmultiplierContext):
        if ctx.logicalrel():
            # Порівняльний вираз
            return self.evaluate_logicalrel(ctx.logicalrel())
        elif ctx.getChild(0).getText() == 'not':
            # Логічне заперечення
            return not self.evaluate_logicalmultiplier(ctx.logicalmultiplier(0))
        elif ctx.getChildCount() == 3:
            # Вираз у дужках
            return self.evaluate_boolexpr(ctx.boolexpr())

    def evaluate_logicalrel(self, ctx: OrkaParser.LogicalrelContext):
        left = self.evaluate_arithmexpr(ctx.arithmexpr(0))
        operator = ctx.relop().getText()
        right = self.evaluate_arithmexpr(ctx.arithmexpr(1))
        if operator == '=':
            return left == right
        elif operator == '<=':
            return left <= right
        elif operator == '<':
            return left < right
        elif operator == '>=':
            return left >= right
        elif operator == '>':
            return left > right
        elif operator == '<>':
            return left != right
        
    def enterCaselist(self, ctx: OrkaParser.CaselistContext):
        print("Вхід у caselist")
        self.cases = []  # Ініціалізуємо список case-блоків
        for i in range(len(ctx.const())):
            case_value = self.evaluate_const(ctx.const(i))
            case_block = ctx.doblock(i)
            self.cases.append((case_value, case_block))
        # print(f"Case-блоки зібрані: {self.cases}")

    def exitCaselist(self, ctx: OrkaParser.CaselistContext):
        # print("Вихід із caselist")    
        print("") 

    def enterSwitchstatement(self, ctx: OrkaParser.SwitchstatementContext):
        # print("Вхід у switchstatement")
        # Обчислюємо значення виразу
        self.switch_expression_value = self.evaluate_expression(ctx.expression())
        # print(f"Значення expression у switch: {self.switch_expression_value}")

    def exitSwitchstatement(self, ctx: OrkaParser.SwitchstatementContext):
        print("Вихід із switchstatement")
        # Перевіряємо зібрані case
        case_executed = False
        for case_value, case_block in self.cases:
            if self.switch_expression_value == case_value:
                # print(f"Збіг з case: {case_value}")
                self.execute_doblock(case_block)
                case_executed = True
                break  # Виконуємо тільки перший відповідний блок
            
        # Якщо жоден case не підійшов, виконуємо default
        if not case_executed and ctx.doblock():
            # print("Виконується default-блок")
            self.execute_doblock(ctx.doblock())    

    def evaluate_const(self, ctx: OrkaParser.ConstContext):
        if ctx.intnumb():
            return int(ctx.intnumb().getText())
        elif ctx.realnumb():
            return float(ctx.realnumb().getText())
        elif ctx.boolconst():
            return ctx.boolconst().getText() == 'true'
        else:
            raise ValueError(f"Невідомий тип константи: {ctx.getText()}")       
    def evaluate_expression(self, ctx: OrkaParser.ExpressionContext):
        if ctx.boolexpr():
            return self.evaluate_boolexpr(ctx.boolexpr())
        elif ctx.arithmexpr():
            return self.evaluate_arithmexpr(ctx.arithmexpr())
        else:
            raise ValueError(f"Невідомий тип виразу: {ctx.getText()}")     