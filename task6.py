def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм для вибору їжі з максимальною калорійністю в межах бюджету
    """
    ratios = {
        item: data["calories"] / data["cost"]
        for item, data in items.items()
    }
    sorted_items = sorted(ratios.items(), key=lambda x: x[1], reverse=True)

    selected_items = []
    total_calories = 0
    remaining_budget = budget

    for item, _ in sorted_items:
        if items[item]["cost"] <= remaining_budget:
            selected_items.append(item)
            total_calories += items[item]["calories"]
            remaining_budget -= items[item]["cost"]

    spent_budget = budget - remaining_budget
    return selected_items, total_calories, spent_budget


def dynamic_programming(items, budget):
    """
    Алгоритм динамічного програмування для вибору їжі з максимальною калорійністю
    """
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    selected = [[set() for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    items_list = list(items.items())

    for i in range(1, len(items) + 1):
        item_name, item_data = items_list[i - 1]
        item_cost = item_data["cost"]
        item_calories = item_data["calories"]

        for w in range(budget + 1):
            if item_cost <= w:
                if dp[i - 1][w] < dp[i - 1][w - item_cost] + item_calories:
                    dp[i][w] = dp[i - 1][w - item_cost] + item_calories
                    selected[i][w] = selected[i - 1][w - item_cost] | {item_name}
                else:
                    dp[i][w] = dp[i - 1][w]
                    selected[i][w] = selected[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w]
                selected[i][w] = selected[i - 1][w]

    selected_items = list(selected[len(items)][budget])
    total_calories = dp[len(items)][budget]
    spent_budget = sum(items[item]["cost"] for item in selected_items)

    return selected_items, total_calories, spent_budget


def compare_algorithms(items, budget):
    """
    Порівняння результатів обох алгоритмів
    """
    greedy_items, greedy_calories, greedy_spent = greedy_algorithm(items, budget)
    dp_items, dp_calories, dp_spent = dynamic_programming(items, budget)

    print("Результати жадібного алгоритму:")
    print(f"Вибрані страви: {greedy_items}")
    print(f"Загальна калорійність: {greedy_calories}")
    print(f"Витрачений бюджет: {greedy_spent}")
    print("\nРезультати динамічного програмування:")
    print(f"Вибрані страви: {dp_items}")
    print(f"Загальна калорійність: {dp_calories}")
    print(f"Витрачений бюджет: {dp_spent}")


# Приклад використання
if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 100

    compare_algorithms(items, budget)