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