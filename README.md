# VK_get_friends_report
task_improvado
Инструкция по запуску программы.
1. Получить Ваш acces_token на [сайте](https://vkhost.github.io/)
2. При необходимости установить пакет ```python -m pip install requests```
3. Запуск программы ```python main.py -t [Токен полученный на шаге 1] -u [Ваш vk id]```

Дополнительная информация по командам ```python main.py -h ```
```
usage: VK_get_friends_report [-h] -t TOKEN -u USER_ID [-f {csv,tsv,json}] [-p PATH]

Improvado Back-end test task for Junior

options:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        access token vk
  -u USER_ID, --user_id USER_ID
                        vk user_id
  -f {csv,tsv,json}, --format {csv,tsv,json}
                        format file
  -p PATH, --path PATH  path file save no extension
```
