import importlib
import pkgutil
import os


import python_workout_pkg.exercises as exercises_pkg


def _load_all_exercises() -> None:
    """Auto-import every module under workout.exercises so decorators fire."""
    for finder, name, _ in pkgutil.walk_packages(
        path=exercises_pkg.__path__,
        prefix=exercises_pkg.__name__ + ".",
    ):
        importlib.import_module(name)


def _print_menu(entries: list) -> None:
    print("\n" + "═" * 40)
    print("   🏋️  Python Workout")
    print("═" * 40)

    current_chapter = None
    for idx, (meta, _cls) in enumerate(entries, start=1):
        if meta.chapter != current_chapter:
            current_chapter = meta.chapter
            print(f"\n  {meta.chapter}")
        print(f"    [{idx:>2}] {meta.id}  —  {meta.title}")

    print("\n    [q]  Quit")
    print("═" * 40)


def _clear_console() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    _clear_console()
    _load_all_exercises()

    from python_workout_pkg.exercise_registry import get_all

    while True:
        entries = get_all()

        if not entries:
            print(
                "No exercises registered yet. Add some to src/python_workout_pkg/exercises/"
            )
            break

        _print_menu(entries)

        raw = input("\n> ").strip().lower()

        if raw == "q":
            print("Bye! 💪")
            break

        if not raw.isdigit() or not (1 <= int(raw) <= len(entries)):
            print("Invalid choice, try again.")
            continue

        _clear_console()
        meta, cls = entries[int(raw) - 1]
        print(f"\n{'─' * 40}")
        print(f"  {meta.title}")
        print(f"  {meta.description}")
        print(f"{'─' * 40}\n")

        try:
            cls.run()
        except KeyboardInterrupt, EOFError:
            print("\n(interrupted)")

        input("\n[Enter] back to menu...")
        _clear_console()
