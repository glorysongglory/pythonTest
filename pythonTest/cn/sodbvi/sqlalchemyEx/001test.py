from sqlalchemy import create_engine,func,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import randint

engine = create_engine("mysql+pymysql://root:[gy~7QFB@123.207.178.189/test1", encoding='utf-8', echo=True)
# 基类
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


# Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

# user=User(name='a',password='1')
# session.add(user)
# session.commit()
# session.close()
#
# user_list=[]
# user_b=User(name='b',password='testb')
# user_c=User(name='c',password='testc')
# user_list.append(user_b)
# user_list.append(user_c)
#
# session.add_all(user_list)
# session.commit()
# session.close()

list=session.query(User).all();
list=session.query(User.name).all();
list=session.query(User).filter(User.name=='a').all()
list=session.query(User).filter(User.id>7,User.name.in_(['a','b'])).all()
list=session.query(User).filter(User.name.like('%c')).all()
list=session.query(User).filter(or_(User.name == 'c',User.id==7)).all()
list=session.query(User).order_by(User.id.desc())
print(session.query(func.count('1')).select_from(User).scalar())
print(session.query(func.count(User.id)).filter(User.id > 7 ).scalar())

#批量新增
session.execute(
    User.__table__.insert(),
    [{'name': randint(1, 100),'password': randint(1, 100)} for i in range(10000)]
)
session.commit()


# for x in list:
#     print(x.name)






