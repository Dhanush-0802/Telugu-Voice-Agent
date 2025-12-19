import re

memory = {
    "age": None,
    "category": None,
    "income": None
}
def extract_age(text):
    numbers = re.findall(r'\d+', text)
    if numbers:
        return int(numbers[0])
    return None

def extract_category(text):
    if "రైతు" in text:
        return "farmer"
    if "విద్యార్థి" in text:
        return "student"
    if "వృద్ధుడు" in text or "సీనియర్" in text:
        return "senior"
    return None

def extract_income(text):
    if "తక్కువ" in text:
        return"low"
    if "ఎక్కువ" in text:
        return"high"
    return None

def check_eligibility():

    if memory["category"] == "student" and memory["income"] == "low":
        return "విద్యార్థి స్కాలర్‌షిప్ పథకం"

    if memory["category"] == "farmer" and memory["income"] == "low":
        return "రైతు భరోసా పథకం"

    if memory["category"] == "senior":
        return "వృద్ధాప్య పెన్షన్ పథకం"

    return "సాధారణ ప్రభుత్వ సహాయ పథకం"

"""
 The logics or functions present 
 above are use to collect the data 
 from user and use it for giving a 
 proper response.
"""

def process_input(user_text):

    if memory["age"] is None:
        age = extract_age(user_text)
        if age is not None:
            memory["age"] = age
            return f"మీ వయస్సు {age} సంవత్సరాలు నమోదు చేశాను"
        else:
            return "మీ వయస్సు చెప్పండి"

    if memory["category"] is None:
        category = extract_category(user_text)
        if category is not None:
            memory["category"] = category
            return "మీ వర్గం నమోదు చేశాను"
        else:
            return "మీరు రైతా, విద్యార్థివా లేదా సీనియర్ సిటిజన్ వా చెప్పండి"

    if memory["income"] is None:
        income = extract_income(user_text)
        if income is not None:
            memory["income"] = income
            return "మీ ఆదాయం నమోదు చేశాను"
        else:
            return "మీ ఆదాయం తక్కువ లేదా ఎక్కువ అని చెప్పండి"


    scheme = check_eligibility()
    return f"మీకు {scheme} అర్హత ఉంది. ధన్యవాదాలు."