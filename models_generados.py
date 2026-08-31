# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
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

    class Meta:
        managed = False
        db_table = 'Users'


class Accounts(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    vatnumber = models.TextField(db_column='VatNumber', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    website = models.TextField(db_column='Website', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone2 = models.TextField(db_column='Phone2', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone3 = models.TextField(db_column='Phone3', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(db_column='Fax', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.
    datedeleted = models.DateTimeField(db_column='DateDeleted', blank=True, null=True)  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted')  # Field name made lowercase.
    extid = models.TextField(db_column='ExtId', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    geocoded = models.BooleanField(db_column='Geocoded')  # Field name made lowercase.
    geocodingaccuracy = models.IntegerField(db_column='GeocodingAccuracy', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    permissionlevel = models.IntegerField(db_column='PermissionLevel', blank=True, null=True)  # Field name made lowercase.
    public = models.BooleanField(db_column='Public')  # Field name made lowercase.
    readonly = models.BooleanField(db_column='ReadOnly')  # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    postcode = models.TextField(db_column='Postcode', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    branchid_id = models.IntegerField(db_column='BranchId_Id', blank=True, null=True)  # Field name made lowercase.
    branchid_value = models.TextField(db_column='BranchId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countryid_id = models.IntegerField(db_column='CountryId_Id', blank=True, null=True)  # Field name made lowercase.
    countryid_value = models.TextField(db_column='CountryId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    typeid_id = models.IntegerField(db_column='TypeId_Id', blank=True, null=True)  # Field name made lowercase.
    typeid_value = models.TextField(db_column='TypeId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segmentid_id = models.IntegerField(db_column='SegmentId_Id', blank=True, null=True)  # Field name made lowercase.
    segmentid_value = models.TextField(db_column='SegmentId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    statusid_id = models.IntegerField(db_column='StatusId_Id', blank=True, null=True)  # Field name made lowercase.
    statusid_value = models.TextField(db_column='StatusId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepid1_id = models.IntegerField(db_column='SalesRepId1_Id', blank=True, null=True)  # Field name made lowercase.
    salesrepid1_value = models.TextField(db_column='SalesRepId1_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepid2_id = models.IntegerField(db_column='SalesRepId2_Id', blank=True, null=True)  # Field name made lowercase.
    salesrepid2_value = models.TextField(db_column='SalesRepId2_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepid3_id = models.IntegerField(db_column='SalesRepId3_Id', blank=True, null=True)  # Field name made lowercase.
    salesrepid3_value = models.TextField(db_column='SalesRepId3_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepid4_id = models.IntegerField(db_column='SalesRepId4_Id', blank=True, null=True)  # Field name made lowercase.
    salesrepid4_value = models.TextField(db_column='SalesRepId4_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepid5_id = models.IntegerField(db_column='SalesRepId5_Id', blank=True, null=True)  # Field name made lowercase.
    salesrepid5_value = models.TextField(db_column='SalesRepId5_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepidcreated = models.IntegerField(db_column='SalesRepIdCreated', blank=True, null=True)  # Field name made lowercase.
    salesrepidupdated = models.IntegerField(db_column='SalesRepIdUpdated', blank=True, null=True)  # Field name made lowercase.
    salesrepiddeleted = models.IntegerField(db_column='SalesRepIdDeleted', blank=True, null=True)  # Field name made lowercase.
    rateid = models.IntegerField(db_column='RateId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Accounts'


class Activities(models.Model):
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
    salesrepid_value = models.TextField(db_column='SalesRepId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepidcreated = models.IntegerField(db_column='SalesRepIdCreated', blank=True, null=True)  # Field name made lowercase.
    salesrepiddeleted = models.IntegerField(db_column='SalesRepIdDeleted', blank=True, null=True)  # Field name made lowercase.
    salesrepidupdated = models.IntegerField(db_column='SalesRepIdUpdated', blank=True, null=True)  # Field name made lowercase.
    typeid_id = models.IntegerField(db_column='TypeId_Id', blank=True, null=True)  # Field name made lowercase.
    typeid_value = models.TextField(db_column='TypeId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activities'


class Calendars(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accountid = models.IntegerField(db_column='AccountId', blank=True, null=True)  # Field name made lowercase.
    allday = models.BooleanField(db_column='AllDay')  # Field name made lowercase.
    branchid_id = models.IntegerField(db_column='BranchId_Id', blank=True, null=True)  # Field name made lowercase.
    branchid_value = models.TextField(db_column='BranchId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    completed = models.BooleanField(db_column='Completed')  # Field name made lowercase.
    contactid = models.IntegerField(db_column='ContactId', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    datedeleted = models.DateTimeField(db_column='DateDeleted', blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    endhour = models.TextField(db_column='EndHour', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    extid = models.TextField(db_column='ExtId', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    opportunityid = models.IntegerField(db_column='OpportunityId', blank=True, null=True)  # Field name made lowercase.
    permissionlevel = models.IntegerField(db_column='PermissionLevel')  # Field name made lowercase.
    readonly = models.BooleanField(db_column='ReadOnly')  # Field name made lowercase.
    reminder = models.IntegerField(db_column='Reminder')  # Field name made lowercase.
    salesrepid_id = models.IntegerField(db_column='SalesRepId_Id', blank=True, null=True)  # Field name made lowercase.
    salesrepid_value = models.TextField(db_column='SalesRepId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepidcreated = models.IntegerField(db_column='SalesRepIdCreated', blank=True, null=True)  # Field name made lowercase.
    salesrepiddeleted = models.IntegerField(db_column='SalesRepIdDeleted', blank=True, null=True)  # Field name made lowercase.
    salesrepidupdated = models.IntegerField(db_column='SalesRepIdUpdated', blank=True, null=True)  # Field name made lowercase.
    sendnotification = models.BooleanField(db_column='SendNotification')  # Field name made lowercase.
    startdate = models.TextField(db_column='StartDate', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    starthour = models.TextField(db_column='StartHour', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    subject = models.TextField(db_column='Subject', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    task = models.BooleanField(db_column='Task')  # Field name made lowercase.
    typeid_id = models.IntegerField(db_column='TypeId_Id', blank=True, null=True)  # Field name made lowercase.
    typeid_value = models.TextField(db_column='TypeId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calendars'


class Opportunities(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accountid1_id = models.IntegerField(db_column='AccountId1_Id', blank=True, null=True)  # Field name made lowercase.
    accountid1_value = models.TextField(db_column='AccountId1_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    accountid2_id = models.IntegerField(db_column='AccountId2_Id', blank=True, null=True)  # Field name made lowercase.
    accountid2_value = models.TextField(db_column='AccountId2_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    accountid3_id = models.IntegerField(db_column='AccountId3_Id', blank=True, null=True)  # Field name made lowercase.
    accountid3_value = models.TextField(db_column='AccountId3_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    branchid_id = models.IntegerField(db_column='BranchId_Id', blank=True, null=True)  # Field name made lowercase.
    branchid_value = models.TextField(db_column='BranchId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    closeddate = models.DateTimeField(db_column='ClosedDate', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countryid_id = models.IntegerField(db_column='CountryId_Id', blank=True, null=True)  # Field name made lowercase.
    countryid_value = models.TextField(db_column='CountryId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    currencyid_id = models.IntegerField(db_column='CurrencyId_Id', blank=True, null=True)  # Field name made lowercase.
    currencyid_value = models.TextField(db_column='CurrencyId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    datedeleted = models.DateTimeField(db_column='DateDeleted', blank=True, null=True)  # Field name made lowercase.
    dategeocoded = models.DateTimeField(db_column='DateGeocoded', blank=True, null=True)  # Field name made lowercase.
    dateupdated = models.DateTimeField(db_column='DateUpdated', blank=True, null=True)  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted')  # Field name made lowercase.
    extid = models.TextField(db_column='ExtId', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    geocoded = models.BooleanField(db_column='Geocoded')  # Field name made lowercase.
    geocodingaccuracy = models.IntegerField(db_column='GeocodingAccuracy', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    lostdate = models.DateTimeField(db_column='LostDate', blank=True, null=True)  # Field name made lowercase.
    permissionlevel = models.IntegerField(db_column='PermissionLevel')  # Field name made lowercase.
    postcode = models.TextField(db_column='Postcode', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    readonly = models.BooleanField(db_column='ReadOnly')  # Field name made lowercase.
    reference = models.TextField(db_column='Reference', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesforecastdate = models.DateTimeField(db_column='SalesForecastDate', blank=True, null=True)  # Field name made lowercase.
    salesprobability = models.IntegerField(db_column='SalesProbability', blank=True, null=True)  # Field name made lowercase.
    salesrepid_id = models.IntegerField(db_column='SalesRepId_Id', blank=True, null=True)  # Field name made lowercase.
    salesrepid_value = models.TextField(db_column='SalesRepId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salesrepidcreated = models.IntegerField(db_column='SalesRepIdCreated', blank=True, null=True)  # Field name made lowercase.
    salesrepiddeleted = models.IntegerField(db_column='SalesRepIdDeleted', blank=True, null=True)  # Field name made lowercase.
    salesrepidupdated = models.IntegerField(db_column='SalesRepIdUpdated', blank=True, null=True)  # Field name made lowercase.
    statusid_id = models.IntegerField(db_column='StatusId_Id', blank=True, null=True)  # Field name made lowercase.
    statusid_value = models.TextField(db_column='StatusId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    typeid_id = models.IntegerField(db_column='TypeId_Id', blank=True, null=True)  # Field name made lowercase.
    typeid_value = models.TextField(db_column='TypeId_Value', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wondate = models.DateTimeField(db_column='WonDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Opportunities'
