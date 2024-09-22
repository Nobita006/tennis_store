
### **Tennis Store E-Commerce Website Documentation**

---

## **Overview**

The Tennis Store is an E-Commerce website developed using the Django Framework. The website allows customers to sign up, browse products in various categories (such as rackets, clothing, and tennis bags), and manage their shopping experience through features like search, pagination, and a shopping cart. Additionally, the website supports different user types, such as managers and customers, each with specific functionalities.

## **Screen Recording**



https://github.com/user-attachments/assets/4b6510b7-6fb3-4d07-9cdb-767ead53d15b




### **Features Implemented:**

1. **User Authentication:**
   - **Sign Up, Log In, Log Out:** Users can create accounts, log in, and log out securely. 
   - **Custom User Model:** Different user roles (manager and customer) are implemented using Django’s custom user model.
   
2. **Product Management:**
   - **Product Listings:** Products are displayed in various categories with pagination and search functionality.
   - **Product Details:** Each product can be viewed with detailed information.
   - **Consistent Image Display:** Product images maintain a consistent aspect ratio across the site.

3. **Shopping Cart:**
   - **Add to Cart:** Customers can add products to their cart.
   - **View Cart:** The cart can be viewed, showing all added products, quantities, and total price.
   - **Update Cart:** Quantities can be adjusted, and products can be removed or the cart emptied.
   - **Finalize Order:** Orders can be finalized and payment processed (simulated).
   - **Cancel Order:** Orders can be canceled, restoring items to the cart.
   - **Order History:** Customers can view their order history and details.

4. **Administrative Functions:**
   - **Django Admin Integration:** Administrators can manage products, categories, and user accounts via Django’s built-in admin interface.

5. **User Interface:**
   - **Bootstrap 5:** The website uses Bootstrap 5 for responsive design and an external CSS file for custom styling.
   - **User-Friendly Interface:** The design prioritizes ease of use and visual appeal.

6. **Data Management:**
   - **Django ORM:** The website uses Django’s ORM for handling database interactions, ensuring secure and efficient data management.
   - **Session Management:** The shopping cart is managed using Django’s session framework.

7. **Additional Features:**
   - **Custom User Types:** Differentiation between user roles, such as manager and customer, allows for role-specific functionalities.
   - **Enhanced Product Model:** The product model includes relationships like one-to-one, one-to-many, and many-to-many mappings, enabling advanced product categorization and management.

---

## **Development Process**

### **1. Project Setup:**
   - **Django Installation:** The project was initialized using Django, with a virtual environment to manage dependencies.
   - **Project Structure:** The project was structured according to Django best practices, separating concerns into apps such as `store` for managing products and `accounts` for user management.

### **2. User Management:**
   - **Custom User Model:** A custom user model was implemented to accommodate different user roles (manager and customer), providing tailored experiences based on the user type.
   - **Forms and Views:** Custom forms were created for user registration and profile management. Views were tailored to handle different user functionalities.

### **3. Product and Cart Functionality:**
   - **Product Display:** Products are displayed with consistent image dimensions, ensuring a clean and uniform layout.
   - **Shopping Cart:** The cart was developed using Django’s session framework, allowing users to manage their cart across sessions.

### **4. Order Management:**
   - **Order Finalization:** Users can finalize their orders, with the option to view and manage past orders.
   - **Cancellation and Cart Restoration:** Orders can be canceled, with products being restored to the shopping cart.

### **5. Search and Pagination:**
   - **Search Functionality:** A search bar was integrated, allowing users to find products based on keywords.
   - **Pagination:** Pagination was implemented to handle large product lists efficiently, improving user navigation.

### **6. Frontend Design:**
   - **Bootstrap Integration:** Bootstrap 5 was used for responsive design, ensuring the website works well across various devices.
   - **Custom CSS:** Additional styling was applied using a custom CSS file, enhancing the visual appeal of the site.

### **7. Version Control:**
   - **Git Integration:** Git was used for version control, with consistent commits documenting the development process.

---

## **File Structure Overview**

- **`manage.py`**: The main script for running Django commands.
- **`db.sqlite3`**: The SQLite database file storing all the data.
- **`settings.py`**: Configuration file for the Django project, including settings for static files, databases, and installed apps.
- **`urls.py`**: Contains URL routing information for the entire project.
- **`wsgi.py` and `asgi.py`**: Configuration files for deploying the project on web servers.
- **`store/`**: Contains the core functionality for managing products, orders, and the shopping cart.
  - **`models.py`**: Defines the database models, including the product, order, and cart models.
  - **`views.py`**: Contains the logic for handling requests and returning responses for product listings, cart operations, and orders.
  - **`urls.py`**: Defines URL patterns specific to the store app.
  - **`forms.py`**: Custom forms for product and order operations.
  - **`templates/`**: Contains HTML templates for rendering the views.
  - **`static/`**: Contains static files like CSS and JavaScript used in the frontend.
  - **`templatetags/`**: Custom template tags for extending the template functionality.
  
- **`accounts/`**: Manages user-related functionalities, including registration, authentication, and profile management.
  - **`models.py`**: Defines the custom user model.
  - **`forms.py`**: Forms for user registration and profile editing.
  - **`views.py`**: Handles user-related views like signup and profile display.
  - **`urls.py`**: Contains URL patterns for user-related actions.
  - **`templates/`**: Templates related to user authentication and profile pages.

---

## **Running the Website**

### **1. Clone the Repository:**

```bash
git clone <repository-url>
cd <project-directory>
```

### **2. Set Up the Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### **3. Install Dependencies:**

```bash
pip install -r requirements.txt
```

### **4. Apply Migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Run the Development Server:**

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/` to access the website.

### **5. Create User with Staf Status:**

```bash
python manage.py createsuperuser 
```

---

## **Development Notes**

- **Bootstrap 5 Integration:** Provides a responsive, modern user interface.
- **Custom User Types:** Enables role-based access control and functionality differentiation.
- **Session Management:** Utilizes Django's session framework to handle shopping cart persistence.
- **Pagination and Search:** Enhances user experience by managing large datasets effectively.

---
