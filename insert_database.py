from models.General import General
from models.Skills import Skills

dict_insert = [
    ('GIT', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-plain.svg'),
    ('SQL', 'https://i.ibb.co/zGJy4h5/sql-server.png'),
    ('React', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg'),
    ('Linux', 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg')
]

database = Skills()
database.connect()

test = Skills()
test.insert_many(dict_insert).execute()
