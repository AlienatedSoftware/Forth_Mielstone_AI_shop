## Testing User Stories 
---
 **As a Visitor**
 - As a Visitor, I want to easily understand the main purpose of the site.
   - The page shows the products clearly followed by indications of where I can signup or browse more categories. 
 
 - As a Visitor, I want to be able to view products available before buying a product.
   - Clicking on the header links I can browse through the different variations of art styles even when I am not logged in.
 
 - As a Visitor, I want to be able to register a new account.
   - Clicking on the "My Account" then "Sign Up" links I am presented with a clear sign up form, and the site even sends me a real email to confirm that I am wanting to create the account.
 
  **As a User**
 - As a User, I want to easily understand the main purpose of the site.
   - The page shows that it is clearly a shopping service for NFTs right from the home page. Followed by indications of where I can browse certain products in the header.
 
 - As a User, I want to be able to update and edit my profile.
   - Clicking on the "My Profile" link after logging in. I can easily change my delivery details. And even view my order history.
 
 - As a User, I want to search all categories
   - I can easily search for categories and filter them by what is available in store.
 
- As a User, I want to order and confirm it.
   - I can purchase a product, and I get an email telling me that my order is confirmed with every detail I need.

 **As a Staff Member**
 - As a Staff Member, I want to be able to update user permissions.
   - Upon entering the admin panel, I can successfully control all user permissions, even on myself.

 - As a Staff Member, I want to be able to manually add new products or remove them.
   - I can easily navigate to the products and completely edit their details, prices, list some new products or remove them. This applies for categories.

 - As a Staff Member, I want to be able to track down all orders by registered users.
   - I can easily navigate to the orders and view peoples orders to double check if they went through to the database. 


## Validation
---
All form validation is handled by django forms and the autentications by allauth.


## Possible exploit possible by users

 - If a user adds '/products/add/' they will be greated to a product add page where they can add their own products onto the database. This should be monitored at all times by memebers of staff incase of any malware or explict content is uploaded, and is to be removed instantly. Developer will address this and make it possible only for staff members to access for a friendly UI envirnment to add/edit products rather then the admin panel. This was a prototype for users to be able to relist their NFT's to mint/flip them for profit.