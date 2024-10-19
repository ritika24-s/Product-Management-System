A minimalist website with a product listing.

Languages/frameworks/technologies: Python 3, Django, PostgreSQL database
1. Note that UI and look and feel is not important. The main focus of this task is the back-
end code and database layer.
2. You need to create a minimalist website with
 Product listing
 Product management actions
 Authorisation (username and password)
 A few roles (see below)
3. Each product has information about
 Supplier
 Name
 Product/Symbol Code (a supplier cannot have more than one product with the same
code)
 Price
 Stock Status (In stock or Out of stock)
 Images (optional, one marked as main/default if it exists)
4. Content and user management is carried out manually through the administrator interface.
5. Roles
 Buyer - can view the product listing
 Supplier - can view the list of their products
 Administrator - access to the administrator interface
6. Website sections:
 Main section
o Main page – Landing page with login for unauthorized users
 Administrator section (available only for administrators)
o User management (a list and option to add, edit, delete)
o Product management (a list and option to add, edit, delete)
 Supplier section (available only for suppliers)
o List of the supplier&#39;s products. Need to show fields: Name, Product Code,
Price, Stock Status, Has image (Yes or No).
o List of supplier products that have cheaper analogues (with the same Product
Code) in stock among other suppliers. Need to show fields: Name, Product
Code, Price.

 Buyer section (available only for buyers)
o General list of products in stock for all suppliers. Need to show fields: Name,
Product Code, Price, Supplier, Main product image

7. Technical requirements
 Django framework &gt;= 3.2 (python &gt;= 3.11)
 Postgres database &gt;= 14
 Unit tests are very welcome.