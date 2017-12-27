# SCRAP

Scrap as a project aims to provide understandable file manipulation for the average user. It is quite common to hear Python recommended as a crucial tool when it comes to dealing with large amounts of data, spreadsheets, emails, etc. While Python is friendly to newer programmers it still has its downfall. Scrap aims to close these gaps between novices and basic office programming.

Basic Scrap syntax is close to human speech and easy to understand for someone reading the code. See an example of Scrap:

```
load "file.txt" into text
replace "string_1" with "string_2" in text

load text
replace first "string_1" with "string_2"

load "clients.excel" into table
foreach email_address in table[1]:
	remove r" [^A-Za-z0-9] "
	append "From, me"
	email from "from@email.com" to var_name"

write text to "file.txt"
```

