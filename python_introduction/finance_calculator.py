# finance_calculator.py

# Demander les revenus et les dépenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calcul des économies mensuelles
monthly_savings = monthly_income - monthly_expenses

# Projection annuelle avec un taux d'intérêt de 5%
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Affichage des résultats
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
