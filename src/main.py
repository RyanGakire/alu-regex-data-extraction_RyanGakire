import json
import re

#opening and reading the raw-text.txt file
with open("../input/raw-text.txt") as f:
    text = f.read()
emails = re.findall(r"[A-Za-z0-9._-]+@[A-Za-z0-9_-]+\.[A-Za-z0-9.]+(?:[A-Za-z0-9]+)", text)
print(emails)

# Validates an extracted address against the three ALU domains. The
# subdomain is captured in a group so a successful match also tells us
# Which category the address belongs to; when the optional group is
# absent the address is a plain @alueducation.com account
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

# Matches Rwandan international numbers: +250 country code, an optional
# (0) trunk prefix, then a 7-series mobile prefix (72/73/75/78/79)
# Followed by three groups of digits. Separators may be spaces or hyphens.
phoneNos_intl = re.findall(r"\+250[ -]?(?:\(0\))?[ -]?7[98532]\d[ -]?\d{3}[ -]?\d{3}", text)
print("\nInternational format phone numbers:\n", phoneNos_intl)

phoneNos_local = re.findall(r"07[98532]\d{7}", text)
print("\nLocal format phone numbers:\n", phoneNos_local)

# Matches 16-digit card numbers written as four groups of four digits.
# Separator between groups may be a space, a hyphen, or absent.
# \b prevents matching a 16-digit run inside a longer number.
creditCards = re.findall(r"\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b", text)
print("\nValid Credit cards:\n", creditCards)

# Matched http and https URLs: scheme, domain (letters, digits, dots,
# hyphens, underscores), then zero or more path segments which may
# include query characters.
url = re.findall(r"https?://[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_?=-]+)*", text)
print("\nValid URLs:\n", url)

# Masks card numbers before output: separators are stripped so every
# card is a uniform digit string, then only the final four digits are
# retained. Raw values are never written to disk.
masked_cards = []

for card in creditCards:
    digits = card.replace(" ", "").replace("-", "")
    masked = "**** **** **** " + digits[-4:]
    masked_cards.append(masked)
print("\nMasked Cards:\n", masked_cards)

# Masks email addresses before output: the address is split at the first
# @, and only the first character of the local part is kept. The domain
# is preserved so ALU addresses remain identifiable in the results.
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