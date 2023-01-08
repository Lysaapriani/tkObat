from pymongo import MongoClient
conn = MongoClient('mongodb://root:p455w0rd@172.21.196.108/transactions?authSource=admin')
dbObat= MongoClient('mongodb://root:p455w0rd@172.21.196.108/obats?authSource=admin')
dbUser= MongoClient('mongodb://root:p455w0rd@172.21.196.108/users?authSource=admin')
