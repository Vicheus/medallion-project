# Supported DataSphere fields
This menu serves as a convenient guide for swiftly navigating through the document detailing a comprehensive list of supported fields in DataSphere, along with their types. Each section encompasses various data aspects, providing a thorough overview of the informational fields.

### Menu Section:
- **[Main Info](#main-info)**: This section gathers primary data, including general information about subject.
- **[Addresses](#addresses)**: This segment includes data about person addresses
- **[Socials](#socials)**: This segment includes data about social media presence, offering key insights into online activities.
- **[Educations](#educations)**: Here, information regarding educational background is presented, covering educational institutions and areas of study.
- **[Works](#works)**: This section compiles employment data, encompassing work history and current positions.
- **[⚠️ Force Divisions](#force-divisions)**: This part details affiliations with various organizational or military divisions.
- **[Divisions](#force-divisions)**: This part details affiliations with various organizational or military divisions.
- **[Documents](#documents)**: This section contains information about various types of documents, such as passports or driver’s licenses.
- **[Vehicles](#vehicles)**: Presented here is information about the car, bike, etc., including models and year of manufacture.
- **[Financials](#financials)**: This segment involves data on bank accounts and financial transactions.
- **[Ownerships](#ownerships)**: Here, you can find information about property ownership, enterprises, and other assets.
- **[Links](#links)**: This section aggregates links to various external sources and resources.
- **[Accounts](#accounts)**: This part presents data on accounts in various services and applications.
- **[Movements](#movements)**: This section reflects information on travel and movements.
- **[⚠️ Source](#source)**: This segment includes data on the source of information.
- **[Incidences](#incidences)**: This segment includes data on various incidents and accidents.
- **[Devices](#devices)**: This part details information about devices used by the subject.
- **[Ip's](#ips)**: This section contains data on IP addresses and their usage.
- **[Other](#other)**: This section includes additional information that doesn’t fit into the other categories.

This menu enhances accessibility to desired information, allowing users to quickly jump to the relevant section, ensuring efficient use of time.

---

### About table in this documentation
In the section, the data fields are described, providing insights into each column's name, its type in Python and Elasticsearch, whether it is indexed, if it's copied to a full-text search field, its format, and an overall description.
Here's a breakdown of the columns:

> - **Field name:** This is the name of the field in the data, representing attributes like "names", "sex", "birth_date", etc.
> - **Type / Python:** Defines the data type used in Python for this field.
> - **Type / ElasticSearch:** Specifies how the field is stored in Elasticsearch. Key Elasticsearch types include:
> - **Index:** Indicates whether the field is indexed in Elasticsearch. If true, this means the field is searchable.
> - **Copy to full:** This specifies whether the field is copied to a full-text search field for easier querying. If true, it’s used in full-text searches.
> - **Format:** Describes the format or values for the field. For example:
> - **Description:** This provides a brief explanation of the field:

The table effectively structures and organizes data for both Python and Elasticsearch, ensuring it is well-formed for search, analysis, and storage.

---

### Main info
```json
{
  "names": ["Sergio Ramos", "Сергио Рамос"],
  "sex": 0,
  "birth_date": "14.20.1996",
  "birth_place": "Ukraine, Kyiv",
  "address": ["address_1", "address_2"],
  "relationship": 0,
  "children": true,
  "phones": ["380000000000", "380000000000"],
  "emails": ["emails@mail.com", "someemail@gmail.com"],
  "relations": ["Алонсо Рамос 12.11.1955 Родитель", "Джулия Рамос 11.04.1960 Родитель"],
  "avatar": "https://localhost:80/avatars/1.jpg",
  "actuality": "12.12.2024"
}
```
| Field name   | Type / Python                     | Type / ElasticSearch                | Index           | Copy to full     | Format                                                                                                       | Description             |
|--------------|-----------------------------------|-------------------------------------|-----------------|------------------|--------------------------------------------------------------------------------------------------------------|-------------------------|
| names        | <kbd>list</kbd> of <kbd>str</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                              | name in other languages           |
| sex          | <kbd>int</kbd>                    | <kbd>byte</kbd>                     | <kbd>true</kbd> | <kbd>false</kbd> | 0 - female<br>1 - male                                                                                       | sex                                                         |
| birth_date   | <kbd>str</kbd>                    | <kbd>date</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd>  | dd.mm.YYYY                                                                                                   | date of birth                                   |
| birth_place  | <kbd>str</kbd>                    | <kbd>text</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                              | place of birth                    |
| address      | <kbd>list</kbd> of <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                              | work address                      |
| relationship | <kbd>int</kbd>                    | <kbd>byte</kbd>                     | <kbd>true</kbd> | <kbd>false</kbd> | 0 - Married<br>1 - Not Married<br>2 - Widow/Widower<br>3 - Divorced<br>4 - Engaged<br>5 - Actively Searching | Relationship status                                              |
| children     | <kbd>bool</kbd>                   | <kbd>boolean</kbd>                  | <kbd>true</kbd> | <kbd>false</kbd> |                                                                                                              | true if have a children            |
| phones       | <kbd>list</kbd> of <kbd>str</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                              | list of phones                    |
| emails       | <kbd>list</kbd> of <kbd>str</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                              | list of emails                    |
| relations    | <kbd>list</kbd> of <kbd>str</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                              | list of person relations          |
| person avatar| <kbd>str</kbd>                    | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> | <kbd>false</kbd>  |                                                                                                              | person avatar photo          |
| actuality    | <kbd>str</kbd>                    | <kbd>date</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd>  | dd.mm.YYYY                                                                                                   | actuality date of row (date of last order/login/registration etc.)

### Addresses
```json
{
  "type": 0,
  "raw": "Москва Москва, 115682, Ореховый бульвар, д. 63, стр. 1, кв. 54",
  "address": "индекс 115682 город Москва бульвар Ореховый дом 63 строение 1 квартира 54",
  "location": {
    "region_type" : "",
    "region_value": "",
    "settlement_region_type": "",
    "settlement_region_value": "",
    "settlement_type": "город",
    "settlement_value": "Москва",
    "street_type": "бульвар",
    "street_value" : "Ореховый",
    "zip": 115682,
    "house": 63,
    "floor": 0,
    "flat": 54,
    "building": 0,
    "office": 0,
    "coordinates": [55.6170147,37.75914376081505],
    "coord_detalization_lvl": 2
  },
  "comments": "Some comments"
}
```
| Field name              | Type / Python                        | Type / ElasticSearch | Index           | Copy to full     | Format                                                                                                       | Description                             |
|-------------------------|--------------------------------------|----------------------|-----------------|------------------|--------------------------------------------------------------------------------------------------------------|-------------------------|
| type                    | <kbd>int</kbd>                       | <kbd>byte</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  | 0-registration, 1-home, 2-delivery, 3-work                                                                  | type of address                         |
| raw                     | <kbd>str</kbd>                       | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                              | raw address string from dataset         |
| address                 | <kbd>str</kbd>                       | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                              | normalized and formatted address string |
| region_type             | <kbd>str</kbd>                       | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>false</kbd> | examples:область, край, муниципальный район, республика                                                      | type of address region                  |
| region_value            | <kbd>str</kbd>                       | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>false</kbd> | | address region                                              |
| settlement_region_type  | <kbd>str</kbd>                       | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>false</kbd> | examples: район, микрорайон                                                                                  | type of settlement region               |
| settlement_region_value | <kbd>str</kbd>                       | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>false</kbd> |                                                                                                              | address settlement region               |
| settlement_type         | <kbd>str</kbd>                       | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>false</kbd> | examples: город, городское поселение, деревня, поселок городского типа, посёлок, поселок             | type of settlement                      |
| settlement_value        | <kbd>str</kbd>                       | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>false</kbd> |                                                                                                              | address settlement                      |
| street_type             | <kbd>str</kbd>                       | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>false</kbd> | examples: проезд, переулок, шоссе, проспект, бульвар, улица                                                  | type of street                          |
| street_value            | <kbd>str</kbd>                       | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>false</kbd> |                                                                                                              | address street                          |
| zip                     | <kbd>int</kbd>                       | <kbd>int</kbd>       | <kbd>true</kbd> | <kbd>false</kbd> |                                                                                                              | address zip code                        |
| house                   | <kbd>int</kbd>                       | <kbd>int</kbd>       | <kbd>true</kbd> | <kbd>false</kbd> |                                                                                                              | house number                            |
| floor                   | <kbd>int</kbd>                       | <kbd>int</kbd>       | <kbd>true</kbd> | <kbd>false</kbd> |                                                                                                              | floor number                            |
| flat                    | <kbd>int</kbd>                       | <kbd>int</kbd        | <kbd>true</kbd> | <kbd>false</kbd> |                                                                                                              | number of flat                          |
| building                | <kbd>int</kbd>                       | <kbd>int</kbd>       | <kbd>true</kbd> | <kbd>false</kbd> |                                                                                                              | number of building                      |
| office                  | <kbd>int</kbd>                       | <kbd>int</kbd>       | <kbd>true</kbd> | <kbd>false</kbd> |                                                                                                              | number of office                        |
| coordinates             | <kbd>list</kbd> of <kbd>double</kbd> | <kbd>geo_point</kbd> | <kbd>true</kbd> | <kbd>true</kbd>  |  [longitude, latitude]                                                                                       | coordinates                             |
| coord_detalization_lvl  | <kbd>int</kbd>                       | <kbd>byte</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  | 0-settlement, 1-settlement_region, 2-street, 3-house                                                         | detalization level of coordinates |
| comments                | <kbd>string</kbd>                    | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                              | some comments                           |


### Socials
```json
{
  "socials": [
    {
      "title": "Telegram",
      "id": "546876878",
      "link": "link",
      "comment": "Some comments"
    }
  ]
}
```
| Field name | Type / Python  | Type / ElasticSearch | Index           | Copy to full    | Format                                          | Description         |
|------------|----------------|----------------------|-----------------|-----------------|-------------------------------------------------|---------------------|
| title      | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd> | <kbd>true</kbd> | Telegram<br>Instagram<br>Vk<br>Facebook<br>etc. | name of social link |
| id         | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd> | <kbd>true</kbd> |                                                 | user id             |
| link       | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd> | <kbd>true</kbd> |                                                 | username of profile |
| comment    | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd> |                                                 | some comments       |

### Educations
```json
{
  "educations": [
    {
      "title": "University",
      "level": 1,
      "country": "UKR",
      "date_start": "20.20.2020", 
      "date_end": "20.20.2021",
      "comment": "Some comments"
    }
  ]
}
```
| Field name | Type / Python  | Type / ElasticSearch | Index           | Copy to full     | Format                                                                                                                                                                                                                                                                                           | Description                           |
|------------|----------------|----------------------|-----------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| title      | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                                                                                                                                                                                                                  | name of school, university or college |
| level      | <kbd>int</kbd> | <kbd>byte</kbd>      | <kbd>true</kbd> | <kbd>false</kbd> | 1 - Primary School<br>2 - Lower Secondary School<br>3 - Upper Secondary School<br>4 - Vocational Training<br>5 - Associate Degree<br>6 - Bachelor's Degree<br>7 - Master's Degree<br>8 - Doctoral Degree (PhD)<br>9 - Postdoctoral Fellowship<br>10 - Professional Certification<br>11 - Diploma | diploma level                         |
| country    | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd> | <kbd>true</kbd>  | ALPHA-3                                                                                                                                                                                                                                                                                          | country code of education             |
| date_start | <kbd>str</kbd> | <kbd>date</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  | dd.mm.YYYY                                                                                                                                                                                                                                                                                       | date of start                         |
| date_end   | <kbd>str</kbd> | <kbd>date</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  | dd.mm.YYYY                                                                                                                                                                                                                                                                                       | date of end                           |
| comment    | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  |                                                                                                                                                                                                                                                                                                  | some comments                         |

### Works
```json
{
  "works": [
    {
      "post": "Barmen",
      "date_start": "14.20.2020",
      "date_end": "20.20.2020",
      "company": "KavaComp",
      "address": "Ukraine, Lviv",
      "comment": "Some comments"
    }
  ]
}
```
| Field name | Type / Python  | Type / ElasticSearch                | Index           | Copy to full    | Format     | Description               |
|------------|----------------|-------------------------------------|-----------------|-----------------|------------|---------------------------|
| post       | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd> |            | name of post              |
| date_start | <kbd>str</kbd> | <kbd>date</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd> | dd.mm.YYYY | works date start          |
| date_end   | <kbd>str</kbd> | <kbd>date</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd> | dd.mm.YYYY | works date end            |
| company    | <kbd>str</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> | <kbd>true</kbd> |            | company or structure name |
| address    | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd> |            | work address              |
| comment    | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd> |            | some comments             |

### ⚠️ Force Divisions 
```json
{
  "divisions": [
    {
      "division_id": 1,
      "title": "ZSU",
      "date_from": 2024,
      "date_to": 2025,
      "post": "Post",
      "rank": "Captain",
      "address": "Ukraine, Lviv",
      "comment": "Some comments"
    }
  ]
}
```
| Field name  | Type / Python  | Type / ElasticSearch                | Index           | Format | Description               |
|-------------|----------------|-------------------------------------|-----------------|--------|---------------------------|
| division_id | <kbd>int</kbd> | <kbd>integer</kbd>                  | <kbd>true</kbd> |        | if of force division      |
| title       | <kbd>str</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> |        | name of force division    |
| date_from   | <kbd>int</kbd> | <kbd>date</kbd>                     | <kbd>true</kbd> | YYYY   | data actuality            |
| date_to     | <kbd>int</kbd> | <kbd>date</kbd>                     | <kbd>true</kbd> | YYYY   | data actuality            |
| post        | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd> |        | post name                 |
| rank        | <kbd>str</kbd> | <kbd>keyword</kbd>                  | <kbd>true</kbd> |        | company or structure name |
| address     | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd> |        | work address              |
| comment     | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd> |        | some comments             |

### Documents
```json
{
  "documents": [
    {
      "type": 0,
      "country": "UKR",
      "serial": "456784354",
      "date_issue": "17.10.2022",
      "date_expire": "17.10.2027",
      "authority": "authority",
      "authority_code": "1598756",
      "comment": "Some comments"
    }
  ]
}
```
| Field name     | Type / Python  | Type / ElasticSearch                | Index            | Copy to full     | Format                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description             |
|----------------|----------------|-------------------------------------|------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| type           | <kbd>int</kbd> | <kbd>byte</kbd>                     | <kbd>true</kbd>  | <kbd>false</kbd> | 0 - Passport<br>1 - INN (Taxpayer Identification Number)<br>2 - SNILS (Individual Insurance Account Number)<br>3 - Driver's License<br>4 - International Passport<br>5 - Birth Certificate<br>6 - Military ID<br>7 - Refugee Certificate<br>8 - Resident card (вид на жительство)<br>9 - Temporary Passport (временный паспорт который дают при утере)<br>10 - Seaman's passport<br>11 - Diplomatic passport<br>12 - служебный паспорт(удостоверение)<br>13 - идентификационный номер гражданина(пример РБ)<br>14 - код причины постановки на учет\учетный номер плательщика(для РБ)<br><br>15 - основной государственный регистрационный номер(ОГРН)<br><br>16 - номер страхового полиса<br> | type of document        |
| country        | <kbd>str</kbd> | <kbd>keyword</kbd>                  | <kbd>true</kbd>  | <kbd>true</kbd>  | ALPHA-3                                                                                                                                                                                                                                                                                                                                                                                                                                               | country of document     |
| serial         | <kbd>str</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                                                                                                                                                                                                                                                                                                                                       | serial number           |
| date_issue     | <kbd>str</kbd> | <kbd>date</kbd>                     | <kbd>true</kbd>  | <kbd>true</kbd>  | dd.mm.YYYY                                                                                                                                                                                                                                                                                                                                                                                                                                            | document date of issue  |
| date_expire    | <kbd>str</kbd> | <kbd>date</kbd>                     | <kbd>true</kbd>  | <kbd>true</kbd>  | dd.mm.YYYY                                                                                                                                                                                                                                                                                                                                                                                                                                            | document date of expire |
| authority      | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                                                                                                                                                                                                                                                                                                                                       | authority               |
| authority_code | <kbd>str</kbd> | <kbd>keyword</kbd>                  | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                                                                                                                                                                                                                                                                                                                                       | authority code          |
| comment        | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                                                                                                                                                                                                                                                                                                                                       | some comments           |

### Vehicles
```json
{
  "vehicles": [
    {
      "type": 0,
      "model": "Tesla Model B",
      "year": 2021,
      "color": "Red",
      "number": "AO4598AA",
      "vin": "5689745431",
      "comment": "Some comments"
    }
  ]
}
```
| Field name | Type / Python  | Type / ElasticSearch                | Index           | Copy to full     | Format | Description                   |
|------------|----------------|-------------------------------------|-----------------|------------------|--------|-------------------------------|
| type       | <kbd>int</kbd> | <kbd>byte</kbd>                     | <kbd>true</kbd> | <kbd>false</kbd> | 1 - car       | type of vehicle        |
| model      | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd>  |        | car model                     |
| year       | <kbd>int</kbd> | <kbd>date</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd>  | YYYY   | year of issue                 |
| color      | <kbd>str</kbd> | <kbd>keyword</kbd>                  | <kbd>true</kbd> | <kbd>true</kbd>  |        | car color                     |
| number     | <kbd>str</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> | <kbd>true</kbd>  |        | car numbers                   |
| vin        | <kbd>str</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> | <kbd>true</kbd>  |        | vehicle identification number |
| comment    | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd>  |        | some comments                 |

### Financials
```json
{
  "financials": [
    {
      "title": "Alfa-Bank",
      "card_number": "5498689754874578",
      "invoice_number": "0000000000000000",
      "date_issue": "11.2020",
      "date_expire": "11.2025",
      "login": "380506254896",
      "comment": "Some comments"
    }
  ]
}
```
| Field name     | Type / Python  | Type / ElasticSearch                | Index           | Copy to full    | Format                | Description                      |
|----------------|----------------|-------------------------------------|-----------------|-----------------|-----------------------|----------------------------------|
| title          | <kbd>str</kbd> | <kbd>keyword</kbd>                  | <kbd>true</kbd> | <kbd>true</kbd> |                       | name of bank                     |
| card_number    | <kbd>int</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> | <kbd>true</kbd> |                       | card number or payment number    |
| invoice_number | <kbd>str</kbd> | <kbd>text</kbd>, <kbd>keyword</kbd> | <kbd>true</kbd> | <kbd>true</kbd> |                       | invoice number or payment number |
| date_issue     | <kbd>str</kbd> | <kbd>date</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd> | dd.mm.YYYY<br>mm.YYYY | date of issue                    |
| date_expire    | <kbd>str</kbd> | <kbd>date</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd> | dd.mm.YYYY<br>mm.YYYY | date of expire                   |
| login          | <kbd>str</kbd> | <kbd>keyword</kbd>                  | <kbd>true</kbd> | <kbd>true</kbd> |                       | if have login username or number |
| comment        | <kbd>str</kbd> | <kbd>text</kbd>                     | <kbd>true</kbd> | <kbd>true</kbd> |                       | some comments                    |

### Ownerships
```json
{
  "ownerships": [
    {
      "title": "House",
      "date": "10.11.2022",
      "comment": "Some comments"
    }
  ]
}
```
| Field name | Type / Python  | Type / ElasticSearch | Index           | Copy to full    | Format     | Description       |
|------------|----------------|----------------------|-----------------|-----------------|------------|-------------------|
| title      | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd> |            | name ownership    |
| date       | <kbd>str</kbd> | <kbd>date</kbd>      | <kbd>true</kbd> | <kbd>true</kbd> | dd.mm.YYYY | date of ownership |
| comment    | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd> |            | some comments     |

### Links
```json
{
  "links": [
    {
      "title": "Profile in OLX",
      "link": "https://olx.com/fsdfsdf",
      "comment": "Some comments"
    }
  ]
}
```
| Field name | Type / Python  | Type / ElasticSearch | Index           | Copy to full    | Format | Description   |
|------------|----------------|----------------------|-----------------|-----------------|--------|---------------|
| title      | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd> |        | title         |
| link       | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd> | <kbd>true</kbd> |        | link          |
| comment    | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd> |        | some comments |

### Accounts
```json
{
  "accounts": [
    {
      "title": "title",
      "link": "link",
      "login": "Login",
      "password": "Password",
      "password_hash": "Password hash",
      "id": "A321B365",
      "client_card_number": "85698563658968",
      "comment": "Some comments"
    }
  ]
}
```
| Field name         | Type / Python   | Type / ElasticSearch | Index             | Copy to full     | Format          | Description                                                                                                |
|--------------------|-----------------|----------------------|-------------------|------------------|-----------------|------------------------------------------------------------------------------------------------------------|
| title              | <kbd>str</kbd>  | <kbd>keyword</kbd>   | <kbd>true</kbd>   | <kbd>true</kbd> |                 | title of service                                                                                           |
| link               | <kbd>str</kbd>  | <kbd>keyword</kbd>   | <kbd>true</kbd>   | <kbd>true</kbd>  |                 | link                                                                                                       |
| login              | <kbd>str</kbd>  | <kbd>keyword</kbd>   | <kbd>true</kbd>   | <kbd>true</kbd>  |                 | login                                                                                                      |
| password           | <kbd>str</kbd>  | <kbd>keyword</kbd>   | <kbd>true</kbd>   | <kbd>true</kbd>  |                 | password                                                                                                   |
| password_hash      | <kbd>str</kbd>  | <kbd>keyword</kbd>   | <kbd>false</kbd>  | <kbd>false</kbd> | MD5, SHA1, etc. | password hash                                                                                              |
| id                 | <kbd>str</kbd>  | <kbd>keyword</kbd>   | <kbd>true</kbd>   | <kbd>true</kbd>  |                 | the internal ID of the site or application that has been assigned to this account                          |
| client_card_number | <kbd>str</kbd>  | <kbd>keyword</kbd>   | <kbd>true</kbd>   | <kbd>true</kbd>  |                 | customer card of a person. It can be a bonus card, a loyalty card, shopping vouchers in supermarkets, etc. |
| comment            | <kbd>str</kbd>  | <kbd>text</kbd>      | <kbd>true</kbd>   | <kbd>true</kbd>  |                 | some comments                                                                                              |
### Movements
```json
{
  "movements": [
    {
      "from": {
        "datetime": "10.20.2022",
        "country": "UKR",
        "city": "Kiev",
        "code": "KBP"
      },
      "to": {
        "country": "UKR",
        "datetime": "11.20.2022",
        "city": "Kiev",
        "code": "KBP"
      },
      "code_type": "IATA",
      "ticket_order_datetime": "10.20.2022",
      "fixation_datetime": "10.20.2022",
      "ticket_issuer": "OOO Ticket box",
      "transport_company_name": "SkyUp",
      "transport_company_code": "PQ",
      "seat": "12A",
      "ticket_number": "54",
      "trip_number": "A407",
      "class": "K",
      "type": 0,
      "comment": "Some comments"
    }
  ]
}
```
| Field name    | Type / Python  | Type / ElasticSearch | Index            | Copy to full     | Format                                                                                                                          | Description            |
|---------------|----------------|----------------------|------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------|------------------------|
| from          |                |                      |                  |                  |                                                                                                                                 |                        |
| - datetime    | <kbd>str</kbd> | <kbd>date</kbd>      | <kbd>true</kbd>  | <kbd>true</kbd>  | dd.mm.YYYY<br>dd.mm.YYYY 'T' HH:mm                                                                                              | datetime               |
| - country     | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                          |            |
| - city        | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | city                   |
| - code        | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | code                   |
| to            |                |                      |                  |                  |                                                                                                                                 |                        |
| - datetime    | <kbd>str</kbd> | <kbd>date</kbd>      | <kbd>true</kbd>  | <kbd>true</kbd>  | dd.mm.YYYY<br>dd.mm.YYYY 'T' HH:mm                                                                                              | datetime               |
| - country     | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                         |            |
| - city        | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | city                   |
| - code        | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | code                   |
| code_type     | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>false</kbd> | <kbd>false</kbd> | IATA - for airlines<br>CODE - if undefined code                                                                                 | code type              |
| ticket_order_datetime      | <kbd>str</kbd> | <kbd>date</kbd>      | <kbd>true</kbd>  | <kbd>true</kbd>  | dd.mm.YYYY<br>dd.mm.YYYY 'T' HH:mm                                                                                              | datetime of ticket buy |
| fixation_datetime          | <kbd>str</kbd> | <kbd>date</kbd>      | <kbd>true</kbd>  | <kbd>true</kbd>  | dd.mm.YYYY<br>dd.mm.YYYY 'T' HH:mm                                                                                              | datetime of movement fixation (cross border date etc.) |
| seat          | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | seat number            |
| ticket_number | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | ticket number          |
| ticket_issuer | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | ticket_issuer   |
| transport_company_name | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | transportcompany name           |
| transport_company_code | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | transport company code          |
| trip_number | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | flight number          |
| class         | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>true</kbd>  | <kbd>true</kbd>  | F<br>А<br>etc.                                                                                                                  | class                  |
| type          | <kbd>int</kbd> | <kbd>byte</kbd>      | <kbd>true</kbd>  | <kbd>false</kbd> | 0 - walk<br>1 - car<br>2 - airplane<br>3 - bus<br>4 - train<br>5 - ship<br>6 - bike<br>7 - subway<br>8 - tram<br>9 - helicopter | type of movement       |
| comment       | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd>  | <kbd>true</kbd>  |                                                                                                                                 | some comments          |

### ⚠️ Source 
```json
{
  "source": [
    {
      "database": "vodafone",
      "actuality": 2024,
      "comment": "Some comments"
    }
  ]
}
```
| Field name | Type / Python  | Type / ElasticSearch | Index            | Copy to full     | Format | Description       |
|------------|----------------|----------------------|------------------|------------------|--------|-------------------|
| database   | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>false</kbd> | <kbd>false</kbd> |        | name of database  |
| actuality  | <kbd>int</kbd> | <kbd>date</kbd>      | <kbd>false</kbd> | <kbd>false</kbd> | YYYY   | year of actuality |
| comment    | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>false</kbd> | <kbd>false</kbd> |        | some comments     |

### Incidences
```json
{
  "incidences": [
    {
      "title": "Car accident",
      "date": "10.11.2022",
      "insurance": "TAC",
      "participants": ["Иванов Сергей Александрович Kia Rio 76789", "Петров Олег Александрович Kia Cerato 72744"],
      "comment": "Some comments"
    }
  ]
}
```
| Field name    | Type / Python   | Type / ElasticSearch | Index           | Copy to full     |  Format             | Description               |
|---------------|-----------------|----------------------|-----------------|------------------|---------------------|---------------------------|
| title         | <kbd>str</kbd>  | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  |                     | name of incidences        |
| date          | <kbd>str</kbd>  | <kbd>date</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  |  dd.mm.YYYY         | year of actuality         |
| insurance     | <kbd>str</kbd>  | <kbd>keyword</kbd>   | <kbd>true</kbd> | <kbd>false</kbd> |                     | insurance company         |
| participants  | <kbd>str</kbd>  | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>false</kbd> |                     | participants of incidence |
| comment       | <kbd>str</kbd>  | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd>  |                     | some comments             |

### Devices
```json
{
  "devices": [
    {
      "title": "Poco X3",
      "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
      "date": "10.11.2022",
      "action": "Buy ticket",
      "comment": "Some comments"
    }
  ]
}
```
| Field name | Type / Python  | Type / ElasticSearch | Index            | Copy to full     | Format                                | Description                   |
|------------|----------------|----------------------|------------------|------------------|---------------------------------------|-------------------------------|
| title      | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>false</kbd> | <kbd>false</kbd> |                                       | name of device                |
| user_agent | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>false</kbd> | <kbd>false</kbd> |                                       | user agent / operation system |
| date       | <kbd>str</kbd> | <kbd>date</kbd>      | <kbd>false</kbd> | <kbd>false</kbd> | dd.mm.YYYY<br>dd.mm.YYYY 'T' HH:mm:ss | date of detect device         |
| action     | <kbd>str</kbd> | <kbd>keyword</kbd>   | <kbd>false</kbd> | <kbd>false</kbd> |                                       | description of action         |
| comment    | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>false</kbd> | <kbd>false</kbd> |                                       | comment                       |


### Ip's
```json
{
  "ips": [
    {
      "ip": "85.14.201.45",
      "date": "10.11.2022 14:20:00",
      "comment": "Some comments"
    }
  ]
}
```
| Field name | Type / Python  | Type / ElasticSearch | Index           | Copy to full    | Format                             | Description       |
|------------|----------------|----------------------|-----------------|-----------------|------------------------------------|-------------------|
| ip         | <kbd>str</kbd> | <kbd>ip</kbd>        | <kbd>true</kbd> | <kbd>true</kbd> |                                    | ip                |
| date       | <kbd>str</kbd> | <kbd>date</kbd>      | <kbd>true</kbd> | <kbd>true</kbd> | dd.mm.YYYY<br>dd.mm.YYYY 'T' HH:mm | date of detect ip |
| comment    | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd> |                                    | some comments     |

### Media
```json
{
  "media": [
    {
      "file_name": "111234112_1.jpg",
      "raw_file_name": "photo44421332.jpg",
      "file_type": 0,
      "url": "https://myfilestorage.com/db1/0/111234112_photo_1.jpg",
      "description": "Personal photo of person",
      "comment": "Some comments"
    }
  ]
}
```
| Field name    | Type / Python  | Type / ElasticSearch | Index           | Copy to full    | Format                             | Description             |
|---------------|----------------|----------------------|-----------------|-----------------|------------------------------------|------------------------|
| file_name     | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>false</kbd>| <kbd>true</kbd> |                                    | name of file on storage                 |
| raw_file_name | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>false</kbd>| <kbd>true</kbd> |                                    | raw name of file on storage              |
| file_type     | <kbd>int</kbd> | <kbd>text</kbd>      | <kbd>false</kbd>| <kbd>true</kbd> |0-photo,1-video,2-audio,3-document  | file type                    |
| url           | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>false</kbd>| <kbd>true</kbd> |                                    | name of file on storage                 |
| description   | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd> |                                    | file description             |
| comment       | <kbd>str</kbd> | <kbd>text</kbd>      | <kbd>true</kbd> | <kbd>true</kbd> |                                    | some comments                |


### Other
```json
{
  "coordinates": [[41.25487, 69.8754], [47.45666, 89.56897]],
  "comment": "Some comments"
}
```
| Field name  | Type / Python                       | Type / ElasticSearch | Index           | Format                | Description   |
|-------------|-------------------------------------|----------------------|-----------------|-----------------------|---------------|
| coordinates | <kbd>list</kbd> of <kbd>float</kbd> | <kbd>geo_point</kbd> | <kbd>true</kbd> | [longitude, latitude] | coordinates   |
| comment     | <kbd>str</kbd>                      | <kbd>text</kbd>      | <kbd>true</kbd> |                       | some comments |
