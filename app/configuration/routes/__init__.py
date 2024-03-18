from app.configuration.routes.routes import Routes
from app.internal.routes import currency

__routes__ = Routes(routers=(currency.router,))
