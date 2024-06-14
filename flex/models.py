from django.db import models
from wagtail.models import Page

from wagtail.fields import StreamField

from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail import blocks as wagtail_blocks

from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.images.blocks import ImageChooserBlock

from streams import blocks
from home.models import new_table_option

# Create your models here.

class FlexPage(Page):
    parent_page_types = ["home.HomePage", "flex.FlexPage"]
    
    body = StreamField([
         ("title", blocks.TitleBlock()),
         ("cards", blocks.Cardsblocks()),
         ("image_and_text", blocks.ImageAndTextBlocks()),
         ("cta", blocks.CallToActionBlock()),
         ("testimonial", SnippetChooserBlock(
            target_model='testimonials.testimonial',
            template = "streams/testimonial.html"
        )),
         ("pricing_table", blocks.PricingTableBlock(
            template = "streams/pricing_table_block.html",
            table_options = new_table_option
        )),
         ("richtext", wagtail_blocks.RichTextBlock(
            template = "streams/simple_richtext_block.html",  
        )),
          ("large_image", ImageChooserBlock(
            help_text = "this is the iamge that be cropprd to 1200px by 775px",
            template = "streams/large_image_blocks.html",
        ))
     ], null = True, blank = True, use_json_field = True
)
    
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
    
    class Meta:
        verbose_name = "Flex (misc) page"
        verbose_name_plural = "Flex (misc) page"
        