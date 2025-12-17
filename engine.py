from loader import load_csv

def apply_where(data, condition):
    if not condition:
        return data

    col = condition["col"]
    op = condition["op"]
    val = condition["val"]

    if col not in data[0]:
        raise ValueError(f"Column '{col}' does not exist")

    result = []

    for row in data:
        cell = row[col]
        if cell == "":
            continue

        try:
            cell_val = float(cell)
            val = float(val)
        except:
            cell_val = cell

        if (
            (op == "=" and cell_val == val) or
            (op == "!=" and cell_val != val) or
            (op == ">" and cell_val > val) or
            (op == "<" and cell_val < val) or
            (op == ">=" and cell_val >= val) or
            (op == "<=" and cell_val <= val)
        ):
            result.append(row)

    return result

def execute(query):
    data = load_csv(query["from"])
    data = apply_where(data, query["where"])

    if query["count"]:
        if query["count"].upper() == "COUNT(*)":
            return len(data)
        col = query["count"][6:-1]
        if col not in data[0]:
            raise ValueError(f"Column '{col}' does not exist")
        return sum(1 for r in data if r[col])

    if query["select"] == "*":
        return data

    for col in query["select"]:
        if col not in data[0]:
            raise ValueError(f"Column '{col}' does not exist")

    return [{col: row[col] for col in query["select"]} for row in data]
