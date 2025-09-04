TOTAL_CREDIT = 17
tuition_fee = eval(input())
living_expenses = 5.0 * eval(input())
loan = (tuition_fee * TOTAL_CREDIT + living_expenses) * 0.6
print(f"本学期你能够贷款{loan:.2f}元")
