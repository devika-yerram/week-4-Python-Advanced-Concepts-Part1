from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_amount):
        pass

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.95  # 5% discount

class PremiumDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.90  # 10% discount

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, order_amount):
        return order_amount * 0.80  # 20% discount

class Order:
    def __init__(self, customer_type, order_amount):
        self.customer_type = customer_type
        self.order_amount = order_amount

    def final_price(self):
        if self.customer_type == 'regular':
            discount_strategy = RegularDiscount()
        elif self.customer_type == 'premium':
            discount_strategy = PremiumDiscount()
        elif self.customer_type == 'VIP':
            discount_strategy = VIPDiscount()
        else:
            raise ValueError("Invalid customer type")

        return discount_strategy.apply_discount(self.order_amount)


if __name__ == "__main__":
    
    regular_order = Order('regular', 100)
    print(f"Final price for regular customer: ${regular_order.final_price():.2f}")

    
    premium_order = Order('premium', 100)
    print(f"Final price for premium customer: ${premium_order.final_price():.2f}")

    
    vip_order = Order('VIP', 100)
    print(f"Final price for VIP customer: ${vip_order.final_price():.2f}")
