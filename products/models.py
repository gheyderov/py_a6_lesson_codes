from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


User = get_user_model()

# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        abstract = True


class Recipe(AbstractModel):
    category = models.ForeignKey(
        "Category", related_name="recipes", on_delete=models.CASCADE
    )
    tags = models.ManyToManyField("Tag", related_name="recipes")
    author = models.ForeignKey(User, related_name="recipes", on_delete=models.CASCADE)

    title = models.CharField("title", max_length=100)
    small_description = models.CharField("small_description", max_length=100)
    description = models.CharField("description", max_length=100)
    image = models.ImageField("image", upload_to="recipe_images/")
    cover_image = models.ImageField("cover_image", upload_to="recipe_images/")
    slug = models.SlugField("slug", max_length=200, null=True, blank=True)
    view_count = models.IntegerField("view_count", default=0)

    def author_name(self):
        return self.author.get_full_name()

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('recipe_detail', kwargs = {'slug' : self.slug})

    # class Meta:
    #     ordering = ['-created_at']


class RecipeComment(AbstractModel):
    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, null=True, blank=True
    )
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, related_name="comments", on_delete=models.CASCADE
    )
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.user.username} / {self.recipe}'


class RecipeImage(AbstractModel):
    recipe = models.ForeignKey(
        "Recipe", related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField("image", upload_to="recipe_images/")

    def __str__(self) -> str:
        return self.recipe.title


class Category(AbstractModel):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField("title", max_length=100)

    def __str__(self) -> str:
        if self.parent:
            return f"{self.parent} - {self.title}"
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Tag(AbstractModel):
    title = models.CharField("title", max_length=100)

    def __str__(self) -> str:
        return self.title


class BlockedIps(AbstractModel):
    ip_address = models.GenericIPAddressField()

    