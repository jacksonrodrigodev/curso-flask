SECRET_KEY = "api_secret_key"

SQLALCHEMY_DATABASE_URI = "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
    SGBD="mysql+mysqlconnector",
    usuario="root",
    senha="admin",
    servidor="db",
    database="jogoteca",
)
