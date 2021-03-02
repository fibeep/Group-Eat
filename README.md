# Group - Eat
------------------
# Description:
> For this project, I made an app that facilitates eating out with friends.
> Users can chose to create or join a group.
> Once they are in a group, they can add restaurants.
> All group members then vote on which restaurant they like,
> Ultimately facilitating the process of choosing where to eat out.

By using an SQL database, I was able to map multiple relationships that allowed users to be in multiple groups, 
joining them via a special code (that protects the group from random joiners), and have restaurants inside the groups.
Moreover, the users are able to "like" the restaurants and all of this information is stored in the database.

## Technical Details:
**Written Python**
**Makes use of:**
- *Flask*
- *SQLAlchemy*
- *Jinja2*
- *Flask-WTF*
- *WTForms*