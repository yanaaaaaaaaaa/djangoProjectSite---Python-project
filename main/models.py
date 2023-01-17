from django.db import models


# Create your models here.
class HomePage(models.Model):
    image = models.ImageField('Изображение', upload_to='home')
    text_before_image = models.TextField('HTML-код до изображения')
    text_after_image = models.TextField('HTML-код после изображения')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Экземляры главных страниц'


class DemandPage(models.Model):
    salary_plot = models.ImageField('График зарплат', upload_to='demand')
    count_plot = models.ImageField('График количества вакансий', upload_to='demand')
    table_html = models.TextField('HTML-код таблицы')

    class Meta:
        verbose_name = 'Страница востребованности'
        verbose_name_plural = 'Экземляры страниц востребованности'


class GeographyPage(models.Model):
    profession_name = models.CharField('Название вакансии', max_length=128)
    profession_plot = models.ImageField('График по указанной вакансии', upload_to='geography')
    profession_salary_html = models.TextField('HTML-код таблицы зарплат по указанной вакансиям')
    profession_share_html = models.TextField('HTML-код таблицы долей по указанной вакансиям')
    it_plot = models.ImageField('График по IT-вакансиям', upload_to='geography')
    it_salary_html = models.TextField('HTML-код таблицы зарплат по IT-вакансиям')
    it_share_html = models.TextField('HTML-код таблицы долей по IT-вакансиям')

    class Meta:
        verbose_name = 'Страница географии'
        verbose_name_plural = 'Экземляры страниц географии'


class SkillYear(models.Model):
    year = models.IntegerField('Год')
    plot = models.ImageField('График за год', upload_to='skills')
    table_html = models.TextField('HTML-код таблицы')

    class Meta:
        verbose_name = 'Статистика навыков за год'
        verbose_name_plural = 'Статистики навыков за год'

    def __str__(self):
        return f"Статистика навыков за {self.year} год"


class VacancyPage(models.Model):
    search = models.CharField('Поисковый запрос', max_length=256)
    count = models.IntegerField('Количество вакансий')

    class Meta:
        verbose_name = 'Страница вакансий'
        verbose_name_plural = 'Экземляры страниц вакансий'
