
from django.db.models import Q
from indian_banks import models
from indian_banks import serializers

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def list_all_branches(page_no,page_count,bank_name,city):
    branches = models.Branches.objects.all()
    if bank_name:
        branches = branches.filter(Q(bank__name__icontains=bank_name))

    if city:
        branches = branches.filter(Q(city__icontains=city))

    paginator = Paginator(branches, page_count)

    try:
        branches = paginator.page(page_no)
    except PageNotAnInteger:
        branches = paginator.page(1)
    except EmptyPage:
        branches = paginator.page(paginator.num_pages)


    serializers_data = list(serializers.BranchSerializer(branches,many=True).data)


    context = {}
    context['branches'] = serializers_data
    context['total_pages'] = paginator.num_pages
    context['page_no'] = page_no
    context['page_count'] = page_count

    return True, context

def get_branch_details(ifsc):
    try:
        branch_obj = models.Branches.objects.get(ifsc__iexact=ifsc)
    except models.Branches.DoesNotExist:
        return False, "Data not available for the given ifsc {ifsc}".format(ifsc=ifsc)

    serializers_data = dict(serializers.BranchSerializer(branch_obj).data)

    return True, serializers_data

