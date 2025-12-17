import re

def parse_sql(query):
    query = query.strip().rstrip(";")

    pattern = re.compile(
        r"SELECT\s+(?P<select>.+?)\s+FROM\s+(?P<table>\w+)"
        r"(?:\s+WHERE\s+(?P<where>.+))?$",
        re.IGNORECASE
    )

    match = pattern.match(query)
    if not match:
        raise ValueError("Invalid SQL syntax")

    select_part = match.group("select").strip()
    table = match.group("table")
    where_part = match.group("where")

    result = {
        "select": None,
        "from": table,
        "where": None,
        "count": None
    }

    if select_part.upper().startswith("COUNT"):
        result["count"] = select_part
    elif select_part == "*":
        result["select"] = "*"
    else:
        result["select"] = [c.strip() for c in select_part.split(",")]

    if where_part:
        w = re.match(r"(\w+)\s*(=|!=|>=|<=|>|<)\s*'?(.+?)'?$", where_part)
        if not w:
            raise ValueError("Invalid WHERE clause")

        result["where"] = {
            "col": w.group(1),
            "op": w.group(2),
            "val": w.group(3)
        }

    return result
