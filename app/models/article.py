"""
 Created by 陈东东 on 2018/12/04.
"""
__author__ = '陈东东'
from sqlalchemy import Column, String, Integer, orm

from app.models.base import Base


class Article(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(String(200))
    thumb = Column(String(50))
    content = Column(String(1000))
    author = Column(String(30), default='未名')
    view = Column(Integer)
    create_time = Column(String(20))

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'title', 'author', 'description',
                       'thumb',
                       'content', 'create_time']
