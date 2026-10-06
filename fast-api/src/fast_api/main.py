from fastapi import FastAPI

from fast_api.controllers import item_controller, root_controller

app = FastAPI()

app.include_router(root_controller.router)
app.include_router(item_controller.router)