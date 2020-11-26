# python_intern
---

## requirements

- python 3.9
- В изначальном коде менять можно *всё*, вплоть до структуры файлов. 
- Использовать можно всё что угодно. 
- Таски со звёздочкой можно пропускать (или делать часть из них)
- Решение выложить через fork/копию/etc репозитория на github


## TODO

- реализовать функцию [is_alive_host](./app.py)

- покрыть функцию [тестами](./tests.py)

- развернуть вокруг функции веб сервис c помощью [fastapi](https://fastapi.tiangolo.com/)
```
>> curl your_service.loc:8001/healthz?hostname=semrush.com
{status: [up|down]}
```

- задача со *звёздочкой*: завернуть приложение в docker
- задача на *две звёздочки*: выкатить куда-либо с помощью github-actions/gitlab/jenkins/etc

## DONE
- [x] is_alive_host logic
- [x] tests
- [x] service 
- [x] Docker
- [x] github actions

## Installation and run
Uses Python 3.9, aiohttp, FastAPI, pytest-asyncio  

1. install dependencies  
  `pip install -r requirements.txt`
2. run tests:  
  `pytest tests.py`
3. start  
dev:  
`uvicorn service:app --host=127.0.0.1 --port=8001 --reload`  
prod:  
`gunicorn service:app --bind=127.0.0.1:8001 -w 4  -k uvicorn.workers.UvicornH11Worker`  
docker:  
`docker build --tag petrov-python-intern:latest .`  
`docker run -p 8001:8001 -d --name petrov-python-intern petrov-python-intern:latest`
