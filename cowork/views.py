from django.views.generic import TemplateView
from authtools.views import LoginRequiredMixin
from accounts import const
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
import json
import sys

from . import mixins
from . import models

from cowork.models import Desk, Location, Company


class DashboardView(mixins.UserMixin, LoginRequiredMixin, TemplateView):
    template_name = 'cowork/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.user.user_type == const.USER_TYPE_COMPANY:
            context['last_locations'] = models.Location.objects.filter(company__user=self.user)[:5]
        return context


class SearchView(TemplateView):
    template_name = 'cowork/search.html'


def desks(request):
    locations = Location.objects.all()
    list = [] #create list
    for row in locations: #populate list
        list.append({'company_name':row.company.name, 'total_desks':row.total_desks, 'free_desks':row.free_desks, 'price':str(row.price), 'logo': row.company.image_url})
    list_json = json.dumps(list) #dump list as JSON
    return HttpResponse(list_json, 'application/json')


def desksByCity(request):
    if request.GET.get('city', False):
        city = request.GET['city']
        filterEmpty = request.GET['filter']
        locations = Location.objects.filter(city=city)
        list = [] #create list
        for row in locations: #populate list
            if 'true' in filterEmpty:
                if(row.free_desks > 0):
                    list.append({'company_name':row.company.name, 'total_desks':row.total_desks, 'free_desks':row.free_desks, 'price':str(row.price), 'logo': row.company.image_url})
            else:
                list.append({'company_name':row.company.name, 'total_desks':row.total_desks, 'free_desks':row.free_desks, 'price':str(row.price), 'logo': row.company.image_url})              
        list_json = json.dumps(list) #dump list as JSON
        return HttpResponse(list_json, 'application/json')
    else:
        list = []
        #list.append({'city':request.GET.get('city', False))
        return HttpResponse(json.dumps(list), 'application/json')


def rentDesk(request):
    if request.user.is_authenticated():
        user = request.user.id
        rent_start = request.GET['rent_start_date']
        rent_end = request.GET['rent_end_date']
        location = request.GET['location']
        desk = Desk(owner_id=user, rent_start_date=rent_start, rent_end_date=rent_end, location_id=location)
        try:
            desk.save()
            location = Locations.models.get(id=location)
            location.reserved_desks += 1
            location.save()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=400)

    else:
        return HttpResponse(status=303)