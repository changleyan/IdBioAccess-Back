import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


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
    position = models.IntegerField(_('Position'), default=1)
    union_section = models.ForeignKey('UnionSection', models.SET_NULL, blank=True, null=True)
    email = models.EmailField(_('Email'), blank=True, null=True)

    EMAIL_FIELD = None

    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created']


class Area(AbsSlugField, AbsTimestamp):
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        db_table = 'tbl_area'
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        ordering = ['-created']


class Donation(AbsSlugField, AbsTimestamp):
    name = models.CharField(_('Name'), max_length=255)
    date = models.DateTimeField(_('Date'))
    area = models.ForeignKey(Area, models.CASCADE)

    class Meta:
        db_table = 'tbl_donation'
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'
        ordering = ['-created']


class InitialState(AbsSlugField, AbsTimestamp):
    total_number_workers = models.IntegerField(_('Total number workers'))
    total_number_affiliates = models.IntegerField(_('Total number affiliates'))
    gross_potential = models.FloatField(_('Gross potential'))
    net_potential = models.FloatField(_('Net potential'))
    accumulated_ten_percent = models.FloatField(_('Accumulated ten percent'))
    fully_committed = models.IntegerField(_('Fully committed'))
    amount = models.FloatField(_('Fully committed'))
    year = models.IntegerField(_('Fully committed'))
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        db_table = 'tbl_initial_state'
        verbose_name = 'Initial State'
        verbose_name_plural = 'Initials State'
        ordering = ['-created']


class UnionSection(AbsSlugField, AbsTimestamp):
    name = models.CharField(_('Name'), max_length=255)
    area = models.ForeignKey(Area, models.CASCADE)
    initial_state = models.ForeignKey(InitialState, models.CASCADE)

    class Meta:
        db_table = 'tbl_union_section'
        verbose_name = 'UnionSection'
        verbose_name_plural = 'UnionSections'
        ordering = ['-created']


class Affiliate(AbsSlugField, AbsTimestamp):
    name = models.CharField(_('Name'), max_length=255)
    high_date = models.DateField(_('High Date'))
    low_date = models.DateField(_('Low Date'), blank=True, null=True)
    initial_state = models.ForeignKey(InitialState, models.CASCADE)
    salary = models.FloatField(_('Salary'))
    monthly_quota = models.FloatField(_('Monthly quota'))
    annual_quota = models.FloatField(_('Annual quota'))
    contribution_commitment = models.FloatField(_('Contribution commitment'))
    month_contribution = models.CharField(_('Month contribution'), max_length=255)

    class Meta:
        db_table = 'tbl_affiliate'
        verbose_name = 'Affiliate'
        verbose_name_plural = 'Affiliates'
        ordering = ['-created']


class Act(AbsSlugField, AbsTimestamp):
    type = models.CharField(_('Type'), max_length=45)
    date = models.DateField(_('Date'))
    union_section = models.ForeignKey(UnionSection, null=True, blank=True, on_delete=models.SET_NULL)
    attendance_percentage = models.FloatField(_('Attendance percentage'))
    place = models.CharField(_('Percentage'), max_length=255)
    start_time = models.TimeField(_('Start time'))
    end_time = models.TimeField(_('End time'))
    direct = models.CharField(_('Direct'), max_length=255)
    guest = models.CharField(_('Guest'), max_length=255)
    order_gives = models.TextField(_('Order gives'))
    body = models.TextField(_('Body'))

    class Meta:
        db_table = 'tbl_act'
        verbose_name = 'Act'
        verbose_name_plural = 'Acts'
        ordering = ['-created']


class Agreement(AbsSlugField, AbsTimestamp):
    act = models.ForeignKey(Act, models.CASCADE)
    agreement = models.TextField(_('Agreement'))
    responsible = models.CharField(_('Responsible'), max_length=255)
    compliance_date = models.DateField(_('Compliance date'), max_length=255)
    state = models.CharField(_('State'), max_length=45)

    class Meta:
        db_table = 'tbl_agreement'
        verbose_name = 'Agreement'
        verbose_name_plural = 'Agreements'
        ordering = ['-created']


class Approach(AbsSlugField, AbsTimestamp):
    act = models.ForeignKey(Act, models.CASCADE)
    affiliate = models.ForeignKey(Affiliate, models.CASCADE)
    approach = models.TextField(_('Approach'))
    type = models.CharField(_('Type'), max_length=255)

    class Meta:
        db_table = 'tbl_approach'
        verbose_name = 'Approach'
        verbose_name_plural = 'Approaches'
        ordering = ['-created']


class DepositFinance(AbsSlugField, AbsTimestamp):
    union_section = models.ForeignKey(UnionSection, models.CASCADE)
    date = models.DateField(_('Date'))
    total_number_workers = models.IntegerField(_('Total number workers'))
    total_number_affiliates = models.IntegerField(_('Total number affiliates'))
    al_da = models.IntegerField(_('Al da'))
    unlisted = models.IntegerField(_('Unlisted'))
    with_arrears = models.IntegerField(_('With arrears'))
    liquidated_year = models.IntegerField(_('Liquidated year'))
    high = models.FloatField(_('High'))
    low = models.FloatField(_('Low'))
    to_quote = models.FloatField(_('To quote'))
    quoted = models.FloatField(_('Quoted'))
    earring = models.FloatField(_('Earring'))
    ten_percent = models.FloatField(_('Ten percent'))
    net_quoted = models.FloatField(_('Net quoted'))
    ten_percent_accumulated = models.FloatField(_('Ten percent accumulated'))
    reduction = models.FloatField(_('Reduction'))
    total_balance = models.FloatField(_('Total balance'))

    class Meta:
        db_table = 'tbl_deposit_finance'
        verbose_name = 'Deposit Finance'
        verbose_name_plural = 'Deposit Finances'
        ordering = ['-created']


class ContributionDeposit(AbsSlugField, AbsTimestamp):
    union_section = models.ForeignKey(UnionSection, models.CASCADE)
    total_number_workers = models.IntegerField(_('Total number workers'))
    total_number_committed = models.IntegerField(_('Total number committed'))
    to_deposit = models.FloatField(_('To deposit'))
    deposited = models.FloatField(_('Deposited'))
    high = models.FloatField(_('High'))
    low = models.FloatField(_('Low'))
    earring = models.FloatField(_('Earring'))

    class Meta:
        db_table = 'tbl_contribution_deposit'
        verbose_name = 'Contribution Deposit'
        verbose_name_plural = 'Contribution Deposits'
        ordering = ['-created']


class PointAct(AbsSlugField, AbsTimestamp):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'))
    act = models.ForeignKey(Act, models.CASCADE)

    class Meta:
        db_table = 'tbl_point_act'
        verbose_name = 'Point Act'
        verbose_name_plural = 'Points Act'
        ordering = ['-created']
