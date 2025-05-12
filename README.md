# Flask API

Uma API simples que fornece operações de soma e multiplicação.

## Endpoints

- `POST /soma`: Soma dois números
- `POST /multiplicacao`: Multiplica dois números

## Como executar

### Com Docker

1. Construa a imagem:

```bash
docker build -t flask-api .
```

2. Execute o container:

```bash
docker run -p 80:80 flask-api
```

A API estará disponível em http://localhost:80

## Exemplos de uso

### Soma

```bash
curl -X POST http://localhost:80/Calculator/soma -H "Content-Type: application/json" -d '{"x": 5, "y": 3}'
```

### Multiplicação

```bash
curl -X POST http://localhost:80/Calculator/multiplicacao -H "Content-Type: application/json" -d '{"x": 5, "y": 3}'
```
