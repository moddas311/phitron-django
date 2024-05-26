from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
   data ={'author': 'Korim Uddin', 'friend': 'zayed khan','age': 20, 'serial': 100, 'title': 'Korim bhai er bazar date of birth and courses details',
          'list': ['Alu', 'Potol', 'Jinga', 'Lau'],
            'birthday': datetime.datetime.now(), 
            'val': '',
            'time': datetime.datetime.now(),
            'post': '1 June 2006',
            'courses': [
               {
                  'id': 1,
                  'name': 'python',
                  'fee': 5000,
               },
               {
                  'id': 2,
                  'name': 'django',
                  'fee': 10000,
               },
               {
                  'id': 3,
                  'name': 'DSA',
                  'fee': 13900,
               }]
        }
   return render(request, 'home.html', context=data)

def about(request):
   
   
   data = {
      'name': 'Amir Khan',
      'roll': 1001,
      'class': 10,
      'title': 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. A dolorem illo autem sed in.',
      'dream': '',
      'course': 'phitron',
      'values': [1, 2, 3, 4, 5],
      'time': datetime.datetime.now(),
      'books': ['Physics', 'Chemistry', 'Math', 'Biology'],
      'friends': [
         {
            'name': 'Shakib Khan',
            'roll': 1002,
            'class': 11,
            'books': ['Physics', 'Chemistry', 'Math', 'Biology'],
         },
         {
            'name': 'Salman Khan',
            'roll': 1003,
            'class': 10,
            'books': ['Physics', 'Chemistry', 'Math', 'Biology'],
         },
         {
            'name': 'Rubel Khan',
            'roll': 1007,
            'class': 11,
            'books': ['Physics', 'Chemistry', 'Math', 'Biology'],
         },
         {
            'name': 'Omuk Khan',
            'roll': 1009,
            'class': 11,
            'books': ['Physics', 'Chemistry', 'Math', 'Biology'],
         },
      ]
   }
   return render(request, 'about.html', context=data)

