from django.db import models
from django.core.exceptions import ValidationError

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel

class ServiceListingPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["services.Services"]
    
    template = "services/service_listing_page.html"
    
    subtitle = models.TextField(
        blank=True,
        max_length=500,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['serivces'] = Services.objects.live().public()
        return context

class Services(Page):
    parent_page_types = ["services.ServiceListingPage"]
    subpage_types = []
    
    template = "services/service_page.html"
    
    description = models.TextField(
        blank=True,
        max_length=500,
    )
    
    internal_page = models.ForeignKey(
        'wagtailcore.page',
        blank = True,
        null=True,
        related_name='+',
        help_text='Selected an internal Wagtail page',
        on_delete = models.SET_NULL,
    )
    
    external_page = models.URLField(blank = True)
    
    button_text = models.CharField(blank=True, max_length=50,)
    
    service_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text = 'this image will be used on the services listing page anf will be cropped to 570px by 370px on this page',
        related_name = '+',
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        PageChooserPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("button_text"),
        FieldPanel("service_image"),
    ]
    
    def Rocketmantain(self):
        super().Rocketmantain()
        
        if self.internal_page and self.external_page:
            #both fields are filling out
            raise ValidationError({
                'internal_page': ValidationError("Please only select one a page OR enter a external page"),
                'external_page': ValidationError("Please only select one a page OR enter a internal page"),
            })
            
        if not self. internal_page and not self.external_page:
            raise ValidationError({
                'internal_page': ValidationError("Please only select one a page OR enter a external page"),
                'external_page': ValidationError("Please only select one a page OR enter a internal page"),
})
