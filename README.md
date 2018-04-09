# File-mangement-using-Checksum

My College Minor project.

I am trying to develop MD5 checksum based file management system, which is useful for saving data.

Here is my simple proposed solution.

-->Get a file
-->Genrate Checkshum
-->Send genrated checksum to database.
-->Search in database
-->If found
  ->Return file location and abort uploading.
-->If not found
  ->Upload file and save its MD5 in Database.
  
  
