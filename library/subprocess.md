# subprocess

## Запуск внешних приложений

Вы можете легко отображать сообщения **libnotify** (Xfce4) из программы на Python или любом другом языке.

Вам понадобится обвязка **libnotify** для Python:

  pacman -S python-notify

Вот простой "hello world" пример на python:

```python
import subprocess

info = "Hello world!"
subprocess.call(['notify-send', info])
```

Подробнее:

* <https://docs.python.org/3/library/subprocess.html> :en:
* <https://natenka.gitbook.io/pyneng/part_ii/12_useful_modules/subprocess>
* <https://pythonworld.ru/moduli/modul-subprocess.html>
* <https://ru.wikibooks.org/wiki/Учебник_Python/Процессы_и_потоки>
* <https://proft.me/2009/04/9/zapusk-vneshnih-prilozhenij-v-python/>
* <https://python-scripts.com/subprocess>
