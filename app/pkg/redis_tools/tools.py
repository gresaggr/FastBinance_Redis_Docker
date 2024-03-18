import redis


class RedisTools:
    __redis_connect = redis.Redis(host='redis', port=6379)

    @classmethod
    def set_pair(cls, pair: str, price: str):
        """
        Set the pair and price in the Redis connection.

        :param pair: str - The pair to set the price for.
        :param price: str - The price to set for the pair.
        :return: None
        """
        cls.__redis_connect.set(pair, price)

    @classmethod
    def get_pair(cls, pair):
        """
        Get the value for a given pair in the Redis cache.

        :param pair: The key to retrieve the value for.
        :return: The value corresponding to the key in the Redis cache.
        """
        return cls.__redis_connect.get(pair)

    @classmethod
    def get_keys(cls):
        return cls.__redis_connect.keys(pattern='*')
