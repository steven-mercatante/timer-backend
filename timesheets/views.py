from django.db import connection
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Entry
from .serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SummaryView(APIView):
    # TODO: throw 400 if require query params are missing
    def get(self, request):
        query = """
        SELECT
            p.name AS project_name
            , SUM(seconds) AS total_time
            , logged_for AS for_date
        FROM
            timesheets_entry te
        INNER JOIN 
            projects_project p ON p.id = te.project_id
        WHERE 
            logged_for >= %s
            AND logged_for <= %s
            AND deleted_at IS NULL
            AND seconds >= 60
        GROUP BY
            project_name, for_date
        ORDER BY
            for_date, project_name
        """
        with connection.cursor() as cursor:
            cursor.execute(query, [
                request.query_params['start_date'],
                request.query_params['end_date']
            ])
            result = cursor.fetchall()
            print(result)
        return Response(result)
