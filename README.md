# TODO CLI

Simple CLI app to manage tasks.

## Features

- add task
- show tasks
- find tasks by text or status
- toggle task done / undone
- edit task
- delete task
- tasks are saved to file
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

Find tasks by text or by status.

You can use:

- any text → search in task title
- `done` → show only completed tasks
- `notdone` → show only not completed tasks

Example (text search):

```text
command: find
find: buy
1. [ ] buy bread
3. [x] buy laptop
```

Example (`done`):

```text
command: find
find: done
2. [x] go gym
3. [x] buy laptop
```

Example (`notdone`):

```text
command: find
find: notdone
1. [ ] buy bread
```

If nothing is found:

```text
command: find
find: xyz
not found
```

---

### done

Toggle task status by number.

Example:

```text
command: done
task num: 1
task marked as done
```

---

### edit

Edit task text by number.

Example:

```text
command: edit
task num: 1
new task: buy milk
task updated
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

This project was integrated into a larger project: `life-cli`.
