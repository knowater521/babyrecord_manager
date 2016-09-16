from django.db import models

# Create your models here.

class DrinkMilk(models.Model):
    DRINK_TYPE_CHOICES = (
        ('TOOL', '奶瓶'),
        ('MOM', '母乳'),
    )

    drink_at    = models.DateTimeField(verbose_name='喝奶时间', null=False, db_index=True)
    amount      = models.IntegerField(verbose_name='数量(ml)', null=False)
    drink_type  = models.CharField(max_length=10, verbose_name='类型', choices=DRINK_TYPE_CHOICES)
    record_at   = models.DateTimeField(verbose_name='纪录时间', auto_now_add=True)

    class Meta:
        verbose_name = '喂奶'
        verbose_name_plural = '喂奶'

class Sleep(models.Model):
    sleep_start = models.DateTimeField(verbose_name='睡眠开始', db_index=True)
    sleep_end   = models.DateTimeField(verbose_name='睡眠结束')
    record_at   = models.DateTimeField(verbose_name='纪录时间', auto_now_add=True)

    class Meta:
        verbose_name = '睡觉'
        verbose_name_plural = '睡觉'

class Pee(models.Model):

    PEE_TYPE_CHOICES = (
        (1, '大便'),
        (2, '小便')
    )

    record_date = models.DateField(verbose_name='日期', db_index=True)
    pee_type    = models.IntegerField(verbose_name='类型', choices= PEE_TYPE_CHOICES)
    amount      = models.IntegerField(verbose_name='次数', null=False)
    record_at   = models.DateTimeField(verbose_name='纪录时间', auto_now_add=True)

    class Meta:
        verbose_name = '大小便'
        verbose_name_plural = '大小便'

class BreastBump(models.Model):
    bump_at     = models.DateTimeField(verbose_name='吸奶时间', null=False, db_index=True)
    amount = models.IntegerField(verbose_name='数量(ml)', null=False)
    record_at   = models.DateTimeField(verbose_name='纪录时间', auto_now_add=True)

    class Meta:
        verbose_name = '吸奶器'
        verbose_name_plural = '吸奶器'