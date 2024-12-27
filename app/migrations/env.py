# from __future__ import with_statement
# import sys
# from os.path import abspath, dirname
# sys.path.insert(0, abspath(dirname(__file__)))
#
# from sqlalchemy import engine_from_config, pool
# from alembic import context
# from app.models.models import Base  # Importa a base do SQLAlchemy
# from app.database.database import SQLALCHEMY_DATABASE_URL  # Sua URL de banco de dados
#
# config = context.config
# config.set_main_option('sqlalchemy.url', SQLALCHEMY_DATABASE_URL)
#
# target_metadata = Base.metadata  # Aqui você passa a metadata dos seus modelos
#
# def run_migrations_online():
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section),
#         prefix='sqlalchemy.',
#         poolclass=pool.NullPool)
#
#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection,
#             target_metadata=target_metadata)
#
#         with context.begin_transaction():
#             context.run_migrations()
#
# if __name__ == '__main__':
#     run_migrations_online()
