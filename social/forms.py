from django import forms
from PIL import Image, UnidentifiedImageError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Comment,Profile

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder':'Email address'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'placeholder':'Username'})}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirm password'})
        for field in self.fields.values():
            field.help_text=''

class PostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['topic'].required=False

    def clean_topic(self):
        return self.cleaned_data.get('topic') or 'BUILD'

    class Meta:
        model=Post
        fields=['topic','content','image','image_url']
        widgets={
            'content':forms.Textarea(attrs={'rows':4,'placeholder':'Share an idea, question or update...'}),
            'image':forms.ClearableFileInput(attrs={'accept':'image/*'}),
            'image_url':forms.URLInput(attrs={'placeholder':'Or paste an image URL (optional)'})
        }
    def clean_image(self):
        image=self.cleaned_data.get('image')
        if image and image.size>5*1024*1024:
            raise forms.ValidationError('Use an image smaller than 5 MB.')
        if image:
            try:
                with Image.open(image) as opened:
                    opened.verify()
            except (UnidentifiedImageError, OSError, ValueError):
                raise forms.ValidationError('Upload a valid image file.')
            finally:
                image.seek(0)
        return image

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        widgets={'content':forms.TextInput(attrs={'placeholder':'Add a thoughtful comment...'})}

class ProfileForm(forms.ModelForm):
    first_name=forms.CharField(required=False,max_length=30)
    last_name=forms.CharField(required=False,max_length=30)
    email=forms.EmailField(required=True)
    class Meta:
        model=Profile
        fields=['bio','avatar_url','location']
