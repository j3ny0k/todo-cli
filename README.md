# TODO CLI

Simple CLI app to manage tasks.

## Features

- add task
- show tasks
- find tasks by text
- toggle task done / undone
- tasks are saved to file
- delete task
- input validation
- invalid task number handling
- empty input handling

---

## Usage

Run the program:

```bash
python todo-cli.py
```

---

## Commands

### add

Add a new task.

Example:

```text
command: add
task: buy bread
```

---

### show

Show all tasks.

Example:

```text
1. [ ] buy bread
2. [x] go gym
```

---

### find

Find tasks by text.

Example:

```text
command: find
find: buy
1. [ ] buy bread
3. [x] buy laptop
```

If nothing is found:

```text
command: find
find: xyz
not found
```

---

### done

Mark a task as done by number.

Example:

```text
command: done
task num: 1
task marked as done
```

---

### delete

Delete a task by number.

Example:

```text
command: delete
task num: 2
task deleted
```

---

### exit

Exit the program.

---

### help

Show available commands.

---

## Notes

- tasks are saved in `tasks.json`
- tasks stay after restart
- `tasks.json` is local data (not pushed to GitHub)
- task number must be an integer
- empty input is handled
- invalid task number is handled
- no tasks case is handled
- find is case-insensitive

---

## Note

This project was later integrated into a larger project: life-cli, where tasks and expenses are combined into a single CLI application.
