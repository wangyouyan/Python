#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

r = redis.Redis(host='10.211.55.4', port=6379)
r = redis.Redis(connection_pool=)
r.set('foo', 'Bar')
print r.get('foo')