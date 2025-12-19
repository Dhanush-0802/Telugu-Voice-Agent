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

def process_input(user_text):

    if memory["age"] is None:
        age = extract_age(user_text)
        if age is not None:
            memory["age"] = age
            return f"మీ వయస్సు {age} సంవత్సరాలు నమోదు చేశాను"
        else:
            return "మీ వయస్సు చెప్పండి"

    if memory["category"] is None:
        return "మీరు రైతా లేదా విద్యార్థివా చెప్పండి"

    if memory["income"] is None:
        return "మీ ఆదాయం తక్కువ లేదా ఎక్కువ అని చెప్పండి"

    return "మీ వివరాలు అందాయి. పథకం పరిశీలిస్తున్నాను"