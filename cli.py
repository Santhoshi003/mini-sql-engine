from parser import parse_sql
from engine import execute

print("Mini SQL Engine")
print("Type 'exit' to quit")

while True:
    query = input("SQL> ").strip()

    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    try:
        parsed = parse_sql(query)
        result = execute(parsed)

        if isinstance(result, int):
            print("Result:", result)
        else:
            for row in result:
                print(row)

    except Exception as e:
        print("Error:", e)
