from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        verbose_name='Название',
        help_text='Введите название группы',
        max_length=200
    )
    slug = models.SlugField(
        verbose_name='URL',
        help_text='Введите адрес ссылки на группу',
        max_length=25,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите подробное описание группы'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'группы публикаций'
        verbose_name_plural = 'Группы публикаций'


class Post(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    text = models.TextField(
        verbose_name='Описание',
        help_text='Введите текст публикации',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='posts'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Группа публикации',
        help_text='Выберите группу, соотвестсвующую публикации'
    )

    class Meta:
        verbose_name = 'публикации'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.text


class Comment(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария',
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост комментария',
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Текст комментария'
    )
    created = models.DateTimeField(
        verbose_name='дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['user', 'following'],
            name='unique_follow'
        )]
        verbose_name_plural = 'Подписки',
        verbose_name = 'Подписку',
