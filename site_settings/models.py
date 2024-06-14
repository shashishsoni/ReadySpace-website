from django.db import models
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

from wagtail.fields import RichTextField
# Create your models here.

@register_setting
class ContactSetting(BaseSiteSetting):
    
    contact = RichTextField(
        blank = True,
        null = True,
        features = ["link"],
        
    )
    
    def save(self, *args,**kwargs):
        
        key = make_template_fragment_key("footer_contact_setting")
        cache.delete(key)
        
        return super().save(*args, **kwargs)
    
@register_setting
class HoursSetting(BaseSiteSetting):
    
    hours = RichTextField(
        blank = True,
        null = True,
        features = ["link"],
        
    )
    
    panels = [
        FieldPanel("hours")
    ]
    
    def save(self, *args,**kwargs):
        
        key = make_template_fragment_key("footer_hours_setting")
        cache.delete(key)
        
        return super().save(*args, **kwargs)

@register_setting
class SocialMediaSetting(BaseSiteSetting):
    
    facebook = models.URLField(
        blank = True,
        help_text = "Enter your Facebook URL"
    )
    twitter = models.URLField(
        blank = True,
        help_text = "Enter your Twitter URL"
    )
    youtube = models.URLField(
        blank = True,
        help_text = "Enter your Youtube URL"
    )
    instagram = models.URLField(
        blank = True,
        help_text = "Enter your Instagram URL"
    )
    
    panels = [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("youtube"),
        FieldPanel("instagram"),
    ]
    
    def save(self, *args,**kwargs):
        
        key = make_template_fragment_key("footer_social_setting")
        cache.delete(key)
        
        return super().save(*args, **kwargs)
    
@register_setting
class FooterCTASetting(BaseSiteSetting):
    
        title = models.CharField(max_length=100)
        subtitle = models.CharField(max_length=250)
        button_text = models.CharField(max_length=25, default='Contact Us')
        button_internal_page = models.ForeignKey(
            'wagtailcore.Page',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+',
            help_text='If an internal page is selected, it will be used before the external page.'
        )
        button_external_page = models.URLField(blank=True, help_text='If an internal page is selected, it will be used before the external page.')

        panels = [
            FieldPanel("title"),
            FieldPanel("subtitle"),
            FieldPanel("button_text"),
            PageChooserPanel("button_internal_page"),
            FieldPanel("button_external_page"),
        ]

        def save(self, *args, **kwargs):
            key = make_template_fragment_key("footer_cta_settings")
            cache.delete(key)
            return super().save(*args, **kwargs)
        
    
    