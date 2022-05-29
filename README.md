# transaction_system

Реализация системы транзакций.

Как происходит транзакция:

Идет запрос на сервер от клиента, по клиенту выстраивается очередь на вывод.

Важно :

1) у каждого клиента есть своя очередь; 
2) при нехватке денег, нужно блокировать запрос

Что нужно реализовавть : 
1) бд на postgresql, где будет схема с клиентами и их балансами
2) сервер, которые проверяет все условия(хватает ли денег, если сервер упадет, то история, которая идет на вывод не должна пропасть) и делает изменение баланса(на + или -)

# implementation

docker-compose services:

app

celery

database

redis


To build project and to install all dependences use command:

docker-compose build

To run server use:

docker-compose up

To stop any service use:

docker-compose stop [name of service]

The Django admin site:

Host: localhost

Port: 8000
