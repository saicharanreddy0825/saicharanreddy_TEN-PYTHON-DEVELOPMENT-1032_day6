# ============================================================
#  Marks Calculator — 5 Students
#  Outputs: Total, Average, Highest, Lowest Marks
# ============================================================

# ── BUG 1 — RUNTIME ERROR ───────────────────────────────────
# Type  : IndexError
# Cause : Trying to access marks[5] but list has only 5 items
#         (valid indexes are 0–4, index 5 is out of range)
# Fix   : Change marks[5] to marks[4] to access the last element

# BUGGY CODE:
# marks = []
# for i in range(5):
#     m = int(input("Enter marks for student " + str(i+1) + ": "))
#     marks.append(m)
# print("Last student marks:", marks[5])   # ❌ IndexError! index 5 doesn't exist

# FIXED CODE:
# marks = []
# for i in range(5):
#     m = int(input("Enter marks for student " + str(i+1) + ": "))
#     marks.append(m)
# print("Last student marks:", marks[4])   # ✅ index 4 = last element


# ── BUG 2 — LOGICAL ERROR ───────────────────────────────────
# Type  : LogicalError
# Cause : Average is calculated by dividing total by 4 instead of 5
#         so the average will always be wrong (higher than actual)
# Fix   : Divide by 5 (total number of students), not 4

# BUGGY CODE:
# total = sum(marks)
# average = total / 4    # ❌ Wrong! Should divide by 5 not 4

# FIXED CODE:
# total = sum(marks)
# average = total / 5    # ✅ Correct — 5 students


# ============================================================
#  FINAL WORKING PROGRAM (with both bugs fixed)
# ============================================================

marks = []

# Taking input from user for 5 students
for i in range(5):
    m = int(input("Enter marks for student " + str(i+1) + ": "))
    marks.append(m)

# Calculations
total   = sum(marks)
average = total / 5        # ✅ Bug 2 fixed — divide by 5
highest = max(marks)
lowest  = min(marks)

# Output
print("-----------------------------")
print("Total Marks   :", total)
print("Average Marks :", average)
print("Highest Marks :", highest)
print("Lowest Marks  :", lowest)
print("-----------------------------")
