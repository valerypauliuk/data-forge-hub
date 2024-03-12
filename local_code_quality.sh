#!/bin/bash
# Code quality check

# Проверяем, передан ли путь к файлу
if [ -z "$1" ]; then
    echo "Не указан путь к файлу."
    exit 1
fi

# Проверка Ruff without --fix
echo "Проверка Ruff..."
ruff сheck "$1"

# Проверка Pylint
echo "Проверка Pylint..."
pylint "$1"

# Проверка MyPy
echo "Проверка MyPy..."
mypy "$1"

# проверка coverage
echo "Введите путь до тестов, если хотите пропустить данный шаг, введите 'ENTER' "
read test_path
if [ -z "$test_path" ]; then
    echo "Не указан путь до тестов"
    exit 1
fi
coverage run --source="$1" -m pytest -v $test_path  && coverage html && coverage report -m

echo "Проверки завершены."

# для работы в Windows
echo "Нажмите любую клавишу, что бы закончить с проверкой!"
read test_path