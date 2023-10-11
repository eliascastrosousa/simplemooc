from django.db import models
from django.contrib.auth.models import User
from simplemooc import settings

class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )   

class Course(models.Model):
    name = models.CharField('Nome', max_length=255)
    slug = models.SlugField('Atalho')
    descripton = models.TextField('Descrição', blank=True, max_length=255)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager()

    def __str__(self) -> str:
        return self.name
    
    """
    def get_absolute_url(self):
        return ('courses:details', (), {'slug':self.slug})
    """
    
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        # ordering = ['name']

class StatusChoice(models.IntegerChoices):
    PENDENTE = 0, 'Pendente'
    APROVADO = 1, 'Aprovado'
    CANCELADO = 2, 'Cancelado'

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             verbose_name='Usuário', 
                             related_name='enrollments',
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Course, 
                               verbose_name='Curso', 
                               related_name='enrollments',
                               on_delete=models.CASCADE)
    status = models.PositiveIntegerField('Situação',
                                         choices=StatusChoice.choices,
                                         default=StatusChoice.PENDENTE)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'course'),)
    
    def __str__(self):
        return f'{self.user.username} - {self.course.name}'