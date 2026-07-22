import re
REGISTER_NO_PATTERN = r"^\d{2}[A-Z]{3}\d{3}$"
EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@university\.edu\.in$"
COURSE_CODE_PATTERN = r"^[A-Z]{2,4}\d{2,3}$"
SEMESTER_PATTERN = r"^[1-8]$"
MOBILE_PATTERN = r"^(?:\+91[-\s]?)?[6-9]\d{9}$"
def validate_field(pattern, value):
    return bool(re.match(pattern, value.strip()))
def validate_student(student):
    results = {}
    results["Register Number"] = validate_field(REGISTER_NO_PATTERN, student["register_no"])
    results["Institutional Email"] = validate_field(EMAIL_PATTERN, student["email"])
    results["Course Code"] = validate_field(COURSE_CODE_PATTERN, student["course_code"])
    results["Semester"] = validate_field(SEMESTER_PATTERN, student["semester"])
    results["Mobile Number"] = validate_field(MOBILE_PATTERN, student["mobile"])
    return results
def print_validation_report(name, values, results):
    print(f"\nValidation Report for: {name}")
    print("-" * 55)
    for field, is_valid in results.items():
        status = "VALID" if is_valid else "INVALID"
        print(f"{field:<22}: {values[field]:<20} -> {status}")
    print("-" * 55)
    overall = all(results.values())
    final_status = "REGISTRATION SUCCESSFUL" if overall else "REGISTRATION FAILED"
    print(f"Final Status: {final_status}")
    return overall
def main():
    print("=" * 55)
    print("UNIVERSITY ONLINE REGISTRATION VALIDATION SYSTEM")
    print("=" * 55)
    students = [
        {
            "name": "Divya Prakash",
            "register_no": "22CSE101",
            "email": "divya.prakash@university.edu.in",
            "course_code": "NLP03",
            "semester": "6",
            "mobile": "+91-9876543210",
        },
        {
            "name": "Rohit Sharma",
            "register_no": "22CS101",
            "email": "rohit.sharma@gmail.com",
            "course_code": "cs101",
            "semester": "9",
            "mobile": "12345",
        },
    ]
    summary = []
    for student in students:
        values = {
            "Register Number": student["register_no"],
            "Institutional Email": student["email"],
            "Course Code": student["course_code"],
            "Semester": student["semester"],
            "Mobile Number": student["mobile"],
        }
        results = validate_student(student)
        overall = print_validation_report(student["name"], values, results)
        summary.append((student["name"], overall))
    print("\n" + "=" * 55)
    print("FINAL REGISTRATION STATUS REPORT")
    print("=" * 55)
    for name, status in summary:
        print(f"{name:<20}: {'SUCCESSFUL' if status else 'FAILED'}")
if __name__ == "__main__":
    main()



Output :
=======================================================
UNIVERSITY ONLINE REGISTRATION VALIDATION SYSTEM
=======================================================

Validation Report for: Divya Prakash
-------------------------------------------------------
Register Number       : 22CSE101             -> VALID
Institutional Email   : divya.prakash@university.edu.in -> VALID
Course Code           : NLP03                -> VALID
Semester              : 6                    -> VALID
Mobile Number         : +91-9876543210       -> VALID
-------------------------------------------------------
Final Status: REGISTRATION SUCCESSFUL

Validation Report for: Rohit Sharma
-------------------------------------------------------
Register Number       : 22CS101              -> INVALID
Institutional Email   : rohit.sharma@gmail.com -> INVALID
Course Code           : cs101                -> INVALID
Semester              : 9                    -> INVALID
Mobile Number         : 12345                -> INVALID
-------------------------------------------------------
Final Status: REGISTRATION FAILED

=======================================================
FINAL REGISTRATION STATUS REPORT
=======================================================
Divya Prakash       : SUCCESSFUL
Rohit Sharma        : FAILED

Process finished with exit code 0
