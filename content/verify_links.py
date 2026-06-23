import os
import re
import sys

workspace_dir = os.path.dirname(os.path.abspath(__file__))

# All targets to check
targets = {
    # Neurology
    "acute increased intracranial pressure": r"Diseases\Neurology\Acute Increased Intracranial Pressure.md",
    "coma": r"Diseases\Neurology\Coma.md",
    "convulsion": r"Diseases\Neurology\Convulsion.md",
    "headache": r"Symptoms\Headache.md",
    "syncope": r"Symptoms\Syncope.md",
    # Rheumatology
    "ankylosing spondylitis": r"Diseases\Rheumatology\Ankylosing Spondylitis.md",
    "psoriatic arthritis": r"Diseases\Rheumatology\Psoriatic Arthritis.md",
    "enteropathic arthritis": r"Diseases\Rheumatology\Enteropathic Arthritis.md",
    "systemic sclerosis": r"Diseases\Rheumatology\Systemic Sclerosis.md",
    "sjögren syndrome": r"Diseases\Rheumatology\Sjögren Syndrome.md",
    "polymyalgia rheumatica": r"Diseases\Rheumatology\Polymyalgia Rheumatica.md",
    "giant cell arteritis": r"Diseases\Rheumatology\Giant Cell Arteritis.md",
    "osteoarthritis": r"Diseases\Rheumatology\Osteoarthritis.md",
    "degenerative disease of spine": r"Diseases\Rheumatology\Degenerative Disease of Spine.md",
    "systemic lupus erythematosus": r"Diseases\Rheumatology\Systemic Lupus Erythematosus.md",
    "fibromyalgia": r"Diseases\Rheumatology\Fibromyalgia.md",
    "vasculitis": r"Diseases\Rheumatology\Vasculitis.md",
    "behçet disease": r"Diseases\Rheumatology\Behçet Disease.md",
    "dermatomyositis": r"Diseases\Rheumatology\Dermatomyositis.md",
    "polymyositis": r"Diseases\Rheumatology\Polymyositis.md",
    "anca-associated vasculitis": r"Diseases\Rheumatology\ANCA-associated Vasculitis.md",
    # Hematology
    "nutritional anemia": r"Diseases\Hematology\Nutritional Anemia.md",
    "iron deficiency anemia": r"Diseases\Hematology\Iron Deficiency Anemia.md",
    "vitamin b12 deficiency anemia": r"Diseases\Hematology\Vitamin B12 Deficiency Anemia.md",
    "folate deficiency anemia": r"Diseases\Hematology\Folate Deficiency Anemia.md",
    "thalassemia": r"Diseases\Hematology\Thalassemia.md",
    "hemoglobinopathy": r"Diseases\Hematology\Hemoglobinopathy.md",
    "g6pd deficiency": r"Diseases\Hematology\G6PD Deficiency.md",
    "autoimmune hemolytic anemia": r"Diseases\Hematology\Autoimmune Hemolytic Anemia.md",
    "hereditary spherocytosis": r"Diseases\Hematology\Hereditary Spherocytosis.md",
    "paroxysmal nocturnal hemoglobinuria": r"Diseases\Hematology\Paroxysmal Nocturnal Hemoglobinuria.md",
    "aplastic anemia": r"Diseases\Hematology\Aplastic Anemia.md",
    "agranulocytosis": r"Diseases\Hematology\Agranulocytosis.md",
    "immune thrombocytopenia": r"Diseases\Hematology\Immune Thrombocytopenia.md",
    "hemophilia": r"Diseases\Hematology\Hemophilia.md",
    "von willebrand disease": r"Diseases\Hematology\Von Willebrand Disease.md",
    "vitamin k deficiency": r"Diseases\Hematology\Vitamin K Deficiency.md",
    "disseminated intravascular coagulation": r"Diseases\Hematology\Disseminated Intravascular Coagulation.md",
    "deep vein thrombosis": r"Diseases\Hematology\Deep Vein Thrombosis.md",
    "thrombotic thrombocytopenic purpura": r"Diseases\Hematology\Thrombotic Thrombocytopenic Purpura.md",
    "multiple myeloma": r"Diseases\Hematology\Multiple Myeloma.md",
    "myeloproliferative neoplasm": r"Diseases\Hematology\Myeloproliferative Neoplasm.md",
    "leukemia": r"Diseases\Hematology\Leukemia.md",
    "lymphoma": r"Diseases\Hematology\Lymphoma.md",
    "monoclonal and polyclonal gammopathies": r"Diseases\Hematology\Monoclonal and Polyclonal Gammopathies.md",
    # Infectious Disease
    "influenza": r"Diseases\Infectious Disease\Influenza.md",
    "upper respiratory tract infection": r"Diseases\Infectious Disease\Upper Respiratory Tract Infection.md",
    "lower respiratory tract infection": r"Diseases\Infectious Disease\Lower Respiratory Tract Infection.md",
    "community acquired pneumonia": r"Diseases\Infectious Disease\Community Acquired Pneumonia.md",
    "deep neck infection": r"Diseases\Infectious Disease\Deep Neck Infection.md",
    "peritonsillar abscess": r"Diseases\Infectious Disease\Peritonsillar Abscess.md",
    "pyothorax": r"Diseases\Infectious Disease\Pyothorax.md",
    "tuberculosis": r"Diseases\Infectious Disease\Tuberculosis.md",
    "chronic pulmonary fungal infection": r"Diseases\Infectious Disease\Chronic Pulmonary Fungal Infection.md",
    "pulmonary nocardiosis": r"Diseases\Infectious Disease\Pulmonary Nocardiosis.md",
    "typhoid and paratyphoid fever": r"Diseases\Infectious Disease\Typhoid and Paratyphoid Fever.md",
    "acute pyelonephritis": r"Diseases\Infectious Disease\Acute Pyelonephritis.md",
    "acute cystitis": r"Diseases\Infectious Disease\Acute Cystitis.md",
    "sexually transmitted infection": r"Diseases\Infectious Disease\Sexually Transmitted Infection.md",
    "gastroenteritis": r"Diseases\Infectious Disease\Gastroenteritis.md",
    "intestinal parasitosis": r"Diseases\Infectious Disease\Intestinal Parasitosis.md",
    "melioidosis": r"Diseases\Infectious Disease\Melioidosis.md",
    "leptospirosis": r"Diseases\Infectious Disease\Leptospirosis.md",
    "septicemia": r"Diseases\Infectious Disease\Septicemia.md",
    "dengue infection": r"Diseases\Infectious Disease\Dengue Infection.md",
    "malaria": r"Diseases\Infectious Disease\Malaria.md",
    "hiv infection and aids": r"Diseases\Infectious Disease\HIV Infection and AIDS.md",
    "bacterial meningitis": r"Diseases\Infectious Disease\Bacterial Meningitis.md",
    "hepatobiliary tract infection": r"Diseases\Infectious Disease\Hepatobiliary Tract Infection.md",
    "intraabdominal infection": r"Diseases\Infectious Disease\Intraabdominal Infection.md",
    "septic arthritis": r"Diseases\Infectious Disease\Septic Arthritis.md",
    "skin and soft tissue infection": r"Diseases\Infectious Disease\Skin and Soft Tissue Infection.md",
    "meningococcemia": r"Diseases\Infectious Disease\Meningococcemia.md",
    "rabies": r"Diseases\Infectious Disease\Rabies.md",
    "varicella zoster infection": r"Diseases\Infectious Disease\Varicella Zoster Infection.md",
    "mumps": r"Diseases\Infectious Disease\Mumps.md",
    "measles": r"Diseases\Infectious Disease\Measles.md",
    "zika virus infection": r"Diseases\Infectious Disease\Zika Virus Infection.md",
    "opportunistic infection in hiv": r"Diseases\Infectious Disease\Opportunistic Infection in HIV.md",
}

# Collect all files in workspace to verify actual existences
all_files = {}
for root, dirs, files in os.walk(workspace_dir):
    dirs[:] = [d for d in dirs if d not in ['.git', '.obsidian', '.agents']]
    for f in files:
        if f.endswith('.md'):
            rel_path = os.path.relpath(os.path.join(root, f), workspace_dir)
            all_files[rel_path.lower()] = rel_path

# Verify targets exist
missing_targets = 0
for k, path in targets.items():
    if path.lower() not in all_files:
        print(f"ERROR: Target file does not exist: {path}")
        missing_targets += 1
    else:
        print(f"Verified target exists: {path} -> {all_files[path.lower()]}")

if missing_targets > 0:
    sys.exit(1)

# Link pattern: [[Target]] or [[Target|Display]]
link_pattern = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')

broken_links = 0
checked_files = 0

for root, dirs, files in os.walk(workspace_dir):
    dirs[:] = [d for d in dirs if d not in ['.git', '.obsidian', '.agents']]
    for f in files:
        if f.endswith('.md'):
            checked_files += 1
            file_path = os.path.join(root, f)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file_content:
                for i, line in enumerate(file_content, 1):
                    for match in link_pattern.finditer(line):
                        target_name = match.group(1).strip()
                        target_clean = target_name.replace('\\', '/')
                        target_base = os.path.basename(target_clean).lower()
                        
                        if target_base in targets:
                            # If it is path-prefixed (e.g. Diseases/Neurology/Coma)
                            if '/' in target_clean:
                                expected_path = targets[target_base].replace('\\', '/').lower()
                                if target_clean.lower() != expected_path and not expected_path.endswith(target_clean.lower()):
                                    print(f"Broken/obsolete path link in [{os.path.basename(file_path)}:L{i}] -> [[{target_name}]]")
                                    broken_links += 1
                            else:
                                # Normal non-path link, which resolves correctly since only one file exists
                                pass

print(f"\nTargeted link verification finished. Checked {checked_files} files.")
if broken_links > 0:
    print(f"Found {broken_links} broken/obsolete links to target files.")
    sys.exit(1)
else:
    print(f"All links to the {len(targets)} target files are 100% correct!")
    sys.exit(0)
