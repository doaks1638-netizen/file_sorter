from pathlib import Path
import random
import shutil

folder_names = [
    "alpha", "archive", "atlas", "amber", "axis", "apex", "aspect", "aura",
    "beacon", "backup", "binary", "buffer", "blast", "bridge", "blade", "bloom",
    "cipher", "core", "cloud", "cache", "crane", "crest", "cortex", "cosmos",
    "delta", "data", "drift", "drive", "depth", "dawn", "dusk", "dist",
    "echo", "edge", "entry", "ether", "engine", "env", "epoch", "error",
    "flux", "flash", "field", "frame", "focal", "frost", "flow", "fragment",
    "gate", "grid", "ghost", "gear", "glass", "grain", "gravity", "grove",
    "hub", "helix", "host", "haven", "halo", "horizon", "hybrid", "haze",
    "index", "input", "iron", "ionic", "inner", "image", "impact", "infra",
    "junction", "joint", "jade", "jet", "jolt", "jump", "jungle", "juneau",
    "kernel", "key", "koda", "kinetic", "krypton", "kite", "knot", "knight",
    "link", "logic", "layer", "lens", "lunar", "loop", "light", "legacy",
    "matrix", "mesh", "macro", "micro", "meta", "mind", "mist", "mirror",
    "node", "nexus", "null", "nova", "net", "neon", "nerve", "notch",
    "origin", "orbit", "omega", "output", "oxide", "ocean", "optic", "outer",
    "pulse", "proxy", "point", "phase", "pixel", "prism", "pilot", "prime",
    "quantum", "quest", "quartz", "quarry", "quark", "quick", "query", "queue",
    "root", "relay", "range", "rift", "radar", "raw", "rise", "rotor",
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

def Haos(path, number_dirs, number_file):
    path = Path(path)
    all_dirs = [path]
    if number_dirs == 0 and number_file == 0:
        return
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
pather = input()
shutil.rmtree(pather)
path1 = Path(pather)
path1.mkdir(exist_ok=True, parents=True)
Haos(pather, 40, 40)
