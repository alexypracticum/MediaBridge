import subprocess


def run_command(command: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

def start_process(command: list[str]):

    return subprocess.Popen(
        command,
        stdout=subprocess.PIPE, # "Не выводи текст сразу в терминал. Отдай его мне."
        stderr=subprocess.STDOUT,
        text=True, # Чтобы получать строки "[download] 17.3%"
        bufsize=1, # Включает построчную буферизацию.
    )



"""Почему отдельный файл?

Потому что позже здесь же появятся:

timeout
логирование
обработка ошибок
выполнение в фоне
запуск ffmpeg
запуск других утилит"""