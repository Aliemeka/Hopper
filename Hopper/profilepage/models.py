from django.db import models
from django.urls import reverse


class Profile(models.Model):
    '''
    Class holds profile information for each user that registers to the site
    '''
    name = models.CharField(max_length = 250, null=True)                   
    username = models.CharField(max_length = 20, null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    photo = models.FileField(null=True)

    def get_absolute_url(self):
        return reverse('profilepage:userprofile', kwargs={'pk': self.pk})

    def get_id(self):
        return self.pk

    def __str__(self):
        return self.name + ' @' + self.username 
    def title(self):
        return self.name + ' @' + self.username 
    
    

class Hobby(models.Model):
    '''
    Class holds the atttribute of hobbies and links them to a particular profile
    '''
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)  #maps the hobby to the primary key of the user
    hobby = models.CharField(max_length = 25)                   #name of hobby
    hobby_nature = models.CharField(max_length = 25)            #description of hobby
    is_favorite = models.BooleanField(default = False)          #used to add favorite hobby

    def get_absolute_url(self):
        return reverse('profilepage:add-hobby', kwargs={'pk': self.pk})
    
    def get_user(self):
        return self.user

    def get_hobby(self):
        return self.hobby

    def get_info(self):
        return self.hobby + ' Description: ' + self.hobby_nature
    
    def __str__(self):
        return self.hobby
