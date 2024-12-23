from fastapi import APIRouter

router = APIRouter()

# Rota de autenticação (login, refresh de token, etc.)
@router.post("/login")
def login():
    return {"message": "Login realizado com sucesso!"}

@router.post("/refresh-token")
def refresh_token():
    return {"message": "Token de atualização realizado com sucesso!"}

@router.post("/logout")
def logout():
    return {"message": "Logout realizado com sucesso!"}

