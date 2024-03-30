## Tutorial de como iniciar o programa de converter de moedas;

1. Instale o Python 3.11;
2. Na pasta do projeto instale as dependências com comando:
```
pip install -r requirements.txt
```
3. Inicie o programa com o comando:
```
python3 index.py
```
-----------------------------------------------------------------
1. Para chamar a API:
Com o programa rodando faça uma chamada HTTP com método POST para a rota '/converte-moedas' enviando um objeto como o exemplo abaixo:
```
{
    "valor": 100
}
```