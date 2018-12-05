"""
 Created by 陈东东 on 2018/12/04.
"""
__author__ = '陈东东'

from flask import jsonify
from sqlalchemy import or_

from app.validators.forms import ArticleSearchForm
from app.libs.redprint import Redprint
from app.models.article import Article


# Redprint
api = Redprint('article')


# 文章搜索
@api.route('/search', methods=['POST'])
def search():
    # url:http://localhost:5000/v1/article/search?q={}
    form = ArticleSearchForm().validate_for_api()
    q = '%' + form.q.data + '%'
    # articles = Article()
    # 元类 ORM
    articles = Article.query.filter(
        or_(Article.title.like(q), Article.content.like(q))).all()
    articles = [article.hide('content', 'id').append('view') for article in articles]
    return jsonify(articles)


# 文章详情
@api.route('/detail/<int:art_id>', methods=['POST'])
def detail(art_id):
    article = Article.query.filter_by(id=art_id).first_or_404()
    return jsonify(article)

