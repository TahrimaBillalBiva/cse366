import random
import os

def read_student_ids(filename):
    """Reads student IDs from a file and returns them as a list."""
    try:
        with open(filename, 'r') as file:
            student_ids = [line.strip() for line in file if line.strip()]
        return student_ids
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def ConductViva(student_ids):
    """Randomly selects students for viva, removes them from the list, and displays them with a counter."""
    viva_count = 1
    while student_ids:
        selected_student = random.choice(student_ids)
        print(f"Viva #{viva_count}: {selected_student}")
        student_ids.remove(selected_student)
        viva_count += 1
    print("All students have been selected. Resetting the list.")
    return viva_count - 1

def main():
    filename = "student_ids.txt"
    original_student_ids = read_student_ids(filename)

    if not original_student_ids:
        print("No student IDs available to select for viva.")
        return

    while True:
        student_ids = original_student_ids.copy()  # Reset the list
        total_vivas = ConductViva(student_ids)

        # Ask if they want to conduct another round of viva
        next_round = input(f"\nDo you want to reset and conduct another round of viva? (yes/no): ").strip().lower()
        if next_round != 'yes':
            print("Exiting the viva process.")
            break

if __name__ == "__main__":
    main()