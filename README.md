# cloudru-test
### Задание 1
Для запуска через скрипт (playbook/setup.sh) заполните файл playbook/inventory.ini актуальными данными.   

<a>WARN</a> Часть "разрешает на хосте авторизацию через ssh по ключу" интерпретирована как "разрешает на хосте авторизацию через ssh *только* по ключу".   
Опционально: если не проброшен ключ и в дальнейшем нужен ssh от старого пользователя, ssh-copy-id перед запуском скрипта.

### Задание 2
#### 2.1 App & Dockerfile  
Приложение: Flask, json&html over http.  
Dockerfile: multistage, alpine в качестве базы, вначале трансляция в Си и компиляция, на выходе свежий alpine с объектным файлом - 17.8MB.

#### 2.2 K8s manifest
Проверялось локально с minikube/kvm. Ограничения на память ставились по анализу `kubectl top pods`.

#### 2.3 Helm chart
Отредактированный `helm create test-task`. Namespace создавался отдельно через kubectl.