Credit Cards
============

Example regex:
```regex
^\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b
```
(Note: we could have used `$` instead of \b at the end of the card number but this would cause validation to fail if, e.g., a person 
copy-pasted a number that had a trailing space.



Example test data:
```
123456789012345 # 15 digits (should not match)
abcd-abcd-abcd-abcd # not digits (should not match)
1234567890123456 # 16 digits (should match)
1234-5678-1234-9876 # 4 sets of dash-separated digits (should match)
4444 4444 4444 4444 # 4 sets of space-separated digits (should match)
12345678901234567 # 17 digits (should not match)
```
