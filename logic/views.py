from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import json
from collections import defaultdict
from django.core.serializers.json import DjangoJSONEncoder

HOME_SQL = '''SELECT  s.*, t.id as tag_id, t.tag, u.username
FROM slide_tag st
INNER JOIN slide s ON s.id = st.slide_id
INNER JOIN tag t ON t.id = st.tag_id
INNER JOIN "user" u ON u.id = s.user_id
INNER JOIN ( 
	SELECT st.tag_id, count(st.tag_id) as counts
	FROM slide_tag AS st
	GROUP BY st.tag_id 
	ORDER BY counts DESC
) AS c ON t.id = c.tag_id
ORDER BY c.counts DESC;'''

def dictfetchall(cursor):
    # TODO limit the number of tags in the query or use faster datastuct
    # **row[9] = row.tag**  getting tag by int index is error prone
    columns = [col[0] for col in cursor.description]
    result = defaultdict(list)
    ordering = []
    for row in cursor.fetchall():
        if row[9] not in ordering: ordering.append(row[9])  
        result[row[9]].append(dict(zip(columns, row)))
    return result, ordering

def index(request):
    with connection.cursor() as cursor:
        cursor.execute(HOME_SQL)
        slides, ordering = dictfetchall(cursor)

    context = {
        "props": json.dumps({
            "slides": slides,
            "ordering": ordering 
        }, cls=DjangoJSONEncoder),
        "component": "home.js"
    }
    
    return render(request, 'logic/index.html', context)

# Create your views here.
