import os
import json
import zipfile
import concurrent.futures
from pathlib import Path
import urllib.request
import shutil


def get_version_data(cache_path="minecraft_versions.json"):
    if Path(cache_path).exists():
        print("Using cached version data.")
        with open(cache_path, 'r') as f:
            return json.load(f)
    else:
        print("Downloading version data from Mojang...")
        gist_url = "https://launchermeta.mojang.com/mc/game/version_manifest_v2.json"
        try:
            with urllib.request.urlopen(gist_url) as response:
                data = json.load(response)
                with open(cache_path, 'w') as f:
                    json.dump(data['versions'], f)
                return data['versions']
        except Exception as e:
            raise RuntimeError(f"Failed to download version data: {e}")


def download_minecraft_jar(version, save_path):
    version_data = get_version_data()
    version_entry = next((entry for entry in version_data if entry['id'] == version), None)
    if not version_entry:
        raise ValueError(f"Version {version} not found in the version manifest.")

    version_details_url = version_entry['url']

    try:
        with urllib.request.urlopen(version_details_url) as response:
            version_details = json.load(response)
            download_info = version_details['downloads']['client']
            url = download_info['url']
            expected_size = download_info['size']
    except Exception as e:
        raise RuntimeError(f"Failed to download version details: {e}")

    if not Path(save_path).exists():
        print(f"Downloading Minecraft {version} Client JAR...")
        temp_file, _ = urllib.request.urlretrieve(url)

        downloaded_size = Path(temp_file).stat().st_size

        if downloaded_size == expected_size:
            shutil.move(temp_file, save_path)
            print("Download complete.")
        else:
            Path(temp_file).unlink()
            raise RuntimeError(f"Download size mismatch. Expected {expected_size}, got {downloaded_size}.")
    else:
        print("Minecraft Client JAR already exists.")


def extract_tags_from_jar(jar_path):
    tags = {}
    try:
        with zipfile.ZipFile(jar_path, 'r') as jar:
            for file in jar.namelist():
                if file.startswith("data/") and file.endswith(".json") and "tags/blocks/" in file:
                    tag_name = Path(file).stem
                    with jar.open(file) as f:
                        try:
                            data = json.load(f)
                            if isinstance(data.get("values"), list):
                                materials = {item if isinstance(item, str) else item.get("id") for item in data["values"] if isinstance(item, (str, dict))}
                                tags.setdefault(tag_name, set()).update(materials)
                        except json.JSONDecodeError:
                            print(f"Invalid JSON in {file} inside {jar_path}")
    except zipfile.BadZipFile:
        print(f"Failed to read {jar_path} (corrupt or not a zip file)")
    return tags


def collect_all_tags(mods_folder, vanilla_jar):
    all_tags = {}
    jar_files = [p for p in Path(mods_folder).rglob("*.jar")]
    if vanilla_jar and Path(vanilla_jar).is_file():
        jar_files.append(Path(vanilla_jar))
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(extract_tags_from_jar, jar_files))
    
    for tags in results:
        for tag, materials in tags.items():
            formatted_materials = {item.upper().replace(":", "_") for item in materials}
            all_tags.setdefault(f"#{tag}", set()).update(formatted_materials)
    
    return {tag: sorted(filter(None, materials)) for tag, materials in all_tags.items()}


def main():
    mods_folder = "./mods" 
    version = "1.20.1"  # Change this to your desired Minecraft version for vanilla tags
    vanilla_jar = f"./cached_minecraft_client_{version}.jar"
    output_file = "materials_tags.json"
    
    download_minecraft_jar(version, vanilla_jar)
    all_tags = collect_all_tags(mods_folder, vanilla_jar)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_tags, f, indent=4)
    
    print(f"Material tags saved to {output_file}")

if __name__ == "__main__":
    main()
