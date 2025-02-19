from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CareerPath, FAQ, Contact
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .serializers import CareerPathSerializer, CareerCategorySerializer
# Create your views here.

class CareerListCreateView(generics.ListAPIView):
    queryset = CareerPath.objects.all()
    serializer_class = CareerPathSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CareerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CareerPath.objects.all()
    serializer_class = CareerPathSerializer
    permission_classes = [permissions.IsAuthenticated]

class CareerCategoryView(APIView):
    def get(self, request):
        categories = [ {"category": choice[0]} for choice in CareerPath.CATEGORY_CHOICES ]
        return Response(categories)

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

def career_detail(request, pk):
    career = get_object_or_404(CareerPath, pk=pk)
    related_careers = CareerPath.objects.filter(category=career.category).exclude(id=career.id)[:3]
    faqs = FAQ.objects.all()  # Fetch all FAQs

    return render(request, 'careers/career.html', {
        'career': career,
        'related_careers': related_careers,
        'faqs': faqs
    })

@login_required
def career_list(request):
    print("User:", request.user)  
    print("Authenticated:", request.user.is_authenticated)

    careers = CareerPath.objects.all()
    return render(request, 'careers/career_list.html', {'careers': careers})


def home(request):
    careers = CareerPath.objects.all()
    return render(request, 'careers/index.html',{'careers': careers})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("Username:", username)
        print("Password:", password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(" Login Successful!", user)

            # Redirect to the 'next' parameter if exists, otherwise to careers page
            next_url = request.GET.get('next', '/careers/')
            return redirect(next_url)
        else:
            print(" Login Failed!")
            messages.error(request, "Invalid Username or Password!")
            return redirect('login')

    return render(request, 'careers/login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')
    return render(request, 'careers/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def password_reset(request):
    return render(request, 'careers/password_reset.html')

def add_career(request):
    return render(request, 'careers/add-career.html')

def search_careers(request):
    query = request.GET.get('q', '')
    careers = CareerPath.objects.filter(name__icontains=query) if query else CareerPath.objects.all()
    
    return render(request, 'careers/search_results.html', {'careers': careers, 'query': query})

def about(request):
    return render(request, 'careers/about.html')

def contact(request):
    return render(request, 'careers/contact.html')

def submit_contact_form(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        country = request.POST.get('country')
        subject = request.POST.get('subject')


        # Save data to database (Optional)
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            country=country,
            subject=subject
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')  # Redirect to the contact page or success page

    return render(request, "contact.html")
