from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from .models import Student, Parent, Faculty, Transaction
from .forms import ParentForm, StudentForm, FacultyForm, TransactionForm

def login_view(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if role == 'student':
            try:
                user = Student.objects.get(mail=mail, password=password)
                request.session['user_id'] = user.uid
                request.session['role'] = 'student'
                return redirect('dashboard')
            except Student.DoesNotExist:
                messages.error(request, 'Invalid credentials for student. Please try again.')
        elif role == 'parent':
            try:
                user = Parent.objects.get(mail=mail, password=password)
                request.session['user_id'] = user.uid
                request.session['role'] = 'parent'
                return redirect('dashboard')
            except Parent.DoesNotExist:
                messages.error(request, 'Invalid credentials for parent. Please try again.')
        elif role == 'faculty':
            try:
                user = Faculty.objects.get(mail=mail, password=password)
                request.session['user_id'] = user.uid
                request.session['role'] = 'faculty'
                return redirect('dashboard')
            except Faculty.DoesNotExist:
                messages.error(request, 'Invalid credentials for faculty. Please try again.')

    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if role == 'student':
            if Student.objects.filter(mail=mail).exists():
                messages.error(request, 'Student with this email already exists. Please login.')
                return redirect('login')
            max_uid = Student.objects.aggregate(Max('uid'))['uid__max'] or 10
            uid = max_uid + 1
            Student.objects.create(uid=uid, mail=mail, password=password)
            request.session['user_id'] = uid
            request.session['role'] = 'student'
        elif role == 'parent':
            if Parent.objects.filter(mail=mail).exists():
                messages.error(request, 'Parent with this email already exists. Please login.')
                return redirect('login')
            max_uid = Parent.objects.aggregate(Max('uid'))['uid__max'] or 100
            uid = max_uid + 1
            Parent.objects.create(uid=uid, mail=mail, password=password)
            request.session['user_id'] = uid
            request.session['role'] = 'parent'
        elif role == 'faculty':
            if Faculty.objects.filter(mail=mail).exists():
                messages.error(request, 'Faculty with this email already exists. Please login.')
                return redirect('login')
            max_uid = Faculty.objects.aggregate(Max('uid'))['uid__max'] or 1000
            uid = max_uid + 1
            Faculty.objects.create(uid=uid, mail=mail, password=password)
            request.session['user_id'] = uid
            request.session['role'] = 'faculty'
        else:
            messages.error(request, 'Please select a role.')
            return redirect('signup')  # Redirect back to signup page if role not selected

        messages.success(request, 'Account created successfully. Please login.')
        return redirect('dashboard')

    return render(request, 'signup.html')

def dashboard(request):
    role = request.session.get('role')
    user_id = request.session.get('user_id')

    if role == 'student':
        user = get_object_or_404(Student, uid=user_id)
    elif role == 'parent':
        user = get_object_or_404(Parent, uid=user_id)
    elif role == 'faculty':
        user = get_object_or_404(Faculty, uid=user_id)
    else:
        messages.error(request, 'Invalid role.')
        return redirect('login')

    return render(request, 'dashboard.html', {'role': role, 'user': user})

def add_personal_details(request):
    role = request.session.get('role')
    if role == 'student':
        return redirect('student_form')
    elif role == 'parent':
        return redirect('parent_form')
    elif role == 'faculty':
        return redirect('faculty_form')

def student_form(request):
    user_id = request.session.get('user_id')
    student = get_object_or_404(Student, uid=user_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'student_form.html', {'form': form})

def parent_form(request):
    user_id = request.session.get('user_id')
    parent = get_object_or_404(Parent, uid=user_id)
    
    if request.method == 'POST':
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ParentForm(instance=parent)
    
    return render(request, 'parent_form.html', {'form': form})

def faculty_form(request):
    user_id = request.session.get('user_id')
    faculty = get_object_or_404(Faculty, uid=user_id)
    
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FacultyForm(instance=faculty)
    
    return render(request, 'faculty_form.html', {'form': form})

def transaction_form(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'transaction_form.html', {'form': form})

def logout_view(request):
    django_logout(request)
    return redirect('login')

def view_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'view_transactions.html', {'transactions': transactions})
