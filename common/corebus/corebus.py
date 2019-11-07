#
# CoreBus
# Redis interface for AVT ADAS DataBridge
#
# @NamoDev, September 2019
#

import time
import redis
from common.utils.debugprint import DebugPrint as dp

class CoreBus():

    # Initiate connection:
    def __init__(self, max_redis_wait = 3, redis_host = "127.0.0.1", redis_port = "6379"):

        # This counts how long we've waited
        rdswait = 0
        while rdswait <= max_redis_wait:
            try:
                conn = redis.Redis(host = redis_host, port = redis_port)
                break;
            except:
                rdswait += 1
                dp.debugPrint("CoreBus: unable to establish redis connection", "error")

                # Wait time exceeded
                if(rdswait >= max_redis_wait):
                    exit(1)

                # Wait for a second before retrying
                time.sleep(1)

        dp.debugPrint("CoreBus: connected to redis at redis://" + redis_host + ":" + redis_port, "success")
        self.connection = conn
