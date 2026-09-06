import re
with open("../input/raw-text.txt") as f:
    text = f.read()
emails = re.findall(r"[A-Za-z0-9._-]+@[A-Za-z0-9_-]+\.[A-Za-z0-9.]+(?:[A-Za-z0-9]+)", text)
print(emails)

alu_official = []
alu_alumni = []
alu_si = []
other_emails = []

for email in emails:
    aluv = re.fullmatch(r"[A-Za-z0-9._-]+@((si|alumni)\.)?alueducation\.com", email)
    if aluv is None:
        other_emails.append(email)
    else:
        sub = aluv.group(2)
        if sub is None:
            alu_official.append(email)
        elif sub == "alumni":
            alu_alumni.append(email)
        elif sub == "si":
            alu_si.append(email)

    
print("\nALU official accounts: \n", alu_official)
print("\nALU Alumni accounts: \n", alu_alumni)
print("\nALU Si accounts: \n", alu_si)
print("\nOther valid emails: \n", other_emails)

phoneNos_intl = re.findall(r"\+250[ -]?(?:\(0\))?[ -]?7[98532]\d[ -]?\d{3}[ -]?\d{3}", text)
print("\nInternational format phone numbers:\n", phoneNos_intl)

phoneNos_local = re.findall(r"07[98532]\d{7}", text)
print("\nLocal format phone numbers:\n", phoneNos_local)

creditCards = re.findall(r"\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b", text)
print("\nValid Credit cards:\n", creditCards)

url = re.findall(r"https?://[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_?=-]+)*", text)
print("\nValid URLs:\n", url)

masked_cards = []

for card in creditCards:
    digits = card.replace(" ", "").replace("-", "")
    masked = "**** **** **** " + digits[-4:]
    masked_cards.append(masked)
print("\nMasked Cards:\n", masked_cards)

masked_emails = []

for email in emails:
    local, domain = email.split("@", 1)
    masked = local[0] + "***@" + domain
    masked_emails.append(masked)
print("\nMasked Emails:\n", masked_emails)

results = {
    "alu_official": alu_official,
    "alu_alumni": alu_alumni,
    "alu_si": alu_si,
    "other_emails": masked_emails,
    "phones_international": phoneNos_intl,
    "phones_local": phoneNos_local,
    "credit_cards": masked_cards,
    "urls": url
}

with open("../output/sample-output.json", "w") as f:
    json.dump(results, f, indent=2)