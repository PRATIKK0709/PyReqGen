import os
import ast
import sys
import subprocess
import pkg_resources
import importlib.metadata

def parse_imports(file_path):
    imports = set()
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), file_path)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module)
    return imports

def filter_std_lib(imports):
    std_lib = set(sys.builtin_module_names)
    return [module for module in imports if module not in std_lib]

def get_package_version(package_name):
    try:
        version = importlib.metadata.version(package_name)
        if version:
            return version
    except importlib.metadata.PackageNotFoundError:
        pass
    except Exception:
        pass
    
    try:
        package_info = pkg_resources.get_distribution(package_name)
        return package_info.version
    except pkg_resources.DistributionNotFound:
        pass
    except Exception:
        pass
    
    try:
        result = subprocess.run(['pip', 'show', package_name], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if line.startswith('Version:'):
                version = line.split(':')[1].strip()
                return version
    except Exception:
        pass
    
    return None

def write_requirements(requirements, output_file="requirements.txt"):
    with open(output_file, "w") as file:
        for module, version in sorted(requirements.items()):
            if version:
                file.write(f"{module}=={version}\n")

def generate_requirements(project_dir):
    all_imports = set()
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                imports = parse_imports(file_path)
                all_imports.update(imports)
    non_std_lib_imports = filter_std_lib(all_imports)
    requirements = {module: get_package_version(module) for module in non_std_lib_imports}
    write_requirements(requirements)

if __name__ == "__main__":
    project_dir = input("Enter the path to your Python project directory: ").strip()
    if not os.path.isdir(project_dir):
        print("Error: Directory not found.")
        sys.exit(1)
    generate_requirements(project_dir)
    print("requirements.txt generated successfully.")
