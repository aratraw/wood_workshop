from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify as django_slugify

from django.conf import settings

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.




    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        default='',
        editable=False,
        unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]

        k = self.parent

        while k is not None:
            full_path.append(k.title)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    slug = models.SlugField(
        default='',
        editable=False,
        unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', related_name='items')

    def get_upload_path(self, filename):
        return "projects/{}/{}".format(self.slug, filename)

    thumbnail = models.ImageField(
        upload_to=get_upload_path, default='thumbnail_default.jpg')
    slug = models.SlugField(
        default='',
        editable=False,
        unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:project-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


"""  LABEL_CHOICES = (
    ('P', 'primart'),
    ('S', 'secondary'),
    ('D', 'danger')
)  """


class ShopItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)

    def get_upload_path(self, filename):
        return "projects/{}/{}".format(self.slug, filename)

    thumbnail = models.ImageField(
        upload_to=get_upload_path, default='thumbnail_default.jpg')
    slug = models.SlugField(
        default='',
        editable=False,
                unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:shop-detail", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Image(models.Model):

    def get_upload_path(self, filename):
        return "projects/{}/{}".format(self.project.slug, filename)
    image = models.ImageField(
        upload_to=get_upload_path)


class OrderItem(models.Model):
    item = models.ForeignKey(ShopItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username


""" ui_size = models.CharField(choices=SIZE_CHOICES, max_length=1) """
