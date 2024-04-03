import shutil
import os
from datetime import datetime

def backup_database(backup_dir='backups'):
    base_dir = os.path.dirname(os.path.abspath(__file__)) 
    db_file = os.path.join(base_dir, 'db.sqlite3')  
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_file = os.path.join(backup_dir, f'db_backup_{timestamp}.sqlite3')
    shutil.copy2(db_file, backup_file)
    print(f'Backup created at {backup_file}')

if __name__ == '__main__':
    backup_database()

