import datetime
import os

import pandas as pd
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class GetResult(APIView):
    def get(self, *args, **kwargs):
        df = pd.read_excel(os.path.join(settings.MEDIA_ROOT, 'data.xlsx'))
        day = self.request.GET.get('day')
        if day is not None:
            try:
                day = int(day) - 1
            except Exception as ex:
                raise ValueError("can't cast to integer")

            data = df.iloc[day].to_list()
            col_list = df.columns

            new_col = [
                col.strftime('%H:%M') if isinstance(col, datetime.time) else 'Day'
                for col in col_list
            ]

            data_dict = {new_col[i]: data[i] for i in range(len(new_col))}

            return Response(data_dict, status=status.HTTP_200_OK)
        return Response()
