import pandas as pd

data = {
    "skill": ["Variables", "Loops", "Functions", "Lists"],
    "score": [90, 65, 40, 55]
}

df = pd.DataFrame(data)

df["status"] = df["score"].apply(
    lambda x:
        "Strong" if x >= 80
        else "Needs Practice" if x >= 60
        else "Needs Improvement"
)

print(df)