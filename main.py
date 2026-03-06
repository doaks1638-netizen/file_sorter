from pathlib import Path
import random
import shutil
from datetime import datetime
import sys

folder_names = [
    "alpha", "ignore_me", "atlas", "amber", "axis", "apex", "aspect", "aura",
    "ignore_me", "backup", "binary", "buffer", "blast", "bridge", "blade", "bloom",
    "cipher", "core", "cloud", "cache", "crane", "crest", "ignore_me", "cosmos",
    "delta", "data", "drift", "drive", "depth", "dawn", "dusk", "dist",
    "echo", "edge", "entry", "ether", "engine", "env", "epoch", "error",
    "flux", "flash", "field", "frame", "focal", "frost", "flow", "fragment",
    "gate", "grid", "ghost", "gear", "ignore_me", "grain", "gravity", "grove",
    "hub", "ignore_me", "host", "haven", "halo", "horizon", "ignore_me", "haze",
    "index", "input", "iron", "ionic", "inner", "image", "impact", "infra",
    "ignore_me", "ignore_me", "jade", "jet", "jolt", "jump", "jungle", "juneau",
    "kernel", "key", "koda", "kinetic", "krypton", "kite", "knot", "knight",
    "link", "logic", "layer", "lens", "lunar", "loop", "light", "legacy",
    "matrix", "mesh", "macro", "micro", "meta", "mind", "mist", "mirror",
    "node", "nexus", "null", "nova", "net", "neon", "nerve", "notch",
    "origin", "orbit", "omega", "output", "oxide", "ocean", "optic", "outer",
    "pulse", "proxy", "point", "phase", "ignore_me", "prism", "pilot", "prime",
    "quantum", "quest", "quartz", "quarry", "quark", "quick", "query", "queue",
    "root", "ignore_me", "range", "rift", "radar", "raw", "rise", "rotor",
    "source", "stack", "sync", "shell", "shift", "spark", "sonic", "space",
    "trace", "target", "task", "tide", "temp", "titan", "terra", "tunnel",
    "unit", "ultra", "urban", "union", "under", "update", "uranus", "utility",
    "vault", "vector", "vortex", "void", "vibe", "valve", "vertex", "view",
    "wave", "wire", "web", "warp", "wind", "west", "wild", "work",
    "xenon", "xray", "xylem", "xeno", "yield", "yard", "yoke", "zenith", "zone"
]

file_list = [
    "abstract_background", "annual_report_2023", "archive_backup", "balance_sheet_v1", 
    "branding_guide", "budget_draft", "client_contacts_final", "company_logo_black", 
    "contract_signed", "customer_feedback", "data_analysis_october", "database_dump", 
    "deployment_log", "design_mockup_mobile", "emergency_contacts", "employee_handbook", 
    "event_photos_01", "expenses_reimbursement", "faq_document", "financial_forecast", 
    "function_specs", "header_image", "holiday_schedule", "icon_set_vector", 
    "index_page", "installation_guide", "inventory_list", "invoice_88241", 
    "it_support_manual", "landing_page_copy", "legal_disclaimer", "marketing_strategy", 
    "meeting_minutes_monday", "new_hire_onboarding", "newsletter_template", "notes_brainstorming", 
    "office_map", "password_policy", "performance_review", "portfolio_update", 
    "presentation_investors", "product_roadmap", "project_timeline", "receipt_scan", 
    "readme_first", "requirements_doc", "sales_pitch_deck", "security_audit", 
    "social_media_plan", "test_cases_v3", "user_manual_en", "website_backup_full"
]

syf_list = ['.txt', '.jpg', '.py', '.json', '.csv']

def generate_chaos(path, number_dirs, number_file):
    try:
        path = Path(path)
        all_dirs = [path]
        n = 0
        n1 = 0
        while n != number_dirs:
            parent = random.choice(all_dirs)
            new_dir = random.choice(folder_names)
            new_path = parent / new_dir
            new_path.mkdir(exist_ok=True, parents=True)
            if new_path not in all_dirs:
                all_dirs.append(new_path)
                n += 1
        while n1 != number_file:
            parent = random.choice(all_dirs)
            new_file = random.choice(file_list) + random.choice(syf_list)
            new_path = parent / new_file
            new_path.touch()
            n1 += 1
    except Exception as e:
        print(f'ОШИБКА!!! Тип {e}')
        sys.exit()

def sort_files(path):
    try:
        path = Path(path)
        for root, dirs, files in path.walk():
            if 'ignore_me' in dirs:
                dirs.remove('ignore_me')
                    
            for file in files:
                full_path = Path(root) / file
                file_to = full_path.suffix.lstrip('.') + '_files' if full_path.suffix != '' else 'other' + '_files'
                dir_to = path.parent / 'Sorted_Data' / file_to
                final = dir_to / file
                point = 0
                dir_to.mkdir(exist_ok=True, parents=True)
                while final.exists():
                    point += 1
                    final = dir_to / f'{Path(file).stem}{point}{Path(file).suffix}'
                full_path.replace(final)
    except Exception as e:
        print(f'ОШИБКА!!! Тип {e}')
        sys.exit()
        
pather = input('Введите путь где нужно навести порядок ----> ')
info = input('Удалить ли выбранную папку? Будет создан zip архив в обоих случаях! y/n --->')
choise = input('Создавать Хаос? y/n ----> ')
if Path(pather).exists():
    if choise == 'y':
        generate_chaos(pather, random.randrange(10, 100), random.randrange(10, 100))
        sort_files(pather)
    else:
        sort_files(pather)
else:
    print('Выбран неверный путь')
    sys.exit()
date_now = datetime.strftime(datetime.now(), '%d-%m-%Y')
shutil.make_archive(Path(pather).parent / f'Sorted_Data_data{date_now}', 'zip', Path(pather).parent / 'Sorted_Data')
if info == 'y':
    shutil.rmtree(Path(pather).resolve())
if (Path(pather).parent / 'Sorted_Data').exists():
    shutil.rmtree((Path(pather).parent / 'Sorted_Data').resolve())


