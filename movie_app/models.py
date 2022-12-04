from django.db import models



class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название фильма:')
    description = models.TextField(null=True, blank=True, verbose_name='Описание фильма:')
    duration = models.IntegerField(default=30)
    director = models.ForeignKey(to=Director, verbose_name='Режиссер:',
                                 related_name='movies', on_delete=models.CASCADE,
                                 null=True, blank=True)

    def __str__(self):
        return self.title



class Review(models.Model):
    rate = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    text = models.TextField("Ваш отзыв")
    movie = models.ForeignKey(to=Movie, verbose_name='Отзыв к фильму',
                              related_name='reviews', on_delete=models.CASCADE,
                              null=True, blank=True)
    stars = models.IntegerField(default=1, choices=rate)

    @property
    def movie_name(self):
        try:
            return self.movie.title
        except:
            return 'OSHIBKA'

    def __str__(self):
        return f"{self.movie}-{self.stars}"
