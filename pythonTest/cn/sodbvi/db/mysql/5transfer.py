# coding:utf8
import sys
import MySQLdb

class TransferMoney(object):
    
    def __init__(self, conn):
        self.conn = conn
        
    def transfer(self, source_acctId, target_acctId, money):
        try:
            self.check_acct_avaliable(source_acctId)
            self.check_acct_avaliable(target_acctId)
            self.has_enouth_money(source_acctId,money)
            self.reduce_money(source_acctId, money)
            self.add_money(target_acctId, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        
    def check_acct_avaliable(self, acctId):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctId=%s" % acctId
            cursor.execute(sql)
            print sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("帐号%s不存在" %acctId)
        finally:
            cursor.close()
                
        
    def has_enouth_money(self, acctId, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctId=%s and money > %s" % (acctId, money)
            print sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("帐号%s不存在")
        finally:
            cursor.close()
            
    
    def reduce_money(self, acctId,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money -%s where acctId=%s " % (money, acctId)
            print sql
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("帐号%s没有足够钱")
        finally:
            cursor.close()
    def add_money(self, acctId,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money +%s where acctId=%s " % (money, acctId)
            print sql
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("帐号%s没有足够钱")
        finally:
            cursor.close()


if __name__ == "__main__":
    source_acctId = sys.argv[1]
    target_acctId = sys.argv[2]
    money = sys.argv[3]
    conn = MySQLdb.Connect(
                     host='127.0.0.1',
                     port=3306,
                     user='root',
                     passwd='',
                     db='imooc',
                     charset='utf8'
                     )
    
    tr_money = TransferMoney(conn)
    
    try:
        tr_money.transfer(source_acctId, target_acctId, money)
        
    except Exception as e:
        print "出现的问题" + str(e);
    
    finally:
        conn.close()
        
        
    
    
