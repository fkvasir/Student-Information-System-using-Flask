from flask import Blueprint, render_template, request
from app.services import search_service

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        results = search_service.search_all(query)
        return render_template('search_results.html', results=results)

    return render_template('search.html')
