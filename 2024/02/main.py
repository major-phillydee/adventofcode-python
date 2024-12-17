def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    reports = []
    for line in lines:
        levels = line.split()
        reports.append(levels)

    safe_reports_amount = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports_amount += 1

    print(safe_reports_amount)
    return safe_reports_amount


def is_report_safe(report):
    prev_val = 0
    direction = 1 if int(report[1]) - int(report[0]) > 0 else -1
    for idx, level in enumerate(report):
        if idx == 0:
            prev_val = int(level)
            continue
        if abs(int(level) - prev_val) > 3 or abs(int(level) - prev_val) < 1:
            return False
        if int(level) - prev_val > 0 and direction == -1:
            return False
        if int(level) - prev_val < 0 and direction == 1:
            return False
        prev_val = int(level)

    return True
        

if __name__ == "__main__":
    main()
