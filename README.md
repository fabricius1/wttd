# Eventex

Sistema de eventos encomendado pela cliente.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.9.0
3. Ative o seu virtualenv
4. Instale as dependencias listadas em requeriments.txt
5. Configure a sua instância com o arquivo .env
6. Execute os testes.

```console
git clone git@github.com:fabricius1/wttd.git wttd
cd wttd
python -m venv .myvenv
source .myenv/bin/activate  # para usuários de Linux/Mac
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a sua instância
4. Defina DEBUG=False
5. Configure o serviço de email (instruções disponíveis, por exemplo, [neste site](https://www.hostinger.com.br/tutoriais/aprenda-a-utilizar-o-smtp-google/).)

```console
heroku create minhaInstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```