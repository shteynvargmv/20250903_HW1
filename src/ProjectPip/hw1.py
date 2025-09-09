"""Cистема для управления клиентами и заказами.

Функции расчета скидок и генерации отчетов.
"""
class CustomerDataClass:
    """Класс для представления данных клиента и управления заказами."""
    
    def __init__(self, customer_id, customer_name):
        """Инициализирует объект клиента.
        
        Args:
            customer_id (int): Уникальный идентификатор клиента
            customer_name (str): Имя клиента
        """
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.orders = []  # Список для хранения заказов клиента

    def add_order(self, order_object):
        """Добавляет заказ в список заказов клиента.
        
        Args:
            order_object (OrderDataClass): Объект заказа для добавления
        """
        self.orders.append(order_object)

    def get_total_amount(self):
        """Вычисляет общую сумму всех заказов клиента.
                
        Returns:
            float: Общая сумма всех заказов клиента
        """
        total = 0
        # Суммируем cумму каждого заказа
        for order in self.orders:
            total = total + order.amount
        return total


class OrderDataClass:
    """Класс для представления данных заказа."""
    
    def __init__(self, order_id, amount):
        """Инициализирует объект заказа.
        
        Args:
            order_id (int): Уникальный идентификатор заказа
            amount (float): Сумма заказа
        """
        self.order_id = order_id
        self.amount = amount


def calculate_discount(customer_obj):
    """Вычисляет размер скидки для клиента на основе общей суммы заказов.
    
    Args:
        customer_obj (CustomerDataClass): Объект клиента
        
    Returns:
        float: Размер скидки (10% если общая сумма > 1000, иначе 0)
    """
    total_amount = customer_obj.get_total_amount()
    # Скидка 10% применяется только для сумм превышающих 1000
    discount = total_amount * 0.1 if total_amount > 1000 else 0
    return discount


def print_customer_report(customer_obj):
    """Выводит детальный отчет по клиенту в консоль.
        
    Args:
        customer_obj (CustomerDataClass): Объект клиента для отчета
    """
    print('Customer Report for:', customer_obj.customer_name)
    print('Total Orders:', len(customer_obj.orders))
    print('Total Amount:', customer_obj.get_total_amount())
    print('Discount:', calculate_discount(customer_obj))
    
    # Вычисляем средний чек, избегая деления на ноль
    if len(customer_obj.orders) > 0:
        average_order = customer_obj.get_total_amount() / len(customer_obj.orders)
    else:
        average_order = 0  # Значение по умолчанию при отсутствии заказов
    print('Average Order:', average_order)


def main_program():
    """Основная функция программы.
    
    Демонстрирует работу с клиентами и заказами.
    Создает тестовые данные и выводит отчеты.
    """
    # Создаем первого клиента с двумя заказами
    c1 = CustomerDataClass(1, 'SAP Customer')
    o1 = OrderDataClass(101, 500)
    o2 = OrderDataClass(102, 800)
    c1.add_order(o1)
    c1.add_order(o2)

    # Генерируем отчет для первого клиента
    print_customer_report(c1)

    # Создаем второго клиента без заказов
    c2 = CustomerDataClass(2, 'Empty Customer')
    
    # Генерируем отчет для второго клиента
    print_customer_report(c2)


# Точка входа в программу
    """Запуск основной функции при прямом выполнении скрипта."""
    main_program()