# Libraries to Install
Make sure to install the required libraries using the `requirements.txt` file
Run the following commands before attempting to run this code.
For Mac users, we need to do some setup before the `pip install` will work,
so we have made a seperate bash script to run instead. 

### Windows
```bash
py -m pip install -r requirements.txt
```

### macOS
You may need to find where mysqlserver has been installed for the following
script to set some flags.
To find where it may be installed at, execute the following command on
the terminal:
```bash
sudo find /usr -name mysql.h
```
Then, using what is found, we may need to update the variable named 
`mysqlhome` if it differs from our default.

```bash
chmod +x ./mac.sh && sudo ./mac.sh
```

# Database setup
Make sure to drop the old walkthrough database and execute the two SQL
files in the exercise folder. `database.sql` builds the database
and includes some data in all tables. 

# User Accounts
FotoBooking is a web application designed for booking photography services.
It provides different functionalities based on the user role:

Admin
- Manage services, types, add-ons, and price
- Username: admin1@gmail.com / admin2@gmail.com
- Password: 1234qwer
Photographer
- Register / Login
- Edit profile and portfolio
- Add / remove services and gallery images
- Manage availability
Photographer1
- Username: john.doe@example.com
- Password: John1234
Photographer2
- Username: emily.smith@example.com
- Password: Emily1234
Client
- Register / Login
- Browse and filter photographers by location, service, and rating
- Add to cart and complete checkout
Client1
- Username: julicortesarb@gmail.com
- Password: JulCor!2026
Client2
- Username: mike.hansen88@yahoo.com
- Password: MicHan!2027