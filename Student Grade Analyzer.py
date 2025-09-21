# 
def analyze_scores(students_data):
    lowest_score = min(students_data, key=lambda x: x[1])
    highest_score = max(students_data, key=lambda x: x[1])
    average = round(sum(score for _, score in students_data) / len(students_data), 2)
    passed = [(name, score) for name, score in students_data if score >= 70]
    failed = [(name, score) for name, score in students_data if score < 70]
    fail_count = len(failed)
    sort_asc = sorted(students_data, key=lambda x: x[0])

    result = {
        'highest': highest_score,
        'lowest': lowest_score,
        'average': average,
        'passed': passed,
        'failed': failed,
        'fail_count': fail_count,
        'Sorted': sort_asc
    }
    return result


# Main program
num_students = int(input('How many are the new Students:	'))
students = []

for i in range(1, num_students + 1):
    name = input(f"Enter the name of Student #{i}:  ")
    clean_name = name.strip().title()
    while True:
        try:
            score = float(input(f'Score:  '))
            if 1 <= score <= 100:
                students.append((clean_name, score))
                break
            else:
                print('Please enter a score between 1 and 100.')
        except ValueError:
            print('Invalid Input! Please enter a numeric value.')

# Process and output results
results = analyze_scores(students)

print("\n--- Analysis Summary ---")
print(f"Highest Scorer: {results['highest'][0]} - {results['highest'][1]}")
print(f"Lowest Scorer: {results['lowest'][0]} - {results['lowest'][1]}")
print(f"Average Score: {results['average']}")
print(f"Passed Students ({len(results['passed'])}): {results['passed']}")
print(f"Failed Students ({results['fail_count']}): {results['failed']}")
