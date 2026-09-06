# Data Extraction & Security Validation System
This system extracts and validates structured data from raw text using regular expressions.
## Running it
```
cd src/
python3 main.py
```

Reads `input/raw-text.txt` and writes `output/sample-output.json`
## What it extracts
- **Email addresses**, with ALU-specific classification into `@alueducation.com`, `@alumni.alueducation.com`, and `@si.alueducation.com`
- **Phone numbers** in Rwandan international (`+250 ...`) and local (`07...`) formats
- **Credit card numbers** in 16-digit form with space, hyphen, or separator
- **URLs** including subdomains, paths, and query strings
## Security considerations
Input is treated as untrusted. Card numbers are masked to the last four digits and email local parts are obscured before anything is written to `/output/`, so raw sensitive values never reach disk.
The input file contains deliberate injection-style payloads (`<script>`blocks, SQL fragments). These are only ever searched as text - never executed, evaluated, or interpolated into another context. A URL found inside a script payload is extracted but flagged as untrusted rather than treated as a legitimate link.
## Known limitations
- A URL ending a sentence may capture the trailing period.
- Card matching allows mixed separators; no Luhn checksum is performed.
- Duplicate occurences are reported separately rather than deduplicated.

**Author:** [RyanGakire](https://github.com/RyanGakire)