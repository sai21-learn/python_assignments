# Day 1: User Profile Validation

## Challenge Description
Validate user profile information (name, email, age, mobile number) against specific criteria. All fields must pass to mark the profile as VALID.

## Approach / Logic Used
- Check each field independently: name must have space and no leading/trailing spaces
- Email must contain @ and . but not start with @
- Mobile must be exactly 10 digits, not starting with 0
- Age must be between 18-60 (exclusive)
- If all fields pass, profile is VALID; else INVALID

## Algorithm / Steps
1. Input and validate full name (check for space, no leading/trailing spaces)
2. Input and validate email (check @ and . presence, proper format)
3. Input and validate mobile (exactly 10 digits, no leading 0)
4. Input and validate age (18 < age < 60)
5. If all fields are valid, print "User Profile is VALID"
6. Otherwise, print "User Profile is INVALID"

## Sample Test Cases

### Test Case 1: Valid Profile ✓
**Input:**

FULL NAME : John Doe
EMAIL ID : john.doe@example.com
MOBILE NUMBER : 9876543210
AGE : 30

**Output:** User Profile is VALID

### Test Case 2: Invalid Email
**Input:**
```
FULL NAME : Jane Smith
EMAIL ID : jane.smith@example
MOBILE NUMBER : 8765432109
AGE : 28
```
**Output:** User Profile is INVALID

### Test Case 3: Invalid Age
**Input:**
```
FULL NAME : Bob Wilson
EMAIL ID : bob@yahoo.com
MOBILE NUMBER : 9111234567
AGE : 65
```
**Output:** User Profile is INVALID
