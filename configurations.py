from environs import Env

env = Env()
env.read_env()


DB_ENGINE = env('DB_ENGINE')
DB_USER = env('DB_USER')
DB_NAME = env('DB_NAME')
DB_PASSWORD = env('DB_PASSWORD')
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')

