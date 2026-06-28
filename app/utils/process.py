import subprocess


def run_command(command: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        command,
        capture_output=True,
        text=True,
    )





"""Почему отдельный файл?

Потому что позже здесь же появятся:

timeout
логирование
обработка ошибок
выполнение в фоне
запуск ffmpeg
запуск других утилит"""