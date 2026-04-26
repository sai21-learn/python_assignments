import random, copy, math
import numpy as np
import pandas as pd
def generate_students(n=12):
    return [
        {
            "id": i,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        for i in range(1, n + 1)
    ]
def mutate(data, roll):
    step = roll % 3 + 1
    for i, s in enumerate(data):
        if i % step == 0:
            s["marks"] += math.sqrt(s["marks"])
            s["attendance"] -= 5
            s["scores"][0] += 5
            s["scores"][1] += 3
def analyze(orig, mod):
    df_o, df_m = pd.DataFrame(orig), pd.DataFrame(mod)

    o_marks = df_o["marks"].values
    m_marks = df_m["marks"].values
    mean = np.mean(m_marks)
    std = np.std(m_marks)
    median = np.median(m_marks)
    manual_mean = sum(m_marks) / len(m_marks)
    drift = abs(np.mean(o_marks) - mean)
    return df_o, df_m, mean, median, std, drift, manual_mean

def classify(original_before, original_after, drift, th=5):
    if original_before != original_after:
        return "Copy Failure Detected"
    elif drift < th:
        return "Stable Data"
    elif drift < th * 2:
        return "Minor Drift"
    return "Critical Drift"

roll_no = 23
original = generate_students()
backup = copy.deepcopy(original)
shallow = copy.copy(original)
deep = copy.deepcopy(original)
mutate(shallow, roll_no)
mutate(deep, roll_no)
df_o, df_s, mean_s, med_s, std_s, drift_s, mmean_s = analyze(backup, shallow)
_, df_d, mean_d, med_d, std_d, drift_d, mmean_d = analyze(backup, deep)
result_s = classify(backup, original, drift_s)
result_d = classify(backup, backup, drift_d)

print("\n--- ORIGINAL ---\n", df_o)
print("\n--- SHALLOW COPY ---\n", df_s)
print("\n--- DEEP COPY ---\n", df_d)
print("\n--- SHALLOW STATS ---")
print((mean_s, drift_s, std_s))
print("\n--- DEEP STATS ---")
print((mean_d, drift_d, std_d))
print("\n--- RESULT ---")
print("Shallow:", result_s)
print("Deep:", result_d)