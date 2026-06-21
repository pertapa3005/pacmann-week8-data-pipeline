from sqlalchemy import create_engine

SOURCE_DB = "postgresql://postgres:postgres@localhost:5433/source_db"
STAGING_DB = "postgresql://postgres:postgres@localhost:5434/staging_db"
WAREHOUSE_DB = "postgresql://postgres:postgres@localhost:5435/warehouse_db"
LOG_DB = "postgresql://postgres:postgres@localhost:5436/log_db"


def get_source_engine():
    return create_engine(SOURCE_DB)


def get_staging_engine():
    return create_engine(STAGING_DB)


def get_warehouse_engine():
    return create_engine(WAREHOUSE_DB)


def get_log_engine():
    return create_engine(LOG_DB)