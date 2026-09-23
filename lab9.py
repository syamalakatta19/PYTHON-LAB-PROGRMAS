# sams_analytics_engine.py
from functools import reduce

students = [
    {"roll_no": "SAMS24CS014", "name": "Ananya Rao", "cgpa": 9.9, "attendance": 92},
    {"roll_no": "SAMS24CS015", "name": "Rohit Verma", "cgpa": 9.0, "attendance": 100},
    {"roll_no": "SAMS24CS016", "name": "Divya Iyer", "cgpa": 10, "attendance": 100},
    {"roll_no": "SAMS24CS017", "name": "Karan Shah", "cgpa": 10, "attendance": 100},
]


def eligible_for_honours(students):
    return list(filter(lambda s: s["cgpa"] >= 8.0 and s["attendance"] >= 85, students))


def class_average_cgpa(students):
    total = reduce(lambda acc, s: acc + s["cgpa"], students, 0)
    return round(total / len(students), 2)


def topper_list(students, top_n=2):
    ranked = sorted(students, key=lambda s: s["cgpa"], reverse=True)
    return list(map(lambda s: (s["name"], s["cgpa"]), ranked[:top_n]))


if __name__ == "__main__":
    print("=== SAMS Analytics Engine ===")
    print("Honours-eligible:", [s["name"] for s in eligible_for_honours(students)])
    print("Class average CGPA:", class_average_cgpa(students))
    print("Toppers:", topper_list(students))
