# Day 2: SmartID Credential Validator

## Challenge Description
Validate student credentials with four components: Student ID (CSE-XXX), Email (.edu domain), Password (8+ chars, uppercase, digit), and Referral Code (REF##@). All must pass for APPROVED verdict.

## Approach / Logic Used
- Student ID: Must be CSE-XXX format (7 chars total)
- Email: Must be valid .edu email with @ and .
- Password: Minimum 8 chars, starts with uppercase, contains digit
- Referral Code: REF##@ format (6 chars total)
- All four components must be valid for APPROVED; any failure means REJECTED

## Algorithm / Steps
1. Input all four credentials and strip whitespace
2. Validate Student ID format (CSE- + 3 digits)
3. Validate Email format (.edu domain required)
4. Validate Password strength (length, uppercase, digit)
5. Validate Referral Code format (REF + 2 digits + @)
6. If all valid, print "APPROVED"; else "REJECTED"

## Sample Test Cases

### Test Case 1: All Valid
**Input:**
```
CSE-789, student789@college.edu, Secure1pass, REF45@
```
**Output:** APPROVED

### Test Case 2: Invalid Email
**Input:**
```
CSE-456, student@gmail.com, Password123, REF23@
```
**Output:** REJECTED

### Test Case 3: Invalid Password
**Input:**
```
CSE-123, user@university.edu, password12, REF89@
```
**Output:** REJECTED
