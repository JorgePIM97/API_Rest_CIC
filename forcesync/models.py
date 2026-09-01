# Create your models here.
from django.db import models

class ForceUser(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    billable = models.BooleanField(db_column='Billable')  # Field name made lowercase.
    branches_id = models.IntegerField(db_column='Branches_Id', blank=True, null=True)  # Field name made lowercase.
    branches_description = models.TextField(db_column='Branches_Description', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    computesfm = models.BooleanField(db_column='ComputeSfm')  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    datedeleted = models.DateTimeField(db_column='DateDeleted', blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.
    dblanguage = models.TextField(db_column='DbLanguage', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted')  # Field name made lowercase.
    email = models.TextField(db_column='Email', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    extid = models.TextField(db_column='ExtId', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idprefix = models.TextField(db_column='IdPrefix', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastpasswordchangedate = models.DateTimeField(db_column='LastPasswordChangeDate', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    locale = models.TextField(db_column='Locale', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    managerid_id = models.IntegerField(db_column='ManagerId_Id', blank=True, null=True)  # Field name made lowercase.
    managerid_description = models.TextField(db_column='ManagerId_Description', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nic = models.TextField(db_column='Nic', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phoneextension = models.TextField(db_column='PhoneExtension', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rateid_id = models.IntegerField(db_column='RateId_Id', blank=True, null=True)  # Field name made lowercase.
    rateid_description = models.TextField(db_column='RateId_Description', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepidcreated = models.IntegerField(db_column='SalesRepIdCreated', blank=True, null=True)  # Field name made lowercase.
    salesrepiddeleted = models.IntegerField(db_column='SalesRepIdDeleted', blank=True, null=True)  # Field name made lowercase.
    salesrepidupdated = models.IntegerField(db_column='SalesRepIdUpdated', blank=True, null=True)  # Field name made lowercase.
    uilanguage = models.TextField(db_column='UiLanguage', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usertypeid_id = models.IntegerField(db_column='UserTypeId_Id', blank=True, null=True)  # Field name made lowercase.
    usertypeid_description = models.TextField(db_column='UserTypeId_Description', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.name} {self.lastname}"

    class Meta:
        managed = False
        db_table = 'Users'


class Activity(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accountid_id = models.IntegerField(db_column='AccountId_Id', blank=True, null=True)  # Field name made lowercase.
    accountid_value = models.TextField(db_column='AccountId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    checkin = models.BooleanField(db_column='Checkin')  # Field name made lowercase.
    checkintypeid = models.IntegerField(db_column='CheckinTypeId', blank=True, null=True)  # Field name made lowercase.
    checkoutdate = models.DateTimeField(db_column='CheckoutDate', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contactid = models.IntegerField(db_column='ContactId', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    datedeleted = models.DateTimeField(db_column='DateDeleted', blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted')  # Field name made lowercase.
    extid = models.TextField(db_column='ExtId', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    geocoded = models.BooleanField(db_column='Geocoded')  # Field name made lowercase.
    geocodingaccuracy = models.IntegerField(db_column='GeocodingAccuracy', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    opportunityid_id = models.IntegerField(db_column='OpportunityId_Id', blank=True, null=True)  # Field name made lowercase.
    opportunityid_value = models.TextField(db_column='OpportunityId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    permissionlevel = models.IntegerField(db_column='PermissionLevel')  # Field name made lowercase.
    readonly = models.BooleanField(db_column='ReadOnly')  # Field name made lowercase.
    salesrepid_id = models.IntegerField(db_column='SalesRepId_Id', blank=True, null=True)  # Field name made lowercase.
    # sales_rep = models.ForeignKey(
    # ForceUser,
    # on_delete=models.DO_NOTHING,
    # db_column='SalesRepId_Id',
    # related_name='activities',
    # blank=True,
    # null=True,
    # db_constraint=False,
    # )
    salesrepid_value = models.TextField(db_column='SalesRepId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepidcreated = models.IntegerField(db_column='SalesRepIdCreated', blank=True, null=True)  # Field name made lowercase.
    salesrepiddeleted = models.IntegerField(db_column='SalesRepIdDeleted', blank=True, null=True)  # Field name made lowercase.
    salesrepidupdated = models.IntegerField(db_column='SalesRepIdUpdated', blank=True, null=True)  # Field name made lowercase.
    typeid_id = models.IntegerField(db_column='TypeId_Id', blank=True, null=True)  # Field name made lowercase.
    typeid_value = models.TextField(db_column='TypeId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activities'