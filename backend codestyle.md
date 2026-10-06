## 1. Naming Conventions

- Variables and functions: snake_case, e.g. `get_history`, `init_database`
- Constants: UPPER_SNAKE_CASE
- Class names: UpperCamelCase

## 2. Indentation

- Use 4 spaces for indentation. Tab characters are not allowed.

## 3. Quotes

- Use single quotes `' '` for string literals.

## 4. Database Rules

- Close SQLite connection after every database operation.
- Do not commit `calc_history.db` to the Git repository.

## 5. Error Handling

- API must use try-except to catch runtime exceptions and return friendly error messages.

## 6. Comments

- Add concise comments for complex logic. Avoid redundant comments.
