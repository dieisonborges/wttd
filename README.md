# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/dieisoncomix/wttd.svg?branch=master)](https://travis-ci.org/dieisoncomix/wttd)

[![Coverage Status](https://coveralls.io/repos/github/dieisoncomix/wttd/badge.svg?branch=master)](https://coveralls.io/github/dieisoncomix/wttd?branch=master)

[![Maintainability](https://api.codeclimate.com/v1/badges/31a43bed14565486e996/maintainability)](https://codeclimate.com/github/dieisoncomix/wttd/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/31a43bed14565486e996/test_coverage)](https://codeclimate.com/github/dieisoncomix/wttd/test_coverage)

## Como desenvolver

1. Clone o Repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/dieisoncomix/wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy

1. Crie uma instância no heroku.
2. Envie as configurações no heroku.
3. Define uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force
```