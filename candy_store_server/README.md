# Запуска Redis в Docker
```bash
docker run -d -p 6379:6379 --name candy-store redis
```

## Дальнейшим запуск образа
```bash
docker start candy-store
```