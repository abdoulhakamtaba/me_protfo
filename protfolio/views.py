from django.shortcuts import render
import csv
from .forms import SubscriberForm

# Create your views here.
def page_view(request):
    
    if request.method == 'POST':
        form = SubscriberForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            print(email)
            write_to_csv(email)

    return render(request, 'index.html')


def write_to_csv(data):
    with open('/Users/abdoul taba/Desktop/TABA/Django/project10_protfo/me_protfo/database.csv', mode='a') as database:
        email = data
        csv_writer = csv.writer(database)
        csv_writer.writerow([email])

write_to_csv({'email':'as@jkl'})
