

def final_value_after_operations(operations):
    plus = set(["bouncy", "flouncy"])
    tigger = 1
    for operation in operations:
        if operation in plus:
            tigger += 1
        else:
            tigger -= 1
    print(tigger)


if __name__ == "__main__":
    operations = ["trouncy", "flouncy", "flouncy"]
    final_value_after_operations(operations)

    operations = ["bouncy", "bouncy", "flouncy"]
    final_value_after_operations(operations)