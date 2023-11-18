import uuid

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from features.core.utils import NullEmailField

# Create your models here.
class AbsSlugField(models.Model):
    slug = models.UUIDField(verbose_name=_('Slug'), default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class AbsTimestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'), editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated Date'), editable=False)

    class Meta:
        abstract = True


class User(AbstractUser, AbsSlugField, AbsTimestamp):
    email = NullEmailField(null=True, blank=True, unique=True)
    ci = models.CharField(max_length=11, validators=[
        RegexValidator(regex=r'^\d{11}$', message='El CI de Cuba debe tener 11 dígitos numéricos')], null=True)
    REQUIRED_FIELDS = ['email']

    EMAIL_FIELD = None

    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created']


class Groupp(Group):
    class Meta:
        db_table = 'tbl_group'
        proxy = True
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        permissions = (
            ("list_group", "Can list groups"),
        )


class Permiso(Permission):
    class Meta:
        proxy = True
        # Aqui se van a crear todos los permisos de los modelos que estan en otra db
        # Ya que no se puede hacer migraciones en la db de enrrolamiento porque es de solo lectura
        # Para cada modelo se deben crear 4 permios (view, add, change, delete)
        # Estos se crean con esas 4 acciones mas el string de la clase '_model' ejemplo 'view_permiso'
        # Lugo de esto hay que hacer las migraciones para que se creen estos permisos
        permissions = (
            ("list_permiso", "Puede listar permisos"),
            ("view_nestado", "Puede listar estados en la db de enrrolamiento"),
            ("add_nestado", "Puede adicoinar estados en la db de enrrolamiento"),
            ("change_nestado", "Puede actualizar estados en la db de enrrolamiento"),
            ("delete_nestado", "Puede eliminar estados en la db de enrrolamiento"),

            ("view_dciudadano", "Puede listar ciudadanos en la db de enrrolamiento"),
            ("add_dciudadano", "Puede adicoinar ciudadanos en la db de enrrolamiento"),
            ("change_dciudadano", "Puede actualizar ciudadanos en la db de enrrolamiento"),
            ("delete_dciudadano", "Puede eliminar ciudadanos en la db de enrrolamiento"),

            ("view_dciudadanobash", "Puede listar ciudadanos bash en la db de enrrolamiento"),
            ("add_dciudadanobash", "Puede adicoinar ciudadanos bash en la db de enrrolamiento"),
            ("change_dciudadanobash", "Puede actualizar ciudadanos bash en la db de enrrolamiento"),
            ("delete_dciudadanobash", "Puede eliminar ciudadanos bash en la db de enrrolamiento"),

            ("view_dimagenfacial", "Puede listar imagen facial en la db de enrrolamiento"),
            ("add_dimagenfacial", "Puede adicoinar imagen facial en la db de enrrolamiento"),
            ("change_dimagenfacial", "Puede actualizar imagen facial en la db de enrrolamiento"),
            ("delete_dimagenfacial", "Puede eliminar imagen facial en la db de enrrolamiento"),
        )


class Nestado(models.Model):
    # Atributos
    idestado = models.IntegerField(primary_key=True)
    descripcion = models.TextField(default='')

    class Meta:
        verbose_name = _('Nestado')
        db_table = 'nestado'
        verbose_name_plural = _('Nestados')
        app_label = 'enrrolamiento'


class Dciudadanobash(models.Model):
    # Atributos
    idexpediente = models.TextField(default='', max_length=20)
    identificadorarea = models.TextField(default='', max_length=150)
    identificadorroluni = models.TextField(default='', max_length=100)
    carnetidentidad = models.TextField(default='', max_length=35)
    fechanacimiento = models.DateField()
    primernombre = models.TextField(default='', max_length=100)
    segundonombre = models.TextField(default='', max_length=100)
    primerapellido = models.TextField(default='', max_length=100)
    segundoapellido = models.TextField(default='', max_length=100)
    solapin = models.TextField(default='', max_length=10)
    provincia = models.TextField(default='', max_length=150)
    municipio = models.TextField(default='', max_length=150)
    sexo = models.TextField(default='', max_length=30)
    residente = models.BooleanField(default=False)
    idestado = models.ForeignKey(Nestado, on_delete=models.CASCADE, db_column='idestado')  # Field name made lowercase.
    fecha_registro_modificacion = models.DateTimeField(auto_now_add=True)
    idpersona = models.TextField(primary_key=True, max_length=32)

    class Meta:
        verbose_name = _('Dciudadanobash')
        db_table = 'dciudadanobash'
        verbose_name_plural = _('Dciudadanobashs')
        app_label = 'enrrolamiento'

class Dciudadano(models.Model):
    # Atributos
    idciudadano = models.IntegerField(primary_key=True)
    area = models.TextField(default='')
    roluniversitario = models.TextField(default='')
    primernombre = models.TextField(default='', max_length=100)
    segundonombre = models.TextField(default='', max_length=100)
    primerapellido = models.TextField(default='', max_length=100)
    segundoapellido = models.TextField(default='', max_length=100)
    solapin = models.TextField(default='', max_length=10)
    carnetidentidad = models.TextField(default='', max_length=35)
    provincia = models.TextField(default='', max_length=150)
    municipio = models.TextField(default='', max_length=150)
    sexo = models.TextField(default='', max_length=30)
    residente = models.BooleanField(default=False)
    fechanacimiento = models.DateField()
    idexpediente = models.TextField(default='', max_length=20)
    fecha = models.DateField(auto_now_add=True)
    idpersona = models.ForeignKey(Dciudadanobash, on_delete=models.CASCADE, db_column='idpersona', max_length=32)

    class Meta:
        verbose_name = _('Dciudadano')
        db_table = 'dciudadano'
        verbose_name_plural = _('Dciudadanos')
        app_label = 'enrrolamiento'

class Dimagenfacial(models.Model):
    # Atributos
    idciudadano = models.ForeignKey(Dciudadano, on_delete=models.CASCADE, db_column='idciudadano', primary_key=True)
    foto = models.BinaryField()
    valida = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = _('Dimagenfacial')
        db_table = 'dimagenfacial'
        verbose_name_plural = _('Dimagenfacials')
        app_label = 'enrrolamiento'
