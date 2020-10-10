MODEL/DB FIELDS

### LISTING
id: INT
realtor: INT (FOREIGN KEY [realtor]) <every listing will need a realtor assigned to it>
title: STR
address: STR
city: STR
state: STR
zipcode: STR
description: TEXT <a text field is different because it is a little longer>
price: INT <not a float because we're not going to do decimal points on prices of homes>
bedrooms: INT
bathrooms: INT
garage: INT [0] <this means 0 is the default>
sqft: INT
lot_size: FLOAT <for example 1.2 acres>
is_published: BOOL [true] <this is so that the client can publish & unpublish listings>
list_date: DATE
photo_main: STR <we're not actually storing images in a database; wer're storing the location of the image. That way we can fetch the location and can simply put it into an img src so that it displays on the page>
photo_1: STR
photo_2: STR
photo_3: STR
photo_4: STR
photo_5: STR
photo_6: STR


### REALTOR
id: INT <all tables will have an id>
name: STR
photo: STR
description: TEXT
email: STR
phone: STR <phone numbers should always be strings>
is_mvp: BOOL [0] <this is the seller of the month>
hire_date: DATE


### CONTACT
id: INT
user_id: INT
listing: INT
listing_id: INT
name: STR
email: STR
phone: STR
message: TEXT
contact_date: DATE