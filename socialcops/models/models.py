from socialcops import db

class Data(db.Document):
  name = db.StringField()
  uploaded_on = db.DateTimeField()
  data = db.ListField()

class Teams(db.Document):
  team_name = db.StringField()
  phone_num = db.StringField()
  email = db.EmailField()



# Supported fields
# StringField
# BinaryField
# URLField
# EmailField
# IntField
# FloatField
# DecimalField
# BooleanField
# DateTimeField
# ListField (using wtforms.fields.FieldList )
# SortedListField (duplicate ListField)
# EmbeddedDocumentField (using wtforms.fields.FormField and generating inline Form)
# ReferenceField (using wtforms.fields.SelectFieldBase with options loaded from QuerySet or Document)
# DictField