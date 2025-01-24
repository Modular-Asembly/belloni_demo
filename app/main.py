from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers

from app.models.Transaction import Transaction
from app.models.Rule import Rule
from app.models.Alert import Alert
from app.api.receive_transaction import router
app.include_router(router)
from app.api.process_transaction import router
app.include_router(router)
from app.api.rules.create_rule import router
app.include_router(router)
from app.api.rules.update_rule import router
app.include_router(router)
from app.api.rules.delete_rule import router
app.include_router(router)
from app.api.rules.list_rules import router
app.include_router(router)

# Database

from app.modassembly.database.sql.get_sql_session import Base, engine
Base.metadata.create_all(engine)
