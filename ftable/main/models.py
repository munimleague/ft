from django.db import models

class seva(models.Model):
    grade_sa = models.CharField('Grade', max_length=20)
    points_sa = models.CharField('Points', max_length=100)
    matp_sa = models.IntegerField('Matches Played')
    goldd_sa = models.IntegerField('Goals Difference')
    place_sa = models.IntegerField('Place')

    def _str_(self):
        return self.title
    class Meta:
        verbose_name = 'Seven A'
        verbose_name_plural = 'Seven A'

class sevb(models.Model):
    grade_sb = models.CharField('Grade', max_length=20)
    points_sb = models.CharField('Points', max_length=100)
    matp_sb = models.IntegerField('Matches Played')
    goldd_sb = models.IntegerField('Goals Difference')
    place_sb = models.IntegerField('Place')

    def _str_(self):
        return self.title
    class Meta:
        verbose_name = 'Seven B'
        verbose_name_plural = 'Seven B'

class nina(models.Model):
    grade_na = models.CharField('Grade', max_length=20)
    points_na = models.CharField('Points', max_length=100)
    matp_na = models.IntegerField('Matches Played')
    goldd_na = models.IntegerField('Goals Difference')
    place_na = models.IntegerField('Place')

    def _str_(self):
        return self.title
    class Meta:
        verbose_name = 'Nine A'
        verbose_name_plural = 'Nine A'

class ninb(models.Model):
    grade_nb = models.CharField('Grade', max_length=20)
    points_nb = models.CharField('Points', max_length=100)
    matp_nb = models.IntegerField('Matches Played')
    goldd_nb = models.IntegerField('Goals Difference')
    place_nb = models.IntegerField('Place')

    def _str_(self):
        return self.title
    class Meta:
        verbose_name = 'Nine B'
        verbose_name_plural = 'Nine B'

class tena(models.Model):
    grade_ta = models.CharField('Grade', max_length=20)
    points_ta = models.CharField('Points', max_length=100)
    matp_ta = models.IntegerField('Matches Played')
    goldd_ta = models.IntegerField('Goals Difference')
    place_ta = models.IntegerField('Place')

    def _str_(self):
        return self.title
    class Meta:
        verbose_name = 'Ten A'
        verbose_name_plural = 'Ten A'

class tenb(models.Model):
    grade_tb = models.CharField('Grade', max_length=20)
    points_tb = models.CharField('Points', max_length=100)
    matp_tb = models.IntegerField('Matches Played')
    goldd_tb = models.IntegerField('Goals Difference')
    place_tb = models.IntegerField('Place')

    def _str_(self):
        return self.title
    class Meta:
        verbose_name = 'Ten B'
        verbose_name_plural = 'Ten B'

class eleva(models.Model):
    grade_ea = models.CharField('Grade', max_length=20)
    points_ea = models.CharField('Points', max_length=100)
    matp_ea = models.IntegerField('Matches Played')
    goldd_ea = models.IntegerField('Goals Difference')
    place_ea = models.IntegerField('Place')

    def _str_(self):
        return self.title
    class Meta:
        verbose_name = 'Eleven A'
        verbose_name_plural = 'Eleven A'

class elevb(models.Model):
    grade_eb = models.CharField('Grade', max_length=20)
    points_eb = models.CharField('Points', max_length=100)
    matp_eb = models.IntegerField('Matches Played')
    goldd_eb = models.IntegerField('Goals Difference')
    place_eb = models.IntegerField('Place')

    def _str_(self):
        return self.title
    class Meta:
        verbose_name = 'Eleven B'
        verbose_name_plural = 'Eleven B'


class tatal(models.Model):
    place = models.IntegerField('Place')
    grade = models.CharField('Grade', max_length=10)
    points = models.IntegerField('Points')
    mtpl = models.IntegerField('Matches Played')
    gldf = models.IntegerField('Goals Difference')

    def __str__(self):
        return f'Grade: {self.grade}'
    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Table'

class lik(models.Model):
    link = models.CharField('Link', max_length=200)

    def __str__(self):
        return f'Link: {self.link}'

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'