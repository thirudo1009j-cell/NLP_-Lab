import re
resumes = [
    """
    Name: Arjun Mehta
    Email: arjun.mehta23@gmail.com
    Mobile: +91-9876543210
    Skills: Python, SQL, Machine Learning
    Experience: 3 years of experience in data analysis and NLP projects.
    """,
    """
    Name: Sneha Reddy
    Email: sneha_reddy@company.co.in
    Phone: 9345678123
    Skills: Java, SQL
    Experience: 1 year of experience as a backend developer.
    """,
]
NAME_PATTERN = r"Name:\s*([A-Za-z]+(?:\s[A-Za-z]+)+)"
EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
MOBILE_PATTERN = r"(?:\+91[-\s]?)?[6-9]\d{9}"
EXPERIENCE_PATTERN = r"(\d+)\s+years?\s+of\s+experience"
SKILL_KEYWORDS = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
def extract_name(text):
    match = re.search(NAME_PATTERN, text)
    return match.group(1).strip() if match else "Not Found"
def extract_email(text):
    match = re.search(EMAIL_PATTERN, text)
    return match.group(0) if match else "Not Found"
def extract_mobile(text):
    match = re.search(MOBILE_PATTERN, text)
    return match.group(0) if match else "Not Found"
def extract_skills(text):
    found = []
    for skill in SKILL_KEYWORDS:
        # word-boundary, case-insensitive match for each known skill
        if re.search(r"\b" + re.escape(skill) + r"\b", text, re.IGNORECASE):
            found.append(skill)
    return found
def extract_experience(text):
    match = re.search(EXPERIENCE_PATTERN, text, re.IGNORECASE)
    return int(match.group(1)) if match else 0
def build_candidate_profile(resume_text):
    return {
        "name": extract_name(resume_text),
        "email": extract_email(resume_text),
        "mobile": extract_mobile(resume_text),
        "skills": extract_skills(resume_text),
        "experience": extract_experience(resume_text),
    }
def is_eligible(profile):
    return profile["experience"] >= 2 and "Python" in profile["skills"]
def print_summary(profile):
    print("Candidate Summary")
    print("-" * 40)
    print(f"Name        : {profile['name']}")
    print(f"Email       : {profile['email']}")
    print(f"Mobile      : {profile['mobile']}")
    print(f"Skills      : {', '.join(profile['skills']) if profile['skills'] else 'None'}")
    print(f"Experience  : {profile['experience']} year(s)")
    print("-" * 40)
def main():
    print("=" * 55)
    print("RESUME INFORMATION EXTRACTION SYSTEM")
    print("=" * 55)
    all_profiles = []
    for idx, resume in enumerate(resumes, start=1):
        print(f"\nProcessing Resume #{idx} ...")
        profile = build_candidate_profile(resume)
        all_profiles.append(profile)
        print_summary(profile)
    print("\n" + "=" * 55)
    print("ELIGIBLE CANDIDATES (>= 2 years experience & Python skill)")
    print("=" * 55)
    eligible = [p for p in all_profiles if is_eligible(p)]
    if eligible:
        for p in eligible:
            print(f"- {p['name']} | {p['experience']} yrs | Skills: {', '.join(p['skills'])}")
    else:
        print("No candidates meet the eligibility criteria.")
if __name__ == "__main__":
    main()

Output : 
=======================================================
RESUME INFORMATION EXTRACTION SYSTEM
=======================================================

Processing Resume #1 ...
Candidate Summary
----------------------------------------
Name        : Arjun Mehta
Email       : arjun.mehta23@gmail.com
Mobile      : +91-9876543210
Skills      : Python, SQL, Machine Learning, NLP
Experience  : 3 year(s)
----------------------------------------

Processing Resume #2 ...
Candidate Summary
----------------------------------------
Name        : Sneha Reddy
Email       : sneha_reddy@company.co.in
Mobile      : 9345678123
Skills      : Java, SQL
Experience  : 1 year(s)
----------------------------------------

=======================================================
ELIGIBLE CANDIDATES (>= 2 years experience & Python skill)
=======================================================
- Arjun Mehta | 3 yrs | Skills: Python, SQL, Machine Learning, NLP

Process finished with exit code 0
