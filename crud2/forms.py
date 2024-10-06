from django import forms

class user_form(forms.Form):
    name = forms.CharField(label= 'Enter Your Name', label_suffix= '', required=True, error_messages={'required': 'Name is required.'})
    email = forms.EmailField(label= 'Email', label_suffix= '', initial='@gmail.com', required=True, error_messages={'required': 'Email is required.'})
    password = forms.CharField(label= 'Password', label_suffix= '', widget=forms.PasswordInput, required=True, error_messages={'required': 'Password is required.'})
    repassword = forms.CharField(label= 'Retype Password', label_suffix= '', widget=forms.PasswordInput, required=True, error_messages={'required': 'Retype Password is required.'})
    textbox = forms.CharField(widget=forms.Textarea, label= 'Comment', label_suffix= '', required=False)
    # file = forms.CharField(widget=forms.FileInput, label= 'Add your photo', label_suffix='', required=False)
    # checkbox = forms.CharField(widget=forms.CheckboxInput, label= 'Check', label_suffix='', required=True, error_messages={'required': 'Must check this box.'})
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     password_confirmation = cleaned_data.get('repassword')
    #     if password != password_confirmation:
    #         raise forms.ValidationError('Passwords do not match')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('repassword')

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')

        return cleaned_data
