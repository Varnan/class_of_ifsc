# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django import http
try:
    import httplib
except:
    import http.client as httplib

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from indian_banks import server_health_check
from indian_banks import helper


# Api for Server Landing Page
# URL : /
def ServerLanding(request):
    return http.HttpResponse()

# Api for Server Health Checking
# URL : /health or /health/
def HealthChecking(request):
    if not server_health_check.page_response('/'):
        return http.HttpResponse(status=httplib.SERVICE_UNAVAILABLE)

    if not server_health_check.migrations_have_applied():
        return http.HttpResponse(status=httplib.SERVICE_UNAVAILABLE)

    return http.HttpResponse()


# Api for list all branches
# URL : /branches/
class ListAllBranches(APIView):
    """ 
        Api for list all branches
        Author : Varnan
        METHOD : GET 
        SAMPLE PARAM :
            bank_name
            city

    """
    def get(self, request):
        bank_name = request.GET.get('bank_name', None)
        city = request.GET.get('city', None)
        page_no = request.GET.get('page_no', 1)
        page_count = request.GET.get('page_count', 10)

        status_code, data = helper.list_all_branches(page_no,page_count,bank_name,city)
        
        if not status_code:
            return Response({"message": data}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"data": data}, status=status.HTTP_200_OK)


# API for get branch details from IFSC code
# URL : /branch/<ifsc>/
class BranchDetails(APIView):
    """ 
        API for get branch details from IFSC code
        Author : Varnan
        METHOD : GET 

    """
    def get(self, request, ifsc):
        if not ifsc:
            return Response({"message": "Enter valid IFSC"}, status=status.HTTP_400_BAD_REQUEST)

        status_code, data = helper.get_branch_details(ifsc)
        
        if not status_code:
            return Response({"message": data}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"data": data}, status=status.HTTP_200_OK)
