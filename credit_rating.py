import json

def calculate_ltv(loan_amount, property_value):
    return (loan_amount / property_value) * 100

def calculate_dti(debt_amount, annual_income):
    return (debt_amount / annual_income) * 100

def calculate_credit_rating(mortgages):
    total_risk_score = 0
    total_credit_score = 0
    num_mortgages = len(mortgages)
    
    for mortgage in mortgages:
        risk_score = 0
        
        # Loan-to-Value Ratio
        ltv = calculate_ltv(mortgage['loan_amount'], mortgage['property_value'])
        if ltv > 90:
            risk_score += 2
        elif ltv > 80:
            risk_score += 1
        
        # Debt-to-Income Ratio
        dti = calculate_dti(mortgage['debt_amount'], mortgage['annual_income'])
        if dti > 50:
            risk_score += 2
        elif dti > 40:
            risk_score += 1
        
        # Credit Score
        credit_score = mortgage['credit_score']
        total_credit_score += credit_score
        if credit_score >= 700:
            risk_score -= 1
        elif 650 <= credit_score < 700:
            risk_score += 0
        else:
            risk_score += 1
        
        # Loan Type
        if mortgage['loan_type'] == 'fixed':
            risk_score -= 1
        elif mortgage['loan_type'] == 'adjustable':
            risk_score += 1
        
        # Property Type
        if mortgage['property_type'] == 'condo':
            risk_score += 1
        
        total_risk_score += risk_score
    
    # Adjust based on average credit score
    avg_credit_score = total_credit_score / num_mortgages
    if avg_credit_score >= 700:
        total_risk_score -= 1
    elif avg_credit_score < 650:
        total_risk_score += 1
    
    # Determine final credit rating
    if total_risk_score <= 2:
        return "AAA"
    elif 3 <= total_risk_score <= 5:
        return "BBB"
    else:
        return "C"
    
if __name__ == "__main__":
    with open("mortgages.json", "r") as f:
        data = json.load(f)
    rating = calculate_credit_rating(data["mortgages"])
    print(f"Credit Rating: {rating}")
