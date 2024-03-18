from fastapi import APIRouter
from app.pkg.redis_tools.tools import RedisTools

router = APIRouter(
    prefix='/api/v1/currency',
    tags=['Получение цены валютной пары']
)


@router.get('/{pair}')
def get_currency_pair(pair: str):
    if pair not in [s.decode('utf-8') for s in RedisTools.get_keys()]:
        return {
            'error': 'Не найдена заданная валютная пара'
        }

    return {
        'pair': pair,
        'price': RedisTools.get_pair(pair)
    }
