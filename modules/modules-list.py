modules = {
    "google_search": {
        "description": "recherche sur Google Internet",
        "path": "google_search.main"
    }
}

def import_module(module_name):
    import importlib
    module_info = modules.get(module_name)
    if module_info:
        module_path = module_info["path"]
        module = importlib.import_module(module_path)
        if hasattr(module, "Main"):
            return module.Main
        else:
            print(f"ImportError: module '{module_name}' has not Main class")
            exit()
    else:
        print(f"ImportError: module '{module_name}' is not in the dictionnary")
        exit()

google_search = import_module("google_search")
google_search.search("chatgpt")
