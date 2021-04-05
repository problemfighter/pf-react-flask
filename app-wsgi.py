import sys
import os

sys.path.insert(0, '/home/v-host/api-goods-mama.problemfighter.com/application')
os.environ['env'] = 'prod'

from bismillah import app as application