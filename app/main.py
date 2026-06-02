from fastapi import FastAPI
from app.api import books, authors , librarians, members, loans, resgistration, login
from app.middleware.auth import auth_middleware
app = FastAPI(
    title="Library API",
    description="API with JWT Authentication",
    version="1.0.0",
    openapi_tags=[
        {"name":"auth", "description":"Authentication routes"},
        {"name":"books", "description":"Protected book routes"}
    ],
    swagger_ui_init_oauth={
        "usePkceWithAuthorizationCodeGrant":True
    }
)
original_openapi = app.openapi
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = original_openapi()

    if "components" not in openapi_schema:
        openapi_schema["components"] = {}

    if "securitySchemes" not in openapi_schema["components"]:
        openapi_schema["components"]["securitySchemes"] = {}

    openapi_schema["components"]["securitySchemes"]["BearerAuth"] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
    }

    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


app.middleware("http")(auth_middleware)

app.include_router(login.router, prefix="/login", tags=["Login"])
app.include_router(resgistration.router, prefix="/registration", tags=["Registration"])
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(authors.router, prefix="/authors", tags=["Authors"])
app.include_router(librarians.router, prefix="/librarians", tags=["Librarians"])
app.include_router(members.router, prefix="/members", tags=["Members"])
app.include_router(loans.router, prefix="/loans", tags=["Loans"])