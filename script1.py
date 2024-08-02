import os

# This Script find files in various directories

def find_file(name="-------"):
    var_name = "PyScripts"
    if var_name in os.environ:
        var_path = os.path.join(f"$var_name",name)
        config_path = os.path.expandvars(var_path)
        print("1.Checking Config path"+{config_path})
        if os.path.exists(config_path):
            return config_path
        
    #Check in current working directory
    config_path = os.path.join(os.getcwd,name)
    print("2.Checking Config path"+{config_path})
    if os.path.exists(config_path):
        return config_path
    
    # Check user home directoery
    home_dir = os.path.expanduser("~/")   #for windows ->  "C:\Users\username" 
    config_path = os.path.join(home_dir,name)
    print("3.Checking Config path"+{config_path})
    if os.path.exists(config_path):
        return config_path
    
    # Check Directoery for file
    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(name)
    config_path = os.path.join(parent_path,name)
    print("4.Checking Config path "+{config_path})
    if os.path.exists(config_path):
        return config_path
    
    print("File "+{name}+" not found")