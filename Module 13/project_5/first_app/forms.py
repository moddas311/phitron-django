from django import forms
from django.core import validators


# widgets == field to html input 
class contactForm(forms.Form):
    name = forms.CharField(label = "Full Name: ", help_text="Tepye Your Name", required=False, 
                           widget=forms.Textarea(attrs={'id': 'text_area', 'class': 'class1 class2', 
                                                        'placeholder': 'Enter Your Full Name'}))
    # file = forms.FileField()
    email = forms.EmailField(label = "User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('s', 'small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)
    meal = [("P", 'Peperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices = meal, widget=forms.CheckboxSelectMultiple)
    
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)
    
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter a name with at least 10 characters.')
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Enter a valid email')
    #     return valemail
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter a name with at least 10 characters.')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Enter a valid email and contain with .com')
    
    
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Enter a value at least 10 characters.')
    
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, 
            message='Enter a name with at least 10 characters.')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.EmailField(widget=forms.EmailInput, validators=[validators.EmailValidator])
    age = forms.CharField()
    age = forms.IntegerField(validators = [validators.MaxValueValidator(34, message='Age must be maximum 34'), 
            validators.MinValueValidator(24, message='Age must be minimum 24')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpj'])])
    
    
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = self
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError('Password doesn''t match.')
        if len(val_name) < 15:
            raise forms.ValidationError('Name must be at least 15 characters.')