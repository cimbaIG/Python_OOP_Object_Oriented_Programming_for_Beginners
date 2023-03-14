## Solution
### Classes and their attributes and methods
- `Todo` (or it can be called `Task`)
  * Instance attributes: `description`, `priority`, `category`, `due_date`, `classroom`.
  * Possible values:
    + `priority`: "urgent", "intermediate", "optional". These could be represented as strings or as integers (2,1,0).
    + `category`: "Personal", "Academic", "Work", "Leisure".
  * Method:
    + `.update()` - update the information in the to-do.
- `TodoList`
  * Instance attributes: `num_todos`
  * Methods:
    + `.show()` - a method to display all the to-dos in the list.
    + `.add()` - a method to add a to-do to the list.
    + `.remove()` - a method to remove a to-do from the list.
    + `.update()` - a method to update the list with multiple to-dos
    + `.clear()` - a method to clear the list (remove all the to-dos)
- `Course`
  * Instance attributes: `code`,`professor`, `start`, `end`, `classroom`.
  * Methods:
    + `.update_professor()` - a method to update the professor for a course.
- `Classroom`
  * Instance attributes: `location`, `building`
- `Professor`
  * Instance attributes: `name`, `phone`, `email`.
We could also include properties for these attributes to add getters and setters.