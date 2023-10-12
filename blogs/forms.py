from django.forms import ModelForm


from blogs.models import Blogs

class BlogForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'title-input'
        self.fields['author'].widget.attrs['class'] = 'title-input'


    class Meta:
        model = Blogs
        fields = '__all__'