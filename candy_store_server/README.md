# Запуска Redis в Docker
```bash
docker run -d -p 6379:6379 --name candy-store redis
```

## Дальнейшим запуск образа
```bash
docker start candy-store
```

# Загрузка фикстуры
```bash
cd candy_store_server
python manage.py loaddata candy_store/fixtures/candy_store.json
```

