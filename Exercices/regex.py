import re
text = "Contact me at 123-456-7890\n"
digits = re.findall(r'\d+', text)
print(digits)

updated_text = re.sub(r'\d+', 'X', text)
updated_text2 = re.sub(r'\d', 'X', text)

print(updated_text)
print(updated_text2)

def cleaned_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = " ".join(text.split())
    return text.lower()

input_text = "       Hello here!! ... How are you?        "
cleaned_text = cleaned_text(input_text)
print(cleaned_text)
