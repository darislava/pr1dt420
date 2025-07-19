


from notes import NoteBook

notebook = NoteBook.load_notes()


def handle_add_note(args):
    if not args:
        return "Введіть текст нотатки після команди."
    text = args[0]
    tags = args[1:] if len(args) > 1 else []
    notebook.add_note(text, tags)
    return "Нотатку додано."


def handle_show_notes(_):
    return notebook.list_notes()


def handle_find_note(args):
    if not args:
        return "Введіть слово для пошуку."
    result = notebook.find_notes(args[0])
    if result:
        return "\n\n".join(str(note) for note in result)
    return "Нічого не знайдено."


def handle_edit_note(args):
    if len(args) < 2:
        return "Введіть номер нотатки та новий текст."
    try:
        index = int(args[0]) - 1
        new_text = " ".join(args[1:])
        if notebook.edit_note(index, new_text):
            return "Нотатку відредаговано."
        return "Нотатку не знайдено."
    except ValueError:
        return "Номер нотатки має бути числом."


def handle_delete_note(args):
    if len(args) < 1:
        return "Введіть номер нотатки для видалення."
    try:
        index = int(args[0]) - 1
        if notebook.delete_note(index):
            return "Нотатку видалено."
        return "Нотатку не знайдено."
    except ValueError:
        return "Номер нотатки має бути числом."


COMMANDS = {
    "add-note": handle_add_note,
    "show-notes": handle_show_notes,
    "find-note": handle_find_note,
    "edit-note": handle_edit_note,
    "delete-note": handle_delete_note,
}


def main():
    print("Персональний помічник з нотатками (введіть 'exit' для завершення)")
    while True:
        user_input = input(">> ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "close"):
            notebook.save_notes()
            print("Нотатки збережено. До побачення!")
            break

        parts = user_input.split()
        command = parts[0].lower()
        args = parts[1:]

        handler = COMMANDS.get(command)
        if handler:
            result = handler(args)
            print(result)
        else:
            print("Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()